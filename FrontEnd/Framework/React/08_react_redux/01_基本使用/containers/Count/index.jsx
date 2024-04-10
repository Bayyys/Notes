// 引入 Count 的 UI 组件
import CountUI from "../../components/Count";
// 引入 connect 用于连接 UI 组件与 redux
import { connect } from "react-redux";
import {
  incrementAction,
  decrementAction,
  incrementAsyncAction,
} from "../../redux/count_action";

// 1. mapStateToProps 返回对象中的key作为传递给 UI 组件 props 的 key，value作为传递给 UI 组件 props 的 value
function mapStateToProps(state) {
  return { count: state };
}

// 2. mapDispatchToProps 返回对象中的key作为传递给 UI 组件 props 的 key，value作为传递给 UI 组件 props 的 value
function mapDispatchToProps(dispatch) {
  return {
    increment: (data) => {
      dispatch(incrementAction(data));
    },
    decrement: (data) => {
      dispatch(decrementAction(data));
    },
    incrementAsync: (data, time) => {
      dispatch(incrementAsyncAction(data, time));
    },
  };
}

// 创建并暴露一个 Count 的容器组件 connect()()
export default connect(mapStateToProps, mapDispatchToProps)(CountUI);
