pragma solidity ^0.4.2;

contract Set {
    uint8 public result;
    struct Data { mapping(uint => bool) flags; }
    Data db;
    bool contain;

    function insert(uint256 value) { 
        db.flags[value] = true; 
    }

    function remove(uint256 value) { 
        db.flags[value] = false; 
    }

    function contains(uint256 value){ 
        contain = db.flags[value]; 
    }

    function setResult(uint8 res){
        result = res; 
    }
     
    function version(){  this.setResult(3);  }
}