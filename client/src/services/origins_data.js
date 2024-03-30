import { ORIGINS_DATA, TRANSLATION_DATAS } from "../routes";

export function getOriginsData(axiosPrivate, data, signal) {
  const _data = {
    user_id: data.user_id,
    language: data.language == null ? "lingala" : data.language,
  };
  return new Promise(async (resolve, reject) => {
    await axiosPrivate
      .get(ORIGINS_DATA, { params: _data, signal: signal })
      .then((response) => {
        resolve(response);
      })
      .catch((error) => {
        reject(error);
      });
  });
}

export function translationDatas(axiosPrivate, _data) {
  return new Promise(async (resolve, reject) => {
    await axiosPrivate
      .post(TRANSLATION_DATAS, _data, {
        headers: { "Content-Type": "multipart/form-data" },
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
