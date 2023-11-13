from web3 import Web3
import solcx
from solcx import compile_source

# Solidity source code
solcx.install_solc('v0.8.0')
solcx.set_solc_version('v0.8.0')
compiled_sol = compile_source(
    '''
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
}
    ''',
    output_values=['abi', 'bin']
)

# retrieve the contract interface
contract_id, contract_interface = compiled_sol.popitem()

# get bytecode / bin
bytecode = contract_interface['bin']

# get abi
abi = contract_interface['abi']

# web3.py instance
w3 = Web3(Web3.EthereumTesterProvider())

# set pre-funded account as sender
w3.eth.default_account = w3.eth.accounts[0]

Greeter = w3.eth.contract(abi=abi, bytecode=bytecode)

# Submit the transaction that deploys the contract
tx_hash = Greeter.constructor().transact()

# Wait for the transaction to be mined, and get the transaction receipt
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

greeter = w3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi
)

greeter.functions.greet().call()


tx_hash = greeter.functions.setGreeting('Nihao').transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
greeter.functions.greet().call()
