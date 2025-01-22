def compress(s):
    compressed = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        compressed.append((s[i], count))  # Store as tuple (char, count)
        i += 1
    return compressed

def decompress(compressed_list):
    return "".join(char * count for char, count in compressed_list)

# Example

s = "AAAABBBB33333AAAARRRR"
compressed_str = compress(s)
print(compressed_str) 
original=decompress(compressed_str)
print(original) 

