package com.example.demo.entity;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

@TableName("pie_data")
@Data
public class PieData {
    private Integer full_munis_count;
    private Integer discount_count;
    private Integer full_munis_date;
    private Integer discount_date;
    private Integer label_1;
    private Integer label_0;
}
