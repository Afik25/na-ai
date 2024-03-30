import React from "react";
import { useTranslation } from "react-i18next";
import { Link } from "react-router-dom";
import {
  BiPhone,
  FaFacebookF,
  FaTwitter,
  FaLinkedinIn,
  FaYoutube,
  FaAt,
  FaMapMarkerAlt,
} from "../../middlewares/icons";

const Footer = () => {
  const { t } = useTranslation();
  return (
    <div className="footer">
      <div className="container">
        <div className="top">
          <div className="left">
            <img src={process.env.PUBLIC_URL + "/na-ai-white.png"} />
            <p className="title t-3">{t("footer.text-1")}</p>
          </div>
          <div className="center">
            <h3 className="title t-2">{t("footer.text-2")}</h3>
            <Link to="" className="link">
              {t("header.text-1")}
            </Link>
            <Link to="" className="link">
              {t("header.text-2")}
            </Link>
            <Link to="" className="link">
              {t("header.text-3")}
            </Link>
            <Link to="" className="link">
              {t("header.text-4")}
            </Link>
          </div>
          <div className="right">
            <h3 className="title t-2">{t("footer.text-3")}</h3>
            <p className="title t-3">
              <FaAt className="icon" /> <span>info@na-ai.com</span>
            </p>
            <p className="title t-3">
              <BiPhone className="icon" /> <span>+243 99 XX XX XXX</span>
            </p>
            <p className="title t-3">
              <FaMapMarkerAlt className="icon" />{" "}
              <span>Kinshasa - Congo DR</span>
            </p>
          </div>
          <div className="socials-network">
            <Link to="" className="link">
              <span className="icon">
                <FaFacebookF />
              </span>
              <span className="social">Facebook</span>
            </Link>
            <Link to="" className="link">
              <span className="icon">
                <FaTwitter />
              </span>
              <span className="social">Twitter</span>
            </Link>
            <Link to="" className="link">
              <span className="icon">
                <FaLinkedinIn />
              </span>
              <span className="social">LinkedIn</span>
            </Link>
            <Link to="" className="link">
              <span className="icon">
                <FaYoutube />
              </span>
              <span className="social">Youtube</span>
            </Link>
          </div>
        </div>
        <div className="bottom">
          <div className="left">
            <span>&copy; {new Date().getFullYear()} na-AI, {t("footer.text-4")}</span>
            <Link to="" className="link">
              {t("footer.text-5")}
            </Link>
          </div>
          <div className="right">
            <Link to="" className="link">
              {t("footer.text-6")}
            </Link>
            <Link to="" className="link">
              {t("footer.text-7")}
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Footer;
