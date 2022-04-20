package com.example.demo.entity;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

@TableName("distance_consume")
@Data
public class DistanceConsume {
    private Integer distance;
    private Integer consume_count;
}
