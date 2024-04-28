import { useState } from "react";

export default function EffectDemo() {
  const [fName, setFName] = useState("John");
  const [lName, setLName] = useState("Doe");
  const fullName = fName + " " + lName;

  console.log(fullName);

  return (
    <>
      <input
        value={fName}
        onChange={(e) => setFName(e.target.value)}
        placeholder="First Name"
      />
      <input
        value={lName}
        onChange={(e) => setLName(e.target.value)}
        placeholder="Last Name"
      />
      <h2>{fullName}</h2>
    </>
  );
}
