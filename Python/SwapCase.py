# Task:
#   You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
  
# Function Description:
#   Complete the swap_case function in the editor below.
  
# swap_case has the following parameters:
#   string s: the string to modify
    
# Returns:
#   string: the modified string
    
# Input Format:
#   A single line containing a string s.
  
# Constraints:
#   0<=len(s)<=1000

# Sample Input 0
# HackerRank.com presents "Pythonist 2".
# Sample Output 0
# hACKERrANK.COM PRESENTS "pYTHONIST 2".

# Code:
  def swap_case(s):
    Output = '';
    for char in s:
        if(char.isupper()==True):
            Output += (char.lower());
        elif(char.islower()==True):
            Output += (char.upper());
        else:
            Output += char;
    return Output
