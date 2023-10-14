def passwordVulnerability(password, max_ops):
    max_length = 1
    current_length = 1
    ops_left = max_ops
    i = 0
    while(i+current_length < len(password)):
        if password[i+current_length] == password[i]:
            current_length += 1
        else:
            if ops_left == 0:
                i += current_length
                current_length = 1
                ops_left = max_ops
                continue
            ops_left -= 1
            current_length += 1

        max_length = max(max_length, current_length)

    return max_length

# Example usage:
password = ["abababa","ababc","abcdabcd","a"]
max_ops = [3,1,2,2]
for i in range(len(password)):
    vulnerability = passwordVulnerability(password[i], max_ops[i])
    print(vulnerability)  # Output: 7,3,3