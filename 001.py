print("This line will be printed.")

print("hello")
print("")
print()

print("bye")

# delete stress symbols from the word
# word = word.replace("\u0301", "")

print("{:d} {:03d} {:>20f}".format(1, 2, 1.1))
print({range(1, 10)})

for x in range(1, 11):
    print(x, end=" ")

print("sdfdsfsfd")
print(*range(1, 11))

print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

# name = input()
# print("What a great name you have, {0}".format(input()))
# print('What a great name you have, {name}!')

# r3, r5, r7 = int(input()), int(input()), int(input())
#
# age = (r3 * 70 + r5 * 21 + r7 * 15) % 105
#
# print("Your age is " + age + "; that's a good time to start programming!")

# n = int(input())
# # n = 8
# print(str((((n + 8) * 8) - 8) // 8))
#
# print(((3 + 5) // 2 * 2 ** 3) % 7)


a = True
b = False
c = a and not b
print(a and (not c or b))

x = [int(input()), int(input()), int(input())]
print(x)
x_original = x
x.sort()
print(x)
print(x_original == x)

i = 0
while i <= 10:
    i = i + 1
    if i > 7:
        i = i + 2
print(i)

print(*range(1, 11))

input_str = input()
listt = list(input_str)
print(listt)


def is_even(number):
    return number % 2 == 0


print(is_even(34))
