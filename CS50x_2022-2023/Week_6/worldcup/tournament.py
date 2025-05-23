# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []

    # Read the csv file as a dictionary, get teams and ratings, and append the teams list
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['rating'] = int(row['rating'])
            teams.append(row)
            # print(row)

    counts = {}

    # for N times
    for i in range(N):
        # Simulate a tournament including teams list, and get the winner
        winning_team = simulate_tournament(teams)
        # If the winning team is in the counts list, add 1 to its counter
        if winning_team in counts:
            counts[winning_team] += 1
        # Else, create a counter = 1
        else:
            counts[winning_team] = 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""

    # While the returning teams list from the sim_round function is greater than 1, simulate rounds
    while len(teams) > 1:
        teams = simulate_round(teams)

    # When the while condition ends, return the remaining team's name from the function
    return teams[0]['team']


if __name__ == "__main__":
    main()
