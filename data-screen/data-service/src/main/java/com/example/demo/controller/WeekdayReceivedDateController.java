package com.example.demo.controller;

import com.example.demo.common.Result;
import com.example.demo.service.serviceImpl.WeekdayReceivedDateServiceImpl;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;

@RestController
@RequestMapping("/WeekdayReceivedDate")
public class WeekdayReceivedDateController {
    @Resource
    WeekdayReceivedDateServiceImpl weekdayReceivedDateService;

    @GetMapping
    public Result<?> get() {
        return weekdayReceivedDateService.get();
    }
}
