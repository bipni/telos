import React from "react";

import '../css/button.css'

class Button1 extends React.Component {
    
    render() {
        return (
            <div>
                <input type="button" className="button1" value={this.props.name}></input>
            </div>
        );
    }
}

export default Button1;