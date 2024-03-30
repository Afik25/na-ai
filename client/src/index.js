import React from "react";
import ReactDOM from "react-dom/client";
import "./languages/i18n";
import "./assets/scss/index.scss";
// pages imports
import App from "./App";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
