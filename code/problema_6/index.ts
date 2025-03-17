
function mergeSort(arr: number[]): number[] {
  if (arr.length <= 1) {
      return arr;
  }

  const middle = Math.floor(arr.length / 2);
  const left = mergeSort(arr.slice(0, middle));
  const right = mergeSort(arr.slice(middle));

  return merge(left, right);
}

function merge(left: number[], right: number[]): number[] {
  let result: number[] = [];
  let i = 0, j = 0;

  while (i < left.length && j < right.length) {
      if (left[i] < right[j]) {
          result.push(left[i]);
          i++;
      } else {
          result.push(right[j]);
          j++;
      }
  }

  return result.concat(left.slice(i)).concat(right.slice(j));
}

//---------------------------------------------------------------- 
//---------------------------------------------------------------- 

const arr = [38, 27, 43, 3, 9, 82, 10];
console.log("Arreglo original:", arr);
const sortedArr = mergeSort(arr);
console.log("Arreglo ordenado:", sortedArr);