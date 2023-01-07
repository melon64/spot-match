import { Link, useParams } from "react-router-dom";
import useFetch from "./useFetch";
const Match_profile = () => {
    const { username, id } = useParams();
    const { data, isLoading, error } = useFetch('http://localhost:8000/matches/' + id);
    return (
        <div className="match_profile">
            {isLoading && <div>Loading...</div>}
            {error && <div>{error}</div>}
            {data && 
            <div className="details">
                <h2>Match Profile for {username}</h2>
                <div className="profile-container">
                    <div className="match-profile-details">
                        <h2>Personal Details:</h2>
                        <p>Name: {data.name}</p>
                        <p>Age: {data.age}</p>
                        <p>Gender: {data.gender}</p>
                    </div>
                    <div className="profile-image-container">
                        <h2>Spotify User:</h2>
                        <img src={data.image} alt="person"/>
                    </div>
                </div>
            </div>}
        </div>
    );
}
 
export default Match_profile;