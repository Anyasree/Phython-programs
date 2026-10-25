class Cricket:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score
    def info(self):
        print(f"Cricket - Player: {self. player}, Score: {self.__score}")
    def play(self):
        print(f"{self.__player} hits a six!")
    def get_score(self):
        return self.__score
    def set__score(self, new_score)
        if new_score >= 0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score cannot be negative.")
class Football:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score
    def info(self):
        print(f"Football - Player: {self. player}, Score: {self.__score}")
    def play(self):
        print(f"{self.__player} scores a goal!")
    def get_score(self):
        return self.__score
    
    def set__score(self, new_score)
        if new_score >= 0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score cannot be negative.")
cricket = Cricket("Rohit", 85)
football = Football("Arjun", 2)
print("=== Sports Scoreboard ===\n")
for sport in (cricket, football):
    sport.info()
    sport.play()
    print()
print("--- Direct change attempt ---")
cricket.__score = 999
print(f"get.score()still shows: {cricket.get_score()}")
print("\n--- Updating scores ---")
cricket.set_score(100)
football.set_score(3)
