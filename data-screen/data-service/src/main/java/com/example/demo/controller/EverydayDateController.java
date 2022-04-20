package com.example.demo.controller;

import com.example.demo.common.Result;
import com.example.demo.service.serviceImpl.EverydayDateServiceImpl;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;

@RestController
@RequestMapping("/EverydayDate")
public class EverydayDateController {
    @Resource
    EverydayDateServiceImpl everydayDateService;

    @GetMapping
    public Result<?> get() {
        return everydayDateService.get();
    }
}
