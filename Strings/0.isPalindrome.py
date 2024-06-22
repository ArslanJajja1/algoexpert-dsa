'''
 Difficulty:
Category:
Strings
Successful Submissions:
85,419+
Palindrome Check
Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a palindrome.

A palindrome is defined as a string that's written the same forward and backward. Note that single-character strings are palindromes.

Sample Input
string = "abcdcba"
Sample Output
true // it's written the same forward and backward
Hints
Hint 1
Start by building the input string in reverse order and comparing this newly built string to the input string. Can you do this without using string concatenations?

Hint 2
Can you optimize your algorithm by using recursion? What are the implications of recursion on an algorithm's space-time complexity analysis?

Hint 3
Go back to an iterative solution and try using pointers to solve this problem: start with a pointer at the first index of the string and a pointer at the final index of the string. What can you do from there?

Optimal Space & Time Complexity
O(n) time | O(1) space - where n is the length of the input string
'''
# Solution 1 - Recursive Solution

def isPalindrome(string,l=0):
    # Write your code here.
    r = len(string)-1-l
    if l >= r:
        return True
    if string[l] == string[r]:
        return isPalindrome(string,l+1)
    else:
        return False
# TC : O(n)
# SC : O(n)

# Solution 2 - 

def isPalindrome(string):
    # Write your code here.
    if len(string) == 0:
        return True
    l = 0
    r = len(string)-1
    while l < r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True
    
    # TC : O(N)
    # SC : O(1)