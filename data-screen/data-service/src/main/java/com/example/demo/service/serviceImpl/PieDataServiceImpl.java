package com.example.demo.service.serviceImpl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.example.demo.common.Result;
import com.example.demo.entity.PieData;
import com.example.demo.mapper.PieDataMapper;
import com.example.demo.service.PieDataService;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.ArrayList;
import java.util.List;

@Service
public class PieDataServiceImpl implements PieDataService {
    @Resource
    PieDataMapper pieDataMapper;

    @Override
    public Result<?> get() {
        ArrayList<List<Object>> resultList = new ArrayList<>();
        QueryWrapper<PieData> queryWrapper = new QueryWrapper<>();
        queryWrapper.select("full_munis_count");
        List<Object> full_munis_count = pieDataMapper.selectObjs(queryWrapper);
        resultList.add(full_munis_count);
        queryWrapper.select("discount_count");
        List<Object> discount_count = pieDataMapper.selectObjs(queryWrapper);
        resultList.add(discount_count);
        queryWrapper.select("full_munis_date");
        List<Object> full_munis_date = pieDataMapper.selectObjs(queryWrapper);
        resultList.add(full_munis_date);
        queryWrapper.select("discount_date");
        List<Object> discount_date = pieDataMapper.selectObjs(queryWrapper);
        resultList.add(discount_date);
        queryWrapper.select("label_1");
        List<Object> label_1 = pieDataMapper.selectObjs(queryWrapper);
        resultList.add(label_1);
        queryWrapper.select("label_0");
        List<Object> label_0 = pieDataMapper.selectObjs(queryWrapper);
        resultList.add(label_0);
        return Result.success(resultList);
    }
}
