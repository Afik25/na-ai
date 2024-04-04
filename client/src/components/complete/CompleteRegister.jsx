import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { MdOutlineArrowForwardIos, FaCamera } from "../../middlewares/icons";
import { useTranslation } from "react-i18next";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import swal from "sweetalert";
import { useSelector } from "react-redux";
import useAxiosPrivate from "../../hooks/context/state/useAxiosPrivate";
import {
  isEmpty,
  wait,
  validationCompleteInscriptionStepOne,
  validationCompleteInscriptionStepTwo,
} from "../../utils/utils";

import countries from "../../middlewares/countries.json";
import useLogout from "../../hooks/context/state/useLogout";
import {
  completeInscription,
  completeActivation,
} from "../../services/authentication";

const CompleteRegister = () => {
  const axiosPrivate = useAxiosPrivate();
  const { t } = useTranslation();
  const [activeOption, setActiveOption] = useState(0);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [selectedFile, setSelectedFile] = useState();
  //
  const navigate = useNavigate();
  const logout = useLogout();
  const signOut = async () => {
    await logout();
    navigate("/login");
  };
  //
  const connectedUser = useSelector(
    (state) => state.setInitConf.initConnectedUser.connectedUserData
  );

  let validations = {
    0: validationCompleteInscriptionStepOne,
    1: validationCompleteInscriptionStepTwo,
  };
  const {
    register,
    setValue,
    handleSubmit,
    formState: { errors },
  } = useForm({
    mode: "all",
    resolver: yupResolver(validations[activeOption]),
    defaultValues: {
      id: connectedUser?.userInfo?.user_id,
      is_completed: true,
      firstname: connectedUser?.userInfo?.prename,
      lastname: connectedUser?.userInfo?.name,
      gender: connectedUser?.userInfo?.gender,
      telephone: connectedUser?.userInfo?.telephone,
      mail: connectedUser?.userInfo?.mail ?? "",
      birth: connectedUser?.userInfo?.birth,
      birth_location: connectedUser?.userInfo?.birth_location,
    },
  });

  const handleFile = (e) => {
    if (e.target.files && e.target.files.length !== 0) {
      setSelectedFile(e.target.files[0]);
    }
  };

  const onSubmit = async (data) => {
    // data traitment for submitting
    await wait(1000);
    //
    if (activeOption === 0) {
      setIsSubmitting(!isSubmitting);
      completeInscription(axiosPrivate, data)
        .then((result) => {
          let response = result;
          if (response?.data?.status === 1) {
            setIsSubmitting(false);
            swal({
              title: "Registration completion",
              text: `${response?.data?.message}. Code : ${response?.data?.code}`,
              icon: "success",
              button: "Ok",
            }).then((res) => {
              swal("A confirmation code have been sent by E-mail.");
            });
            setActiveOption(1);
          }
        })
        .catch((error) => {
          setIsSubmitting(false);
          if (!error?.response) {
            swal({
              title: "Oups!",
              text: "No server response!",
              icon: "warning",
              buttons: true,
            });
          } else {
            swal({
              title: "Operation failed!",
              text: error?.response?.data?.detail?.message,
              icon: "warning",
              buttons: true,
            });
          }
        });
    } else {
      setIsSubmitting(!isSubmitting);
      completeActivation(axiosPrivate, data)
        .then((result) => {
          let response = result;
          if (response?.data?.status === 1) {
            setIsSubmitting(false);
            swal({
              title: "Completion process",
              text: response?.data?.message,
              icon: "success",
              button: "Ok",
            }).then((res) => {
              swal(
                "The system will automatically disconnect you. And Get connected!"
              );
              signOut();
            });
          }
        })
        .catch((error) => {
          setIsSubmitting(false);
          if (!error?.response) {
            swal({
              title: "Oups!",
              text: "No server response!",
              icon: "warning",
              buttons: true,
            });
          } else {
            swal({
              title: "Operation failed!",
              text: error?.response?.data?.message,
              icon: "warning",
              buttons: true,
            });
          }
        });
    }
  };

  let fragments = {
    0: (
      <div className="steps">
        <p className="title t-2">Complete your personal informations.</p>
        <div className="first-step containers">
          <div className="input-div" style={{ textAlign: "center" }}>
            <p className="title t-3">Picture for your profile(Optional).</p>
            <div className="input-image">
              <img
                src={
                  !selectedFile
                    ? process.env.PUBLIC_URL + "/user.png"
                    : URL.createObjectURL(selectedFile)
                }
                className="image"
                alt="user-prof"
              />
              <div className="input-upload">
                <input
                  type="file"
                  id="thumbnails"
                  className="input-file"
                  autoComplete="none"
                  placeholder=" "
                  onChange={handleFile}
                  //   {...register("thumbnails")}
                  accept="image/*"
                />
                <label htmlFor="thumbnails" className="input-file-label">
                  <FaCamera />
                </label>
              </div>
            </div>
          </div>
          <div className="container-48">
            <div className="input-div">
              <input
                type="text"
                className="input-form"
                autoComplete="none"
                placeholder=" "
                {...register("firstname")}
              />
              <label htmlFor="firstname" className="label-form">
                First name
              </label>
              {errors.firstname && (
                <span className="fade-in">{errors.firstname.message}</span>
              )}
            </div>
            <div className="input-div">
              <input
                type="text"
                className="input-form"
                autoComplete="none"
                placeholder=" "
                {...register("lastname")}
              />
              <label
                htmlFor="lastname
"
                className="label-form"
              >
                Last Name
              </label>
              {errors.lastname && (
                <span className="fade-in">{errors.lastname.message}</span>
              )}
            </div>
          </div>
          <div className="input-div">
            <select className="input-form" {...register("gender")}>
              <option value="" style={{ color: "grey" }}>
                Gender
              </option>
              <option value="Female">Female</option>
              <option value="Male">Male</option>
            </select>
            {errors.gender && (
              <span className="fade-in">{errors.gender.message}</span>
            )}
          </div>
          <div className="input-div">
            <input
              type="text"
              className="input-form"
              autoComplete="none"
              placeholder=" "
              {...register("telephone")}
            />
            <label htmlFor="telephone" className="label-form">
              Telephone
            </label>
            {errors.telephone && (
              <span className="fade-in">{errors.telephone.message}</span>
            )}
          </div>
          <div className="input-div">
            <input
              type="text"
              className="input-form"
              autoComplete="none"
              placeholder=" "
              {...register("mail")}
            />
            <label htmlFor="mail" className="label-form">
              Mail
            </label>
            {errors.mail && (
              <span className="fade-in">{errors.mail.message}</span>
            )}
          </div>
          <div className="container-48">
            <div className="input-div">
              <input
                type="date"
                className="input-form"
                autoComplete="none"
                placeholder=" "
                {...register("birth")}
              />
              <label htmlFor="birth" className="label-form">
                Date de Naissance
              </label>
              {errors.birth && (
                <span className="fade-in">{errors.birth.message}</span>
              )}
            </div>
            <div className="input-div">
              <input
                type="text"
                className="input-form"
                autoComplete="none"
                placeholder=" "
                {...register("birth_location")}
              />
              <label htmlFor="birth_location" className="label-form">
                Lieu de Naissance
              </label>
              {errors.birth_location && (
                <span className="fade-in">{errors.birth_location.message}</span>
              )}
            </div>
          </div>
          <div className="input-div">
            <select className="input-form" {...register("nationality")}>
              <option value="" style={{ color: "grey" }}>
                Country of Origin
              </option>
              {isEmpty(countries) ? (
                <option value="" selected>
                  No country available!
                </option>
              ) : (
                countries.map((item, i) => (
                  <option key={i} value={item.name.official}>
                    {item.name.official}
                  </option>
                ))
              )}
            </select>
            {errors.nationality && (
              <span className="fade-in">{errors.nationality.message}</span>
            )}
          </div>
        </div>
      </div>
    ),
    1: (
      <div className="steps">
        <p className="title t-2">An Activation code was send by SMS.</p>
        <div className="containers">
          <div className="input-div">
            <input
              type="text"
              className="input-form"
              autoComplete="none"
              placeholder=" "
              {...register("confirmation_code")}
            />
            <label htmlFor="username" className="label-form">
              Activation code
            </label>
            {errors.confirmation_code && (
              <span className="fade-in">
                {errors.confirmation_code.message}
              </span>
            )}
          </div>
        </div>
      </div>
    ),
  };

  return (
    <div className="complete-register">
      <div className="cr-head">
        <div className={activeOption === 0 ? "cr-tab active-tab" : "cr-tab"}>
          <span>Personal informations</span>
        </div>
        <div className="cr-tab">
          <MdOutlineArrowForwardIos />
        </div>
        <div className={activeOption === 3 ? "cr-tab active-tab" : "cr-tab"}>
          <span>Activation</span>
        </div>
      </div>
      <div className="cr-body">
        <form onSubmit={handleSubmit(onSubmit)}>
          {fragments[activeOption]}
          <div className="buttons">
            {isSubmitting ? (
              <div className="loader"></div>
            ) : (
              <button type="submit" className="button validate">
                {activeOption === 0 ? "Valider" : "Confirmer & Activer"}
              </button>
            )}
          </div>
        </form>
      </div>
    </div>
  );
};

export default CompleteRegister;
