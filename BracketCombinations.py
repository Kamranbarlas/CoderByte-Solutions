#Bracket Combinations
#Have the function BracketCombinations(num) read num which will be an integer greater than or equal to zero, and return the number of valid combinations that can be formed with num pairs of parentheses. For example, if the input is 3, #then the possible combinations of 3 pairs of parenthesis, namely: ()()(), are ()()(), ()(()), (())(), ((())), and (()()). There are 5 total combinations when the input is 3, so your program should return 5.
#Examples
#Input: 3
#Output: 5
#Input: 2
#Output: 2
#Tags
#combinatoricsGooglefree


def BracketCombinations(n):
  result = []
  def backtrack(current, open_count, closed_count):
    if len(current) == n*2:
      result.append(current)
      return
    if open_count < n:
      backtrack(current + "(", open_count + 1,closed_count)
    if closed_count < open_count:
      backtrack(current + "(", open_count,closed_count + 1)
  backtrack("",0,0)
  return len(result)

print(BracketCombinations(input()))
