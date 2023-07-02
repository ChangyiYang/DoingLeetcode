k = int(input())
n = 0

while k > 0:
    n += 7
    
    if '4' not in str(n):
        k -= 1
        continue

    print(n)

        
# print(n)