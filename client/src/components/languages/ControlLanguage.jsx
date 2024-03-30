import { useState, useEffect } from "react";
import { BiChevronDown, BiChevronUp } from "../../middlewares/icons";
import languages from "../../languages/languages.json";
//
import { useTranslation } from "react-i18next";

const ControlLanguage = () => {
  const { i18n } = useTranslation();
  const [open, setOpen] = useState(false);
  const [language, setLanguage] = useState({
    flag: "flag-en.png",
    label: "english",
  });

  // en-US
  // fr

  useEffect(()=>{
    const lng = navigator.language;
    i18n.changeLanguage(lng);
  }, [])

  return (
    <div className="languages">
      <div
        className="display-flex justify-content-center align-items-center lang-selected"
        onClick={() => setOpen(!open)}
      >
        <img
          src={process.env.PUBLIC_URL + `/flags/${language.flag}`}
          alt="default-flag"
        />
        <span>{language.label}</span>
        <span>{open ? <BiChevronUp /> : <BiChevronDown />}</span>
      </div>
      {open && (
        <div className="lang-options">
          {languages.map((item, i) => {
            if (item.label !== language.label) {
              return (
                <div
                  key={i}
                  className="display-flex justify-content-flex-start align-items-center lang-option"
                  onClick={() => {
                    setLanguage({
                      flag: item.flag,
                      label: item.label,
                    });
                    i18n.changeLanguage(item.lang);
                    setOpen(false);
                  }}
                >
                  <img
                    src={process.env.PUBLIC_URL + `/flags/${item.flag}`}
                    alt={item.label + "-" + item.flag}
                  />
                  <span>{item.label}</span>
                </div>
              );
            }
          })}
        </div>
      )}
    </div>
  );
};

export default ControlLanguage;
