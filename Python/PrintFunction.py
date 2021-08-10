# Task:-
#   The included code stub will read an integer,n, from STDIN.
#   Without using any string methods, try to print the following:
#   123....n
#   Note that "..." represents the consecutive values in between.
  
# Example:- 
#   n = 5
#   Print the string 12345.
  
# Input Format:-
#   The first line contains an integer .
# Constraints:-
#   1<=n<=150
  
# Output Format:-
#   Print the list of integers from 1 through n as a string, without spaces.
  
# Sample Input 0
# 3
# Sample Output 0
# 123

# Code:-
  from __future__ import print_function

  if __name__ == '__main__':
      n = int(raw_input())
      for i in range(n):
          print(i+1, end="")

#  Don't worry with the new line of if condition. It is used in Oops. On this platform it is used everywhere. In this problem we don't 
# use the string method to print the numbers. Basically this problem takes you more deeper into your understanding of loops.
# In this problem we just have to use the for loop in a correct manner.
# if you like the code:
#   give a star.
# else:
#   give a star.
