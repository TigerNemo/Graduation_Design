package com.example.demo.controller;

import com.example.demo.common.Result;
import com.example.demo.service.serviceImpl.EverydayConsumeServiceImpl;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;

@RestController
@RequestMapping("/EverydayConsume")
public class EverydayConsumeController {
    @Resource
    EverydayConsumeServiceImpl everydayConsumeService;

    @GetMapping
    public Result<?> get() {
        return everydayConsumeService.get();
    };
}
