function solution(babbling) {
  var answer = 0;
  
  const pronouncableList = /(aya|ye|woo|ma)/g;

  babbling.forEach((pronunciation) => {
      const result = pronunciation.replaceAll(pronouncableList, '');
      
      if (result.length === 0) {
          answer += 1    
      }
  });
  
  return answer;
}