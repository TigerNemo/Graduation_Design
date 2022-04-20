package com.example.demo.controller;

import com.example.demo.common.Result;
import com.example.demo.service.serviceImpl.PieDataServiceImpl;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;

@RestController
@RequestMapping("/PieData")
public class PieDataController {
    @Resource
    PieDataServiceImpl pieDataService;

    @GetMapping
    public Result<?> get() {
        return pieDataService.get();
    }
}
