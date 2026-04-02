print("🧠 Welcome to Mind Reader Game!")
print("Think of a number between 1 and 100... I will guess it 😎")

low = 1
high = 100
attempts = 0

while True:
    guess = (low + high) // 2
    attempts += 1

    print(f"My guess is: {guess}")
    print("Is it correct, too high, or too low?")

    feedback = input("Enter (c = correct, h = too high, l = too low): ").lower()

    if feedback == 'c':
        print(f"🎉 I guessed your number in {attempts} attempts!")
        break
    elif feedback == 'h':
        high = guess - 1
    elif feedback == 'l':
        low = guess + 1
    else:
        print("Invalid input, try again!")

input("Press Enter to exit...")
