import React from "react";
import './Message.css'


function Message(props){
    return (
        <div className="Message">
            
            {props.info.content}
        </div>
    )
}

export default Message;