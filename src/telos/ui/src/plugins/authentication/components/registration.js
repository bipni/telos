import React, {useState} from "react";

import '../styles/Login.css';


function Registration() {

    const [isSubmitted, setIsSubmitted] = useState(false);

    const renderForm = (
        <div className="login-form">
            <form>
                <div className="input-container">
                    <label>Name </label>
                    <input type="text" name="name" required />
                </div>

                <div className="input-container">
                    <label>Email </label>
                    <input type="text" name="email" required />
                </div>

                <div className="input-container">
                    <label>Username </label>
                    <input type="text" name="uname" required />
                </div>

                <div className="input-container">
                    <label>Passsword </label>
                    <input type="password" name="pass" required />
                </div>

                <div className="input-container">
                    <label>Re-enter Passsword </label>
                    <input type="password" name="repass" required />
                </div>

                <div className="button-container">
                    <input type="submit" />
                </div>
            </form>
        </div>
    );

    return (
        <div className="app">
            <div className="login-form">
                <div className="title">Registration</div>
                {isSubmitted ? <div>Registration is successfull.</div> : renderForm}
            </div>
        </div>
    );
}

export default Registration;