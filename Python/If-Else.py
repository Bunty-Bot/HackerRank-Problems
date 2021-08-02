# Task:-
#   Given an integer, , perform the following conditional actions:
#   If n is odd, print Weird
#   If n is even and in the inclusive range of  to , print Not Weird
#   If n is even and in the inclusive range of  to , print Weird
#   If n is even and greater than , print Not Weird
  
# Input:-
#   A single line containing a positive integer,n.
  
# Constraints:-
#   1<=n<=100
  
# Output:-
#   Print Weird if the number is weird. Otherwise, print Not Weird.
  

# Sample Input 0
# 3
# Sample Output 0
# Weird
# Explanation 0
# n = 3
# n is odd and odd numbers are weird, so print Weird.
# Sample Input 1
# 24
# Sample Output 1
# Not Weird
# Explanation 1
# n = 24
# n>20 and n is even, so it is not weird.

# Code:-
  n = int(input())
if n%2==0:
    if 2<=n<=5:
        print("Not Weird")
    elif 6<=n<=20:
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")
    
# This is the next problem in this python folder. In this problem we just have to use the if-else conditions.
# In this program we are given a task which has conditions in it and these conditions are the statements of if-else:
# If you like the code:-
#   give a star
# else:-
#   give a star
  
