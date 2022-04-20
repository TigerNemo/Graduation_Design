package com.example.demo.controller;

import com.example.demo.common.Result;
import com.example.demo.service.serviceImpl.TitleDataServiceImpl;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;

@RestController
@RequestMapping("/TitleData")
public class TitleDataController {
    @Resource
    TitleDataServiceImpl titleDataService;

    @GetMapping
    public Result<?> get() {
        return titleDataService.get();
    }
}
