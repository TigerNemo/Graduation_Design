import pymysql
import pandas as pd
from pymysql.constants import CLIENT


class DataBase:

    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="nemo", database="o2o",
                                  client_flag=CLIENT.MULTI_STATEMENTS)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()

    def show_tables(self):  # 查看表中的数据
        self.cursor.execute("show tables from o2o")
        datas = self.cursor.fetchall()
        for data in datas:
            print(data[0])

    '创建原始数据表'

    def create_database_ccf_offline_stage1_train(self):
        self.cursor.execute("drop table if exists ccf_offline_stage1_train")
        sql = """
            create table ccf_offline_stage1_train (
            user_id varchar(20) ,
            merchant_id varchar(20),
            coupon_id varchar(20),
            discount_rate varchar(20),
            distance int,
            date_received date,
            date date
            )
        """
        self.cursor.execute(sql)

    '创建有效数据表'

    def create_database_row_train(self):
        self.cursor.execute("drop table if exists row_train")
        sql = """
        create table row_train (
            user_id varchar(20) ,
            merchant_id varchar(20),
            coupon_id varchar(20),
            discount_rate varchar(20),
            distance int,
            date_received date,
            date date,
            label int)
        """
        self.cursor.execute(sql)

    '创建大屏数据表'

    def create_database_title_data(self):
        self.cursor.execute("drop table if exists title_data")
        sql = """
        create table title_data (
            record_count int,
            user_count int,
            merchant_count int,
            coupon_count int,
            received_coupon int,
            date_count int)
        """
        self.cursor.execute(sql)

    '创建每天被消费的数量统计表'

    def create_database_everyday_consume(self):
        self.cursor.execute("drop table if exists everyday_consume")
        sql = """
        create table everyday_consume (
            date DATE,
            consume_count int)
        """
        self.cursor.execute(sql)

    '创建每天被核销的数量统计表'

    def create_database_everyday_date(self):
        self.cursor.execute("drop table if exists everyday_date")
        sql = """
        create table everyday_date (
        date DATE,
        date_count int)
        """
        self.cursor.execute(sql)

    '创建每天被领取的数量统计表'

    def create_database_everyday_received(self):
        self.cursor.execute("drop table if exists everyday_received")
        sql = """
        create table everyday_received (
        date_received DATE,
        received_count int)
        """
        self.cursor.execute(sql)

    '创建消费距离分析表'

    def create_database_distance_date(self):
        self.cursor.execute("drop table if exists distance_date")
        sql = """
        create table distance_date (
        distance int,
        date_rate float)
        """
        self.cursor.execute(sql)

    '创建周领券数与核销数统计表'

    def create_database_weekday_received_date(self):
        self.cursor.execute("drop table if exists weekday_received_date")
        sql = """
        create table weekday_received_date (
        weekday int,
        received int,
        date int)
        """
        self.cursor.execute(sql)

    '创建消费距离分析表'

    def create_database_distance_consume(self):
        self.cursor.execute("drop table if exists distance_consume")
        sql = """
        create table distance_consume (
        distance int,
        consume_count int)
        """
        self.cursor.execute(sql)

    '创建月优惠券使用情况统计表'

    def create_database_month_received_date_consume(self):
        self.cursor.execute("drop table if exists month_received_date_consume")
        sql = """
        create table month_received_date_consume (
        month int,
        date_count int,
        received_count int,
        consume_count int)
        """
        self.cursor.execute(sql)

    '饼状图数据统计表'

    def create_database_pie_data(self):
        self.cursor.execute("drop table if exists pie_data")
        sql = """
        create table pie_data (
        full_munis_count int,
        discount_count int,
        full_munis_date int,
        discount_date int,
        label_1 int,
        label_0 int)
        """
        self.cursor.execute(sql)

    def insert_into_ccf_offline_stage1_train(self, user_id, merchant_id, coupon_id, discount_rate, distance,
                                             date_received, date):
        self.create_database_ccf_offline_stage1_train()
        sql = "INSERT INTO ccf_offline_stage1_train (user_id, merchant_id, coupon_id, discount_rate, distance, date_received, date) \
       VALUES ('%s', '%s', '%s', '%s', %s, %s, %s)" % (
        user_id, merchant_id, coupon_id, discount_rate, distance, date_received, date)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def insert_into_row_train(self, user_id, merchant_id, coupon_id, discount_rate, distance, date_received, date,
                              label):
        self.create_database_row_train()
        sql = "INSERT INTO row_train (user_id, merchant_id, coupon_id, discount_rate, distance, date_received, date, label) \
               VALUES ('%s', '%s', '%s', '%s', %s, %s, %s, %s)" % (
            user_id, merchant_id, coupon_id, discount_rate, distance, date_received, date, label)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def insert_into_title_data(self, record_count, user_count, merchant_count, coupon_count, received_coupon,
                               date_count):
        self.create_database_title_data()
        sql = "INSERT INTO title_data (record_count, user_count, merchant_count, coupon_count, received_coupon, date_count) \
                       VALUES (%s, %s, %s, %s, %s, %s)" % (
            record_count, user_count, merchant_count, coupon_count, received_coupon, date_count)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def insert_into_everyday_consume(self, date, consume_count):
        self.create_database_everyday_consume()
        sql = "INSERT INTO everyday_consume (date, consume_count) VALUES (%s, %s)" % (date, consume_count)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def insert_into_everyday_date(self, date, date_count):
        self.create_database_everyday_date()
        sql = "INSERT INTO everyday_date (date, date_count) VALUES (%s, %s)" % (date, date_count)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def insert_into_everyday_received(self, date_received, received_count):
        self.create_database_everyday_received()
        sql = "INSERT INTO everyday_received (date_received, received_count) VALUES (%s, %s)" \
              % (date_received, received_count)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def insert_into_distance_date(self, distance, date_rate):
        self.create_database_distance_date()
        sql = "INSERT INTO distance_date (distance, date_rate) VALUES (%s, %s)" % (distance, date_rate)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def insert_into_weekday_received_date(self, weekday, received, date):
        self.create_database_weekday_received_date()
        sql = "INSERT INTO weekday_received_date (weekday, received, date) VALUES (%s, %s, %s)" \
              % (weekday, received, date)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def insert_into_distance_consume(self, distance, consume_count):
        self.create_database_distance_consume()
        sql = "INSERT INTO distance_consume (distance, consume_count) VALUES (%s, %s)" \
              % (distance, consume_count)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def insert_into_month_received_date_consume(self, month, date_count, received_count, consume_count):
        self.create_database_month_received_date_consume()
        sql = "INSERT INTO month_received_date_consume (month, date_count, received_count, consume_count)" \
              " VALUES (%s, %s, %s, %s)" % (month, date_count, received_count, consume_count)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def insert_into_pie_data(self, full_munis_count, discount_count, full_munis_date, discount_date, label_1, label_0):
        self.create_database_pie_data()
        sql = "INSERT INTO pie_data (full_munis_count, discount_count, full_munis_date, discount_date, label_1, label_0)" \
              " VALUES (%s, %s, %s, %s, %s, %s)" % (
              full_munis_count, discount_count, full_munis_date, discount_date, label_1, label_0)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def select(self, table):
        sql = "select * from %s" % table
        try:
            print("=====正在读取数据=====")
            df1 = pd.read_sql(sql, self.db)
            return df1
        except:
            print("无法查询到数据！")
            return None

    def ccf_offline_train_To_row_train(self):
        # 原始数据清洗完后导入有效数据表
        # 筛选出是否使用领取优惠券的用户，即正负样本
        # 用户有领取优惠券但没有核销，负样本，标0
        # 用户在领取优惠券后15天内使用则为正样本（标1），否则为负样本
        sql = """
        select *
        from (select *,if(datediff(date,date_received)<=15, 1, 0) as label
        from ccf_offline_stage1_train) as t1
        """
        try:
            print("=====数据正在写入row_train=====")
            df1 = pd.read_sql(sql, self.db)
            return df1
        except:
            print("无法查询到数据！")
            return None
        pass

    '大屏基础数据'

    def select_title_data(self):
        # 总记录次数
        sql_record_count = """
        select count(*) from row_train
        """
        # 用户个数
        sql_user_count = """
        select count(*)
        from (select user_id from row_train
        where user_id!='null' group by user_id) as t1
        """
        # 商家个数
        sql_merchant_count = """
        select count(*)
        from (select merchant_id from row_train
        where merchant_id!='null' group by merchant_id) as t1;
        """
        # 优惠券种类
        sql_coupon_count = """
        select count(*)
        from (select coupon_id from row_train
        where coupon_id!='null' group by coupon_id) as t1
        """
        # 优惠券领取次数
        sql_received_count = """
        select count(*) from row_train
        where date_received is not null
        """
        # 优惠券核销次数
        sql_date_count = """
        select count(*) from row_train
        where date is not null and date_received is not null
        """
        try:
            self.cursor.execute(sql_record_count)
            data = self.cursor.fetchall()
            record_count = int(data[0][0])

            self.cursor.execute(sql_user_count)
            data = self.cursor.fetchall()
            user_count = int(data[0][0])

            self.cursor.execute(sql_merchant_count)
            data = self.cursor.fetchall()
            merchant_count = int(data[0][0])

            self.cursor.execute(sql_coupon_count)
            data = self.cursor.fetchall()
            coupon_count = int(data[0][0])

            self.cursor.execute(sql_received_count)
            data = self.cursor.fetchall()
            received_count = int(data[0][0])

            self.cursor.execute(sql_date_count)
            data = self.cursor.fetchall()
            date_count = int(data[0][0])

            return record_count, user_count, merchant_count, coupon_count, received_count, date_count
        except:
            print("大屏基础数据异常！")

    '每天被消费的数量'

    def select_everyday_consume(self):
        sql_everyday_consume = """
        select date, count(*) as consume_count
        from (select * from row_train where date is not null) as t1 group by date order by date asc 
        """
        try:
            df = pd.read_sql(sql_everyday_consume, self.db)
            return df
        except:
            print("无法查询到数据！")
        pass

    '每天被核销的数量'

    def select_everyday_date(self):
        sql_everyday_date = """
        select date, count(*) as date_count
        from (select * from row_train where label=1) as t1 group by date order by date asc 
        """
        try:
            df = pd.read_sql(sql_everyday_date, self.db)
            return df
        except:
            print("无法查询到数据！")

    '每天被领券的数量'

    def select_everyday_received(self):
        sql_everyday_received = """
        select date_received, count(*) as received_count
        from (select * from row_train where date_received is not null ) as t1
        group by date_received order by date_received asc 
        """
        try:
            df = pd.read_sql(sql_everyday_received, self.db)
            return df
        except:
            print("无法查询到数据！")

    '消费距离与核销率'

    def select_distance_date(self):
        sql_distance_date = """
        select t1.distance as distance, (t2.领取数/t1.总数) as date_rate
        from (select distance, count(*) as '总数' from row_train
        where distance!=-1 group by distance order by distance) as t1
        left join (select distance, count(*) as '领取数' from row_train
        where distance!=-1 and label=1 group by distance order by distance) as t2
        on t1.distance=t2.distance
        """
        try:
            df = pd.read_sql(sql_distance_date, self.db)
            return df
        except:
            print("无法查询到数据！")

    '周领券数与核销数'

    def select_weekday_received_date(self):
        sql_Monday_received = """
        select count(*) from row_train where (dayofweek(date_received)=2)
        """
        sql_Monday_date = """
        select count(*) from row_train where label=1 and (dayofweek(date_received)=2)
        """
        sql_Tuesday_received = """
        select count(*) from row_train where (dayofweek(date_received)=3)
        """
        sql_Tuesday_date = """
        select count(*) from row_train where label=1 and (dayofweek(date_received)=3)
        """
        sql_Wednesday_received = """
        select count(*) from row_train where (dayofweek(date_received)=4)
        """
        sql_Wednesday_date = """
        select count(*) from row_train where label=1 and (dayofweek(date_received)=4)
        """
        sql_Thursday_received = """
        select count(*) from row_train where (dayofweek(date_received)=5)
        """
        sql_Thursday_date = """
        select count(*) from row_train where label=1 and (dayofweek(date_received)=5)
        """
        sql_Friday_received = """
        select count(*) from row_train where (dayofweek(date_received)=6)
        """
        sql_Friday_date = """
        select count(*) from row_train where label=1 and (dayofweek(date_received)=6)
        """
        sql_Saturday_received = """
        select count(*) from row_train where (dayofweek(date_received)=7)
        """
        sql_Saturday_date = """
        select count(*) from row_train where label=1 and (dayofweek(date_received)=7)
        """
        sql_Sunday_received = """
        select count(*) from row_train where (dayofweek(date_received)=1)
        """
        sql_Sunday_date = """
        select count(*) from row_train where label=1 and (dayofweek(date_received)=1)
        """
        try:
            self.cursor.execute(sql_Monday_received)
            data = self.cursor.fetchall()
            Monday_received = data[0][0]
            self.cursor.execute(sql_Monday_date)
            data = self.cursor.fetchall()
            Monday_date = data[0][0]

            self.cursor.execute(sql_Tuesday_received)
            data = self.cursor.fetchall()
            Tuesday_received = data[0][0]
            self.cursor.execute(sql_Tuesday_date)
            data = self.cursor.fetchall()
            Tuesday_date = data[0][0]

            self.cursor.execute(sql_Wednesday_received)
            data = self.cursor.fetchall()
            Wednesday_received = data[0][0]
            self.cursor.execute(sql_Wednesday_date)
            data = self.cursor.fetchall()
            Wednesday_date = data[0][0]

            self.cursor.execute(sql_Thursday_received)
            data = self.cursor.fetchall()
            Thursday_received = data[0][0]
            self.cursor.execute(sql_Thursday_date)
            data = self.cursor.fetchall()
            Thursday_date = data[0][0]

            self.cursor.execute(sql_Friday_received)
            data = self.cursor.fetchall()
            Friday_received = data[0][0]
            self.cursor.execute(sql_Friday_date)
            data = self.cursor.fetchall()
            Friday_date = data[0][0]

            self.cursor.execute(sql_Saturday_received)
            data = self.cursor.fetchall()
            Saturday_received = data[0][0]
            self.cursor.execute(sql_Saturday_date)
            data = self.cursor.fetchall()
            Saturday_date = data[0][0]

            self.cursor.execute(sql_Sunday_received)
            data = self.cursor.fetchall()
            Sunday_received = data[0][0]
            self.cursor.execute(sql_Sunday_date)
            data = self.cursor.fetchall()
            Sunday_date = data[0][0]

            week = [[1, Monday_received, Monday_date],
                    [2, Tuesday_received, Tuesday_date],
                    [3, Wednesday_received, Wednesday_date],
                    [4, Thursday_received, Thursday_date],
                    [5, Friday_received, Friday_date],
                    [6, Saturday_received, Saturday_date],
                    [7, Sunday_received, Sunday_date]]
            return week
        except:
            print("无法查询到数据！")
        pass

    '消费距离分析'

    def select_distance_consume(self):
        sql_distance_consume = """
        select distance, count(*) as consume_count from row_train where distance!=-1 group by distance order by distance
        """
        try:
            df = pd.read_sql(sql_distance_consume, self.db)
            return df
        except:
            print("无法查询到数据！")

    '月优惠券使用情况'

    def select_month_received_date_consume(self):
        sql_January_received = """
        select count(*) from row_train where (month(date_received)=1)
        """
        sql_January_date = """
        select count(*) from row_train where (label=1) and (month(date_received)=1)
        """
        sql_January_consume = """
        select count(*) from row_train where (month(date)=1)
        """
        sql_February_received = """
        select count(*) from row_train where (month(date_received)=2)
        """
        sql_February_date = """
        select count(*) from row_train where (label=1) and (month(date_received)=2)
        """
        sql_February_consume = """
        select count(*) from row_train where (month(date)=2)
        """
        sql_March_received = """
        select count(*) from row_train where (month(date_received)=3)
        """
        sql_March_date = """
        select count(*) from row_train where (label=1) and (month(date_received)=3)
        """
        sql_March_consume = """
        select count(*) from row_train where (month(date)=3)
        """
        sql_April_received = """
        select count(*) from row_train where (month(date_received)=4)
        """
        sql_April_date = """
        select count(*) from row_train where (label=1) and (month(date_received)=4)
        """
        sql_April_consume = """
        select count(*) from row_train where (month(date)=4)
        """
        sql_May_received = """
        select count(*) from row_train where (month(date_received)=5)
        """
        sql_May_date = """
        select count(*) from row_train where (label=1) and (month(date_received)=5)
        """
        sql_May_consume = """
        select count(*) from row_train where (month(date)=5)
        """
        sql_June_received = """
        select count(*) from row_train where (month(date_received)=6)
        """
        sql_June_date = """
        select count(*) from row_train where (label=1) and (month(date_received)=6)
        """
        sql_June_consume = """
        select count(*) from row_train where (month(date)=6)
        """
        try:
            self.cursor.execute(sql_January_received)
            data = self.cursor.fetchall()
            January_received = data[0][0]
            self.cursor.execute(sql_January_date)
            data = self.cursor.fetchall()
            January_date = data[0][0]
            self.cursor.execute(sql_January_consume)
            data = self.cursor.fetchall()
            January_consume = data[0][0]

            self.cursor.execute(sql_February_received)
            data = self.cursor.fetchall()
            February_received = data[0][0]
            self.cursor.execute(sql_February_date)
            data = self.cursor.fetchall()
            February_date = data[0][0]
            self.cursor.execute(sql_February_consume)
            data = self.cursor.fetchall()
            February_consume = data[0][0]

            self.cursor.execute(sql_March_received)
            data = self.cursor.fetchall()
            March_received = data[0][0]
            self.cursor.execute(sql_March_date)
            data = self.cursor.fetchall()
            March_date = data[0][0]
            self.cursor.execute(sql_March_consume)
            data = self.cursor.fetchall()
            March_consume = data[0][0]

            self.cursor.execute(sql_April_received)
            data = self.cursor.fetchall()
            April_received = data[0][0]
            self.cursor.execute(sql_April_date)
            data = self.cursor.fetchall()
            April_date = data[0][0]
            self.cursor.execute(sql_April_consume)
            data = self.cursor.fetchall()
            April_consume = data[0][0]

            self.cursor.execute(sql_May_received)
            data = self.cursor.fetchall()
            May_received = data[0][0]
            self.cursor.execute(sql_May_date)
            data = self.cursor.fetchall()
            May_date = data[0][0]
            self.cursor.execute(sql_May_consume)
            data = self.cursor.fetchall()
            May_consume = data[0][0]

            self.cursor.execute(sql_June_received)
            data = self.cursor.fetchall()
            June_received = data[0][0]
            self.cursor.execute(sql_June_date)
            data = self.cursor.fetchall()
            June_date = data[0][0]
            self.cursor.execute(sql_June_consume)
            data = self.cursor.fetchall()
            June_consume = data[0][0]

            datas = [[1, January_date, January_received, January_consume],
                     [2, February_date, February_received, February_consume],
                     [3, March_date, March_received, March_consume],
                     [4, April_date, April_received, April_consume],
                     [5, May_date, May_received, May_consume],
                     [6, June_date, June_received, June_consume]]
            return datas
        except:
            print("无法查询到数据！")

    '饼状图数据'

    def select_pie_data(self):
        # 优惠券数量占比
        sql_full_munis_count = """
        select count(*) from row_train where discount_rate!='null' and discount_rate like '%:%' 
        """
        sql_discount_count = """
        select count(*) from row_train where discount_rate!='null' and discount_rate not like '%:%' 
        """
        self.cursor.execute(sql_full_munis_count)
        data = self.cursor.fetchall()
        full_munis_count = data[0][0]
        self.cursor.execute(sql_discount_count)
        data = self.cursor.fetchall()
        discount_count = data[0][0]

        # 核销优惠券占比
        sql_full_munis_date = """
        select count(*) from row_train
        where discount_rate!='null' and discount_rate like '%:%' and label=1 
        """
        sql_discount_date = """
        select count(*) from row_train
        where discount_rate!='null' and discount_rate not like '%:%' and label=1 
        """
        self.cursor.execute(sql_full_munis_date)
        data = self.cursor.fetchall()
        full_munis_date = data[0][0]
        self.cursor.execute(sql_discount_date)
        data = self.cursor.fetchall()
        discount_date = data[0][0]

        # 正-负比例
        sql_label_1 = """
        select count(*) from row_train where label=1 
        """
        sql_label_0 = """
        select count(*) from row_train where label!=1
        """
        self.cursor.execute(sql_label_1)
        data = self.cursor.fetchall()
        label_1 = data[0][0]
        self.cursor.execute(sql_label_0)
        data = self.cursor.fetchall()
        label_0 = data[0][0]

        return full_munis_count, discount_count, full_munis_date, discount_date, label_1, label_0


