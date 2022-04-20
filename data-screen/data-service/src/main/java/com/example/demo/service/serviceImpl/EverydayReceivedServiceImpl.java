package com.example.demo.service.serviceImpl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.example.demo.common.Result;
import com.example.demo.entity.EverydayReceived;
import com.example.demo.mapper.EverydayReceivedMapper;
import com.example.demo.service.EverydayReceivedService;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.ArrayList;
import java.util.List;

@Service
public class EverydayReceivedServiceImpl implements EverydayReceivedService {
    @Resource
    EverydayReceivedMapper everydayReceivedMapper;

    @Override
    public Result<?> get() {
        ArrayList<List<Object>> resultList = new ArrayList<>();
        QueryWrapper<EverydayReceived> queryWrapper = new QueryWrapper<>();
        queryWrapper.select("date_received");
        List<Object> date_received = everydayReceivedMapper.selectObjs(queryWrapper);
        List<Object> mid_date = new ArrayList<>();
        for (Object str : date_received) {
            mid_date.add(str.toString().replaceAll("-","."));
        }
        resultList.add(mid_date);
        queryWrapper.select("received_count");
        List<Object> received_count = everydayReceivedMapper.selectObjs(queryWrapper);
        resultList.add(received_count);
        return Result.success(resultList);
    }
}
