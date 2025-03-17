"use strict";
function isAnagram(str1, str2) {
    const normalize = (str) => str.toLowerCase().replace(/\s/g, '').split('').sort().join('');
    return normalize(str1) === normalize(str2);
}
//---------------------------------------------------------------- 
//---------------------------------------------------------------- 
console.log(isAnagram("alejandro", "dronajela")); // true
console.log(isAnagram("francisco", "cocisnarf")); // false
console.log(isAnagram("perro", "ardrp")); // false
