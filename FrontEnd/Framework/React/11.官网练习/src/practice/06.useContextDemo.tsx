import { createContext, useContext, useRef, useState } from "react";

const CurrentUserContext = createContext(null);

export default function UseContextDemo() {
  const [currentUser, setCurrentUser] = useState(null);
  const val = useRef("test");
  return (
    <CurrentUserContext.Provider
      value={{
        currentUser,
        setCurrentUser,
      }}
    >
      <input
        placeholder="modify the test"
        onChange={(e) => {
          val.current = e.target.value;
        }}
      ></input>
      {val.current}
      <progress value={1} />
      <WelcomePannel />
    </CurrentUserContext.Provider>
  );
}

const WelcomePannel = () => {
  const { currentUser } = useContext(CurrentUserContext);
  return (
    <>
      {currentUser === null ? (
        <>
          <Form />
        </>
      ) : (
        <Greeting />
      )}
    </>
  );
};

const Form = () => {
  const { setCurrentUser } = useContext(CurrentUserContext);
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  return (
    <div>
      <label>
        姓: &nbsp;
        <input
          placeholder="请输入姓"
          onChange={(e) => {
            setFirstName(e.target.value);
          }}
        />
      </label>
      <label>
        名: &nbsp;
        <input
          placeholder="请输入名"
          onChange={(e) => {
            setLastName(e.target.value);
          }}
        />
      </label>
      <Button
        onClick={() => {
          setCurrentUser({
            name: firstName + " " + lastName,
          });
        }}
      >
        Log in
      </Button>
    </div>
  );
};

const Button = ({ children, onClick }) => {
  return <button onClick={onClick}>{children}</button>;
};

const Greeting = () => {
  const { currentUser, setCurrentUser } = useContext(CurrentUserContext);
  return (
    <>
      <h2>Welcome logged in as {currentUser.name}</h2>
      <Button
        onClick={() => {
          setCurrentUser(null);
        }}
      >
        Logout
      </Button>
    </>
  );
};
