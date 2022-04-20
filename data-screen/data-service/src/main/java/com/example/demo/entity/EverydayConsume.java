package com.example.demo.entity;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.util.Date;

@TableName("everyday_consume")
@Data
public class EverydayConsume {
    private Date date;
    private Integer consume_count;
}
