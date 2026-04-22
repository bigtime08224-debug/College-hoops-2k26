class Game:
    def __init__(self):
        self.team1_score = 0
        self.team2_score = 0
        self.stats = {'team1': {}, 'team2': {}}

    def score_points(self, team, points):
        if team == 1:
            self.team1_score += points
            self.update_stats('team1', points)
        elif team == 2:
            self.team2_score += points
            self.update_stats('team2', points)

    def update_stats(self, team, points):
        if 'total_points' in self.stats[team]:
            self.stats[team]['total_points'] += points
        else:
            self.stats[team]['total_points'] = points

    def get_winner(self):
        if self.team1_score > self.team2_score:
            return 'Team 1 wins!'
        elif self.team2_score > self.team1_score:
            return 'Team 2 wins!'
        else:
            return "It's a tie!"

    def game_summary(self):
        return {
            'team1_score': self.team1_score,
            'team2_score': self.team2_score,
            'stats': self.stats
        }

# Example of using the Game class
if __name__ == '__main__':
    game = Game()
    game.score_points(1, 3)
    game.score_points(2, 2)
    print(game.game_summary())
    print(game.get_winner())