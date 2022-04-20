package com.example.demo.service.serviceImpl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.example.demo.common.Result;
import com.example.demo.entity.EverydayConsume;
import com.example.demo.mapper.EverydayConsumeMapper;
import com.example.demo.service.EverydayConsumeService;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.ArrayList;
import java.util.List;

@Service
public class EverydayConsumeServiceImpl implements EverydayConsumeService {
    @Resource
    EverydayConsumeMapper everydayConsumeMapper;


    @Override
    public Result<?> get() {
        ArrayList<List<Object>> resultList = new ArrayList<>();
        QueryWrapper<EverydayConsume> queryWrapper = new QueryWrapper<>();
        queryWrapper.select("date");
        List<Object> date = everydayConsumeMapper.selectObjs(queryWrapper);
        List<Object> mid_date = new ArrayList<>();
        for (Object str : date) {
            mid_date.add(str.toString().replaceAll("-","."));
        }
        resultList.add(mid_date);
        queryWrapper.select("consume_count");
        List<Object> consume = everydayConsumeMapper.selectObjs(queryWrapper);
        resultList.add(consume);
        return Result.success(resultList);
    }
}
