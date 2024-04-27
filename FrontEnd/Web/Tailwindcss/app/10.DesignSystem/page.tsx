"use client";

import { useState } from "react";
import ArrowDown from "../arrowDown";

export default function DesignSystem() {
  const [isOpened, setIsOpened] = useState(false);
  const [selectValue, setSelectValue] = useState("My selected option");

  const updateValue = (value: string) => {
    setSelectValue(value);
    setIsOpened(false);
  };

  return (
    <div>
      <h1>This is a title</h1>
      <h2>This is a subtitle</h2>
      <p>This is a paragraph</p>
      <a href="www.baidu.com">This is an anchor</a>
      <div className="my-2 space-x-2">
        <button className="btn btn-primary">This is a button</button>
        <button className="btn btn-sencondary">This is another button</button>
        <button disabled className="btn btn-primary">
          This is another button
        </button>
      </div>
      <div className="my-2 space-x-2">
        <input type="text" />
        <input disabled type="text" placeholder="Email" />
        <input type="date" />
      </div>
      <div className="flex items-start my-4">
        <input type="checkbox" id="checkbox" />
        <label htmlFor="checkbos">
          Lorem ipsum dolor sit, amet consectetur adipisicing elit. Doloremque
          dolorum architecto hic! Corporis vel dicta magni vitae laborum, autem
          pariatur minima suscipit totam, vero deserunt, nisi unde. Sit, at
          esse?
        </label>
      </div>
      <div className="flex space-x-2">
        <select name="" id="">
          <option value="">Optino 1</option>
          <option value="">Optino 2</option>
        </select>
      </div>
      <div className="Myselect">
        <div
          className="child flex items-center justify-between"
          onClick={() => {
            setIsOpened(!isOpened);
          }}
        >
          {selectValue}
          <div
            className={
              isOpened
                ? "rotate-180 transition duration-300"
                : "transitio duration-300"
            }
          >
            <ArrowDown />
          </div>
        </div>
        {isOpened && (
          <ul className="flex flex-col divide-y-2">
            <li
              onClick={() => {
                updateValue("option 1");
              }}
              className="child"
            >
              Option 1
            </li>
            <li
              onClick={() => {
                updateValue("option 2");
              }}
              className="child"
            >
              Option 2
            </li>
            <li
              onClick={() => {
                updateValue("option 3");
              }}
              className="child"
            >
              Option 3
            </li>
          </ul>
        )}
      </div>
    </div>
  );
}
