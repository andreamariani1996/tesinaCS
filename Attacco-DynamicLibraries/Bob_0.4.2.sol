pragma solidity ^0.4.2;

// Set interface
library Set {
  
    struct Data { mapping(uint => bool) flags; }

    function insert(Data storage self, uint value) returns (bool);
    function remove(Data storage self, uint value) returns (bool);
    function contains(Data storage self, uint value) returns (bool);
    function version() returns (uint);
}

// SetProvider interface
contract SetProvider { 
    function getSet() returns (Set);
}

contract Bob { 
    address public providerAddr;
    uint8 public result;
    struct Data { mapping(uint => bool) flags; }
    Data db; 
    bool contain;

    function Bob()payable{}
    function setResult(uint8 res){ result = res; } 
    function setProvider(address arg) { providerAddr = arg; }

    function insertData(uint256 n) returns (bool) {
        address setAddr = SetProvider(providerAddr).getSet();
        bool res = setAddr.delegatecall.gas(55555)(
                   bytes4(sha3("insert(uint256)")),n);

        return res; 
    }

    function containsData(uint256 n) returns (bool) {
        address setAddr = SetProvider(providerAddr).getSet();
        bool res = setAddr.delegatecall.gas(55555)(
                   bytes4(sha3("contains(uint256)")),n);
                   
        return contain; 
    }
    
    function getVersion() returns (uint) {
        address setAddr = SetProvider(providerAddr).getSet();
        bool res = setAddr.delegatecall.gas(55555)(
                   bytes4(sha3("version()")));

        return result; 
    }
    
    function() payable{
    }
    
    function getDB(uint n) public view returns (bool) {
        return db.flags[n];
    }

    // Helper function to check the balance of this contract
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
}