# python3
import numpy as np

p = 37
x = 31
    
def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def poly_hash(s):
    ans = 0
    for c in reversed(s):
        ans = (ans * x + ord(c)) % p
    return ans

def precompute_hash(text, len_pattern):    
    len_text = len(text)
    h = np.zeros(len_text - len_pattern + 1, np.int32)
    s = text[len_text-len_pattern:]
    
    h[-1] = poly_hash(s)
    y = 1
    for i in range(len_pattern):
        y = (y * x) % p
        
    for i in range(len(h)-2, -1, -1):
        a1 = ((x%p) * (h[i+1]%p))%p
        a2 = ord(text[i])%p
        a3 = ((y%p) * (ord(text[i + len_pattern])%p))%p
    
        h[i] =  (a1 + a2 - a3) % p

    return h                

def get_occurrences(pattern, text):
#    return [
#        i 
#        for i in range(len(text) - len(pattern) + 1) 
#        if text[i:i + len(pattern)] == pattern
#    ]
#    
    len_text = len(text)
    len_pattern = len(pattern)
    result = []
    if len_pattern > len_text:
        return result
    
    pHash = poly_hash(pattern)
    h = precompute_hash(text, len_pattern)
    for i in range(0, len_text - len_pattern + 1):
#        print("{0}:{1}:{2}".format(i, h[i], pHash))
        
        if h[i] != pHash:
            continue
        
        if pattern == text[i: i+len_pattern]:
            result.append(i)

    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

