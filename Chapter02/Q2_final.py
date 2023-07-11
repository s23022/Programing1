import random


def generate_random_alphabet():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    random_letter = random.choice(alphabet)
    return random_letter


target_letter = "h"

while True:
    random_letter = generate_random_alphabet()
    print(random_letter)

    if random_letter == target_letter:
        break
