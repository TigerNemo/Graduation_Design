package com.example.demo.controller;

import com.example.demo.common.Result;
import com.example.demo.service.serviceImpl.DistanceConsumeServiceImpl;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;

@RestController
@RequestMapping("/DistanceConsume")
public class DistanceConsumeController {
    @Resource
    DistanceConsumeServiceImpl distanceConsumeService;

    @GetMapping
    public Result<?> get() {
        return distanceConsumeService.get();
    }
}
