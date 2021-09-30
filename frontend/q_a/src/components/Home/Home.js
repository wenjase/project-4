import { useState } from "react";
import React from 'react';

function Home(props) {

   const [question, setQuestion] = useState("")
    const handleSubmit = (e) => {
        e.preventDefault()
        try{
        fetch("http://localhost:8001/questions/", {
  "headers": {
    "content-type": "application/json",
  },
  "body": JSON.stringify({question:question, "csrfmiddlewaretoken": "mTqdPljNmlWUekEY3VQPgGuMyHtxYs0FavJmT5hhbB2APAQukPmmhQqj8OQhUdAy"}),
  "method": "POST",
//   "mode": "cors",
//   "credentials": "include"
});

} catch {
    console.log("err")
}
    }
const handleChange = (e) => {
    console.log(e.target.value)
    setQuestion(e.target.value)
}
    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input name='question' type='text' onChange={handleChange}/>
                <input type='submit' />
            </form>
        </div>
    );
}

export default Home;