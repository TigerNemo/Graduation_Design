package com.example.demo.entity;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.util.Date;

@TableName("everyday_received")
@Data
public class EverydayReceived {
    private Date date_received;
    private Integer received_count;
}
