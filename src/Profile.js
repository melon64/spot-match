import person from './imgs/person3.jpg';
import { useState } from 'react';
import { useHistory } from 'react-router-dom';
const Profile = () => {
    const [name, setName] = useState("");
    const [age, setAge] = useState("");
    const [gender, setGender] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const hist = useHistory();

    const handleSubmit = (e) => {
        e.preventDefault();
        const profile = {name, age, gender};
        
        setIsLoading(true);

        fetch("http://localhost:8000/profile", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(profile)
        }).then(() => {
            console.log("New profile added")
            setIsLoading(false);
            // hist.go(-1)
            hist.push('/Home')
        })
    }

    return ( 
        <div className="profile">
            <h1 className="title">My Profile</h1>
            <div className="profile-container">
                <form className="profile-form-container" onSubmit={handleSubmit}>
                    <label htmlFor="name" color="black">Name</label>
                    <input type="text" name="name" required value={name} onChange={(e) => setName(e.target.value)}/>
            
                    <label htmlFor="age" color="black">Age</label>
                    <input type="text" name="age" required value={age} onChange={(e) => setAge(e.target.value)}/>

                    <p color="black">Gender</p>
                
                    <label htmlFor="gender" color="black">Male</label>
                    <input type="radio" name="gender" value="Male" onClick={(e) => setGender(e.target.value)}/>

                    <label htmlFor="gender" color="black">Female</label>
                    <input type="radio" name="gender" value="Female" onClick={(e) => setGender(e.target.value)}/>

                    {!isLoading && <button className="btn">Save</button>}
                    {isLoading && <button disabled className="btn">Saving Changes...</button>}
                </form>

                <div className="profile-image-container">
                    <h2>Spotify User:</h2>
                    <img src={person} alt="person"/>
                </div>
            </div>
        </div>
    );
}
 
export default Profile;