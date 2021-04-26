const sieve = require("./sieve");
const fs = require("fs");
const numprimes = 1E5;
//clear prime file
fs.writeFileSync("primes.txt","","utf8");
console.log("Calculating primes...");
var primes = sieve(numprimes);
console.log("Complete!");
primes.forEach((num,i)=>{
  if((i+1)%1000 === 0) fs.appendFileSync("primes.txt","\n","utf8");
  fs.appendFileSync("primes.txt",num+" ","utf8");
});
