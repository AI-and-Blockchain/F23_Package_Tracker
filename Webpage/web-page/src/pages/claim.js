import React, { useState } from 'react';
import Navbar from "./navbar"
import axios from 'axios';

//Temporary way of making sure deliverer is valid
const ids = ['19047629']

//Controls the claim page
const ClaimPage = () => {
  return (
    <div>
      <Navbar/>
      <h1>Claim a Package</h1>
      <Input/>
      <h1>Mark a Package as delivered</h1>
      <Delivered/>
    </div>
  );
};

//window.location.reload()

//Sends data to the smart contract through the API, making sure the deliverer is valid
const Input = () => {
  const [name, setName] = useState("");
  const [id, setID] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault()
    if(name !== ""){
      if(ids.includes(id)){
        axios
        .get('http://127.0.0.1:8000/deliverer/' + name)
        alert("A package has been claimed!")
      } else {
        alert("Your id is invalid, the package cannot be claimed!")
      }
    } else{
      alert("Please enter your name")
    }
  }

  //A form that allows input and submits them through the API
  return (
    <>
    <form onSubmit={handleSubmit}>
      <label>
        Your Name:
        <input
        name="Deliverer"
        placeholder="Enter your name"
        onChange={e => setName(e.target.value)}
        />
      </label>
      <hr/>
      <label>
        Your ID:
        <input
        name="ID"
        placeholder="Enter your user ID"
        onChange={e => setID(e.target.value)}
        />
      </label>
      <hr/>
      <button type="submit">Claim a Package</button>
    </form>
    </>
  )
}

//The second form, which allows the package to be marked as delivered
const Delivered = () => {
  const [id, setID] = useState("");

  //If id is valid, mark the package as delivered
  const handleSubmit = (event) => {
    event.preventDefault()
    if(ids.includes(id)){
      axios
      .get('http://127.0.0.1:8000/delivered')
      alert("The package has been delivered")
    } else {
      alert("Your id is invalid, the package has not been marked as delivered")
    }
  }

  //Form that allows user to enter their ID
  return (
    <>
    <form onSubmit={handleSubmit}>
      <label>
        Your ID:
        <input
        name="ID"
        placeholder="Enter your user ID"
        onChange={e => setID(e.target.value)}
        />
      </label>
      <hr/>
      <button type="submit">Mark Package as Delivered</button>
    </form>
    </>
  )
}

export default ClaimPage;