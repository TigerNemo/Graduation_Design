package com.example.demo.service.serviceImpl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.example.demo.common.Result;
import com.example.demo.entity.DistanceConsume;
import com.example.demo.mapper.DistanceConsumeMapper;
import com.example.demo.service.DistanceConsumeService;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.ArrayList;
import java.util.List;

@Service
public class DistanceConsumeServiceImpl implements DistanceConsumeService {
    @Resource
    DistanceConsumeMapper distanceConsumeMapper;

    @Override
    public Result<?> get() {
        ArrayList<List<Object>> resultList = new ArrayList<>();
        QueryWrapper<DistanceConsume> queryWrapper = new QueryWrapper<>();
        queryWrapper.select("distance");
        List<Object> distance = distanceConsumeMapper.selectObjs(queryWrapper);
        resultList.add(distance);
        queryWrapper.select("consume_count");
        List<Object> consume_count = distanceConsumeMapper.selectObjs(queryWrapper);
        resultList.add(consume_count);
        return Result.success(resultList);
    }
}
