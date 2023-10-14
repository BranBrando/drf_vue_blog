def replace_char(c):
    # Helper function to replace a character with the previous character in alphabetical order.
    if c == 'a':
        return 'z'
    else:
        return chr(ord(c) - 1)

def storedWord(word, max_operations):
    operations_left = max_operations
    largest_char = ord(word[0])
    res = ""

    for i in range(len(word)):
        c = word[i]
        
        if ord(c) - ord('a') > operations_left:
            if largest_char - ord('a') <= operations_left:
                operations_left -= largest_char - ord('a')
            if operations_left >= 0:
                res += chr(ord(c) - operations_left)
            else:
                res += c
            print(operations_left)
            i+=1
            while i < len(word):
                tmp = word[i]
                if ord(tmp) > ord(c) - operations_left and ord(tmp) <= ord(c):
                    res += chr(ord(c) - operations_left)
                elif ord(tmp) <= largest_char:
                    res += "a"
                else:
                    res += word[i]
                i += 1
            break
        else:
            res += "a"
            largest_char = max(largest_char, ord(c))

    return res

# Example usage:
word = ["abcde","cba","yzwyz"]
max_operations = [4, 2, 3]
for i in range(len(word)):
    stored_word = storedWord(word[i], max_operations[i])
    print(stored_word)  # Output: "aaaaa", "aaa", "vzvvz"