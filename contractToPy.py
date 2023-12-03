from solcx import compile_standard, install_solc
from web3 import Web3
import json 
from contextlib import asynccontextmanager
from typing import Annotated

import uvicorn
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

#Compiles solidity code in python so that it can be interacted with, then create API
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
address = "0x36a5526981F69E104553bbEbF6e3072AF9052D2F"
private_key = "0x016ddaad616481081959bef005937272eb58c67830b258075b23df07061a33ee" # leaving the private key like this is very insecure if you are working on real world project 
nonce = w3.eth.get_transaction_count(address)
transaction_receipt = None
abi = None


with open("PackageTrackerRoot.sol", "r") as file:
    package_tracker_file = file.read()

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"PackageTrackerRoot.sol": {"content": package_tracker_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"] # output needed to interact with and deploy contract 
                }
            }
        },
    },
    solc_version="0.8.0",
)
#print(compiled_sol)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["PackageTrackerRoot.sol"]["PackageTrackerRoot"]["evm"]["bytecode"]["object"]
# get abi
abi = json.loads(compiled_sol["contracts"]["PackageTrackerRoot.sol"]["PackageTrackerRoot"]["metadata"])["output"]["abi"]

# For connecting to ganache
    #w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
    #chain_id = 1337
    #address = "0x36a5526981F69E104553bbEbF6e3072AF9052D2F"
    #private_key = "0x016ddaad616481081959bef005937272eb58c67830b258075b23df07061a33ee" # leaving the private key like this is very insecure if you are working on real world project
# Create the contract in Python
PackageTrackerRoot = w3.eth.contract(abi=abi, bytecode=bytecode)
# Get the number of latest transaction
nonce = w3.eth.get_transaction_count(address)

# build transaction
transaction = PackageTrackerRoot.constructor().build_transaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": address,
        "nonce": nonce,
    }
)
# Sign the transaction
sign_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
print("Deploying Contract!")
# Send the transaction
transaction_hash = w3.eth.send_raw_transaction(sign_transaction.rawTransaction)
# Wait for the transaction to be mined, and get the transaction receipt
print("Waiting for transaction to finish...")
transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
print(f"Done! Contract deployed to {transaction_receipt.contractAddress}")

    ##Update status of package
    #package_tracker_root = w3.eth.contract(address=transaction_receipt.contractAddress, abi=abi)
    #update_status = package_tracker_root.functions.updateStatus("lost").build_transaction({
    #    "chainId": chain_id, "from": address, "gasPrice": w3.eth.gas_price, "nonce": nonce + 1
    #})
    ##Sign the transaction
    #sign_update = w3.eth.account.sign_transaction(
    #    update_status, private_key = private_key
    #)
    ##Send the transaction
    #send_start = w3.eth.send_raw_transaction(sign_update.rawTransaction)
    #w3.eth.wait_for_transaction_receipt(send_start)

#Call displayStatus function to test update
#print("package status: " + package_tracker_root.functions.displayStatus().call())

#Create API
app = FastAPI()

origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



#Change this to put
#Update Status of package
@app.get("/status/{status}")
def updateStatus(status: str):
    global nonce
    nonce += 1
    #Update status of package
    package_tracker_root = w3.eth.contract(address=transaction_receipt.contractAddress, abi=abi)
    update_status = package_tracker_root.functions.updateStatus(status).build_transaction({
    "chainId": chain_id, "from": address, "gasPrice": w3.eth.gas_price, "nonce": nonce 
    })
    #Sign the transaction
    sign_update = w3.eth.account.sign_transaction(
        update_status, private_key = private_key
    )
    #Send the transaction
    send_start = w3.eth.send_raw_transaction(sign_update.rawTransaction)
    w3.eth.wait_for_transaction_receipt(send_start)
    #return { "Package was successfully updated" if (previous_status != new_status) else "Package was not updated"}  
    return "Package was successfully updated"

#Deprecated function
#Get status of package
#@app.get("/status")
#def getDetails():
#    package_tracker_root = w3.eth.contract(address=transaction_receipt.contractAddress, abi=abi)
#    return {package_tracker_root.functions.displayStatus().call()}


#Change to post
#Update package to have a driver
@app.get("/deliverer/{driver}")
def updateDriver(driver: str):
    global nonce
    nonce += 1
    #Update package to have deliverer
    package_tracker_root = w3.eth.contract(address=transaction_receipt.contractAddress, abi=abi)
    update_driver = package_tracker_root.functions.updateDeliverer(driver).build_transaction({
        "chainId": chain_id, "from": address, "gasPrice": w3.eth.gas_price, "nonce": nonce
    })
    #Sign the transaction
    sign_update = w3.eth.account.sign_transaction(
        update_driver, private_key = private_key
    )
    #Send the transaction
    send_start = w3.eth.send_raw_transaction(sign_update.rawTransaction)
    w3.eth.wait_for_transaction_receipt(send_start)
    return {package_tracker_root.functions.displayStatus().call()}

#@app.get("/details/")
#async def updatePackage(q: Annotated[list[str] | None, Query()] = None):
#    global nonce
#    nonce += 1
#    #Add details to package
#    query = {"q" : q}['q']
#    sender = query[0]
#    recipient = q[1]
#    start = q[2]
#    end = q[3]
#    package_tracker_root = w3.eth.contract(address=transaction_receipt.contractAddress, abi=abi)
#    updatePackage = package_tracker_root.functions.initialPackage(sender, recipient, start, end).build_transaction({
#        "chainId": chain_id, "from": address, "gasPrice": w3.eth.gas_price, "nonce": nonce
#    })
#    #Sign the transaction
#    sign_update = w3.eth.account.sign_transaction(
#        updatePackage, private_key = private_key
#    )
#    #Send the transaction
#    send_start = w3.eth.send_raw_transaction(sign_update.rawTransaction)
#    w3.eth.wait_for_transaction_receipt(send_start)
#    return query

@app.get("/details/")
async def addPackage(q: Annotated[list[str] | None, Query()] = None):
    global nonce
    nonce += 1
    #Add details to package 
    query = {"q": q}['q']
    sender = query[0]
    recipient = query[1]
    start = query[2]
    end = query[3]
    package_tracker_root = w3.eth.contract(address=transaction_receipt.contractAddress, abi=abi)
    initialPackage = package_tracker_root.functions.createOrder(sender, recipient, "Package created", start, end).build_transaction({
        "chainId": chain_id, "from": address, "gasPrice": w3.eth.gas_price, "nonce": nonce
    })
    #Sign the transaction
    sign_update = w3.eth.account.sign_transaction(
        initialPackage, private_key=private_key
    )
    #Send the transaction
    send_start =  w3.eth.send_raw_transaction(sign_update.rawTransaction)
    w3.eth.wait_for_transaction_receipt(send_start)
    return query


@app.get("/package_details")
async def getPackage():
    package_tracker_root = w3.eth.contract(address=transaction_receipt.contractAddress, abi=abi)
    all_details = package_tracker_root.functions.returnPackageDetails().call()
    return(all_details)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5049)