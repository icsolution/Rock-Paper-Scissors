import random


winning_cases = {
    'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}


class Game:

    def __init__(self, ratings, rules):
        self.rating = open(ratings, 'r').read()
        self.rules = rules
        self.mode = self.choice = None
        self.score = 0
        self.name = input('Enter your name: ')
        print(f'Hello, {self.name}')
        self.set_mode()

    def set_mode(self):
        rules = input()
        if not rules:
            self.mode = ['paper', 'rock', 'scissors']
        else:
            self.mode = rules.split(',')
        print("Okay, let's start")
        self.start()

    def start(self):
        self.choice = input()
        if self.choice in self.mode:
            self.play()
        elif self.choice == '!exit':
            print('Bye!')
            quit()
        elif self.choice == '!rating':
            for result in self.rating.split('\n'):
                if self.name == result.split()[0]:
                    self.score += int(result.split()[1])
            print(f'Your rating: {self.score}')
            self.start()
        else:
            print('Invalid input')
            self.start()

    def play(self):
        options = self.mode
        computer = random.choice(options)
        if self.choice == computer:
            self.score += 50
            print(f'There is a draw ({self.choice})')
        elif computer in self.rules[self.choice]:
            self.score += 100
            print(f'Well done. The computer chose {computer} and failed')
        else:
            print(f'Sorry, but the computer chose {computer}')
        self.start()


if __name__ == '__main__':
    Game('rating.txt', winning_cases)
