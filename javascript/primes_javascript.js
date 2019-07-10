"use strict";
function primes(nb_primes){
    var p = []
    var n = 2
    while (p.length < nb_primes){
        var i;
        for (i of p){
            if (n % i == 0){
                break;
            }
        }
        p = p.concat(n);
        n += 1;
    }
    return p
}

function primes_time(){
    var times = []
    var i;
    for (i=0; i<100; i++){
        var start = performance.now();
        primes(1000);
        var end = performance.now();
        times = times.concat(end-start);
    }
    return times
}

var t = math.mean(primes_time());
console.log(t);
document.write(t);