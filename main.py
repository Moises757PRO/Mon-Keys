import string
from random import randint
from random import choice
import time

ai = list(string.ascii_letters + string.digits)

word = input("Write here your word: ")
long = len(word)

print(f"Working results for: {word} (lenght: {long})")
print(f"Characters: {' '.join(ai)} ({len(ai)})")

atem = 0

probability = (1 / len(ai)) ** long
totalProbability = probability * 100

start = time.time()

while time.time() - start < 1:
    result = ""
    for i in range(long):
        result += choice(ai)
    atem += 1

print(f"Calculations per/second: {atem}")

result = ""
atem = 0

print(f"probability: {totalProbability:.10f}%")

pro = input(f"proceed with {word}")

while word != result:
    for i in range(long):
        numb = randint(0, len(ai) - 1)
        char = ai[numb]

        result += char
    if result == word:
        print(f"Found! {result}!")
        break
    else:
        atem += 1
        print(f"atempt {atem}\ncurrent cobination: {result}")
        result = ""

# conclusion
print(f"atempts: {atem}")
