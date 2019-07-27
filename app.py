"""
Python Web Development Techdegree
Project 2 - Basketball Team Stats Tool
AUTHOR: RAISS BAHATI
--------------------------------
"""
import constants
import sys
import copy

team_names = copy.deepcopy(constants.TEAMS)
team_players = copy.deepcopy(constants.PLAYERS)


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
    new_balanced_teams_experience = list()
    new_balanced_teams_inexperience = list()
    new_balanced_teams_data_structure = dict()
    new_panthers_players = list()
    new_bandits_players = list()
    new_warriors_players = list()

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

    for player in formatted_players_data:
        if player["experience"]:
            new_balanced_teams_experience.append(player)
        else:
            new_balanced_teams_inexperience.append(player)

    for player in team_names:
        if player == "Panthers":
            new_panthers_players.extend(new_balanced_teams_experience[0:3])
            new_panthers_players.extend(new_balanced_teams_inexperience[0:3])
        elif player == "Bandits":
            new_bandits_players.extend(new_balanced_teams_experience[3:6])
            new_bandits_players.extend(new_balanced_teams_inexperience[3:6])
        elif player == "Warriors":
            new_warriors_players.extend(new_balanced_teams_experience[6:])
            new_warriors_players.extend(new_balanced_teams_inexperience[6:])

    # Adding players into a new data structure

    for team in team_names:
        if team == "Panthers":
            new_balanced_teams_data_structure[team] = new_panthers_players
        elif team == "Bandits":
            new_balanced_teams_data_structure[team] = new_bandits_players
        elif team == "Warriors":
            new_balanced_teams_data_structure[team] = new_warriors_players

    return new_balanced_teams_data_structure


def display_main_menu(formatted_teams_data):
    """This is the main menu function"""
    while True:
        print("BASKETBALL TEAM STATS TOOL\n\n")
        print("---- MENU----\n\n")
        print("Here are your choices:\n")
        print("\t 1) Display Team Stats\n")
        print("\t 2) Quit\n\n")
        main_options = (input("Enter an option > ").strip())
        if main_options == "1":
            display_teams(formatted_teams_data)
            print("\n")
            input("Press ENTER to continue...")
            continue

        elif main_options == "2":
            break

    print("Thank you for using the Basketball Team Stats Tool!\nSee you soon :)")
    sys.exit(0)


def display_teams(team_data):
    """This is the display teams submenu" function"""
    number = 1
    print("\n")
    for team in team_data.keys():
        if number <= len(team_data.keys()):
            print(str(number)+") " + team + "\n")
            number += 1
    team_options = (input("Enter an option > ").strip())
    if team_options == "1":
        display_panthers_stats(team_data)
    elif team_options == "2":
        display_bandits_stats(team_data)
    elif team_options == "3":
        display_warriors_stats(team_data)


def display_panthers_stats(global_stat_data):
    """This is the function that displays stats for Panthers team"""
    sum_height = list()
    average = int()
    guardian_list = list()

    print("\n")
    print("Team: Panthers Stats")
    print("--------------------")
    print("Total players:", len(global_stat_data["Panthers"]))
    print("\n")
    print("Players on Team:")
    print("\t", end="")
    for team_player in global_stat_data["Panthers"]:
        if team_player["name"] == "Chloe Alaska":
            team_player["name"] = "Chloe Alaska."
            print(team_player["name"])
            break
        print(team_player["name"] + ", ", end="")
    print("\n")
    print("Player with experience:")
    for team_player in global_stat_data["Panthers"][0:3]:
        if team_player["name"] == "Phillip Helm":
            team_player["name"] = "Phillip Helm."
            print(team_player["name"])
            break

        print(team_player["name"] + ", ", end="")
    print("\n")
    print("Player with no experience:")
    for team_player in global_stat_data["Panthers"][3:]:
        if team_player["name"] == "Chloe Alaska":
            team_player["name"] = "Chloe Alaska."
            print(team_player["name"])
            break

        print(team_player["name"] + ", ", end="")
    print("\n")

    for team_player in global_stat_data["Panthers"][:]:
        sum_height.append(team_player["height"])
    average = sum(sum_height) // len(global_stat_data["Panthers"])
    print("The average height of the team is:", average, "inches")
    print("\n")

    for team_player in global_stat_data["Panthers"][:]:
        guardian_list.append(team_player["guardians"][:])
    print("The guardians of the team are:", ", ".join(guardian_list))


def display_bandits_stats(global_stat_data):
    """This is the function that displays stats for Bandits team"""
    sum_height = list()
    average = int()
    guardian_list = list()

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
    print("\n")
    print("Player with experience:")
    for team_player in global_stat_data["Bandits"][0:3]:
        if team_player["name"] == "Jill Tanner":
            team_player["name"] = "Jill Tanner."
            print(team_player["name"])
            break

        print(team_player["name"] + ", ", end="")

    print("\n")

    print("Player with no experience:")
    for team_player in global_stat_data["Bandits"][3:]:
        if team_player["name"] == "Arnold Willis":
            team_player["name"] = "Arnold Willis."
            print(team_player["name"])
            break

        print(team_player["name"] + ", ", end="")
    print("\n")
    for team_player in global_stat_data["Bandits"][:]:
        sum_height.append(team_player["height"])
    average = sum(sum_height) // len(global_stat_data["Bandits"])
    print("The average height of the team is:", average, "inches")
    print("\n")
    for team_player in global_stat_data["Bandits"][:]:
        guardian_list.append(team_player["guardians"][:])
    print("The guardians of the team are:", ", ".join(guardian_list))


def display_warriors_stats(global_stat_data):
    """This is the function that displays stats for Warriors team"""
    sum_height = list()
    average = int()
    guardian_list = list()

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
    print("\n")
    print("Player with experience:")
    for team_player in global_stat_data["Warriors"][0:3]:
        if team_player["name"] == "Diego Soto":
            team_player["name"] = "Diego Soto."
            print(team_player["name"])
            break

        print(team_player["name"] + ", ", end="")
    print("\n")
    print("Player with no experience:")
    for team_player in global_stat_data["Warriors"][3:]:
        if team_player["name"] == "Kimmy Stein":
            team_player["name"] = "Kimmy Stein."
            print(team_player["name"])
            break

        print(team_player["name"] + ", ", end="")
    print("\n")
    for team_player in global_stat_data["Warriors"][:]:
        sum_height.append(team_player["height"])
    average = sum(sum_height) // len(global_stat_data["Warriors"])
    print("The average height of the team is:", average, "inches")
    print("\n")
    for team_player in global_stat_data["Warriors"][:]:
        guardian_list.append(team_player["guardians"][:])
    print("The guardians of the team are:", ", ".join(guardian_list))


def start_app():
    """This is the main function call"""
    formatted_players = clean_data()
    formatted_teams = balance_total_players(formatted_players)
    display_main_menu(formatted_teams)


if __name__ == "__main__":
    start_app()  # Runs the entire program
