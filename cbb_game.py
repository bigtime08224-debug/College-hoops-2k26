class CollegeBasketballGame:
    def __init__(self):
        self.modes = {
            'Quick Game': self.quick_game,
            'Bubble Run': self.bubble_run,
            'Mascot Mode': self.mascot_mode,
            'Road to the Draft': self.road_to_the_draft,
            'Dynasty': self.dynasty,
            'March Madness': self.march_madness,
            'Nike Tutorial': self.nike_tutorial,
            'Athletic Director Mode': self.athletic_director_mode,
        }

    def start_game(self, mode):
        if mode in self.modes:
            print(f'Starting {mode}...')
            self.modes[mode]()
        else:
            print('Invalid game mode selected.')

    def quick_game(self):
        # Implementation for Quick Game
        print('Playing a Quick Game!')

    def bubble_run(self):
        # Implementation for Bubble Run
        print('Running the Bubble Run!')

    def mascot_mode(self):
        # Implementation for Mascot Mode
        print('Entering Mascot Mode!')

    def road_to_the_draft(self):
        # Implementation for Road to the Draft
        print('Starting Road to the Draft!')

    def dynasty(self):
        # Implementation for Dynasty
        print('Embarking on a Dynasty!')

    def march_madness(self):
        # Implementation for March Madness
        print('Joining March Madness!')

    def nike_tutorial(self):
        # Implementation for Nike Tutorial
        print('Starting Nike Tutorial!')

    def athletic_director_mode(self):
        # Implementation for Athletic Director Mode
        print('Managing as Athletic Director!')

    def show_modes(self):
        print('Available Game Modes:')
        for mode in self.modes:
            print(f'- {mode}')


if __name__ == '__main__':
    game = CollegeBasketballGame()
    game.show_modes()  
    # Example of starting a game mode
    game.start_game('Quick Game')
