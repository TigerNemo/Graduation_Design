package com.example.demo.service.serviceImpl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.example.demo.common.Result;
import com.example.demo.entity.WeekdayReceivedDate;
import com.example.demo.mapper.WeekdayReceivedDateMapper;
import com.example.demo.service.WeekdayReceivedDateService;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.ArrayList;
import java.util.List;

@Service
public class WeekdayReceivedDateServiceImpl implements WeekdayReceivedDateService {
    @Resource
    WeekdayReceivedDateMapper weekdayReceivedDateMapper;

    @Override
    public Result<?> get() {
        ArrayList<List<Object>> resultList = new ArrayList<>();
        QueryWrapper<WeekdayReceivedDate> queryWrapper = new QueryWrapper<>();
        queryWrapper.select("weekday");
        List<Object> weekday = weekdayReceivedDateMapper.selectObjs(queryWrapper);
        resultList.add(weekday);
        queryWrapper.select("received");
        List<Object> received = weekdayReceivedDateMapper.selectObjs(queryWrapper);
        resultList.add(received);
        queryWrapper.select("date");
        List<Object> date = weekdayReceivedDateMapper.selectObjs(queryWrapper);
        resultList.add(date);
        return Result.success(resultList);
    }
}
