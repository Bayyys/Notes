import React, { Component } from "react";
import Item from "../Item";
import "./index.css";

export default class List extends Component {
  render() {
    return (
      <div className="row">
        {this.props.users.map((user) => {
          return <Item key={user.id} {...user} />;
        })}
      </div>
    );
  }
}
