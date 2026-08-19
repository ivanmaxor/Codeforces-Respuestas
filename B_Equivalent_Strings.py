def recursion(a_word, b_word):
    if a_word == b_word:
        return True

    a_len = len(a_word)
    b_len = len(b_word)

    if a_len % 2 != 0: 
        return False

    mitad = a_len // 2
    
    a1 = a_word[:mitad]
    a2 = a_word[mitad:]
    
    b1 = b_word[:mitad]
    b2 = b_word[mitad:]
    
    return (recursion(a1, b1) and recursion(a2, b2)) or (recursion(a1, b2) and recursion(a2, b1))


a_word = input()
b_word = input()

a_large = len(a_word)
b_large = len(b_word)

if a_large != b_large:
    print("NO")
elif recursion(a_word, b_word):
    print("YES")
else:
    print("NO")