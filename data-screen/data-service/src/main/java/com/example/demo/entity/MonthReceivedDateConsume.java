package com.example.demo.entity;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

@TableName("month_received_date_consume")
@Data
public class MonthReceivedDateConsume {
    private Integer month;
    private Integer date_count;
    private Integer received_count;
    private Integer consume_count;
}
