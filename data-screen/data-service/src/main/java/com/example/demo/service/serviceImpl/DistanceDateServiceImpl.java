package com.example.demo.service.serviceImpl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.example.demo.common.Result;
import com.example.demo.entity.DistanceDate;
import com.example.demo.mapper.DistanceDateMapper;
import com.example.demo.service.DistanceDateService;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.ArrayList;
import java.util.List;

@Service
public class DistanceDateServiceImpl implements DistanceDateService {
    @Resource
    DistanceDateMapper distanceDateMapper;

    @Override
    public Result<?> get() {
        ArrayList<List<Object>> resultList = new ArrayList<>();
        QueryWrapper<DistanceDate> queryWrapper = new QueryWrapper<>();
        queryWrapper.select("distance");
        List<Object> distance = distanceDateMapper.selectObjs(queryWrapper);
        resultList.add(distance);
        queryWrapper.select("date_rate");
        List<Object> dateRate = distanceDateMapper.selectObjs(queryWrapper);
        resultList.add(dateRate);
        return Result.success(resultList);
    }
}
