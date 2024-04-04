import React from "react";
import Header from "../components/header/Header";
import Footer from "../components/footer/Footer";

const TextTranslation = () => {
  return (
    <div className="text-translations">
      <div className="head">
        <Header />
      </div>
      <div className="body">
        <h1 className="title t-1">Make your translations easily and with more precision...</h1>
        <div
        className="container">
            <div className="left">
                <div className="input-select-box">
                    <select>
                        <option value={'en'}>English</option>
                        <option value={'fr'}>French</option>
                        <option value={'ki'}>Kikongo</option>
                        <option value={'li'}>Lingala</option>
                        <option value={'sw'}>Swahili</option>
                        <option value={'tshi'}>Tshiluba</option>
                    </select>
                </div>
                <div className="input-textarea-box">
                    <textarea></textarea>
                </div>
                <div className="input-voice-box"></div>
            </div>
            <div className="middle">
                <button className="button">Swap</button>
                <button className="button">Translate</button>
            </div>
            <div className="right"></div>
        </div>
      </div>
      <div className="foot">
        <Footer />
      </div>
    </div>
  );
};

export default TextTranslation;
