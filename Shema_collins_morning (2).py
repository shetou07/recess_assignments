# Exercise 1.
# Asking a user how they rate their mental health using a scale from 1 to 10.
emotion_scale = int(input("Using a scale of 1-10 , rate your mental health? "))
try:
    if emotion_scale <= 5:
        print("Everything is going to be well. Don't feel sad")
    elif 5 < emotion_scale <= 7:
        print("You're doing well")
    elif 7 < emotion_scale <= 10:
        print("You're on fire")
    else:
        print("Something is wrong")
except ValueError:
    print("Enter a value😉 between 1 and 10")
