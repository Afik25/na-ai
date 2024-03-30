import React from "react";
import {
  MdOutlineArrowBackIos,
  MdOutlineArrowForwardIos,
  FaLockOpen,
  FaLock,
} from "../../middlewares/icons";
import { useDispatch, useSelector } from "react-redux";
import useAxiosPrivate from "../../state/context/hooks/useAxiosPrivate";
import { isEmpty, wait } from "../../utils/utils";
import { getUsers, onAssignationLanguage } from "../../services/users";
import moment from "moment";
import swal from "sweetalert";

const User = () => {
  const axiosPrivate = useAxiosPrivate();
  const dispatch = useDispatch();
  const users = useSelector(
    (state) => state.setInitConf.initUsersData.usersData
  );

  React.useEffect(() => {
    let isMounted = true;
    const controller = new AbortController();
    const signal = controller.signal;

    getUsers(axiosPrivate, signal).then((result) => {
      dispatch({
        type: "setUp/getUsers",
        payload: result,
      });
    });

    return () => {
      isMounted = false;
      isMounted && controller.abort();
    };
  }, []);

  const onAssignedLanguage = (user_id, language) => {
    // alert(user_id + " - " + language);
    const data = {
      user_id: user_id,
      language: language,
    };
    onAssignationLanguage(axiosPrivate, data).then((response) => {
      let isMounted = true;
      const controller = new AbortController();
      const signal = controller.signal;
      if (response?.data?.status === 1) {
        swal({
          icon: "success",
          title: "Language's Assignation Process",
          text: response?.data?.result,
        });

        getUsers(axiosPrivate, signal).then((result) => {
          dispatch({
            type: "setUp/getUsers",
            payload: result,
          });
        });
      }

      return () => {
        isMounted = false;
        isMounted && controller.abort();
      };
    }).catch((error) => {
      if (!error?.response) {
        swal({
          icon: "warning",
          title: "Language's Assignation Process",
          text: "No server response",
        });
      } else {
        swal({
          icon: "warning",
          title: "Language's Assignation Process",
          text: error?.response?.data?.message,
        });
      }
    });
  };

  return (
    <div className="users">
      <div className="head">
        <h2 className="title t-1">Inscribed users</h2>
        <p className="title t-3">All inscribed users from here.</p>
      </div>
      <div className="body">
        <div className="table">
          <table>
            <thead>
              <tr>
                <th>Date inscription</th>
                <th>Username</th>
                <th>Names</th>
                <th>Gender</th>
                <th>Mail</th>
                <th>Role</th>
                <th>Assigned Language</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              {isEmpty(users?.data?.result) ? (
                <tr>
                  <td
                    colSpan="8"
                    style={{
                      textAlign: "center",
                      color: "lightslategray",
                      fontSize: "1em",
                    }}
                  >
                    {users?.data?.message}
                  </td>
                </tr>
              ) : (
                users?.data?.result.map((item, i) => {
                  return (
                    <tr key={i}>
                      <td className="tbody-col-1">
                        {`${moment(item.created_at).format("ll")} at ${moment(
                          item.created_at
                        ).format("LT")}`}
                      </td>
                      <td className="tbody-col-2">{item.username}</td>
                      <td className="tbody-col-3">
                        {item.prename + " " + item.name}
                      </td>
                      <td className="tbody-col-4">{item.gender}</td>
                      <td className="tbody-col-5">{item.mail}</td>
                      <td className="tbody-col-6">{item.sys_role}</td>
                      <td className="tbody-col-7">
                        <div className="container">
                          <p className="title t-2">
                            {item.assigned_language != null
                              ? item.assigned_language
                              : "---"}
                          </p>
                          <div>
                            <button
                              className="button"
                              onClick={() =>
                                onAssignedLanguage(item.id, "kikongo")
                              }
                            >
                              Kikongo
                            </button>
                            <button
                              className="button"
                              onClick={() =>
                                onAssignedLanguage(item.id, "lingala")
                              }
                            >
                              Lingala
                            </button>
                            <button
                              className="button"
                              onClick={() =>
                                onAssignedLanguage(item.id, "swahili")
                              }
                            >
                              Swahili
                            </button>
                            <button
                              className="button"
                              onClick={() =>
                                onAssignedLanguage(item.id, "tshiluba")
                              }
                            >
                              Tshiluba
                            </button>
                          </div>
                        </div>
                      </td>
                      <td className="tbody-col-8">
                        <button className="btn btn-remove">
                          <FaLockOpen />
                          <span>lock</span>
                        </button>
                      </td>
                    </tr>
                  );
                })
              )}
            </tbody>
          </table>
        </div>
        <div className="pagination display-flex justify-content-space-between align-items-center">
          <span>1-5 of 45</span>
          <div className="display-flex align-items-center">
            <div className="display-flex align-items-center">
              <span>Rows per page :</span>
              <select>
                <option>5</option>
                <option>10</option>
              </select>
            </div>
            <div className="display-flex align-items-center">
              <button className="button">
                <MdOutlineArrowBackIos className="icon" />
              </button>
              <button className="button">
                <MdOutlineArrowForwardIos className="icon" />
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default User;
