import SignIn from "./SigninForm";
import { Link } from "react-router-dom"; 
const Navbar = () => {
    return (
        <nav className="navbar">
            <a href="/Home" className="h1">InSync</a>
            <div className="links">
                <Link className="link" to="/Home">Home</Link>
                <Link className="link" to="/Match">Match</Link>
                <Link className="link" to="/Profile">Profile</Link>
                <Link className="link" to="/SignIn">Sign In</Link>
            </div>
        </nav>
    );
}
 
export default Navbar;