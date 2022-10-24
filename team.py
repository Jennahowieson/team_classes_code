class Team:
    def __init__(self, team_name, player, coach):
        self.name = team_name
        self.players = player
        self.coach = coach 

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player):
       return player in self.players
    
    def has_points(self):
         return self.team.points
            