const SignIn = () => {
    return ( 
        <div className="signin-form">
            <form action="" className="form-container">
                <h2>Login</h2>

                <label htmlFor="email"><b>Email</b></label>
                <input htmltype="text" htmlplaceholder="Enter Email" htmlname="email" required/>

                <label htmlFor="psw"><b>Password</b></label>
                <input htmltype="password" htmlplaceholder="Enter Password" htmlname="psw" required/>

                <button htmltype="submit" className="btn">Login</button>
            </form>
        </div>
    );
}
 
export default SignIn;