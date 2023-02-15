from random import randint
from typing import List

nums: List[str] = []
lennums = 0
finlen = 100
print("Please give AI some data to learn...")
print("The current data length is 0, 100 symbols left")
while finlen > lennums:
    print("Print a random string containing 0 or 1\n")
    imp = str(input())
    nums.extend([x for x in imp if x in "01"])
    lennums = len(nums)
    left = finlen - lennums
    if finlen > lennums:
        print(f"Current data lenght is {lennums}, {left} symbols left")
#  nums = "010100101001010101111110001001011000010101010101010010101010101001010010101010001111001010010101010010101010101"
nums = "".join(nums)
print(f"Final data string:\n{nums}")

print("You have $1000. Every time the system successfully predicts your next press, you lose $1.")
print("Otherwise, you earn $1. Print \"enough\" to leave the game. Let's go!")

del finlen
del lennums

triad_map = {"000": [0, 0],
             "001": [0, 0],
             "010": [0, 0],
             "011": [0, 0],
             "100": [0, 0],
             "101": [0, 0],
             "110": [0, 0],
             "111": [0, 0]}

for i in range(3, len(nums)):
    triad = nums[i - 3] + nums[i - 2] + nums[i - 1]
    if nums[i] == "0":
        triad_map[triad][0] += 1
    else:
        triad_map[triad][1] += 1

def genpred():
    l_u_input = []
    nums: List[str] = []
    nums.extend([x for x in u_input if x in "01"])
    if len(nums) == 0:
        return
    nums = "".join(nums)

    for i in range(3, len(nums) + 1):
        triad = nums[i - 3] + nums[i - 2] + nums[i - 1]
        l_u_input.append(triad)

    pred = ""
    for i in range(1, 4):
        x = randint(0, 1)
        x = str(x)
        pred = pred + x
    for i in range(0, (len(l_u_input) - 1)):
        t = l_u_input[i]
        if triad_map[t][0] > triad_map[t][1]:
            x = "0"
        if triad_map[t][0] == triad_map[t][1]:
            x = randint(0, 1)
            x = str(x)
        if triad_map[t][0] < triad_map[t][1]:
            x = "1"
        pred = pred + x
    print("prediction:")
    print(pred)
    del (t)
    del (triad)

    global right
    right = 0 # верно угаданые цифры, вычитаем из банка
    for i in range(0, (len(nums) - 3)):
        x = nums[i + 3]
        y = pred[i + 3]
        if x == y:
            right += 1


    perc = (right / (len(nums) - 3)) * 100
    perc = round(perc, 2)
    global wrong
    wrong = (len(nums) - 3) - right #неверно угаданные, прибавляем
    print("Computer guessed right", right, "out of", (len(nums) - 3), "symbols", "(", perc, "%)")

bank = 1000
right = 0
wrong = 0
while bank > 0:
    u_input = str(input("Print a random string containing 0 or 1\n")) # 0111001001
    if u_input == "enough":
        print("Game over!")
        bank = 0
    else:
        genpred()
        bank = bank - right + wrong
        if bank < 1:
            print("Game over!")
        print(f"Your balance is now ${bank}")