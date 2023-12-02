import React, { useState, useEffect } from 'react';
import axios from 'axios';

const AddPage = () => {
  return (
    <div>
      <h1>Please enter all details below</h1>
      <Input/>
    </div>
  );
};

const Input = () => {
  const [sender, setSender] = useState("");
  const [recipient, setRecipient] = useState("");
  const [start, setStart] = useState("");
  const [end, setEnd] = useState("");

  const handleSubmit = (event) => {
    let begin = '?q='
    let string = begin.concat(sender, '&q=', recipient, '&q=', start, '&q=', end)
    axios
    .get('http://127.0.0.1:8000/details/' + string)
    alert("Your Package has been submitted!")
  }

  return (
    <>
    <form onSubmit={handleSubmit}>
      <label>
        Your Name:
        <input
        name="sender"
        placeholder="Enter your name"
        onChange={e => setSender(e.target.value)}
        />
      </label>
      <hr/>
      <label>
        Recipient's Name:
        <input
        name="recipient"
        placeholder="Enter the recipient's name"
        onChange={e => setRecipient(e.target.value)}
        />
      </label>
      <hr/>
      <label>
        Your Address:
        <input
        name="start"
        placeholder="Enter the starting Address"
        onChange={e => setStart(e.target.value)}
        />
      </label>
      <hr/>
      <label>
        Recipient's Address:
        <input
        name="end"
        placeholder="Enter the ending Address"
        onChange={e => setEnd(e.target.value)}
        />
      </label>
      <hr/>
      <input type="submit"/>
    </form>
    </>
  )
}

//<button onCLick={acceptData(sender, recipient, start, end)}>Submit Data</button>

export default AddPage;