def store_ccf_offline_train():
    # 将原始数据通过简单处理，读入到原始数据表
    # 主要进行格式转换和缺失值填充
    ccf_offline_stage1_train = pd.read_csv('ccf_offline_stage1_train.csv')
    database = DataBase()
    for index, row in ccf_offline_stage1_train.iterrows():
        UserId = "null" if pd.isnull(row['User_id']) else str(int(row['User_id']))
        MerchantId = "null" if pd.isnull(row['Merchant_id']) else str(int(row['Merchant_id']))
        CouponId = "null" if pd.isnull(row['Coupon_id']) else str(int(row['Coupon_id']))
        DiscountRate = "null" if pd.isnull(row['Discount_rate']) else str(row['Discount_rate'])
        Distance = -1 if pd.isnull(row['Distance']) else int(row['Distance'])
        Date_received = "null" if pd.isnull(row['Date_received']) else str(int(row['Date_received']))
        Date = "null" if pd.isnull(row['Date']) else str(int(row['Date']))
        database.insert_into_ccf_offline_stage1_train(UserId, MerchantId, CouponId, DiscountRate, Distance,
                                                      Date_received, Date)
        print(UserId, MerchantId, CouponId, DiscountRate, Distance, Date_received, Date)
    pass


def store_row_train():
    # 清洗无效数据并划分标签，将数据写入有效数据表
    count = 0
    database = DataBase()
    ccf_offline_stage1_train = database.ccf_offline_train_To_row_train()
    for index, row in ccf_offline_stage1_train.iterrows():
        count += 1
        # print(str(row['date_received']).replace('-',''))
        UserId = "null" if pd.isnull(row['user_id']) else str(row['user_id'])
        MerchantId = "null" if pd.isnull(row['merchant_id']) else str(row['merchant_id'])
        CouponId = "null" if pd.isnull(row['coupon_id']) else str(row['coupon_id'])
        DiscountRate = "null" if pd.isnull(row['discount_rate']) else str(row['discount_rate'])
        Distance = -1 if pd.isnull(row['distance']) else int(row['distance'])
        Date_received = "null" if pd.isnull(row['date_received']) else str(row['date_received']).replace("-", "")
        Date = "null" if pd.isnull(row['date']) else str(row['date']).replace("-", "")
        Label = int(row['label'])
        database.insert_into_row_train(UserId, MerchantId, CouponId, DiscountRate, Distance, Date_received, Date, Label)
        print(count)


