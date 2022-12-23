import React from "react";
import {Outlet} from "react-router-dom";
import Navbar1 from "./Navbar";

const Layout = () => {
  return (
    <>
      <Navbar1 />
      <Outlet />
    </>
  );
};

export default Layout;