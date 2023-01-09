import { useState } from "react";

const SignIn = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    return ( 
        <div className="signin-form">
            <form className="form-container">
                <h2>Login</h2>

                <label htmlFor="email"><b>Email</b></label>
                <input htmltype="text" htmlplaceholder="Enter Email" htmlname="email" required value={email} onChange={(e) => setEmail(e.target.value)}/>

                <label htmlFor="psw"><b>Password</b></label>
                <input htmltype="password" htmlplaceholder="Enter Password" htmlname="psw" required value={password} onChange={(e) => setPassword(e.target.value)}/>

                <button htmltype="submit" className="btn">Login</button>
            </form>
        </div>
    );
}
 
export default SignIn;