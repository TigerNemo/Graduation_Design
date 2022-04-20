package com.example.demo.service.serviceImpl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.example.demo.common.Result;
import com.example.demo.entity.TitleData;
import com.example.demo.mapper.TitleDataMapper;
import com.example.demo.service.TitleDataService;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.ArrayList;
import java.util.List;

@Service
public class TitleDataServiceImpl implements TitleDataService {
    @Resource
    TitleDataMapper titleDataMapper;

    @Override
    public Result<?> get() {
        ArrayList<Integer> resultList = new ArrayList<>();
        QueryWrapper<TitleData> queryWrapper = new QueryWrapper<>();
        queryWrapper.select("record_count");
        List<Object> record_count = titleDataMapper.selectObjs(queryWrapper);
        resultList.add((Integer) record_count.get(0));
        queryWrapper.select("user_count");
        List<Object> user_count = titleDataMapper.selectObjs(queryWrapper);
        resultList.add((Integer) user_count.get(0));
        queryWrapper.select("merchant_count");
        List<Object> merchant_count = titleDataMapper.selectObjs(queryWrapper);
        resultList.add((Integer) merchant_count.get(0));
        queryWrapper.select("coupon_count");
        List<Object> coupon_count = titleDataMapper.selectObjs(queryWrapper);
        resultList.add((Integer) coupon_count.get(0));
        queryWrapper.select("received_coupon");
        List<Object> received_coupon = titleDataMapper.selectObjs(queryWrapper);
        resultList.add((Integer) received_coupon.get(0));
        queryWrapper.select("date_count");
        List<Object> date_count = titleDataMapper.selectObjs(queryWrapper);
        resultList.add((Integer) date_count.get(0));
        return Result.success(resultList);
    }
}
