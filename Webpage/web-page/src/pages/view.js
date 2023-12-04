import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Navbar from "./navbar";



function GetETA(start, end) {
  // if (start === "None" || end === "None") {
  //   return "None";
  // }
  console.log("Entered ETA");

  // fetch("http://127.0.0.1:8000/process", {
  //   method: "POST",
  //   mode: "no-cors",
  //   headers: {
  //     "Accept": "application/json",
  //     "Content-Type": "application/json; charset=utf-8",
  //   },
  //   body: JSON.stringify({
  //     name: "start",
  //     email: "end"
  //   }),
  // })
  // .then(response => response.json())
  // .then(data => {
  //   console.log(data);
  // })
  // .catch(error => {
  //   console.error("Error:", error);
  // });

  const [eta, setETA] = useState("None");

  fetch("http://127.0.0.1:8000/process")
    .then(response => response.text())
    .then(data => {
      console.log(data);
      setETA(data);
    })
    .catch(error => {
      console.log("FAILED");
      console.error("Error:",error);
    });
  
  return eta;
  
}

const ViewPage = () => {
  const [sender, setSender] = useState("None");
  const [recipient, setRecipient] = useState("None");
  const [startAddress, setStart] = useState("None");
  const [endAddress, setEnd] = useState("None");
  const [deliverer, setDeliverer] = useState("None");
  const [status, setStatus] = useState("None");

  
  axios
   .get('http://127.0.0.1:8000/package_details')
   .then((result) => {
    setSender(result.data[0])
    setRecipient(result.data[1])
    setStart(result.data[2])
    setEnd(result.data[3])
    setDeliverer(result.data[4])
    setStatus(result.data[5])
    })
    .catch(error => {
      console.error("Error:", error);
    })
  
  
  return (
    <div>
      <Navbar/>
      <h1>Package Details</h1>
      <hr/>
      {"Sender: " + sender}
      <hr/>
      {"Recipient: " + recipient}
      <hr/>
      {"Starting Address: " + startAddress}
      <hr/>
      {"Destination Address: " + endAddress}
      <hr/>
      {"Deliverer: " + deliverer}
      <hr/>
      {"Status: " + status}
      <hr/>
      {"ETA: " + GetETA("1", "2")}
      <hr/>
    </div>
  );
};

/*
const returnData = () => {
  axios
   .get('http://127.0.0.1:8000/package_details')
   .then((result) => {
    sender = result.data[0]
    recipient = result.data[1]
    startAddress = result.data[2]
    endAddress = result.data[3]
    deliverer = result.data[4]
    status = result.data[5]
   })
}*/

export default ViewPage;