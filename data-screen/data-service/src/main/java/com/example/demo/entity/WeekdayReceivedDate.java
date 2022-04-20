package com.example.demo.entity;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

@TableName("weekday_received_date")
@Data
public class WeekdayReceivedDate {
    private Integer weekday;
    private Integer received;
    private Integer date;
}
