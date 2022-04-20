import pandas as pd
import xgboost as xgb
from xgboost import plot_importance
import matplotlib.pyplot as plt
from feat_section import FeatSection
from label_section import LabelSection


def mk_label():
    ccf_offline_stage1_train = pd.read_csv('ccf_offline_stage1_train.csv')
    # # 筛选出领取优惠券的用户
    ccf_offline_stage1_train = ccf_offline_stage1_train[
         ccf_offline_stage1_train['Date_received'].isnull().values == False]

    # # 筛选出是否使用优惠券消费的用户，即正负样本
    # 用户有领取优惠券但没有核销，负样本，标0
    part1 = ccf_offline_stage1_train[
        ccf_offline_stage1_train['Date'].isnull().values == True]
    part1['label'] = 0
    part1['Date_received'] = part1['Date_received'].map(lambda x: str(int(x)))
    part1['Date_received'] = pd.to_datetime(part1['Date_received'],format='%Y-%m-%d')
    part1['Date'] = pd.to_datetime(part1['Date'],format='%Y-%m-%d')

    # # 用户在领取优惠券后15天内使用则为正样本（标1），否则为负样本
    part2 = ccf_offline_stage1_train[ccf_offline_stage1_train['Date'].isnull().values == False]
    part2['Date_received'] = part2['Date_received'].map(lambda x: str(int(x)))
    part2['Date_received'] = pd.to_datetime(part2['Date_received'], format='%Y-%m-%d')
    part2['Date'] = part2['Date'].map(lambda x: str(int(x)))
    part2['Date'] = pd.to_datetime(part2['Date'],format='%Y-%m-%d')
                   # 转换为时间类型进行，对天数进行相加减
    part2['label'] = [0 if int(i.days) > 15 else 1 for i in (part2['Date']-part2['Date_received'])]
    ccf_offline_stage1_train = part1.append(part2)
    return ccf_offline_stage1_train

def split():
    row_train = mk_label()
    '数据预处理和数据集划分'
    row_train['Date_received'] = [str(i)[:10].replace('-','') for i in row_train['Date_received']]
    row_train['Date_received'] = row_train['Date_received'].map(lambda x:int(x))
    row_train['Distance'] = row_train['Distance'].fillna(-1)  # 缺失值填充
    row_train.rename(columns={'User_id' : 'user_id',
                              'Merchant_id' : 'merchant_id',
                              'Coupon_id' : 'coupon_id',
                              'Discount_rate' : 'discount_rate',
                              'Distance' : 'distance',
                              'Date_received' : 'date_received',
                              'Date' : 'date'},inplace=True)  # 原地替换，节省内存
    def getrate(x):
        if len(x)==2:
            x[0] = int(x[0])
            x[1] = int(x[1])
            tmp = (x[0] - x[1])/x[0]
            return tmp
    row_train['discount'] = row_train['discount_rate'].map(lambda x: x.split(':'))  # 筛选出满减类型
    row_train['dis_left'] = row_train['discount'].map(lambda x: int(x[0]) if len(x) == 2 else -1)
    row_train['dis_right'] = row_train['discount'].map(lambda x: int(x[1]) if len(x) == 2 else -1)
    row_train['dis_rate'] = row_train['discount'].map(lambda x: getrate(x))
    del row_train['discount']
    '按领券日期划分数据集'
    '训练集'
    train_feat = row_train[(row_train['date_received'] >= 20160401) & (row_train['date_received'] <= 20160530)]
    train_label = row_train[(row_train['date_received'] >= 20160601) & (row_train['date_received'] <= 20160630)]
    '测试集'
    test_feat = row_train[(row_train['date_received'] >= 20160501) & (row_train['date_received'] <= 20160630)]
    '线上提交区间数据处理'
    test_label = pd.read_csv('ccf_offline_stage1_test_revised.csv')
    test_label['Distance'] = test_label['Distance'].fillna(-1)
    test_label.rename(columns={'User_id' : 'user_id',
                              'Merchant_id' : 'merchant_id',
                              'Coupon_id' : 'coupon_id',
                              'Discount_rate' : 'discount_rate',
                              'Distance' : 'distance',
                              'Date_received' : 'date_received'},inplace=True)
    test_label['discount'] = test_label['discount_rate'].map(lambda x: x.split(':'))
    test_label['dis_left'] = test_label['discount'].map(lambda x: int(x[0]) if len(x) == 2 else -1)
    test_label['dis_right'] = test_label['discount'].map(lambda x: int(x[1]) if len(x) ==2 else -1)
    test_label['dis_rate'] = test_label['discount'].map(lambda x: getrate(x))
    del test_label['discount']  # 实现满减类型的分离转化，并删除原来的discount
    return train_feat, train_label, test_feat, test_label

def featgen_train():
    '训练集特征生成'
    feat = split()[0]
    label = split()[1]
    label = FeatSection(data=feat,label=label)
    label = LabelSection(label=label)
    label = label.fillna(-1)
    return label

def featgen_test():
    '测试集特征生成'
    feat = split()[2]
    label = split()[3]
    label = FeatSection(data=feat,label=label)
    label = LabelSection(label=label)
    label = label.fillna(-1)
    return label


def XgbTest(train,test):
    train_x = train.drop(['user_id','merchant_id','coupon_id','date_received','discount_rate','date','label'],axis=1)
    train_y = train['label']
    test_id = test[['user_id','coupon_id','date_received']]
    test_x = test.drop(['user_id','merchant_id','coupon_id','date_received','discount_rate',],axis=1)
    # xgb矩阵赋值
    xgb_train = xgb.DMatrix(train_x,label=train_y.values)
    xgb_test = xgb.DMatrix(test_x)
    params = {'booster' : 'gbtree',  # 基于树模型
              'objective' : 'binary:logistic',  # 二分类逻辑回归
              'eta' : '0.01',   # 学习率，通过减少每一步的权重，提高模型的鲁棒性
              'eval_metric' : 'auc',  # 模型的评估指标
              'subsample' : 0.8,   # 控制每个树随机采样的比例
              'colsample_bytree' : 0.8,  # 控制每个树随机采样的例数（特征）的占比
              'scale_pos_weight' : 1,   # 在样本不平衡时>0,使算法更快收敛
              'min_child_weight' : 18,  # 最小样本权重的和，用于避免过拟合
              }
    model = xgb.train(params,xgb_train,num_boost_round=1200)
    result = model.predict(xgb_test)
    test_id['Probability'] = result
    test_id.rename(columns={'user_id' : 'User_id',
                            'coupon_id' : 'Coupon_id',
                            'date_received' : 'Date_received'},inplace=True)
    test_id.to_csv('xgb.csv',index=False)
    plot_importance(model)
    plt.show()

def Xgb():
    train = featgen_train()
    test = featgen_test()
    XgbTest(train=train, test=test)

if __name__=='__main__':
    Xgb()