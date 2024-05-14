import random

def play_rock_paper_scissors():
    player_score = 0
    ai_score = 0
    options = ['rock', 'paper', 'scissors']

    while True:
        print("\nChoose your weapon!")
        player_choice = input("Enter rock, paper, or scissors: ").lower()

        while player_choice not in options:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            player_choice = input("Enter rock, paper, or scissors: ").lower()

        ai_choice = random.choice(options)
        print(f"Computer chose: {ai_choice}")

        if player_choice == ai_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and ai_choice == "scissors") or \
             (player_choice == "paper" and ai_choice == "rock") or \
             (player_choice == "scissors" and ai_choice == "paper"):
            print("You win!")
            player_score += 1
        else:
            print("You lose!")
            ai_score += 1

        print(f"Score: You {player_score} - Computer {ai_score}")

        if input("Play again? (yes/no): ").lower() != 'yes':
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    play_rock_paper_scissors()
