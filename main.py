import random
import json


with open("mind.json", "r") as f:
    cups = json.loads(f.read())

stone = 10
picks = {}

def ai_turn():
    pick = cups[f"{stone}"][random.randint(0, len(cups[f"{stone}"]) - 1)]
    print(f"Ai takes {pick} stones")
    return pick


def your_turn():
    pick = int(input("You take 1-3 stones: "))
    return pick

def check_win(turn):
    if stone <= 1 and turn == "ai":
        print("AI Learns...")
        learn()
        quit()
    elif stone <= 1:
        print("AI Wins!")
        quit()
    else:
        pass

def learn():
    if len(cups[str(list(picks.keys())[-1])]) > 1:
        cups[str(list(picks.keys())[-1])].remove(list(picks.values())[-1])
    json_string = json.dumps(cups, indent=4)
    with open("mind.json", "w") as f:
        f.write(json_string)

while True:
    pick = ai_turn()
    picks[stone] = pick
    stone -= pick
    print("  .  " * (10 - stone) + "  #  " * stone)
    check_win("player")

    stone -= your_turn()
    print("  .  " * (10 - stone) + "  #  " * stone)
    check_win("ai")
