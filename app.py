import constants


if __name__ == "__main__":
    pass

#  Define my app.py namespace constants variables

PLAYERS = []
TEAMS = []

# Read from constants.py data (PLAYERS and TEAMS)

# Build the PLAYERS data collection (a list of dictionaries)

for player in constants.PLAYERS:
    PLAYERS.append(player)

# Build the TEAMS data collection (a list of string)

for team in constants.TEAMS:
    TEAMS.append(team)