def store_title_data():
    database = DataBase()
    record_count, user_count, merchant_count, coupon_count, received_count, date_count = database.select_title_data()
    database.insert_into_title_data(record_count, user_count, merchant_count, coupon_count, received_count, date_count)


def store_everyday_consume():
    database = DataBase()
    everyday_consume = database.select_everyday_consume()
    for index, row in everyday_consume.iterrows():
        date = str(row['date']).replace("-", "")
        consume_count = int(row['consume_count'])
        database.insert_into_everyday_consume(date, consume_count)


def store_everyday_date():
    database = DataBase()
    everyday_date = database.select_everyday_date()
    for index, row in everyday_date.iterrows():
        date = str(row['date']).replace("-", "")
        date_count = int(row['date_count'])
        database.insert_into_everyday_date(date, date_count)


def store_everyday_received():
    database = DataBase()
    everyday_received = database.select_everyday_received()
    for index, row in everyday_received.iterrows():
        date_received = str(row['date_received']).replace("-", "")
        received_count = int(row['received_count'])
        database.insert_into_everyday_received(date_received, received_count)


def store_distance_date():
    database = DataBase()
    distance_date = database.select_distance_date()
    for index, row in distance_date.iterrows():
        distance = int(row['distance'])
        date_rate = float(row['date_rate'])
        database.insert_into_distance_date(distance, date_rate)


