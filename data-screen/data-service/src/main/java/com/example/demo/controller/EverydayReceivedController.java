package com.example.demo.controller;

import com.example.demo.common.Result;
import com.example.demo.service.serviceImpl.EverydayReceivedServiceImpl;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;

@RestController
@RequestMapping("/EverydayReceived")
public class EverydayReceivedController {
    @Resource
    EverydayReceivedServiceImpl everydayReceivedService;

    @GetMapping
    public Result<?> get() {
        return everydayReceivedService.get();
    }

}
