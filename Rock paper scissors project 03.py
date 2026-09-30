import random

print("=" * 45)
print("       🎮 ROCK PAPER SCISSORS")
print("=" * 45)

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0
draws = 0

while True:
    print("\nChoose your option:")
    print("1. 🪨 Rock")
    print("2. 📄 Paper")
    print("3. ✂️ Scissors")
    print("4. 🚪 Quit")

    user_choice = input("\nEnter your choice (1-4): ")

    if user_choice == "4":
        break

    if user_choice not in ["1", "2", "3"]:
        print("❌ Invalid choice! Please enter 1, 2, 3, or 4.")
        continue

    player = choices[int(user_choice) - 1]
    computer = random.choice(choices)

    print(f"\nYou chose:     {player}")
    print(f"Computer chose: {computer}")

    # Check the winner
    if player == computer:
        print("🤝 It's a DRAW!")
        draws += 1

    elif (
        (player == "rock" and computer == "scissors")
        or
        (player == "paper" and computer == "rock")
        or
        (player == "scissors" and computer == "paper")
    ):
        print("🎉 YOU WIN!")
        player_score += 1

    else:
        print("💻 COMPUTER WINS!")
        computer_score += 1

    # Display score
    print("\n----- SCORE -----")
    print(f"🏆 You:      {player_score}")
    print(f"💻 Computer: {computer_score}")
    print(f"🤝 Draws:    {draws}")

print("\n" + "=" * 45)
print("             FINAL SCORE")
print("=" * 45)

print(f"You:      {player_score}")
print(f"Computer: {computer_score}")
print(f"Draws:    {draws}")

if player_score > computer_score:
    print("\n🏆 Congratulations! You are the champion!")

elif computer_score > player_score:
    print("\n💻 Computer wins the game!")

else:
    print("\n🤝 The game ended in a draw!")

print("\nThanks for playing! 🎮")