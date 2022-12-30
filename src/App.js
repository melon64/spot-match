import Navbar from './Navbar';
import Home from './Home';
import Match from './Match';
import Profile from './Profile';
import SignIn from './SigninForm';
import { useState } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <div className="content">
          <Switch>
            <Route exact path="/">
              <Home />
            </Route>
            <Route exact path="/Match">
              <Match />
            </Route>
            <Route exact path="/Profile">
              <Profile />
            </Route>
            <Route exact path="/SignIn">
              <SignIn />
            </Route>
          </Switch>
        </div>
      </div>
    </Router>
  );
}

export default App;
