import React, { useState } from 'react';
import {Button , Form} from 'react-bootstrap';
import axios from 'axios';

const Cricker =()=> {
    const [CricketerName, setCricketerName] = useState()
    
    const changeHandler = (event) =>{
        CricketerName[event.target.name]=event.target.value;
        setCricketerName({...CricketerName})
    }
    
    const submitHandler = (event) =>{
        debugger
        axios.post('/name/',{
            name:CricketerName
        } )
        .then((Response)=>{
            setCricketerName(Response.data)
        })
        .catch((err)=>{
            console.log(err)
        })
    }

  return (
    <>
    <Form>
      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Cricketer name</Form.Label>
        <Form.Control
         type="text" 
         placeholder=""
         name = "CricketerName"
         value={CricketerName}
         onChange={(event)=>{changeHandler(event)}}
         />
        <Form.Text className="text-muted">
          We'll never share your email with anyone else.
        </Form.Text>
      </Form.Group>
      <Button variant="primary" type="submit"
      onClick={submitHandler}
      >
        Submit
      </Button>
    </Form>
    </>
  )
}

export default Cricker