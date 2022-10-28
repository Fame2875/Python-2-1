text = input().lower()
if text[::-1] == text:
    r = len(text)
    if r % 2 == 0:
        if text[:r // 2][::-1] == text[:r // 2] and text[r // 2:][::-1] == text[r // 2:]:
            print('Double Palindrome')
        else:
            print('Palindrome')
    else:
        if text[:r // 2][::-1] == text[:r // 2] and text[r // 2 + 1:][::-1] == text[r // 2 + 1:]:
            print('Double Palindrome')
        else:
            print('Palindrome')
else:
    print('No')