package com.example.demo.entity;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

@TableName("distance_date")
@Data
public class DistanceDate {
    private Integer distance;
    private Float date_rate;
}
