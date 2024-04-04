import * as Yup from "yup";

export const isEmpty = (value) => {
  return (
    value === undefined ||
    value === null ||
    (typeof value === "object" && Object.keys(value).length === 0) ||
    (typeof value === "object" && Object.entries(value).length === 0) ||
    (typeof value === "string" && value.trim().length === 0)
  );
};

export const wait = (duration = 1000) => {
  return new Promise((resolve) => {
    window.setTimeout(resolve, duration);
  });
};

export const capitalize = (s) => s && s[0].toUpperCase() + s.slice(1);

export const validationSchemaSubmit = Yup.object().shape({
  prename: Yup.string()
    .required("First Name is required")
    .min(2, "The first name must have at least 2 caractors"),
  name: Yup.string()
    .required("Last Name is required")
    .min(2, "The last name must have at least 2 caractors"),
  username: Yup.string().required("Username is required"),
  password: Yup.string()
    .required("Password is required")
    .min(6, "The password must have at least 6 caractors"),
  confirm_password: Yup.string()
    .required("Confirm password is required")
    .oneOf([Yup.ref("password"), null], "The password must match!"),
  gcu: Yup.boolean().oneOf(
    [true],
    "You have to be agree with the terms and privacy of using."
  ),
});

export const validationSchemaRegister = Yup.object().shape({
  firstname: Yup.string()
    .required("First Name is required")
    .min(2, "The first name must have at least 2 caractors"),
  lastname: Yup.string()
    .required("Last Name is required")
    .min(2, "The last name must have at least 2 caractors"),
  username: Yup.string().required("Username is required"),
  password: Yup.string()
    .required("Password is required")
    .min(6, "The password must have at least 6 caractors"),
  confirm_password: Yup.string()
    .required("Confirm password is required")
    .oneOf([Yup.ref("password"), null], "The password must match!"),
  gcu: Yup.boolean().oneOf(
    [true],
    "You have to be agree with the terms and privacy of using."
  ),
});

export const validationSchemaLogin = Yup.object().shape({
  username: Yup.string().required(
    "Username or telephone or E-mail is required."
  ),
  password: Yup.string().required("Password is required."),
});

export const validationCompleteInscriptionStepOne = Yup.object().shape({
  firstname: Yup.string()
    .required("First name is required")
    .min(2, "First name require at least 2 caractors"),
  lastname: Yup.string()
    .required("Last name is required")
    .min(2, "Last name require at least 2 caractors"),
  gender: Yup.string().required("Gender is required"),
  telephone: Yup.number()
    .typeError("You should specify a phone number")
    .required("Phone number is required")
    .min(8, "Input a valid phone number"),
  mail: Yup.string()
    .required("E-mail is required")
    .email("Input a valid address e-mail"),
  birth: Yup.string().required("Birth date is required"),
  birth_location: Yup.string().required("Birth location is required"),
  nationality: Yup.string().required("the country of origin is required"),
});

export const validationCompleteInscriptionStepTwo = Yup.object().shape({
  confirmation_code: Yup.string().required("Input confirmation's code"),
});

export const validationLoadData = Yup.object().shape({
  fileName: Yup.string().required("Provide the name of file"),
  category: Yup.string().required("Provide the category of data"),
});
