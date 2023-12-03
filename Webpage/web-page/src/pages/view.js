import React, { useState, useEffect } from 'react';
import add from './add'
import axios from 'axios';


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
  
  
  return (
    <div>
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