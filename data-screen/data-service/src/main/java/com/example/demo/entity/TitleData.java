package com.example.demo.entity;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

@TableName("title_data")
@Data
public class TitleData {
    private Integer record_count;
    private Integer user_count;
    private Integer merchant_count;
    private Integer coupon_count;
    private Integer received_coupon;
    private Integer date_count;
}
