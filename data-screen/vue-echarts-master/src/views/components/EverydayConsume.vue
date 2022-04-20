<template>
  <div class="EverydayConsume">
  </div>
</template>

<script>
import request from "@/utils/request";

export default {
  name: "EverydayConsume",
  data() {
    return {
      option: {
        tooltip: {
          trigger: 'axis',
          axisPointer: {            // 坐标轴指示器，坐标轴触发有效
            type: 'line'        // 默认为直线，可选为：'line' | 'shadow'
          },
          backgroundColor: '#11367a',
          textStyle: {
            color: '#6dd0e3',
            fontSize: 10,
          },
        },
        grid: {
          top: '12%',
          bottom: '12%',
          left: '9%',
          right: '5%',
        },
        legend: {
          right: '5%',
          top: '10%',
          itemWidth: 7,
          itemHeight: 7,
          textStyle: {
            color: '#5CB1C1',
          }
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          axisLabel: {
            color: '#61B9C8',
            fontSize: 10,
          },
          axisLine: {
            symbol: ['none', 'arrow'],
            symbolSize: [6, 6],
            symbolOffset: [0, 5],
            lineStyle: {
              color: '#122C49'
            }
          },
          axisTick: {
            color: '#122C49',
            inside: true
          },
          z: 2,
          data: []
        },
        yAxis:
            {
              type: 'value',
              interval: 2000,
              min: 0,
              max: 14000,
              splitNumber: 7,
              axisLine: {
                symbol: ['none', 'arrow'],
                symbolSize: [6, 6],
                lineStyle: {
                  color: '#122C49'
                }
              },
              axisLabel: {
                color: '#61B9C8',
                showMaxLabel: false,
                fontSize: 10
              },
              splitLine: {
                show: false,
              },
              name: '(个)',
              nameGap: -10,
              nameTextStyle: {
                color: '#61B9C8',
                fontSize: 9,
                align: 'right',
                padding: [0, 6, 0, 0]
              },
            },
        series: [{
          name: '消费个数',
          type: 'line',
          symbol: 'none',
          smooth: true,
          data: [],
          lineStyle: {
            width: 0
          },
          itemStyle: {
            color: '#48cefd'
          },
          areaStyle: {
            color: {
              type: 'linear',
              x: 0,
              y: 0,
              x2: 0,
              y2: 1,
              colorStops: [{
                offset: 0, color: '#48cefd' // 0% 处的颜色
              },
                {
                  offset: 0.4, color: '#48cefd' // 40% 处的颜色
                }, {
                  offset: 1, color: '#5356f1' // 100% 处的颜色
                }],
              global: false // 缺省为 false
            }, //背景渐变色
            origin: 'start'
          }
        },
        ]
      }
    }
  },
  methods: {
    setChart() {
      let myChart = this.$echarts(this.$el);
      myChart.clear();
      myChart.resize()
      myChart.setOption(this.option);
    },
    load() {
      request.get("/EverydayConsume").then(res => {
        const { data } = res;
        this.option.xAxis.data = data[0]
        this.option.series[0].data = data[1]
        this.setChart()
      })
    }
  },
  mounted() {
    this.load()
  }
}
</script>

<style lang="less" scoped>
.EverydayConsume {
  height: 100%;
}
</style>