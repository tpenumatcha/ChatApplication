import React from "react";
import { useState, useEffect } from "react";
import { withRouter } from "react-router-dom";
import './Chat.css'
import Message from "../Message/Message";
import axios from "axios";



function Chat(props){
    const [messages, setMessages] = useState(null)


    const handleSubmit = () => {
        console.log(document.getElementById('message').value)
        const res = sendMessage(document.getElementById('message').value)
        console.log(res)
        if (res === 200){
            getMessages()
        }
        document.getElementById('message').value = ""
    }

    const sendMessage = async () => {
        console.log(document.getElementById('message').value)
        const message = {
            'user': sessionStorage.getItem('name'),
            'group': sessionStorage.getItem('group'),
            'message': document.getElementById('message').value
        }
        console.log(message)
        const config = {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Methods': "POST, GET, OPTIONS, DELETE, PUT",
            'Access-Control-Allow-Origin': "*",
            'Access-Control-Allow-Headers': "Origin, X-Requested-With, Content-Type, Accept, X-API-KEY, Authorization",
            'Access-Control-Allow-Credentials': true
        }
        console.log('sending message')
        const res = await axios.post(`http://localhost:5000/send`, {message}, config)
        console.log('send message' + res)
        //getMessages()
    }


    const getMessages = async () => {
        const res = await axios.get(`http://localhost:5000/get_messages/${sessionStorage.getItem('group')}`);
        console.log(res)
        setMessages(res['data']['messages'])
        console.log(messages)
    }

    useEffect(() => {
        console.log('running useeffect')

        console.log(props.username)
        if (props.username && props.group_id){
            sessionStorage.setItem('name', props.username)
            sessionStorage.setItem('group', props.group_id)
        }
        
        console.log(messages)
        if (sessionStorage.getItem('name')) {
            getMessages();
        }
        
        const interval = setInterval(() => {
            getMessages()
        }, 3000);
        return () => clearInterval(interval);
        
    }, []);



    if (messages && Array.isArray(messages)){
        console.log('rendering')
        return (
            <div className="Chatbox">
                
                
                {console.log(messages)}
                {messages.map(message =>{
                    return (
                        <Message key={sessionStorage.getItem('name')} info={{username: sessionStorage.getItem('name'), content: message}}/>
                    )
                        
                })}
                
                <form className="submit-form">
                    <input id="message" type="text"/>
                    <button type="button" onClick={handleSubmit}>Send</button>
                </form>

            </div>
        )
    }
    else{
        return (
            <div className="Chatbox">
                <h1>Loading Messages</h1>
            </div>
        )
    }

    
}

       

export default withRouter(Chat);