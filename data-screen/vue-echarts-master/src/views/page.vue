<template>
  <div class="page">
    <Row class='content'>
      <Col span="8">
        <div class="list">
          <div class="left">
            <span class='title'><span class="title-4">每天被消费的数量</span></span>
            <span class="angle1"></span>
            <span class="angle2"></span>
            <span class="angle3"></span>
            <span class="angle4"></span>
            <div class="chart-68">
              <EverydayConsume ref="chart8" id="left1" ></EverydayConsume>
            </div>
          </div>
        </div>
        <div class="list">
          <div class="left">
            <span class='title'><span class="title-8">每天被核销的数量</span></span>
            <span class="angle1"></span>
            <span class="angle2"></span>
            <span class="angle3"></span>
            <span class="angle4"></span>
            <div class="chart-68">
              <EverydayDate ref="chart1" id="left2" ></EverydayDate>
            </div>
          </div>
        </div>
      </Col>
      <Col span="8">
        <div class="circlePie" id="circlePie">
          <canvas id="main" width="500" height="500"></canvas>
        </div>
      </Col>
      <Col span="8">
        <div class="list">
          <div class="right">
            <span class='title'><span class="title-4">消费距离与核销率</span></span>
            <span class="angle1"></span>
            <span class="angle2"></span>
            <span class="angle3"></span>
            <span class="angle4"></span>
            <div class="chart-68">
              <DistanceDate ref="chart6"></DistanceDate>
            </div>

          </div>
        </div>
        <div class="list">
          <div class="right">
            <span class='title'><span class="title-8">每天被领券的数量</span></span>
            <span class="angle1"></span>
            <span class="angle2"></span>
            <span class="angle3"></span>
            <span class="angle4"></span>
            <div class="chart-68">
              <EverydayReceived ref="chart8" id="right_4"></EverydayReceived>
            </div>
          </div>
        </div>

      </Col>
    </Row>
    <Row class="bottom-list">
      <Col span="16">
        <div class="list">
          <div class="bottom">
            <span class='title'><span class="title-10">周领券数与核销数</span></span>
            <span class="angle1"></span>
            <span class="angle2"></span>
            <span class="angle3"></span>
            <span class="angle4"></span>
            <WeekdayReceivedDate ref="chart9" id="bottom_1"></WeekdayReceivedDate>
          </div>
        </div>
        <div class="list">
          <div class="bottom">
            <span class='title'><span class="title-10">消费距离分析</span></span>
            <span class="angle1"></span>
            <span class="angle2"></span>
            <span class="angle3"></span>
            <span class="angle4"></span>
            <DistanceConsume ref="chart10" id="bottom_2"></DistanceConsume>
          </div>
        </div>
        <div class="list">
          <div class="bottom">
            <span class='title'><span class="title-10">月优惠券使用情况</span></span>
            <span class="angle1"></span>
            <span class="angle2"></span>
            <span class="angle3"></span>
            <span class="angle4"></span>
            <MonthReceivedDateConsume ref="chart11" id="bottom_3"></MonthReceivedDateConsume>
          </div>
        </div>
      </Col>
      <Col span="8">
        <div class="list right-bottom">
          <div class="bottom bottom1">
            <span class='title'><span class="title-10">优惠券种类及核销情况</span></span>
            <span class="angle1"></span>
            <span class="angle2"></span>
            <span class="angle3"></span>
            <span class="angle4"></span>
            <PieData ref="chart12" id="bottom_4"></PieData>
          </div>
        </div>
      </Col>
    </Row>
  </div>
</template>

<script>

import request from "@/utils/request";

const EverydayConsume = () => import('./components/EverydayConsume');
const EverydayDate = () => import('./components/page/EverydayDate');
const DistanceDate = () => import('./components/page/DistanceDate');
const EverydayReceived = () => import('./components/page/EverydayReceived');
const WeekdayReceivedDate = () => import('./components/page/WeekdayReceivedDate');
const MonthReceivedDateConsume = () => import('./components/page/MonthReceivedDateConsume');
const PieData = () => import('./components/page/PieData');
const DistanceConsume = () => import('./components/page/DistanceConsume');

