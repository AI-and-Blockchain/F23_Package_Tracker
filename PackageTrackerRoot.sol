// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PackageTrackerRoot {
    // Define a struct
    struct Parcel {
        string sender;
        string recipient;
        string deliverer;
        string status;
        string startAddress;
        string endAddress;
    }

    // Declare a state variable of the struct type
    Parcel public MyParcel;

    // Constructor to create the parcel 
    constructor(string memory _sender, string memory _recipient, string memory _status) {
        MyParcel.sender = _sender;
        MyParcel.recipient = _recipient;
        MyParcel.status = _status;
    }

    function initialPackage(string memory _sender, string memory _recipient, string memory start, string memory end) public returns (Parcel memory){
        MyParcel.sender = _sender;
        MyParcel.recipient = _recipient;
        MyParcel.startAddress = start;
        MyParcel.endAddress = end;
        return MyParcel;
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

    function returnPackageDetails() public returns (string memory, string memory, string memory, string memory){
        return (MyParcel.sender, MyParcel.recipient, MyParcel.startAddress, MyParcel.endAddress);
    }

    function displayStatus() public view returns (string memory) {
        return MyParcel.status;
    }
}