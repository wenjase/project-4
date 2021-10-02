import React, { useState } from 'react';


function Login(props) {
    const [user, setUser] = useState({username: "", password: ""})

    const handleChange = (e) => {
        const {id, value} = e.target
        setUser(prevUser => ({
            ...prevUser,
            [id] : value
        }))
    }



    return (
        <div className="card col-12 col-lg-4 login-card mt-2 hv-center">
            <input type="username"
            className="login-control"
            id='username'
            placeholder="enter username"
            value={user.username}
            onChange={handleChange}
            />
            <input type="password"
            className="password"
            id="password"
            placeholder="enter password"
            value={user.password}
            onChange={handleChange}
            />
        </div>
    );
}

export default Login;