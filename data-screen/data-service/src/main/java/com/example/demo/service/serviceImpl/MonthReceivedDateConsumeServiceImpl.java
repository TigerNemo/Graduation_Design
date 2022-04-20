package com.example.demo.service.serviceImpl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.example.demo.common.Result;
import com.example.demo.entity.MonthReceivedDateConsume;
import com.example.demo.mapper.MonthReceivedDateConsumeMapper;
import com.example.demo.service.MonthReceivedDateConsumeService;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.ArrayList;
import java.util.List;

@Service
public class MonthReceivedDateConsumeServiceImpl implements MonthReceivedDateConsumeService {
    @Resource
    MonthReceivedDateConsumeMapper monthReceivedDateConsumeMapper;

    @Override
    public Result<?> get() {
        ArrayList<List<Object>> resultList = new ArrayList<>();
        QueryWrapper<MonthReceivedDateConsume> queryWrapper = new QueryWrapper<>();
        queryWrapper.select("month");
        List<Object> weekday = monthReceivedDateConsumeMapper.selectObjs(queryWrapper);
        resultList.add(weekday);
        queryWrapper.select("date_count");
        List<Object> date_count = monthReceivedDateConsumeMapper.selectObjs(queryWrapper);
        resultList.add(date_count);
        queryWrapper.select("received_count");
        List<Object> received_count = monthReceivedDateConsumeMapper.selectObjs(queryWrapper);
        resultList.add(received_count);
        queryWrapper.select("consume_count");
        List<Object> consume_count = monthReceivedDateConsumeMapper.selectObjs(queryWrapper);
        resultList.add(consume_count);
        return Result.success(resultList);
    }
}
