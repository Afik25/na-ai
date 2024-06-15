import React, { useState } from "react";
import { Helmet, HelmetProvider } from "react-helmet-async";
import { Link, useNavigate } from "react-router-dom";
import { BsEyeSlash, BsEye } from "../middlewares/icons";
import ControlLanguage from "../components/languages/ControlLanguage";
//
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import { validationSchemaLogin, wait } from "../utils/utils";
//
import { login } from "../services/authentication";
import useAuth from "../hooks/context/state/useAuth";
import MessageBox from "../components/msgBox/MessageBox";
//
const Login = () => {
  const [showPwd, setShowPwd] = useState(false);
  const [isSending, setIsSending] = useState(false);
  const [onRequest, setOnRequest] = useState({ show: false, onSucces: false });
  const [msg, setMsg] = useState("");

  const { setAuth } = useAuth();
  const navigate = useNavigate();

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    mode: "onTouched",
    resolver: yupResolver(validationSchemaLogin),
  });

  const onSubmit = async (data) => {
    setIsSending(true);
    await wait(1000);
    //
    login(data)
      .then((response) => {
        console.log({ "Tala reponse ": response });
        if (response?.data?.isLogged) {
          setIsSending(false);
          setMsg(response?.data?.message);
          setOnRequest({ show: true, onSucces: true });
        }
        const accessToken = response?.data?.accessToken;
        const sys_role = response?.data?.sys_role;
        const to = "/" + sys_role;
        const timer = setTimeout(() => {
          setOnRequest({ show: false, onSucces: false });
          setAuth({ sys_role, accessToken });
          navigate(to, { replace: true });
        }, 2000);
        return () => clearTimeout(timer);
      })
      .catch((error) => {
        setIsSending(false);
        setOnRequest({ show: true, onSucces: false });
        if (!error?.response) {
          setMsg("No server response");
        } else {
          setMsg(error?.response?.data?.message);
        }
        const timer = setTimeout(() => {
          setOnRequest({ show: false, onSucces: false });
        }, 2000);
        return () => clearTimeout(timer);
      });
  };

  return (
    <HelmetProvider>
      <Helmet>
        <title>na-AI - Sign In.</title>
        <meta
          name="description"
          content="Get connected and navigate in opportunities."
        />
        <meta
          name="keywords"
          content="Language, Communication, École, School, Masomo, Étudier, Éducation"
        />
      </Helmet>
      <div className="sign-in-up">
        <div className="head">
          <Link to="/" className="link logo">
            <img src={process.env.PUBLIC_URL + "/logo.png"} alt="na-ai-logo" />
          </Link>
          <ControlLanguage />
        </div>
        <div className="container">
          <div className="left">
            <form onSubmit={handleSubmit(onSubmit)} className="form">
              <h2 className="title t-1">Sing In</h2>
              <p className="title t-3">
                Get connected and start manage your activities with Shop
              </p>
              {onRequest.show && (
                <MessageBox text={msg} isSuccess={onRequest.onSucces} />
              )}
              <div className="form-components">
                <div className="input-div">
                  <input
                    type="text"
                    className="input-form"
                    autoComplete="none"
                    placeholder=" "
                    {...register("username")}
                  />
                  <label htmlFor="username" className="label-form">
                    Username ou E-mail ou Telephone
                  </label>
                  {errors.username && (
                    <span className="fade-in">{errors.username.message}</span>
                  )}
                </div>
                <div className="input-div">
                  <input
                    type={showPwd ? "text" : "password"}
                    className="input-form"
                    autoComplete="none"
                    placeholder=" "
                    {...register("password")}
                  />
                  <label htmlFor="password" className="label-form">
                    Password
                  </label>
                  <label htmlFor="password" className="label-icon">
                    {showPwd ? (
                      <BsEye
                        style={{ cursor: "pointer" }}
                        onClick={() => setShowPwd(!showPwd)}
                      />
                    ) : (
                      <BsEyeSlash
                        style={{ cursor: "pointer" }}
                        onClick={() => setShowPwd(!showPwd)}
                      />
                    )}
                  </label>
                  {errors.password && (
                    <span className="fade-in">{errors.password.message}</span>
                  )}
                </div>
              </div>
              <div className="input-div display-flex justify-content-flex-end">
                <Link to="" className="link">
                  Forgot password ?
                </Link>
              </div>
              <button
                type="submit"
                className={isSending ? "width button" : "width button normal"}
              >
                {isSending ? "Connexion..." : "Sign In"}
              </button>
              <div className="get_sign-in">
                <span>You don't have account ?</span>
                <Link to="/register" className="btn-sign-in link">
                  Sign Up
                </Link>
              </div>
            </form>
          </div>
          <div className="right">
            <h1 className="title t-1">with na-AI</h1>
            <h3 className="title t-2">
              Make simple your communication and understanding in local
              languages!
            </h3>
            <img
              src={process.env.PUBLIC_URL + "/people-speech.png"}
              alt="na-ai-brand"
            />
          </div>
        </div>
        <div className="foot">
          <span>
            All rights reserved Afik Foundation &copy;{" "}
            {new Date().getFullYear()} - na-AI Platform.
          </span>
        </div>
      </div>
    </HelmetProvider>
  );
};
export default Login;
