import React, { useState, useEffect } from 'react';

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

  return (
    <>
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
    <button onCLick={acceptData(sender, recipient, start, end)}>Submit Data</button>
    </>
  )
}

function acceptData(sender, recipient, start, end) {
  alert("Your package has been added!")
   dataToView([sender, recipient, start, end])
}

export default AddPage;