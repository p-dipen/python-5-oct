# A string is a palindrome if it reads the same forward and backward. The words “mom”, “dad”, and “noon”, for example, are all palindromes.

# How do you write a program to check whether a string is a palindrome ? 

# mom

# second

# Get the length of the string -> 
# index = the numerical position of an item within an ordered sequence
word = "raddar"
left = 0
right = len(word) - 1
isPalindrome = True
while left <= right:
    print(f"{left=},{word[left]},{right=},{word[right]}")
    if word[left] == word[right]:
        print("In the condition = ",word[left], word[right])
        left += 1
        right -= 1
        continue
    else:
        print("Is is not a palindrome")
        isPalindrome = False
        break

if isPalindrome:
    print("This is a Palindrome")


