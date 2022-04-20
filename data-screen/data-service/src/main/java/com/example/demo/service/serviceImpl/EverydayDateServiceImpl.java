package com.example.demo.service.serviceImpl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.example.demo.common.Result;
import com.example.demo.entity.EverydayDate;
import com.example.demo.mapper.EverydayDateMapper;
import com.example.demo.service.EverydayDateService;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.ArrayList;
import java.util.List;

@Service
public class EverydayDateServiceImpl implements EverydayDateService {
    @Resource
    EverydayDateMapper everydayDateMapper;

    @Override
    public Result<?> get() {
        ArrayList<List<Object>> resultList = new ArrayList<>();
        QueryWrapper<EverydayDate> queryWrapper = new QueryWrapper<>();
        queryWrapper.select("date");
        List<Object> date = everydayDateMapper.selectObjs(queryWrapper);
        List<Object> mid_date = new ArrayList<>();
        for (Object str : date) {
            mid_date.add(str.toString().replaceAll("-","."));
        }
        resultList.add(mid_date);
        queryWrapper.select("date_count");
        List<Object> dateCount = everydayDateMapper.selectObjs(queryWrapper);
        resultList.add(dateCount);
        return Result.success(resultList);
    }
}
