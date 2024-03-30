import React, { useState } from "react";
import { Link } from "react-router-dom";
import { useTranslation } from "react-i18next";
import ControlLanguage from "../languages/ControlLanguage";

const Header = () => {
  const { t } = useTranslation();
  const [fix, setFix] = useState(false);
  const [open, setOpen] = useState(false);

  function fixedOnscroll() {
    if (window.scrollY >= 600) {
      setFix(true);
    } else {
      setFix(false);
    }
  }
  window.addEventListener("scroll", fixedOnscroll);

  return (
    <div className={fix ? "header fixed" : "header"}>
      <div className="container">
        <Link to="/">
          <img src={process.env.PUBLIC_URL + "/logo.png"} className="logo" />
        </Link>
        <div
          className={open ? "menu-drawer open" : "menu-drawer"}
          onClick={() => setOpen(!open)}
        >
          <div className="burger"></div>
        </div>
        <div className={open ? "nav display-flex-important" : "nav"}>
          <Link to="" className="nav-item link">
            {t("header.text-1")}
          </Link>
          <Link to="" className="nav-item link">
          {t("header.text-2")}
          </Link>
          <Link to="/about" className="nav-item link">
          {t("header.text-3")}
          </Link>
        </div>
        <div className={open ? "sign-nav display-flex-important" : "sign-nav"}>
          <Link to="/login" className="button">
          {t("header.text-4")}
          </Link>
          <Link to="/register" className="button">
          {t("header.text-5")}
          </Link>
          <ControlLanguage />
        </div>
      </div>
    </div>
  );
};

export default Header;
