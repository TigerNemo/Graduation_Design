package com.example.demo.service;

import com.example.demo.common.Result;
import org.springframework.stereotype.Service;

@Service
public interface EverydayConsumeService {
    Result<?> get();
}
