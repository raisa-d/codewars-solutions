/*
Mary brought home a "spot the differences" book. The book is full of a bunch of problems, and each problem consists of two strings that are similar. However, in each string there are a few characters that are different. An example puzzle from her book is:

String 1: "abcdefg"
String 2: "abcqetg"
Notice how the "d" from String 1 has become a "q" in String 2, and "f" from String 1 has become a "t" in String 2.

It's your job to help Mary solve the puzzles. Write a program spot_diff/Spot that will compare the two strings and return a list with the positions where the two strings differ. In the example above, your program should return [3, 5] because String 1 is different from String 2 at positions 3 and 5.

NOTES:
• If both strings are the same, return []
• Both strings will always be the same length
• Capitalization and punctuation matter
*/

// method 1: turn to array, for each
const spot = (s1,s2) => {
  let res = [];
  s1 = s1.split('');
  s2 = s2.split('');
  // loop through s2 array
  s2.forEach((char, i, arr) => {
    // if the current char isn't equal to that index of s1
    if(char !== s1[i]) {
      // add that index to result
      res.push(i);
    };
  });
  // return result
  return res;
};

// method 2: regular for loop
const spot = (s1,s2) => {
  let res = [];
  for(let i = 0; i < s1.length; i++) {
    if(s1[i] !== s2[i]) res.push(i);
  };
  return res;
};
