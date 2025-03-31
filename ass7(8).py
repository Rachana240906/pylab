def decode_ways(s, index=0, path="", result=None):
    if result is None:
        result = []
    
    if index == len(s):
        result.append(path)
        return result
    
    if s[index] == '0':
        return result
    
    num1 = int(s[index])
    decode_ways(s, index + 1, path + chr(64 + num1), result)
    
    if index + 1 < len(s):
        num2 = int(s[index:index+2])
        if 10 <= num2 <= 26:
            decode_ways(s, index + 2, path + chr(64 + num2), result)
    
    return result

s = input("Enter the encoded message: ")
possible_decodings = decode_ways(s)
print("Possible decoded messages:")
for decoding in possible_decodings:
    print(decoding)
