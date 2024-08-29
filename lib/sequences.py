#!/usr/bin/env python3

#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return
    
    result = [0] * length  
    if length > 0:
        result[0] = 0 
    if length > 1:
        result[1] = 1  
    for i in range(2, length):
        result[i] = result[i - 1] + result[i - 2]
    print(result)
