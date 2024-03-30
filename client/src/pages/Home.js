import React, { useState } from "react";
import { Helmet } from "react-helmet";
import { Link } from "react-router-dom";
import Header from "../components/header/Header.jsx";
import Footer from "../components/footer/Footer.jsx";
import {MdTranslate, MdRecordVoiceOver, BsFileEarmarkText, IoMdChatboxes} from "../middlewares/icons.js";

const Home = () => {
  const [fix, setFix] = useState(false);

  function fixedOnscroll() {
    if (window.scrollY >= 600) {
      setFix(true);
    } else {
      setFix(false);
    }
  }
  window.addEventListener("scroll", fixedOnscroll);
  return (
    <React.Fragment>
      <Helmet>
        <title>Home - na-AI.</title>
        <meta
          name="description"
          content="La communication devient simple avec les langues locales en République Démocratique du Congo."
        />
        <meta
          name="keywords"
          content="Langue, Language, Communication, Lingala, Kikongo, Tshiluba, Swahili"
        />
      </Helmet>
      <div className="home">
        <Header />
        <div className="banner">
          <div className="content">
            <h1 className="title t-1">Communication in Democratic Republic of Congo !</h1>
            <p className="title t-3">na-AI makes communication very simple in DR Congo through the official local languages !</p>
            <div className="get-in-touch">
              <Link to='' className="button">Get in touch with Us</Link>
            </div>
          </div>
          <img src={process.env.PUBLIC_URL + "/ai-banner.jpg"} alt="ai-banner" />
        </div>
        <div className="features">
          <h2 className="title t-2">Discover Our Full Range of Features</h2>
          <p className="title t-3">Features based entirely on the locales languages such Kikongo, Lingala, Swahili and Tshiluba; beyond English and French ...</p>
          <div className="container">
            <Link to='ttranslations' className="button"><MdTranslate className="icon"/><span>Translations</span></Link>
            <Link to='' className="button"><MdRecordVoiceOver className="icon"/><span>Speech Translations</span></Link>
            <Link to='' className="button"><BsFileEarmarkText className="icon"/><span>Text Summerization</span></Link>
            <Link to='' className="button"><IoMdChatboxes className="icon"/><span>Conversational ChatBot</span></Link>
          </div>
        </div>
        <Footer/>
      </div>
    </React.Fragment>
  );
};

export default Home;
