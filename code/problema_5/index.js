"use strict";
function findCommonElements(lists) {
    if (lists.length === 0)
        return [];
    return lists.reduce((acc, curr) => acc.filter(item => curr.includes(item)));
}
//---------------------------------------------------------------- 
//---------------------------------------------------------------- 
const lists = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 6, 2]
];
console.log(findCommonElements(lists)); // Output: [2, 3, 4]