export default {
  name: 'page',
  components: {
    EverydayConsume,
    EverydayDate,
    DistanceDate,
    EverydayReceived,
    WeekdayReceivedDate,
    MonthReceivedDateConsume,
    PieData,
    DistanceConsume
  },
  data() {
    return {
      everyPer: 0,
      xOffset: 0,
      circle: {
        x: 250,
        y: 250,
        radius: 218
      },
      series: ["Area Under Curve", '79.80'],
      title: ['总记录次数:','用户个数:', '商家个数:','优惠券种类:','优惠券领取次数:','优惠券核销次数:'],
      warea: {x: 250, y: 250, max: 700},
      dots: [],
      resizeFn: null,
      animationFrame1: null,
      animationFrame2: null,
      centerBox: {
        width: 0,
        height: 0
      }
    }
  },
  methods: {
    rads(x) { // 弧度转换
      return Math.PI * x / 180;
    },
    act() {
      //清空画布
      const canvas = document.querySelector('#main');
      canvas.style.width = this.centerBox.height + 'px';
      canvas.style.height = this.centerBox.height + 'px';
      const context = canvas.getContext('2d');
      context.clearRect(0, 0, canvas.width, canvas.height);
      this.drawPie(this.everyPer, context);
      this.animationFrame2 = window.requestAnimationFrame(this.act);
      this.everyPer += Math.PI / 180;
      let speed = 0.07; //波浪速度，数越大速度越快
      this.xOffset += speed;
    },
    drawPie(everyPer, context) {
      context.save();
      context.fillStyle = 'rgba(18,55,88,.2)';
      context.beginPath();
      context.arc(this.circle.x, this.circle.y, 245, 0, 2 * Math.PI, true);
      context.closePath();
      context.fill();
      context.restore();

      //外圆
      context.save();
      context.shadowBlur = 50;
      context.shadowColor = "#123959";
      context.fillStyle = '#080D27';
      context.beginPath();
      context.arc(this.circle.x, this.circle.y, 235, 0, 2 * Math.PI, true);
      context.closePath();
      context.fill();
      context.restore();
      // 环形字
      for (let i = 0; i < this.title.length; i++) {//绘制文字。
        context.save()
        // 画文字
        this.drawCircularText(this.circle, this.title[i], this.rads(i * 60 - 110), this.rads(i * 60 - 65), i, context);
        context.restore();
      }
      let nowRange = this.series[1];
      context.save();
      this.drawCircle(context);
      this.drawSin(this.xOffset, context, nowRange);
      this.drawText(context, nowRange);
      context.restore();
      for (let i = 0; i < 6; i++) {//绘制刻度。
        context.save();
        context.translate(this.circle.x, this.circle.y);
        context.rotate((-Math.PI / 2 + Math.PI / 6) + i * Math.PI / 3);  //旋转坐标轴。坐标轴x的正方形从 向上开始算起
        context.beginPath();
        context.moveTo(190, 0);
        context.lineTo(200, 0);
        context.lineWidth = 4;
        context.strokeStyle = '#0A122D';
        context.stroke();
        context.closePath();
        context.restore();
      }
    },
    drawCircle(ctx) { // 画圆 中心圆
      ctx.beginPath();
      ctx.fillStyle = '#209ADF';
      ctx.arc(this.circle.x, this.circle.y, 150, 0, 2 * Math.PI);
      ctx.fill();
      ctx.beginPath();
      ctx.arc(this.circle.x, this.circle.y, 150, 0, 2 * Math.PI);
      ctx.clip();
    },
    drawSin(xOffset, ctx, nowRange) { //画sin 曲线函数
      let mW = 300;
      let mH = 300;
      let sX = 0;
      let axisLength = mW; //轴长
      let waveWidth = 0.04; //波浪宽度,数越小越宽
      let waveHeight = 12; //波浪高度,数越大越高
      ctx.save();
      ctx.translate(100, 130);
      let points = []; //用于存放绘制Sin曲线的点
      ctx.beginPath();
      //在整个轴长上取点
      for (let x = sX; x < sX + axisLength; x += 20 / axisLength) {
        //此处坐标(x,y)的取点，依靠公式 “振幅高*sin(x*振幅宽 + 振幅偏移量)”
        let y = -Math.sin((sX + x) * waveWidth + xOffset);
        let dY = mH * (1 - nowRange / 100);
        points.push([x, dY, dY + y * waveHeight]);
        ctx.lineTo(x, dY + y * waveHeight);
      }
      //封闭路径
      ctx.lineTo(axisLength, mH);
      ctx.lineTo(sX, mH);
      ctx.lineTo(points[0][0], points[0][1]);
      ctx.fillStyle = '#2C50B1';
      ctx.fill();

      ctx.restore();
    },
    // 中心显示文字
    drawText(ctx, nowRange) {
      ctx.save();
      ctx.translate(130, 130);
      let size = 50;
      ctx.font = size + 'px Microsoft Yahei';
      ctx.textAlign = 'center';
      ctx.fillStyle = "#95EFFF";
      ctx.fillText(nowRange + '%', 120, 120 - size / 2);
      ctx.restore();
      ctx.save()
      size = 25;
      ctx.translate(130, 130);
      ctx.font = size + 'px Microsoft Yahei';
      ctx.textAlign = 'center';
      ctx.fillStyle = "#95EFFF";
      ctx.fillText(this.series[0], 120, 120 + size);
      ctx.restore();
    },
    // 旋转的文字
    drawCircularText(s, string, startAngle, endAngle, n, context) {
      let radius = s.radius, // 文字环绕的中心圆半径
          angleDecrement, // 一个文字所占的角度
          angle = parseFloat(startAngle), // 文字的起始角度
          index = 0, // 文字的索引值
          character; // 当前要画的文字
      let arr = string.split(':')
      context.save();
      context.fillStyle = '#fff';
      context.font = '14px 微软雅黑 ';
      context.textAlign = 'center';
      context.textBaseline = 'middle';
      if (n < 2 || n === 5) { // 上三个不需要反转的文字
        while (index < string.length) {
          character = string.charAt(index);
          if (arr[0].indexOf(character) >= 0) {
            if (arr[0].length > 6) {
              angleDecrement = (startAngle - endAngle) / (string.length - 3)
            } else {
              angleDecrement = (startAngle - endAngle) / (string.length - 1)
            }

          } else {
            angleDecrement = (startAngle - endAngle) / (string.length + 6)
          }
          context.save();
          context.beginPath();
          context.translate(s.x + Math.cos(angle) * radius,
              s.y + Math.sin(angle) * radius);
          context.rotate(Math.PI / 2 + angle);
          context.fillText(character, 0, 0);
          angle -= angleDecrement;
          index++;
          context.restore();
        }
      } else { // 下面三个需要反转的文字
        while (index < string.length) {
          character = string.split("").reverse().join("").charAt(index);// 字符串反转
          if (arr[1].indexOf(character) >= 0) {
            angleDecrement = (startAngle - endAngle) / (string.length + 6)
          } else {
            if (arr[0].length > 6) {
              angleDecrement = (startAngle - endAngle) / (string.length - 3)
            } else {
              angleDecrement = (startAngle - endAngle) / (string.length - 1)
            }
          }
          context.save();
          context.beginPath();
          context.translate(s.x + Math.cos(angle) * radius,
              s.y + Math.sin(angle) * radius);
          context.rotate(-Math.PI / 2 + angle);// 旋转文字
          context.fillText(character, 0, 0);
          angle -= angleDecrement;
          index++;
          context.restore();
        }
      }
      context.restore();
    },

    load() {
      request.get("/TitleData").then(res => {
        const { data } = res;
        this.title[0] = this.title[0]+data[0]
        this.title[1] = this.title[1]+data[1]
        this.title[2] = this.title[2]+data[2]
        this.title[3] = this.title[3]+data[3]
        this.title[4] = this.title[4]+data[4]
        this.title[5] = this.title[5]+data[5]
      })
    }
  },
  mounted() {
    this.load()
    this.centerBox = {
      width: document.querySelector('#circlePie').offsetWidth,
      height: document.querySelector('#circlePie').offsetHeight
    }

    this.act();
    // this.drawDot();
    this.resizeFn = this.$debounce(() => {
      // 通过捕获系统的onresize事件触发我们需要执行的事件
      this.centerBox = {
        width: document.querySelector('#circlePie').offsetWidth,
        height: document.querySelector('#circlePie').offsetHeight
      }
      for (let i = 1; i < 13; i++) {
        this.$refs['chart' + i].setChart();
      }
    }, 500)
    window.addEventListener('resize', this.resizeFn)
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.resizeFn)
    window.cancelAnimationFrame(this.animationFrame1)
    window.cancelAnimationFrame(this.animationFrame2)
  }
}
</script>

