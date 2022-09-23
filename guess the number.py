

class GuesstheNumber:
    def __init__(self, number, mn=0, mx=100):
        self.number = number
        self.guesses = 0
        self.min = mn
        self.max = mx
    
    def get_guess(self):
        guess = input(f"please guess a number between {self.min} - {self.max}: ")

        if self.valid_number(guess):
            return int(guess)
        else:
            print("You did not enter a number!")
            return self.get_guess()

    def valid_number(self, str_number):
        try:
            number = int(str_number)
        except:
            return False

        return self.min <= number <= self.max

    def play_game(self):
        while True:
            self.guesses += 1

            guess = self.get_guess()

            if guess < self.number:
                print("your guess was lower")
            elif guess > self.number:
                print("your guess was higher")
            else:
                break
        
        print(f"You have guessed it in {self.guesses} guesses")


game = GuesstheNumber(30, 20, 40)
game.play_game()