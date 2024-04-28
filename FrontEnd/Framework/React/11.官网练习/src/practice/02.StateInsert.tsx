import { useState } from "react";

export default function StateInsert() {
  const [isShow, setIsShow] = useState(true);
  const [fName, setFName] = useState("Jane");
  const [lName, setLName] = useState("Jacobs");
  return (
    <>
      <form
        className="flex flex-col items-center  "
        onSubmit={(e) => {
          e.preventDefault();
          setIsShow(!isShow);
        }}
      >
        <label>
          First name:{" "}
          {isShow ? (
            <b>{fName}</b>
          ) : (
            <input
              value={fName}
              onChange={(e) => {
                if (e.target.value.trim.length > 0) {
                  setFName(e.target.value);
                }
              }}
            />
          )}
        </label>
        <label>
          Last name:{" "}
          {isShow ? (
            <b>{lName}</b>
          ) : (
            <input
              value={lName}
              onChange={(e) => {
                if (e.target.value.trim().length > 0) setLName(e.target.value);
              }}
            />
          )}
        </label>
        <button type="submit">{isShow ? "Edit" : "Save"}</button>
        <p>
          <i>
            Hello, {fName} {lName}!
          </i>
        </p>
      </form>
    </>
  );
}
