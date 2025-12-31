import random
n = random.randint(1,100)
a=-1
guesses=0
while(a!=n):
    guesses+=1
    a=int(input("Guess the number: "))
    if(a>n):
        print("The number is lower than that..")
    else:
        print("The number is higher than that")
print(f"Guessed !!\n Guessed in - {guesses} attempts")

# Read previous best score (if any) and handle errors with friendly messages
try:
    with open("attempts.txt", "r") as f:
        content = f.read().strip()
        if content:
            past_score = int(content)
            print(f"Past highest score: {past_score}")
        else:
            past_score = None
except FileNotFoundError:
    past_score = None
    print("No previous high score found.")
except ValueError:
    past_score = None
    print("Previous high score is invalid; resetting.")
except Exception as e:
    past_score = None
    print(f"Could not read high score: {e}")

# Update the high score if current score is better
if past_score is None or guesses < past_score:
    try:
        with open("attempts.txt", "w") as f:
            f.write(str(guesses))
        print(f"New High Score: {guesses}")
    except Exception as e:
        print(f"Could not save high score: {e}")

print("Thank you for playing!")