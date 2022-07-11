import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./components/home";
import Login from "./components/login";
import Registration from "./components/registration";

function Entry() {
        
    return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />}>
          <Route index element={<Home />} />
          <Route path="signin" element={<Login />} />
          <Route path="registration" element={<Registration />} />
          {/* <Route path="*" element={<NoPage />} /> */}
        </Route>
      </Routes>
    </BrowserRouter>
    );
}

export default Entry;