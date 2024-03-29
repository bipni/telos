import React from "react";
import { Outlet, Link } from "react-router-dom";


function Home () {

    return (
        <>
            <nav>
                <ul>
                <li>
                    <Link to="/">Home</Link>
                </li>
                <li>
                    <Link to="/signin">Sign In</Link>
                </li>
                <li>
                    <Link to="/registration">Registration</Link>
                </li>
                </ul>
            </nav>

            <Outlet />
        </>
    );
}

export default Home;