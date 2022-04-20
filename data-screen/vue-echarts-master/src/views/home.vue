<template>
  <div style="height:100%;">
    <div class="header">
      <div class="selectRange">
        <div class="">
        </div>
      </div>
      <div class="header-title">
        大数据可视化平台
      </div>
      <div class="selectRange">
        <Menu mode="horizontal" >
        </Menu>
      </div>
    </div>
    <div class="page">
      <router-view v-if="flag" ></router-view>
    </div>

  </div>
</template>

<script>
import request from "@/utils/request";

export default {
  name: '',
  data() {
    return {
      modal: false,
      flag: true,
      optionEnd: {},
      resizeFn: null
    }
  },
  mounted() {
    window.addEventListener('resize', this.resizeFn);
  },
  methods: {
    // 前端发送数据，新增
    save() {
      request.post("/api/DistanceDate")
    },
  },
}
</script>

<style lang="less">
.ivu-modal {
  .ivu-modal-content {
    background: #071332;

    .ivu-modal-header {
      border-bottom: 1px solid #1a3c58;

      .ivu-modal-header-inner {
        color: #75deef;
      }
    }

    .ivu-modal-body {
      text-align: center;

      .ivu-icon {
        color: #75deef
      }

      .ivu-modal-confirm-body {
        padding-left: 0;
        color: #75deef
      }

      .ivu-input {
        background-color: rgba(0, 0, 0, 0);
        border: 1px solid #1a3c58;
        color: #75deef;

        &::-webkit-input-placeholder { /* WebKit, Blink, Edge */
          color: #75deef;
        }

        &::-moz-placeholder { /* Mozilla Firefox 4 to 18 */
          color: #75deef;
        }

        &::-moz-placeholder { /* Mozilla Firefox 19+ */

          color: #75deef;
        }
        &::-ms-input-placeholder { /* Internet Explorer 10-11 */
          color: #75deef;
        }
      }

      .ivu-picker-panel-body {
        background: #071332;

        .ivu-date-picker-header {
          color: #75deef;
          border-bottom: 1px solid #1a3c58
        }

        .ivu-date-picker-cells-cell {
          color: #75deef;

          &:hover em {
            background: #1a3c58;
          }
        }

        .ivu-date-picker-cells-cell-disabled {
          background: rgba(0, 0, 0, 0);
          color: #eee
        }

        .ivu-date-picker-cells-focused em {
          box-shadow: 0 0 0 1px #1a3c58 inset;

          &::after {
            background: #1a3c58;
          }
        }
      }
    }

    .ivu-modal-footer {
      border-top: 1px solid #1a3c58;

      .ivu-btn-primary {
        color: #75deef;
        background: #1a3c58;
      }

      .ivu-btn-text {
        color: #ddd;

        &:hover {
          color: #75deef;
          background: #1a3c58;
        }
      }
    }
  }

}

.header {
  height: 80px;
  background: #03044A;
  display: flex;
  justify-content: space-between;
  align-items: center;



  &-title {
    color: #75deef;
    font-size: 40px;
    letter-spacing: 10px;
  }

  .header-title {
    width: auto;
  }

  .selectRange {
    width: 300px;
    height: 100%;

    .ivu-menu-horizontal {
      background: rgba(255, 255, 255, 0);

      &::after {
        height: 0;
      }

      .ivu-menu-item-active {
        border-bottom: 2px solid #264e5e;

      }

      .ivu-menu-item, .ivu-menu-submenu {
        color: #75deef;

        &:hover {
          border-bottom: 2px solid #264e5e;
        }
      }

      .ivu-select-dropdown {
        background: #09102E;

        .ivu-menu-item {
          color: #75deef;

          &:hover {

            border-bottom: 2px solid #264e5e;
            background-color: rgba(255, 255, 255, 0);
          }
        }
      }

      .ivu-menu-submenu-title {
        i {
          margin-right: 0;
        }

        .ivu-icon-ios-arrow-down {
          display: none;
        }
      }
    }
  }
}

.page {
  height: calc(~ '100% - 80px');

}
</style>
