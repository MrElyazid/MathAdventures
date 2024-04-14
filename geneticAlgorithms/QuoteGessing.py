import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,?!. "
target = "ruy lopez for life, London system for noobs!"
score = 0
guess = []
counter = 0

guess = [random.choice(letters) for _ in range(len(target))]

def mutate(string_list, indices):
    for i in indices:
        string_list[i] = random.choice(letters)




def update_score_indices(target, guess):
    score = 0
    indices = []
    for i in range(len(target)):
        if guess[i] == target[i]:
            score += 1
        else:
            indices.append(i)
    return score, indices



while score != len(target):
    score, indices = update_score_indices(target, guess)
    mutate(guess, indices)
    print("".join(guess)) 
    counter += 1 



print("Final guess:", "".join(guess))
print("number of trials : ", counter)
