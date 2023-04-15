input_ = input().split()

n = int(input_[0])
x = int(input_[1])
y = int(input_[2])

x -= 0.5
y -= 0.5

distance = max(abs(x - n//2),abs(y - n//2))

print((int(distance + 0.5)*2 - 1)*4)