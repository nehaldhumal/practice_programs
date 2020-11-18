
# Loops And Iterations

nums = [1,2,3,4,5]
for num in nums:
    if num == 4:
        print('Found')
        # break
        continue
    print(num)

for num in nums:
    for letter in 'abc':
        print(num, letter)

for a in range(10):
    print(a)

for i in range(1, 10):
    print(i)

# while loops

x = 0
while x < 10:
    print(x)
    x += 1

x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1
