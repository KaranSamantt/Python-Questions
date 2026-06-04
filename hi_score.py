def game():

    score  = int(input("Enter your score: "))
    return score


file = open("Hi-score.txt", "r")

content = file.read().strip()
file.close()

if content == "":
    hi_score = 0
else:
    hi_score = int(content)

print("Previous hi score : ", hi_score)

# Play the game
score = game()

print("Your score: ", score)

if(score>hi_score):
    hi_score = score
    file = open("Hi-score.txt", "w")
    file.write(str(hi_score))
    file.close()
    print("New Hi-score! Updated to: ", hi_score)
else:
    print("You did not beat the Hi-score of: ", hi_score)

