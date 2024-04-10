import React, { Component } from "react";

export default class Item extends Component {
  render() {
    const { avatar_url, html_url, login } = this.props;
    return (
      <div className="card">
        <a rel="noreferrer" href={html_url} target="_blank">
          <img alt="" src={avatar_url} style={{ width: "100px" }} />
        </a>
        <p className="card-text">{login}</p>
      </div>
    );
  }
}
