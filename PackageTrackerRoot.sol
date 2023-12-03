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
        bool claimed;
        //to be done:
        /*
            add address(delivery) and verify that the delivery address coincides with
            the final address of the final scan

            possibly take in wallet addresses of deliverer and recipient for secuirty
        */
    }

    //logs that the order has been initiated/created
    event OrderCreated(
        string indexed _sender, 
        string indexed _recipient, 
        string indexed _status);

    event UpdateDelivererInfo(string indexed deliverer);

    //emitted when the contract is first claimed
    event Claimed(bool _claimed);

    // Declare a state variable of the struct type
    Parcel public MyParcel;

    function createOrder(string memory _sender, string memory _recipient, string memory _status, string memory _startAddress, string memory _endAddress) 
    public {
        // Constructor to create the parcel 
        MyParcel = Parcel({
            sender: _sender,
            recipient: _recipient,
            deliverer: "",
            status: _status,
            claimed: true,
            startAddress: _startAddress,
            endAddress: _endAddress
        });
        //This is where we first scan the parcel and create the order
        emit OrderCreated(_sender, _recipient, _status);
        emit Claimed(true);
    }
    

    // Function to update the struct with the deliverer and subsequently update the status
    function updateDeliverer(string memory _deliverer) public returns (Parcel memory) {
        MyParcel.deliverer = _deliverer;
        updateStatus("Deliverer Found");
        //Second scan complete and deliverer has been found and updated
        emit UpdateDelivererInfo(_deliverer);
        return MyParcel;
    }

    //Function to update status of the parcel
    function updateStatus(string memory _status) public returns (Parcel memory) {
        MyParcel.status = _status;
        return MyParcel;
    }

    //Function to return all details of package
    function returnPackageDetails() public returns (string memory, string memory, string memory, string memory, string memory, string memory){
        return (MyParcel.sender, MyParcel.recipient, MyParcel.startAddress, MyParcel.endAddress, MyParcel.deliverer, MyParcel.status);
    }


    //function to be launched on termination of the order
    function endOrder() public returns (Parcel memory) {
        MyParcel.status = "Delivered";
        return MyParcel;
    }

    function claimed() public view returns (bool) {
        return MyParcel.claimed;
    }
}