<style lang="less" scoped>
.page {
  height: 100%;
  width: 100%;
  padding: 14px 20px 20px;
  background: #03044A;
  overflow: hidden;

  .content {
    height: 65%;

    .ivu-col {
      height: 100%;
    }

    .circlePie {
      height: 100%;
      padding: 0 0 40px;
      text-align: center;
      position: relative;

      canvas {
        position: absolute;
        left: 50%;
        top: 0;
        transform: translate(-50%, 0);
      }

      #dot {
        background: rgba(0, 0, 0, 0);
      }
    }

    .list {
      height: 48%;

      .left, .right {
        background: #0D1341;
      }

      .left, .right, .center {
        width: 100%;
        height: 90%;
        border: 1px solid #0D2451;
        position: relative;

        #left1, #left2, #left3, #right1, #right2, #right3, #center2 {
          height: 100%;
        }

        .chart-68 {
          width: 100%;
          height: 100%;
        }
      }
    }
  }

  .bottom-list {
    height: 35%;

    .ivu-col {
      height: 100%;

      .list {
        height: 100%;
        width: 33.3333%;
        padding-right: 1.5%;
        float: left;

        #bottom_4 {
          padding: 0 20px;
        }

        .bottom {
          width: 100%;
          height: 100%;
          border: 1px solid #0D2451;
          position: relative;
        }
      }

      .right-bottom {
        width: 100%;
        padding-right: 0;

        .bottom1 {
          width: 100%;
        }
      }
    }
  }

}
</style>
