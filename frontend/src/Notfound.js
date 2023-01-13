import { Link } from "react-router-dom";

const Notfound = () => {
    return (
        <div className="notfound">
            <h2>Sorry</h2>
            <p>That page cannot be found</p>
            <Link to="/Home">Back to the Homepage...</Link>
        </div>
    );
}
 
export default Notfound;