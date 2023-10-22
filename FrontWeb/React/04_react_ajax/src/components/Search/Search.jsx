import React, { Component } from "react";
import PubSub from "pubsub-js";
// import axios from "axios";

export default class Search extends Component {
  search = async () => {
    const {
      keyWordNode: { value: keyword },
    } = this;

    PubSub.publish("updateListState", {
      isFirst: false,
      isLoading: true,
      err: "",
    });

    // axios
    //   .get(`https://api.github.com/search/users?q=${keyword}`)
    //   .then((res) => {
    //     const users = res.data.items.map((item) => {
    //       return {
    //         id: item.id,
    //         login: item.login,
    //         avatar_url: item.avatar_url,
    //         html_url: item.html_url,
    //       };
    //     });
    //     PubSub.publish("updateListState", { isLoading: false, users, err: "" });
    //   })
    //   .catch((error) => {
    //     PubSub.publish("updateListState", {
    //       isLoading: false,
    //       users: [],
    //       err: error.message,
    //     });
    //   });

    // 直接的返回收到的数据是 联系服务器的状态和信息(状态码, 状态信息, 响应头, 响应体)
    // 即便是404, 也会返回一个对象, 但是没有响应体
    // 只有当网络故障护着请求被阻止时, 才会标记为 reject
    // 需要对该数据进行处理, 得到数据
    // fetch(`https://api.github.com/search/users?q=${keyword}`)
    //   .then(
    //     (res) => res.json() // res.json() 是一个新的 promise 对象
    //     // 只要有接收的数据, 就会有返回(包括 404)
    //   )
    //   .then((data) => {
    //     const users = data.items.map((item) => {
    //       return {
    //         id: item.id,
    //         login: item.login,
    //         avatar_url: item.avatar_url,
    //         html_url: item.html_url,
    //       };
    //     });
    //     PubSub.publish("updateListState", { isLoading: false, users, err: "" });
    //   })
    //   .catch((err) => {
    //     PubSub.publish("updateListState", {
    //       isLoading: false,
    //       users: [],
    //       err: err.message,
    //     });
    //   });

    try {
      const res = await fetch(
        `https://api.github.com/search/users?q=${keyword}`
      );
      const data = await res.json();
      const users = data.items.map((item) => {
        return {
          id: item.id,
          login: item.login,
          avatar_url: item.avatar_url,
          html_url: item.html_url,
        };
      });
      PubSub.publish("updateListState", { isLoading: false, users, err: "" });
    } catch (err) {
      PubSub.publish("updateListState", {
        isLoading: false,
        users: [],
        err: err.message,
      });
    }
  };

  render() {
    return (
      <section className="jumbotron">
        <h3 className="jumbotron-heading">搜索GitHub用户</h3>
        <div>
          <input
            ref={(c) => (this.keyWordNode = c)}
            type="text"
            placeholder="搜索关键词进行搜索"
          />
          &nbsp;<button onClick={this.search}>搜索</button>
        </div>
      </section>
    );
  }
}
