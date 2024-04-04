import { useState } from "react";
import { Helmet, HelmetProvider } from "react-helmet-async";
import { Link, Outlet, useNavigate } from "react-router-dom";
import { NavLink } from "../routes/NavLink";
import {
  FiUser,
  FiUsers,
  FiLogOut,
  BiChevronDown,
  BiChevronUp,
  BiEnvelope,
  IoNotificationsOutline,
  IoHelp,
  MdOutlineDashboard,
  FaCloudUploadAlt,
} from "../middlewares/icons";
import useAxiosPrivate from "../hooks/context/state/useAxiosPrivate";
import useLogout from "../hooks/context/state/useLogout";
import Modal from "../components/modal/Modal";
import CompleteRegister from "../components/complete/CompleteRegister";
import { useSelector } from "react-redux";
import { capitalize } from "../utils/utils";
import LoadData from "../components/upload/LoadData";

const Administration = () => {
  const axiosPrivate = useAxiosPrivate();
  const [option, setOption] = useState(false);
  const [isLoadProcess, setIsLoadProcess] = useState(false);
  const [activeOption, setActiveOption] = useState(0);
  const [isSubmitting, setIsSubmitting] = useState(false);

  // logout
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

  return (
    <HelmetProvider>
      <Helmet>
        <title>na-AI - Administration</title>
        <meta name="description" content="" />
        <meta name="keywords" content="" />
      </Helmet>
      <>
        <div className="user">
          <div className="left">
            <div className="header">
              <img src={process.env.PUBLIC_URL + "/logo.png"} alt="logo" />
            </div>
            <div className="body">
              <div className="navigation">
                <NavLink
                  activeClassName="active-option"
                  inactiveClassName="inactive-option"
                  className="link-option"
                  to="/admin"
                  exact={true}
                >
                  <MdOutlineDashboard className="option-icon" />
                  <span>Dashboard</span>
                </NavLink>
                <NavLink
                  activeClassName="active-option"
                  inactiveClassName="inactive-option"
                  className="link-option"
                  to="/admin/users"
                >
                  <FiUsers className="option-icon" />
                  <span>Users</span>
                </NavLink>
              </div>
            </div>
          </div>
          <div className="right">
            <div className="header">
              <div className="options display-flex">
                <div className="profile">
                  <div
                    className="profile-item"
                    onClick={() => setIsLoadProcess(!isLoadProcess)}
                    style={{ cursor: "pointer" }}
                  >
                    <div className="option">
                      <FaCloudUploadAlt className="icon-element" />
                    </div>
                  </div>
                  <div
                    className={
                      isLoadProcess
                        ? "profile-item load-frame display"
                        : "profile-item"
                    }
                  >
                    <LoadData />
                  </div>
                </div>
                <div className="option">
                  <IoNotificationsOutline className="icon-element" />
                  <span></span>
                </div>
                <div className="option">
                  <BiEnvelope className="icon-element" />
                  <span></span>
                </div>
                <div className="profile">
                  <div
                    className="profile-item display-flex align-items-center"
                    onClick={() => setOption(!option)}
                    style={{ cursor: "pointer" }}
                  >
                    <div className="option">
                      <img
                        src={
                          !connectedUser?.userInfo?.thumbnails
                            ? process.env.PUBLIC_URL + "/user.png"
                            : `${process.env.REACT_APP_API_SERVER_URL}:${process.env.REACT_APP_API_SERVER_PORT}/${connectedUser?.userInfo?.thumbnails}`
                        }
                        alt="user-profile"
                        style={{ width: "100%", height: "100%" }}
                      />
                    </div>
                    <h3 className="title t-2">
                      {capitalize(connectedUser?.userInfo?.prename) +
                        " " +
                        capitalize(connectedUser?.userInfo?.name)}
                    </h3>
                    {option ? (
                      <BiChevronUp className="icon" />
                    ) : (
                      <BiChevronDown className="icon" />
                    )}
                  </div>
                  <div
                    className={option ? "profile-item display" : "profile-item"}
                  >
                    <Link to="" className="nav-link">
                      <FiUser className="icon" />
                      <span>Profile</span>
                    </Link>
                    <Link to="" className="nav-link">
                      <IoHelp className="icon" />
                      <span>Help</span>
                    </Link>
                    <div className="nav-link" onClick={signOut}>
                      <FiLogOut className="icon" />
                      <span>Logout</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div className="body">
              <Outlet />
            </div>
          </div>
        </div>
        {!connectedUser?.userInfo?.is_completed && (
          <Modal
            visibility={false}
            height="auto"
            maxHeight="97%"
            width="70%"
            title="Complete Initial Configuration"
            content={<CompleteRegister />}
          />
        )}
      </>
      {/* <Modal
        contentLabel="Complete configuration"
        isOpen={connectedUser.userInfo?.is_completed ? false : true}
        shouldCloseOnOverlayClick={false}
        style={{
          overlay: { backgroundColor: "rgba(0,0,0,0.75)", zIndex: 5 },
          content: {
            color: "inherit",
            width: "70%",
            height: "90%",
            margin: "auto",
            padding: 0,
          },
        }}
      >
        <div className="modal">
          <div className="modal-head display-flex justify-content-space-between align-items-center">
            <h3 className="title t-1">Complete your Registration</h3>
          </div>
          <div className="modal-body">
            <div className="config-head">
              <div
                className={
                  activeOption === 0 ? "config-tab active-tab" : "config-tab"
                }
              >
                <span>Personal Informations</span>
              </div>
              <div className="config-tab">
                <MdOutlineArrowForwardIos />
              </div>
              <div
                className={
                  activeOption === 1 ? "config-tab active-tab" : "config-tab"
                }
              >
                <span>Account activation</span>
              </div>
            </div>
            <div className="config-body">
              <form className="width" onSubmit={handleSubmit(onSubmit)}>
                {fragments[activeOption]}
                <div className="width">
                  {activeOption !== 1 ? (
                    <div className="col-l-6 col-s-11 m-auto">
                      {isSubmitting ? (
                        <div className="loader"></div>
                      ) : (
                        <button type="submit" className="button normal">
                          Validate
                        </button>
                      )}
                    </div>
                  ) : isSubmitting ? (
                    <div className="loader"></div>
                  ) : (
                    <div className="col-l-7 col-s-11 m-auto">
                      <button type="submit" className="button validate">
                        Confirm & Activate
                      </button>
                    </div>
                  )}
                </div>
              </form>
            </div>
          </div>
        </div>
      </Modal> */}
    </HelmetProvider>
  );
};

export default Administration;
