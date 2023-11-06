import React, { useState, useEffect } from "react";
import { formateDate } from "../../utils/dateUtils";

export default function Timer() {
  const [currentTime, setCurrentTime] = useState(formateDate(Date.now()));
  useEffect(() => {
    const token = setInterval(() => {
      setCurrentTime(formateDate(Date.now()));
    }, 1000);
    return () => {
      clearInterval(token);
    };
  }, [currentTime]);
  return <span className="header-bottom-right-time">{currentTime}</span>;
}
