function isAnagram(str1: string, str2: string): boolean {
    const normalize = (str: string) => str.toLowerCase().replace(/\s/g, '').split('').sort().join('');
    
    return normalize(str1) === normalize(str2);
}

//---------------------------------------------------------------- 
//---------------------------------------------------------------- 

console.log(isAnagram("alejandro", "dronajela"));    //-- true
console.log(isAnagram("francisco", "cocisnarf"));   //-- true
console.log(isAnagram("perro", "ardrp"));         //-- false