import random

class Rock_paper_scissors:
    def __init__(self, rounds):
        self.rounds = rounds
        self.current = 1
        self.p_wins = 0
        self.c_wins = 0
    
    def get_c_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])
    
    def find_winner(self, p_choice, c_choice):
        if p_choice == c_choice:
            return "It's a tie!"
        elif (p_choice == 'rock' and c_choice == 'scissors') or \
             (p_choice == 'scissors' and c_choice == 'paper') or \
             (p_choice == 'paper' and c_choice == 'rock'):
            self.p_wins += 1
            return "You win this round!"
        else:
            self.c_wins += 1
            return "Computer wins this round!"
    
    def game_winner(self):
        if self.p_wins > self.c_wins:
            return "You win the game!"
        elif self.c_wins > self.p_wins:
            return "Computer wins the game!"
        else:
            return "It's a tie game!"
    
    def play_game(self):
        while self.current <= self.rounds:
            p_choice = input("Enter your choice: ").lower()
            while p_choice not in ['rock', 'paper', 'scissors']:
                print("Invalid choice")
                p_choice = input("Enter your choice: ").lower()
            
            c_choice = self.get_c_choice()
            print(f"Round {self.current}:")
            print(f"Your choice: {p_choice}")
            print(f"Computer's choice: {c_choice}")
            print(self.find_winner(p_choice, c_choice))
            self.current += 1
        
        print("\nGame Over!")
        print(f"Final score -> You: {self.p_wins} | Computer: {self.c_wins}")
        print(self.game_winner())


rounds = int(input("Enter the number of rounds you want to play: "))
game = Rock_paper_scissors(rounds)
game.play_game()
