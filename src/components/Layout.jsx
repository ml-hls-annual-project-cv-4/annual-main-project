import React from "react";
import {Outlet} from "react-router-dom";
import Navbar1 from "./Navbar";

const Layout = () => {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen overflow-hidden bg-gradient-to-b from-gray-700 via-sky-400 to-white">
      <Navbar1 />
      <div className="flex-grow overflow-auto">
        <Outlet />
      </div>
    </div>
  );
};

export default Layout;