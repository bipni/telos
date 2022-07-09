import React from "react";
import Login from "./login";
import Registration from "./registration";


class Home extends React.Component {

    render() {
        return (
            <div>
                <Login />
                {/* <Registration /> */}
            </div>
        );
    }
}

export default Home;