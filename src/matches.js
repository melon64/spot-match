import { Link } from "react-router-dom";

const Matches = ({matches}) => {
    return (
        <div className="match-container">
            {matches.map((matches) => (
            <div className="match" key={matches.id}>
                <div className="match-pfp">
                    <img src={matches.image} alt={matches.id} />
                </div>
                <h2 className="personal-details">{matches.name}</h2>
                <p className="personal-details">Age: {matches.age}</p>
                <p className="personal-details">Gender: {matches.gender}</p>
                <Link className="personal-details" to = {`/Match_profile/${matches.username}/${matches.id}`}> View Profile </Link>
            </div>
        ))}
        </div>
    );
}
 
export default Matches;