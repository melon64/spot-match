import { useState } from 'react';
import person from './imgs/person.jpg';

const Match = () => {
    const [match, setmatch] = useState([
        { name: "Jane Doe", age: 21, gender:"Female", image: <img src={person} />, id:1},
        { name: "Mary Jane", age: 22, gender: "Female", image: <img src={person} />, id:2}
    ]);

    return (
        <div className="match-container">
            {match.map((match) => (
            <div className="match" key={match.id}>
                {match.image}
                <h2 className="personal-details">{match.name}</h2>
                <p className="personal-details">Age: {match.age}</p>
                <p className="personal-details">Gender: {match.gender}</p>
            </div>
        ))}
        </div>
    );
}
 
export default Match;