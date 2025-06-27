// 
// function calc_area(width,height){
//     return (width<=0 ||height<=0)?(`Invalid ${width} and ${height}`):width*height;
// }
// console.log(calc_area(4,0));

// const createMessage=function(message,prefix="Info"){
//     return `[${prefix}] ${message};`
// }
// console.log(createMessage("login successfull","chores"));


// write a function that takes an array of numbers and return an Object
// with the same and avg of the numbers

// function sum_avg(array){
//     let sum=0;
//     for(let i=0;i<array.length;i++){
//         sum+=array[i];
//     }
   
//     let avg=sum/array.length;
//      return {
//         sum: sum,
//         average: avg
//     };
   


// }
// let arr=[2,4,6,8,9]
// console.log(sum_avg(arr));

// function square(num){
//     return num*num;
// }
// console.log(square(50));
// const summ=(a,b)=> b+a;
// console.log(summ(4,3))




const filterEven=numbers=>numbers.filter(num=>num%2==0);
console.log(filterEven([1,2,3,4,5,6]))

