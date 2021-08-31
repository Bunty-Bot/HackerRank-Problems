# Task: 
#   Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).
#   Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
    
# Input Format:
#   The first line contains an integer, n, denoting the number of elements in the tuple. 
#   The second line contains n space-separated integers describing the elements in tuple t.
# Output Format:
#   Print the result of hash(t).
  
# Sample Input 0
# 2
# 1 2
# Sample Output 0
# 3713081631934410656

# Code:
  if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t = tuple(integer_list)
    print(hash(t))

# This is the solution of this problem. This is one of the easiest problem on the hackerrank platform.
# To solve this problem you just need to have the knowledge of tuple.
# if you like the code:
#   give a star.
# else:
#   give a star.
