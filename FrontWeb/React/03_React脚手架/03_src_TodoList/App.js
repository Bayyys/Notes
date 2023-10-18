import { Component } from "react";
import Header from "./Components/Header/Header";
import Footer from "./Components/Footer/Footer";
import List from "./Components/List/List";
import "./App.css";

export default class App extends Component {
  state = {
    todos: [
      { id: "001", name: "吃饭", done: true },
      { id: "002", name: "睡觉", done: true },
      { id: "003", name: "打豆豆", done: false },
    ],
  };

  addTodo = (todoObj) => {
    console.log("App", todoObj);
    const { todos } = this.state;
    const newTodos = [todoObj, ...todos];
    this.setState({ todos: newTodos });
  };

  changeTodo = (id, done) => {
    const { todos } = this.state;
    const newTodos = todos.map((todo) => {
      if (todo.id === id) {
        return {
          ...todo,
          done,
        };
      }
      return todo;
    });
    this.setState({ todos: newTodos });
  };

  deleteTodoById = (id) => {
    const { todos } = this.state;
    const newTodos = todos.filter((todo) => {
      return todo.id !== id;
    });
    this.setState({ todos: newTodos });
  };

  changeAllTodoDone = (done) => {
    console.log(done);
    const { todos } = this.state;
    const newTodos = todos.map((todo) => {
      return {
        ...todo,
        done,
      };
    });
    this.setState({ todos: newTodos });
  };

  deleteAllDoneTodo = () => {
    const { todos } = this.state;
    const newTodos = todos.filter((todo) => {
      return !todo.done;
    });
    this.setState({ todos: newTodos });
  };

  render() {
    return (
      <div className="todo-container">
        <Header addTodo={this.addTodo} />
        <List
          todos={this.state.todos}
          changeTodo={this.changeTodo}
          deleteTodoById={this.deleteTodoById}
        />
        <Footer
          todos={this.state.todos}
          changeAllTodoDone={this.changeAllTodoDone}
          deleteAllDoneTodo={this.deleteAllDoneTodo}
        />
      </div>
    );
  }
}
