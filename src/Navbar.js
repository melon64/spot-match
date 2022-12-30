import SignIn from "./SigninForm";

const Navbar = () => {
    return (
        <nav className="navbar">
            <a href="/" className="h1">InSync</a>
            <div className="links">
                <a className="link" href="/">Home</a>
                <a className="link" href="/Match">Match</a>
                <a className="link" href="/Profile">Profile</a>
                <a className="link" href="/SignIn">Sign In</a>
            </div>
        </nav>
    );
}
 
export default Navbar;