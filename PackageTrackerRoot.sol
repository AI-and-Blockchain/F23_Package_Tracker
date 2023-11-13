// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PackageTrackerRoot {
    // Define a struct
    struct Parcel {
        string sender;
        string recipiant;
        string deliverer;
        string status;
    }

    // Declare a state variable of the struct type
    Parcel public MyParcel;

    // Constructor to create the parcel 
    constructor(string memory _sender, string memory _recipiant, string memory _status) {
        MyParcel.sender = _sender;
        MyParcel.recipiant = _recipiant;
        MyParcel.status = _status;
    }

    // Function to update the struct with the deliverer and subsequently update the status
    function updateDeliverer(string memory _deliverer) public returns (Parcel memory) {
        MyParcel.deliverer = _deliverer;
        updateStatus("Deliverer Found");
        return MyParcel;
    }

    //Function to update status of the parcel
    function updateStatus(string memory _status) public returns (Parcel memory) {
        MyParcel.status = _status;
        return MyParcel;
    }

    function displayStatus() public view returns (string memory) {
        return MyParcel.status;
    }
}