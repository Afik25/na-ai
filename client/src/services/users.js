import { USERS, ON_ASSIGNATION } from "../routes";

export function getUsers(axiosPrivate, signal) {
  return new Promise(async (resolve, reject) => {
    await axiosPrivate
      .get(USERS, {
        signal: signal,
      })
      .then((response) => {
        resolve(response);
      })
      .catch((error) => {
        reject(error);
      });
  });
}

export function onAssignationLanguage(axiosPrivate, data) {
  const _data = {
    user_id: data.user_id,
    language: data.language
  };
  return new Promise(async (resolve, reject) => {
    await axiosPrivate
      .post(ON_ASSIGNATION, _data, {
        headers: { "Content-Type": "application/json" },
        withCredentials: true,
      })
      .then((response) => {
        resolve(response);
      })
      .catch((error) => {
        reject(error);
      });
  });
}
