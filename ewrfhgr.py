s = input()
nums = [int(x) for x in s.split(",") if x.strip()]
for x in reversed(nums):
    if x % 2 == 0:
        print(x)