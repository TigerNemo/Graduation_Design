<template>
    <div class="MonthReceivedDateConsume"></div>
</template>

<script>
import request from "@/utils/request";

export default {
    name: '',
    data() {
        return {
          option: {
            grid: {
              top: "13%",
              bottom: "15%",
              left: 60,
              right: 40,
            },
            tooltip: {
              trigger: 'axis'
            },
            legend: {
              right: "7%",
              top: "11%",
              itemWidth: 10,
              itemHeight: 10,
              textStyle: {
                color: '#5CB1C1',
                fontSize: 10
              },
              orient: "vertical"
            },
            calculable: true,
            xAxis: [
              {
                type: 'category',
                axisLine: {
                  // symbol: ['none', 'arrow'],
                  symbolSize: [6, 10],
                  lineStyle: {
                    color: '#122C49'
                  }
                },
                axisLabel: {
                  color: '#61B9C8',
                  showMaxLabel: true,
                  fontSize: 10
                },
                data: ['1月', '2月', '3月', '4月', '5月', '6月']
              }
            ],
            yAxis: [
              {
                type: 'value',
                interval: 100000,
                min: 0,
                max: 400000+100000,
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
                name: '(次)',
                nameGap: -10,
                nameTextStyle: {
                  color: '#61B9C8',
                  fontSize: 9,
                  align: 'right',
                  padding: [0, 6, 0, 0]
                }
              }
            ],
            series: [
              {
                name: '核销',
                type: 'bar',
                barGap: 0,
                barWidth: 6,
                data: [],
                itemStyle: {
                  barBorderRadius: [3, 3, 0, 0],
                  color: {
                    type: 'linear',
                    x: 0,
                    y: 0,
                    x2: 1,
                    y2: 0,
                    colorStops: [
                      {
                        offset: 0, color: 'rgba(252,145,134,1)' // 0% 处的颜色
                      }, {
                        offset: 1, color: 'rgba(241,88,135,1)' // 100% 处的颜色
                      }
                    ],
                    global: false // 缺省为 false
                  } //背景渐变色
                }
              },
              {
                name: '领取',
                type: 'bar',
                barGap: 0,
                barWidth: 6,
                data: [],
                itemStyle: {
                  barBorderRadius: [3, 3, 0, 0],
                  color: {
                    type: 'linear',
                    x: 0,
                    y: 0,
                    x2: 1,
                    y2: 0,
                    colorStops: [
                      {
                        offset: 0, color: 'rgba(144,20,238,1)' // 0% 处的颜色
                      }, {
                        offset: 1, color: 'rgba(74,8,211,1)' // 100% 处的颜色
                      }
                    ],
                    global: false // 缺省为 false
                  } //背景渐变色
                }
              },
              {
                name: '消费',
                type: 'bar',
                barGap: 0,
                barWidth: 6,
                data: [],
                itemStyle: {
                  barBorderRadius: [3, 3, 0, 0],
                  color:  {
                    type: 'linear',
                    x: 0,
                    y: 0,
                    x2: 1,
                    y2: 0,
                    colorStops: [
                      {
                        offset: 0, color: 'rgba(0,204,255,1)' // 0% 处的颜色
                      }, {
                        offset: 1, color: 'rgba(8,59,126,1)' // 100% 处的颜色
                      }
                    ],
                    global: false // 缺省为 false
                  } //背景渐变色
                }
              }
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
        request.get("/MonthReceivedDateConsume").then(res => {
          const { data } = res;
          // this.option.series type array
          this.option.series[0].data = data[1]
          this.option.series[1].data = data[2]
          this.option.series[2].data = data[3]
          this.setChart()
        })
      }
    },
    mounted() {
        this.load()
    },
}
</script>

<style lang="less" scoped>
.MonthReceivedDateConsume {
    height: 100%;
    width: 100%;
}
</style>