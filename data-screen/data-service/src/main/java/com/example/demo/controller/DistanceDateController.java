package com.example.demo.controller;

import com.example.demo.common.Result;
import com.example.demo.service.serviceImpl.DistanceDateServiceImpl;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;

@RestController
@RequestMapping("/DistanceDate")
public class DistanceDateController {

    @Resource
    DistanceDateServiceImpl distanceDateService;


    @GetMapping
    public Result<?> get() {
        return distanceDateService.get();
    }

}
