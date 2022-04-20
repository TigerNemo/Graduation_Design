package com.example.demo.controller;

import com.example.demo.common.Result;
import com.example.demo.service.serviceImpl.MonthReceivedDateConsumeServiceImpl;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;

@RestController
@RequestMapping("/MonthReceivedDateConsume")
public class MonthReceivedDateConsumeController {
    @Resource
    MonthReceivedDateConsumeServiceImpl monthReceivedDateConsumeService;

    @GetMapping
    public Result<?> get() {
        return monthReceivedDateConsumeService.get();
    }
}
