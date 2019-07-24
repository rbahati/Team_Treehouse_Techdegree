"""
Python Web Development Techdegree
Project 2 - Basketball Team Stats Tool
AUTHOR: RAISS BAHATI
--------------------------------
"""
import constants
import sys

team_names = constants.TEAMS
team_players = constants.PLAYERS


# Additional balancing to the team
# Include additional stats for a given displayed team:

def clean_data():

    #  Cleaning up the experience key values from team_players

    for item in range(len(team_players)):
        if team_players[item]["experience"] == "YES":
            team_players[item]["experience"] = True
        elif team_players[item]["experience"] == "NO":
            team_players[item]["experience"] = False

    # Cleaning up the height key values from team_players

    for item in range(len(team_players)):
        if "inches" in team_players[item]["height"]:
            team_players[item]["height"] = int(team_players[item]["height"].replace("inches", "").strip())

    # Cleaning up the guardian field

    for item in range(len(team_players)):
        if team_players[item]["guardians"]:
            team_players[item]["guardians"].split("and")

    return team_players


def balance_total_players(formatted_players_data):
    team_balance = len(team_players) // len(team_names)
    balanced_teams = dict()
    # Balancing the players across teams equally (6 players per team)
    for team in team_names:
        for step in range(len(formatted_players_data)):
            if team == "Panthers":
                balanced_teams[team] = formatted_players_data[:team_balance]
            elif team == "Bandits":
                balanced_teams[team] = formatted_players_data[team_balance:team_balance*2]
            elif team == "Warriors":
                balanced_teams[team] = formatted_players_data[team_balance*2:team_balance*3]

    # Balancing the experienced vs the inexperienced players evenly across the teams

    return balanced_teams


def display_main_menu(formatted_teams_data):
    while True:
        print("BASKETBALL TEAM STATS TOOL\n\n")
        print("---- MENU----\n\n")
        print("Here are your choices:\n")
        print("\t 1) Display Team Stats\n")
        print("\t 2) Quit\n\n")
        main_options = int(input("Enter an option > ").strip())  # Put a try catch here later
        if main_options == 1:
            display_teams(formatted_teams_data)
            print("\n")
            input("Press ENTER to continue...")
            continue

        elif main_options == 2:
            break

    print("Thank you for using the Basketball Team Stats Tool!\nSee you soon :)")
    sys.exit(0)


def display_teams(team_data):
    number = 1
    print("\n")
    for team in team_data.keys():
        if number <= len(team_data.keys()):
            print(str(number)+") " + team + "\n")
            number += 1
    team_options = int(input("Enter an option > ").strip())
    if team_options == 1:
        display_panthers_stats(team_data)
    elif team_options == 2:
        display_bandits_stats(team_data)
    elif team_options == 3:
        display_warriors_stats(team_data)


def display_panthers_stats(global_stat_data):
    print("\n")
    print("Team: Panthers Stats")
    print("--------------------")
    print("Total players:", len(global_stat_data["Panthers"]))
    print("\n")
    print("Players on Team:")
    print("\t", end="")
    for team_player in global_stat_data["Panthers"]:
        if team_player["name"] == "Joe Kavalier":
            team_player["name"] = "Joe Kavalier."
            print(team_player["name"])
            break
        print(team_player["name"] + ", ", end="")


def display_bandits_stats(global_stat_data):
    print("\n")
    print("Team: Bandits Stats")
    print("--------------------")
    print("Total players:", len(global_stat_data["Bandits"]))
    print("\n")
    print("Players on Team:")
    print("\t", end="")
    for team_player in global_stat_data["Bandits"]:
        if team_player["name"] == "Arnold Willis":
            team_player["name"] = "Arnold Willis."
            print(team_player["name"])
            break
        print(team_player["name"] + ", ", end="")


def display_warriors_stats(global_stat_data):
    print("\n")
    print("Team: Warriors Stats")
    print("--------------------")
    print("Total players:", len(global_stat_data["Warriors"]))
    print("\n")
    print("Players on Team:")
    print("\t", end="")
    for team_player in global_stat_data["Warriors"]:
        if team_player["name"] == "Kimmy Stein":
            team_player["name"] = "Kimmy Stein."
            print(team_player["name"])
            break
        print(team_player["name"] + ", ", end="")


def start_app():
    formatted_players = clean_data()  # We first clean the data that we imported from constants.py
    formatted_teams = balance_total_players(formatted_players)  # We format the team data
    display_main_menu(formatted_teams)  # We use that in the rest of our program


if __name__ == "__main__":
    start_app()
