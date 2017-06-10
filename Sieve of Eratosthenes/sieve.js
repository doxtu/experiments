/*
  How to use:
  html:
  <script src="/path/to/sieve.js"></script>
  module:
  var sieve = require("./path/to/sieve");
*/

(function sieveCreator(context){
  "use strict";

  //dopey module implementation
  if(typeof module.exports !== "undefined"){
    module.exports = sieve;
  }else{
    //Yup, just slap it on the global scope. Nobody will care.
    context.sieve = sieve
  }

  function sieve(n){
    //list will have n length containing numbers 2 to n
    //primes will obviously contain primes
    //p is our initial prime
    var list = [],
    primes = [],
    p = 2;

    var start = Date.now();

    //fix n to make sure it's reasonable
    if(isNaN(n)) return;
    n = Math.floor(n);

    for(let i=2;i<=n;i++)
      list.push(i);

    while(list.length > 0){
      //saves prime number for later use
      primes.push(p);
      //deletes filthy composite numbers
      for(let i = 0;i<list.length;i++){
        if(list[i]%p === 0){
          list.splice(i,1);
        }
      }
      //advances to next prime
      p = list[0];
    }

    console.log("Execution time (s):",(Date.now()-start)/1000,"\n\n");

    return primes;
  }

})(this);

// var primes = module.exports(1000);
// process.exit(1);
