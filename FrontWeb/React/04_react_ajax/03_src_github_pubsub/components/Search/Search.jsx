import React, { Component } from "react";
import PubSub from "pubsub-js";
import axios from "axios";

export default class Search extends Component {
  search = () => {
    const {
      keyWordNode: { value: keyword },
    } = this;
    PubSub.publish("updateListState", {
      isFirst: false,
      isLoading: true,
      err: "",
    });
    axios
      .get(`https://api.github.com/search/users?q=${keyword}`)
      .then((res) => {
        const users = res.data.items.map((item) => {
          return {
            id: item.id,
            login: item.login,
            avatar_url: item.avatar_url,
            html_url: item.html_url,
          };
        });
        PubSub.publish("updateListState", { isLoading: false, users, err: "" });
      })
      .catch((error) => {
        PubSub.publish("updateListState", {
          isLoading: false,
          users: [],
          err: error.message,
        });
      });
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
