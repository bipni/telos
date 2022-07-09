import React from "react";

import Button1 from "../../../commons/components/button1";

import '../css/Login.css';


class Login extends React.Component {

    render() {
        return (
            <div>
                <div className="base">
                    <h1 className="logo">Authentication</h1>
                    <div className="login">
                        <label className="label" for="email">Email:</label>
                        <input className="label" type="text" name="email"></input>
                        <label className="label" for="password">Password:</label>
                        <input className="label" type="password" name="password"></input>
                    </div>
                    <div className="btn"><Button1 name="Login"/></div>
                </div>
            </div>
        );
    }
}

export default Login;