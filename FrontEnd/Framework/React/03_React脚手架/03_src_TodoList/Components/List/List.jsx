import React, { Component } from "react";
import PropTypes from "prop-types";
import Item from "../Item/Item";
import "./List.css";

export default class index extends Component {
  static propTypes = {
    todos: PropTypes.array.isRequired,
    changeTodo: PropTypes.func.isRequired,
    deleteTodoById: PropTypes.func.isRequired,
  };

  render() {
    const { todos, changeTodo, deleteTodoById } = this.props;
    return (
      <ul className="todo-main">
        {todos.map((todo) => {
          return (
            <Item
              key={todo.id}
              {...todo}
              changeTodo={changeTodo}
              deleteTodoById={deleteTodoById}
            />
          );
        })}
      </ul>
    );
  }
}
