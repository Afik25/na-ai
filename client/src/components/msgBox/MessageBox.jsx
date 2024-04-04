import React from "react";

const MessageBox = ({ text, isSuccess }) => {
  return (
    <div className="msg-box fade-in">
      <div className={isSuccess ? "onSuccess" : "onFailed"}>{text}</div>
    </div>
  );
};

export default MessageBox;
