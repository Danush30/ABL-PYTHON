def hackathon_team_ranking():
    teams = [
        ("Team A", 85, 90, 80, 4),
        ("Team B", 90, 85, 85, 3),
        ("Team C", 85, 90, 80, 4),
        ("Team D", 70, 75, 80, 5),
        ("Team E", 95, 88, 92, 2)
    ]

    valid_teams = []

    for name, round1, round2, round3, size in teams:
        total = round1 + round2 + round3

        print(f"\n{name}: Team size = {size}, Total = {total}")

        if 3 <= size <= 5:
            valid_teams.append((name, total, round1, size))
            print("Team size: Valid")
        else:
            print("Team size: Invalid")

    # Tie-break: higher Round 1 score, then smaller team name alphabetically
    valid_teams.sort(key=lambda x: (-x[1], -x[2], x[0]))

    print("\nFinal Ranking:")
    for rank, (name, total, round1, size) in enumerate(valid_teams, 1):
        print(f"{rank}. {name} - {total} points")


if __name__ == "__main__":
    hackathon_team_ranking()
    