import React, { Component } from "react";
import axios from "axios";

export default class App extends Component {
  state = {
    showData: [],
  };

  queryData = () => {
    axios.get("api2/students").then(
      (response) => {
        this.setState({ showData: [...response.data] });
      },
      (error) => {
        console.log(error);
      }
    );
  };

  render() {
    return (
      <div>
        <button onClick={this.queryData}>请求数据</button>
        <ul>
          {this.state.showData.map((item) => {
            return <li key={item.id}>{item.name} -- {item.age}</li>;
          })}
        </ul>
      </div>
    );
  }
}
