# Task:-
#   The provided code stub reads two integers, a and b, from STDIN.
#   Add logic to print two lines. The first line should contain the result of integer division, a // b. 
#   The second line should contain the result of float division, a / b.
#   No rounding or formatting is necessary.
  
# Example:- 
#   a = 3
#   b = 5
#   The result of the integer division a//b = 0.
#   The result of the float division is a/b = 0.6.
#   Print:
#   0
#   0.6

# Input Format:-
#   The first line contains the first integer, a. 
#   The second line contains the second integer, b.
  
# Output Format:-
#   Print the two lines as described above.
  
# Sample Input 0
# 4
# 3
# Sample Output 0
# 1
# 1.33333333333

# Code:-
  from __future__ import division
  a = int(input())
  b = int(input())
  print(a//b)
  print(a/b)
  
# This is the another type of arithmatic operator problem. In this problem we learn that in python,
# we have to different symbols for int and float division. For int division we use '//' and for float
# we use '/' symbol. To solve this problem we are importing division library.
