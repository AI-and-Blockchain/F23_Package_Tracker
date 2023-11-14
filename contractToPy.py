from solcx import compile_standard, install_solc
from web3 import Web3
import json 

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
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
address = "0xBd77397c684DA2b81AE8861f87c18089f7b5764D"
private_key = "0x58d9f9d0c52b0b16b7b0fd761db24d0005d724b32c89551d3b76bbf94a8b6835" # leaving the private key like this is very insecure if you are working on real world project
# Create the contract in Python
PackageTrackerRoot = w3.eth.contract(abi=abi, bytecode=bytecode)
# Get the number of latest transaction
nonce = w3.eth.get_transaction_count(address)

# build transaction
transaction = PackageTrackerRoot.constructor("test1", "test2", "delivered").build_transaction(
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

package_tracker_root = w3.eth.contract(address=transaction_receipt.contractAddress, abi=abi)
update_status = package_tracker_root.functions.updateStatus("lost").build_transaction({
    "chainId": chain_id, "from": address, "gasPrice": w3.eth.gas_price, "nonce": nonce + 1
})

sign_update = w3.eth.account.sign_transaction(
    update_status, private_key = private_key
)
send_start = w3.eth.send_raw_transaction(sign_update.rawTransaction)
w3.eth.wait_for_transaction_receipt(send_start)

print("package status: " + package_tracker_root.functions.displayStatus().call())