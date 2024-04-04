import React, { useState } from "react";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import useAxiosPrivate from "../../hooks/context/state/useAxiosPrivate";
import { wait, validationLoadData } from "../../utils/utils";
import { loadData } from "../../services/authentication";
import swal from "sweetalert";

const LoadData = () => {
  const axiosPrivate = useAxiosPrivate();
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [onProcessEnded, setOnProcessEnded] = useState({
    onSucces: false,
    onFailed: false,
  });

  const {
    register,
    setValue,
    handleSubmit,
    formState: { errors },
  } = useForm({
    mode: "all",
    resolver: yupResolver(validationLoadData),
  });

  const onSubmit = async (data) => {
    // data traitment for submitting
    await wait(1000);
    //
    setIsSubmitting(!isSubmitting);
    loadData(axiosPrivate, data)
      .then((result) => {
        let response = result;
        if (response?.data?.status === 1) {
          setIsSubmitting(false);
          setOnProcessEnded({ onSucces: true, onFailed: false });
        }
        const timer = setTimeout(() => {
          setOnProcessEnded({ onSucces: false, onFailed: false });
        }, 50000);
        return () => clearTimeout(timer);
      })
      .catch((error) => {
        setIsSubmitting(false);
        setOnProcessEnded({ onSucces: false, onFailed: true });
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
        const timer = setTimeout(() => {
          setOnProcessEnded({ onSucces: false, onFailed: false });
        }, 50000);
        return () => clearTimeout(timer);
      });
  };

  return (
    <div className="load-data">
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className="input-div">
          <input
            type="text"
            className="input-form"
            autoComplete="none"
            placeholder=" "
            {...register("fileName")}
          />
          <label htmlFor="fileName" className="label-form">
            File name
          </label>
          {errors.fileName && (
            <span className="fade-in">{errors.fileName.message}</span>
          )}
        </div>
        <div className="input-div">
          <input
            type="text"
            className="input-form"
            autoComplete="none"
            placeholder=" "
            {...register("category")}
          />
          <label htmlFor="category" className="label-form">
            Category Data
          </label>
          {errors.category && (
            <span className="fade-in">{errors.category.message}</span>
          )}
        </div>
        <button type="submit" className="button validate">
          Process
        </button>
      </form>
      {isSubmitting && (
        <div className="loagin-data-process">
          {!onProcessEnded.onSucces && !onProcessEnded.onFailed && (
            <span>Data processing and loading...</span>
          )}
          {onProcessEnded.onSucces && (
            <span>Data processing and loading complete successfully.</span>
          )}
          {onProcessEnded.onFailed && (
            <span>Data processing and loading process failed</span>
          )}
        </div>
      )}
    </div>
  );
};

export default LoadData;
