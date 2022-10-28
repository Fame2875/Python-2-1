'''
เขียน Recursive เพื่อหาว่า String ที่รับเข้ามาเป็น Palindrome หรือไม่
Enter Input : abba
'abba' is palindrome
'''
def ispalindrome(word):
    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    return ispalindrome(word[1:-1])
word = input("Enter Input : ")

if ispalindrome(word) == True:
    print("'"+word+"'"+" is palindrome")
else:
    print("'"+word+"'"+" is not palindrome") 