import copy
import math
from typing import Optional, Dict

AVERAGE_ELO = float(0.00)
DEFAULT_GAIN = 25
distribution_example = []
ELO_HELL = 1


class Player:
    def __init__(self, name: str, elo: Optional[float] = 1200.00):
        self.name = name
        self.elo = elo if elo is not None else 1200
        self.expectation = None

    def __str__(self) -> str:
        return (
            f"{self.name} : {self.elo} "
            f"| expectation: {'win' if self.expectation else 'lose'}"
        )


def game(lobby: list[Player]) -> float:
    avg_elo = sum(
        [
            player.elo for player in lobby
        ]
    ) / len(lobby)
    for player in lobby:
        if player.elo < avg_elo:
            player.expectation = False
        else:
            player.expectation = True
        print(player)
    return avg_elo


def elo_change(average_elo: float, result: Dict[Player, int]) -> None:
    global DEFAULT_GAIN
    global distribution_example
    elo_primary_distribution = []
    print("\n", "*" * 10, "GG", "*" * 10, "\n")
    print(f"\nAverage ELO: {AVERAGE_ELO}\n")
    for i in range(int(len(result) / 2)):
        elo_primary_distribution.append(
            DEFAULT_GAIN
        )
        DEFAULT_GAIN /= 2
    part_reverse = copy.deepcopy(elo_primary_distribution)[::-1]

    if not len(result) % 2 == 0:
        elo_primary_distribution.append(int(1))

    for i in part_reverse:
        elo_primary_distribution.append(-i)

    sorted_players = sorted(result.keys(), key=lambda x: result[x])
    distribution_example = copy.deepcopy(elo_primary_distribution)
    index_ = 0
    for player in sorted_players:
        old_elo = player.elo
        mult = player.elo / AVERAGE_ELO
        if mult < 1:
            mult = 2 - mult

        points = distribution_example[index_] * mult
        if not player.expectation and points > 0:
            points *= 1 * ELO_HELL

        player.elo += points
        index_ += 1
        print(f"{player.name}: {old_elo} -> {round(player.elo, 2)}"
              f" {'[+' if points > 0 else '['}{round(points, 2)}]")


player_1 = Player("Sanya", elo=None)
player_2 = Player("Ed, prosto Ed", elo=1300)
player_3 = Player("Kolya BARBARIAN", elo=1350)
player_4 = Player("Naebwuk Church", elo=1370)
player_5 = Player("Nuclear Gandhi", elo=1570)

players = [
    player_1,
    player_2,
    player_3,
    player_4,
    # player_5
]

game_result = {
    player_1: 1,
    player_2: 2,
    player_3: 3,
    player_4: 4,
    # player_5: 5
}

AVERAGE_ELO = game(players)
elo_change(AVERAGE_ELO, game_result)
print("___________")
print(distribution_example)
