import React from "react";
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom'
import Home from "./Home/Home";
import Chat from "./Chat/Chat";


function App() {
    return(
        <Router>
            <Switch>
                <Route path="/" exact component={Home}/>
                <Route path="/:id" exact component={Chat}/>
            </Switch>
        </Router>
        
    )
}

export default App

