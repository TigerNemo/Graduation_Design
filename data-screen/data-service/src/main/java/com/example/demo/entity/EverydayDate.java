package com.example.demo.entity;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.util.Date;

@TableName("everyday_date")
@Data
public class EverydayDate {
    private Date date;
    private Integer date_count;
}
