# Task:
#   The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
#   Print the average of the marks array for the student name provided, showing 2 places after the decimal.
 
# Input Format:
#   The first line contains the integer n, the number of students' records. The next n lines contain the names and marks 
#   obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.
  
# Constraints:
#   2<=n<=10
#   0<=marks[i]<=100
#   length of marks arr = 3
  
# Output Format:
#   Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
    
# Sample Input 0
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# Sample Output 0
# 56.00
# Explanation 0
# Marks for Malika are  whose average is 
# Sample Input 1
# 2
# Harsh 25 26.5 28
# Anurag 26 28 30
# Harsh
# Sample Output 1
# 26.50

# Code:
  if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    if query_name in student_marks:
        x = ((float(student_marks[query_name][0]) + float(student_marks[query_name][1]) + float(student_marks[query_name][2])) / 3)
    
    print('%.2f' % x)
    
# This is the answer for this problem. This is a very simple problem. This problem is so common in coding platforms.
# In this problem we should have a good knowledge of arithmatic operation and all.
# if you like the code:
#   give a star.
# else:
#   give a star.





















