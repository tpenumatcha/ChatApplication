import React from "react";
import { useState, useEffect } from "react";
import { useHistory } from 'react-router-dom'
import axios from 'axios'
import './Home.css'
import Chat from "../Chat/Chat";



function Home() {
    const [name, setName] = useState(null)
    const [group, setGroup] = useState(null)
    let history = useHistory()

    const submit = () => {
        setName(document.getElementById('username').value)
        setGroup(document.getElementById('group').value)
        sessionStorage.setItem("user", name)
        sessionStorage.setItem("group", group)
        
        console.log('states set')
        
        
    }


    const sendInfo = async () => {
        const user = {
            'username': name,
            'group_id': group
        }
        console.log(user)

        const config = {
            'Content-Type': 'application/json'
        }
        console.log('awaiting')
        const res = await axios.post('http://localhost:5000/add', {user}, config)
        console.log(res)
        console.log(user)
        Chat.defaultProps = user
        if (res['data'] === 200) {
            history.push(`/${group}`)
        } 
    }

    useEffect( () => {
        if (name && group){
            console.log('useeffect running')
            sendInfo()
        }
        
        
       
    })
    

    if (!name && !group){
        return (
            <div className="Home">
                 <form className="form">
                    <label for="username">Enter Username:</label>
                    <input id="username" type="text"/>
                    <label for="group">Enter Group Name:</label>
                    <input id="group" type="text"/>
                    <button type="button" onClick={submit}>Join</button>
                </form>
            </div>
        )
    }
    else {
        return (
            <div className="form">
                <h1>Logging in</h1>
            </div>
        )
    }
    
    
}

export default Home;



