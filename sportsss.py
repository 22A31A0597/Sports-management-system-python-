class Player:
    def fun(self, name, age, position, stats=None):
        self.name = name
        self.age = age
        self.position = position
        self.stats = stats 
        self.team = None
    def update_stats(self, stat_name, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Stat value must be a positive number.")
        self.stats[stat_name] = self.stats.get(stat_name, 0) + value
    def __str__(self):
        stats_str = ', '.join([f"{k}: {v}" for k, v in self.stats.items()])
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Team: {self.team or 'None'}, Stats: [{stats_str}]"
class Team:
    def __init__(self, team_name):
        if not team_name.strip():
            raise ValueError("Team name cannot be empty.")
        self.team_name = team_name.strip().title()
        self.players = []
        self.matches = []
    def add_player(self, player):
        if any(p.name == player.name for p in self.players):
            print(f"Player {player.name} is already in the team.")
        else:
            player.team = self.team_name
            self.players.append(player)
            print(f"Player {player.name} added to the team.")
    def remove_player(self, player_name):
        for player in self.players:
            if player.name == player_name.title():
                self.players.remove(player)
                player.team = None
                print(f"Player {player_name} removed from the team.")
                return
        print(f"Player {player_name} not found in the team.")
    def display_team(self):
        if not self.players:
            print(f"Team {self.team_name} has no players.")
        else:
            print(f"Team {self.team_name}:")
            for player in self.players:
                print(player)
    def schedule_match(self, opponent_team, date):
        if any(match["opponent"] == opponent_team.title() and match["date"] == date for match in self.matches):
            print(f"Match against {opponent_team} on {date} is already scheduled.")
            return
        match = {
            "opponent": opponent_team.title(),
            "date": date,
            "result": None
        }
        self.matches.append(match)
        print(f"Match scheduled against {opponent_team} on {date}.")
    def record_match_result(self, opponent_team, result):
        for match in self.matches:
            if match["opponent"] == opponent_team.title() and match["result"] is None:
                match["result"] = result.title()
                print(f"Result recorded for match against {opponent_team}: {result}.")
                return
        print(f"No scheduled match found against {opponent_team} or result already recorded.")
    def display_matches(self):
        if not self.matches:
            print(f"Team {self.team_name} has no scheduled matches.")
        else:
            print(f"Match Schedule for {self.team_name}:")
            for match in self.matches:
                result = match["result"] if match["result"] else "Pending"
                print(f"Opponent: {match['opponent']}, Date: {match['date']}, Result: {result}")
    def calculate_win_loss_ratio(self):
        wins = sum(1 for match in self.matches if match["result"] == "Win")
        losses = sum(1 for match in self.matches if match["result"] == "Loss")
        total = wins + losses
        if total == 0:
            print(f"Team {self.team_name} has not completed any matches.")
            return
        ratio = wins / total
        print(f"Team {self.team_name} Win/Loss Ratio: {wins}/{losses} ({ratio:.2f})")
# Interactive Menu
if __name__ == "__main__":
    team = None
    while True:
        print("\n--- Team Management System ---")
        print("1. Create a Team")
        print("2. Add Player")
        print("3. Remove Player")
        print("4. Display Team")
        print("5. Schedule Match")
        print("6. Record Match Result")
        print("7. Display Matches")
        print("8. Calculate Win/Loss Ratio")
        print("9. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            team_name = input("Enter team name: ")
            try:
                team = Team(team_name)
                print(f"Team '{team_name}' created successfully!")
            except ValueError as e:
                print(e)
        elif choice == "2":
            if team:
                name = input("Enter player name: ")
                age = int(input("Enter player age: "))
                position = input("Enter player position: ")
            else:
                print("Please create a team first.")
        elif choice == "3":
            if team:
                player_name = input("Enter player name to remove: ")
                team.remove_player(player_name)
            else:
                print("Please create a team first.")
        elif choice == "4":
            if team:
                team.display_team()
            else:
                print("Please create a team first.")
        elif choice == "5":
            if team:
                opponent_team = input("Enter opponent team name: ")
                date = input("Enter match date (YYYY-MM-DD): ")
                team.schedule_match(opponent_team, date)
            else:
                print("Please create a team first.")
        elif choice == "6":
            if team:
                opponent_team = input("Enter opponent team name: ")
                result = input("Enter match result (Win/Loss): ")
                team.record_match_result(opponent_team, result)
            else:
                print("Please create a team first.")
        elif choice == "7":
            if team:
                team.display_matches()
            else:
                print("Please create a team first.")
        elif choice == "8":
            if team:
                team.calculate_win_loss_ratio()
            else:
                print("Please create a team first.")
        elif choice == "9":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")