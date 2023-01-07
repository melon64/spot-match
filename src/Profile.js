import person from './imgs/person3.jpg';

const Profile = () => {
    return ( 
        <div className="profile">
            <h1 className="title">My Profile</h1>
            <div className="profile-container">
                <form action="" className="profile-form-container">
                    <label htmlFor="name" color="black">Name</label>
                    <input type="text" name="name"/>
            
                    <label htmlFor="age" color="black">Age</label>
                    <input type="text" name="age"/>

                    <p color="black">Gender</p>
                
                    <label htmlFor="gender" color="black">Male</label>
                    <input type="radio" name="gender"/>

                    <label htmlFor="gender" color="black">Female</label>
                    <input type="radio" name="gender"/>
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