<template>
    <div class="WeekdayReceivedDate"></div>
</template>

<script>
import request from "@/utils/request";

export default {
    name: '',
    data() {
        return {
          option: {
            tooltip: {
              trigger: 'axis'
            },
            legend: {
              right: "13",
              top: "13%",
              itemWidth: 7,
              itemHeight: 7,
              textStyle: {
                color: '#5CB1C1',
                fontSize: 11
              }
            },
            grid: {
              top: '17%',
              left: '14%',
              right: '10%',
              bottom: '10%',
              containLabel: false
            },
            xAxis: {
              type: 'category',
              boundaryGap: false,
              axisLine: {
                symbol: ['none', 'arrow'],
                symbolSize: [6, 6],
                symbolOffset: [0, 10],
                lineStyle: {
                  color: '#122C49'
                }
              },
              axisTick: {show: false},
              axisLabel: {
                color: '#61B9C8',
                fontSize: 9
              },
              data: ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
            },
            yAxis: {
              type: 'value',
              scale: true,
              max: 210000+30000,
              min: 0,
              interval: 30000,
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
                fontSize: 9
              },
              name: '(次)',
              nameGap: -10,
              nameTextStyle: {
                color: '#61B9C8',
                fontSize: 9,
                align: 'right',
                padding: [0, 6, 0, 0]
              },
              splitLine: {
                show: false,
              }
            },
            series: [
              {
                name: '领券',
                type: 'line',
                smooth: true,
                symbol: 'none',
                lineStyle: {
                  color: '#F39800',
                },
                itemStyle: {
                  color: '#F39800'
                },
                data: []
              },
              {
                name: '核销',
                type: 'line',
                smooth: true,
                symbol: 'none',
                lineStyle: {
                  color: '#BF232A',

                },
                itemStyle: {
                  color: '#BF232A'
                },
                data: []
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
        request.get("/WeekdayReceivedDate").then(res => {
          const { data } = res;
          // this.option.series type array
          this.option.series[0].data = data[1]
          this.option.series[1].data = data[2]
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
.WeekdayReceivedDate {
    height: 100%;
    width: 100%;
}
</style>