<template>
    <div class="PieData"></div>
</template>

<script>
import request from "@/utils/request";

export default {
    name: '',
    data() {
        return {
          option: {
            title: [
              {
                text: "【优惠券数量占比】",
                left: '4%',
                bottom: '3%',
                textStyle: {
                  color: "#fff",
                  fontSize: 12
                }
              },
              {
                text: "【核销优惠券占比】",
                left: '38%',
                bottom: '3%',
                textStyle: {
                  color: "#fff",
                  fontSize: 12
                }
              },
              {
                text: "【正-负比例】",
                right: '8%',
                bottom: '3%',
                textStyle: {
                  color: "#fff",
                  fontSize: 12
                }
              }
            ],
            tooltip: {
              trigger: 'item',
              formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            legend: {
              left: "8%",
              top: "10%",
              itemWidth: 7,
              itemHeight: 7,
              textStyle: {
                color: '#00CCFF',
                fontSize: 10
              }
            },
            series: [
              {
                name: '【优惠券数量占比】',
                type: 'pie',
                radius: '45%',
                center: ['17%', '55%'],
                data: [
                  {value: 0, name: '折扣'},
                  {value: 0, name: '满减'},
                ],
                label: {
                  fontSize: 10,
                  color: '#00CCFF'
                },
                labelLine: {
                  length: 15,
                  length2: 10,
                  lineStyle: {
                    color: '#3F3F5C'
                  }
                },
                itemStyle: {
                  color: function (params) {
                    var colorList = ['#F74F64', '#00CCFF'];
                    return colorList[params.dataIndex];
                  },
                  emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                  }
                }
              },
              {
                name: '【核销优惠券占比】',
                type: 'pie',
                radius: '45%',
                center: ['50%', '55%'],
                data: [
                  {value: 0, name: '折扣'},
                  {value: 0, name: '满减'},
                ],
                label: {
                  fontSize: 10,
                  color: '#00CCFF'
                },
                labelLine: {
                  length: 15,
                  length2: 10,
                  lineStyle: {
                    color: '#3F3F5C'
                  }
                },
                itemStyle: {
                  color: function (params) {
                    var colorList = ['#F74F64', '#00CCFF'];
                    return colorList[params.dataIndex];
                  },
                  emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                  }
                }
              },
              {
                name: '【正-负比例】',
                type: 'pie',
                radius: '45%',
                center: ['82%', '55%'],
                data: [
                  {value: 0, name: '正例'},
                  {value: 0, name: '负例'},
                ],
                label: {
                  fontSize: 10,
                  color: '#00CCFF'
                },
                labelLine: {
                  length: 15,
                  length2: 10,
                  lineStyle: {
                    color: '#3F3F5C'
                  }
                },
                itemStyle: {
                  color: function (params) {
                    var colorList = ['#ca0df8', '#202065'];
                    return colorList[params.dataIndex];
                  },
                  emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                  }
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
        request.get("/PieData").then(res => {
          const { data } = res;
          // this.option.series type array
          this.option.series[0].data[0].value = data[1]
          this.option.series[0].data[1].value = data[0]
          this.option.series[1].data[0].value = data[3]
          this.option.series[1].data[1].value = data[2]
          this.option.series[2].data[0].value = data[4]
          this.option.series[2].data[1].value = data[5]
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
.PieData {
    height: 100%;
    width: 100%;
    padding: 0 20px;
}
</style>