def store_weekday_received_date():
    database = DataBase()
    weekday_received_date = database.select_weekday_received_date()
    for data in weekday_received_date:
        weekday = data[0]
        received = data[1]
        date = data[2]
        database.insert_into_weekday_received_date(weekday, received, date)


def store_distance_consume():
    database = DataBase()
    distance_consume = database.select_distance_consume()
    for index, row in distance_consume.iterrows():
        distance = int(row['distance'])
        consume_count = int(row['consume_count'])
        database.insert_into_distance_consume(distance, consume_count)


def store_month_received_date_consume():
    database = DataBase()
    month_received_date_consume = database.select_month_received_date_consume()
    for data in month_received_date_consume:
        month = data[0]
        date_count = data[1]
        received_count = data[2]
        consume_count = data[3]
        database.insert_into_month_received_date_consume(month, date_count, received_count, consume_count)


def store_pie_data():
    database = DataBase()
    full_munis_count, discount_count, full_munis_date, discount_date, label_1, label_0 = database.select_pie_data()
    database.insert_into_pie_data(full_munis_count, discount_count, full_munis_date, discount_date, label_1, label_0)


def save():
    """将数据通过计算和清晰，持久化到数据库"""
    store_ccf_offline_train()
    store_row_train()
    store_title_data()
    store_everyday_consume()
    store_everyday_date()
    store_everyday_received()
    store_distance_date()
    store_weekday_received_date()
    store_distance_consume()
    store_month_received_date_consume()
    store_pie_data()


if __name__ == '__main__':
    # save()
    pass

