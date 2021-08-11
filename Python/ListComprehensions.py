# task:-
#   Let's learn about list comprehensions! You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n. 
#   Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n. Here,0<=i<=x, 0<=j<=y, 0<=k<=z. 
#   Please use list comprehensions rather than multiple loops, as a learning exercise.
#   Print an array of the elements that do not sum to .

# Input Format:-
#   Four integers  and , each on a separate line.
# Constraints:-
#   Print the list in lexicographic increasing order.

# Sample Input 0
# 1
# 1
# 1
# 2
# Sample Output 0
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
# Explanation 0
# Each variable  and  will have values of  or . All permutations of lists in the form . 
# Remove all arrays that sum to  to leave only the valid permutations.

# Sample Input 1
# 2
# 2
# 2
# 2
# Sample Output 1
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], 
#  [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]

# Code:-
  if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    print [list([i,j,k]) for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n]
    
# This is the solution of this problem. In this problem we have to use our knowledge of list comprehension.
# List comprehension is nothing but writing the same 5-6 lines of program in one line.
# In this problem we have to use the for loop but instead of writng one below other we write it one after other.
# This is known as list comprehension. The problem is so simple everything is given in the problem statement we just have to use the list comprehension.
