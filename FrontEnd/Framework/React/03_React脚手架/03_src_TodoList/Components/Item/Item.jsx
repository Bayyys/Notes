import React, { Component } from "react";
import PropTypes from "prop-types";
import "./Item.css";

export default class index extends Component {
  state = {
    mouse: false,
  };

  static propTypes = {
    id: PropTypes.string.isRequired,
    name: PropTypes.string.isRequired,
    done: PropTypes.bool.isRequired,
    changeTodo: PropTypes.func.isRequired,
    deleteTodoById: PropTypes.func.isRequired,
  };

  handleMouse = (flag) => {
    return () => {
      this.setState({ mouse: flag });
    };
  };

  handleChange = (id) => {
    return (event) => {
      this.props.changeTodo(id, event.target.checked);
    };
  };

  handleDelete = (id) => {
    return () => {
      if (window.confirm("确定删除吗？")) {
        this.props.deleteTodoById(id);
      }
    };
  };

  render() {
    const { id, name, done } = this.props;
    return (
      <li
        style={{ backgroundColor: this.state.mouse ? "#ddd" : "white" }}
        onMouseMove={this.handleMouse(true)}
        onMouseLeave={this.handleMouse(false)}
      >
        <label>
          <input
            type="checkbox"
            checked={done}
            onChange={this.handleChange(id)}
          />
          <span>{name}</span>
        </label>
        <button
          className="btn btn-danger"
          style={{ display: this.state.mouse ? "block" : "none" }}
          onClick={this.handleDelete(id)}
        >
          删除
        </button>
      </li>
    );
  }
}
