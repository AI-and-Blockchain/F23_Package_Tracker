from eth_utils import address
from web3 import Web3
import os
import solcx
from solcx import compile_standard, install_solc
from dotenv import load_dotenv
import json
 

#print(solcx.get_installable_solc_versions())
install_solc('v0.8.0')
solcx.set_solc_version('v0.8.0')
with open("./PackageTrackerRoot.sol", "r") as file:
    PackageTracker = file.read()

# set up connection
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chain_id = 1337
my_address = "0x22d9529aa7b67b2738d4B082Bf4074758D04b0ff"
#private_key = os.getenv("PRIVATE_KEY")
private_key = "0xafb98d224dcc7768934bee92d8b6c330b06ff88a5e12b9cfb629bc30323b6547"

file_path = "."
name = "PackageTrackerRoot.sol"
input = {
    'language': 'Solidity',
    'sources': {
        name: {'urls': [file_path + "/" + name]}},
    'settings': {
        'outputSelection': {
            '*': {
                '*': ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"],
            },
            'def': {name: ["abi", "evm.bytecode.opcodes"]},
        }
    }
}


output = compile_standard(input, allow_paths=file_path, solc_version='0.8.0')
contracts = output["contracts"]

with open('compiled_code.json', "w") as file:
    json.dump(output, file)

bytecode = contracts["PackageTrackerRoot.sol"]["PackageTrackerRoot"]["evm"]["bytecode"]["object"]

#abi = json.loads(contracts["PackageTrackerRoot.sol"]["PackageTrackerRoot"]["metadata"])["output"]["abi"]
abi = contracts["PackageTrackerRoot.sol"]["PackageTrackerRoot"]["abi"]

# initialize contract
PackageTracker = w3.eth.contract(abi=abi, bytecode=bytecode)
nonce = w3.eth.get_transaction_count(my_address)
# set up transaction from constructor which executes when firstly
transaction = PackageTracker.constructor().buildTransaction(
    {"gasPrice": w3.eth.gas_price, "chainId": chain_id, "from": my_address, "nonce": nonce}
)

transaction = PackageTracker.constructor().transact({})
signed_tx = w3.eth.account.signTransaction(transaction, private_key=private_key)
tx_hash = w3.eth.account.send_raw_transaction(signed_tx.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)