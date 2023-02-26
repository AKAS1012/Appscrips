import React, { useEffect, useState } from 'react'
import axios from 'axios';

function GetCricketer() {
    const [getData, setGetdata] = useState([])
    
    useEffect(() => {
        axios.get("/name/")
            .then((Response) => {
                setGetdata(Response.data)
            })
            .catch((err) => {
                console.log(err)
            })
    }, [])


    return (
        <>
            {
                getData.map((item) => (
                    <div key={item.id}>
                        <h1>{item.name}</h1>
                    </div>
                ))
            }
        </>
    )
}

export default GetCricketer;