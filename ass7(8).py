def decode_ways(e_str):
    def decode_helper(e_str, i, current, r):
        if i == len(e_str):
            r.append("".join(current))
            return
        
        if i < len(e_str) and e_str[i] != '0':
            current.append(chr(int(e_str[i]) + ord('A') - 1))
            decode_helper(e_str, i + 1, current, r)
            current.pop()
        
        if i + 1 < len(e_str) and e_str[i] != '0' and 1 <= int(e_str[i:i+2]) <= 26:
            current.append(chr(int(e_str[i:i+2]) + ord('A') - 1))
            decode_helper(e_str, i + 2, current, r)
            current.pop()

    r = []
    decode_helper(e_str, 0, [], r)
    return r

e_msg = input("Enter encoded message: ")
d_msg = decode_ways(e_msg)

print("Decoded messages:")
for msg in d_msg:
    print(msg)
