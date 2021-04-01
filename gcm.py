import sys
num_count = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
print(num)
for i in range(1, max(num)):
    if num[0] % i == 0 and num[1] % i == 0:
        print(i)
