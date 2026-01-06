import random
import json
import os
import art

print(art.logo)

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11
}
STARTING_BALANCE = 100
SAVE_FILE = "players.json"

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

def calculate_hand_value(hand):
    value = sum(card.value for card in hand)
    aces = sum(1 for card in hand if card.rank == 'Ace')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def is_blackjack(hand):
    return len(hand) == 2 and calculate_hand_value(hand) == 21

def display_hand(hand, name, hide_first_card=False):
    print(f"{name}'s hand:")
    for i, card in enumerate(hand):
        if hide_first_card and i == 0:
            print("  Hidden card")
        else:
            print(f"  {card}")
    if not hide_first_card:
        print(f"  Value: {calculate_hand_value(hand)}\n")

def load_players():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_players(players_data):
    with open(SAVE_FILE, "w") as f:
        json.dump(players_data, f, indent=2)

def get_player_bet(name, balance):
    while True:
        try:
            bet = int(input(f"{name}, your balance is ${balance}. Enter your bet: "))
            if 1 <= bet <= balance:
                return bet
            else:
                print(f"Invalid bet. Enter between 1 and {balance}.")
        except ValueError:
            print("Enter a valid number.")

def select_players_for_round(players):
    print("\n--- Select Players for This Round ---")
    active = []

    if players:
        print("Current players:")
        for name in players:
            choice = input(f"Include {name} this round? (y/n): ").strip().lower()
            if choice == 'y':
                active.append(name)

    while True:
        new_name = input("Add a new player (or press Enter to skip): ").strip()
        if not new_name:
            break
        if new_name in players:
            print(f"{new_name} already exists and will be included.")
        else:
            players[new_name] = {"balance": STARTING_BALANCE, "games_played": 0, "wins": 0, "losses": 0}
            print(f"{new_name} added with ${STARTING_BALANCE}")
        active.append(new_name)

    if not active:
        print("No active players selected. Exiting.")
        return None
    return active

def play_blackjack():
    players = load_players()

    while True:
        active_players = select_players_for_round(players)
        if not active_players:
            break

        deck = Deck()
        player_bets = {}
        split_hands = {}
        player_insurance = {}
        player_status = {}
        blackjack_players = {}

        dealer_hand = [deck.deal(), deck.deal()]
        dealer_upcard = dealer_hand[1]

        for player in active_players:
            balance = players[player]["balance"]
            bet = get_player_bet(player, balance)
            players[player]["balance"] -= bet
            player_bets[player] = [bet]
            hand = [deck.deal(), deck.deal()]
            display_hand(hand, player)
            split_hands[player] = [hand]

            if is_blackjack(hand):
                blackjack_players[player] = [True]
            else:
                blackjack_players[player] = [False]

            if hand[0].rank == hand[1].rank and players[player]["balance"] >= bet:
                choice = input(f"{player}, you have a pair. Split? (y/n): ").lower()
                if choice == 'y':
                    players[player]["balance"] -= bet
                    player_bets[player] = [bet, bet]
                    hand1 = [hand[0], deck.deal()]
                    hand2 = [hand[1], deck.deal()]
                    split_hands[player] = [hand1, hand2]
                    blackjack_players[player] = [is_blackjack(hand1), is_blackjack(hand2)]

        print("\nDealer shows:", dealer_upcard)

        if dealer_upcard.rank == 'Ace':
            for player in active_players:
                insurance = player_bets[player][0] // 2
                if players[player]["balance"] >= insurance:
                    choice = input(f"{player}, buy insurance for ${insurance}? (y/n): ").lower()
                    if choice == 'y':
                        players[player]["balance"] -= insurance
                        player_insurance[player] = insurance

        dealer_blackjack = is_blackjack(dealer_hand)
        if dealer_blackjack:
            print("\nDealer has Blackjack!")
            for player, amount in player_insurance.items():
                payout = amount * 2
                players[player]["balance"] += payout
                print(f"{player}'s insurance pays ${payout}.")

            for player in active_players:
                for i, hand in enumerate(split_hands[player]):
                    if blackjack_players[player][i]:
                        print(f"{player}'s Hand {i+1} pushes with dealer. Bet returned.")
                        players[player]["balance"] += player_bets[player][i]
                    else:
                        print(f"{player}'s Hand {i+1} loses.")
                        players[player]["losses"] += 1
                players[player]["games_played"] += len(split_hands[player])
            save_players(players)
            cont = input("Play another round? (y/n): ").lower()
            if cont != 'y':
                print("Thanks for playing!")
                break
            else:
                continue

        for player in active_players:
            player_status[player] = []
            hands = split_hands[player]
            for i, hand in enumerate(hands):
                if blackjack_players[player][i]:
                    print(f"{player}'s Hand {i+1}: Blackjack! 🂡")
                    winnings = int(player_bets[player][i] * 1.5)
                    players[player]["balance"] += player_bets[player][i] + winnings
                    print(f"✅ Paid 3:2. Won ${winnings}.")
                    player_status[player].append("Blackjack")
                    players[player]["wins"] += 1
                    continue
                print(f"\n--- {player}'s Hand {i+1} ---")
                while calculate_hand_value(hand) < 21 and len(hand) < 5:
                    display_hand(hand, f"{player}'s Hand {i+1}")
                    action = input(f"{player}'s Hand {i+1}: [h]it or [s]tand? ").lower()
                    if action == 'h':
                        hand.append(deck.deal())
                        display_hand(hand, f"{player}'s Hand {i+1}")
                        if len(hand) == 5 and calculate_hand_value(hand) <= 21:
                            print("✅ 5 Card Win!")
                            player_status[player].append("5 Card Win")
                            break
                    elif action == 's':
                        break
                    else:
                        print("Invalid input.")
                if len(player_status[player]) <= i:
                    value = calculate_hand_value(hand)
                    if value > 21:
                        print("❌ Busted.")
                        player_status[player].append("Bust")
                    else:
                        player_status[player].append(value)

        print("\n--- Dealer's Turn ---")
        display_hand(dealer_hand, "Dealer")
        while calculate_hand_value(dealer_hand) < 17:
            dealer_hand.append(deck.deal())
            display_hand(dealer_hand, "Dealer")
        dealer_value = calculate_hand_value(dealer_hand)
        print(f"Dealer ends with {dealer_value}")

        for player in active_players:
            hands = split_hands[player]
            results = player_status[player]
            bets = player_bets[player]

            for i, result in enumerate(results):
                print(f"\n{player}'s Hand {i+1}:")
                if result == "5 Card Win":
                    winnings = int(bets[i] * 2.5)
                    players[player]["balance"] += winnings
                    print(f"✅ 5 Card Win! Won ${winnings}.")
                    players[player]["wins"] += 1
                elif result == "Bust":
                    print(f"❌ Busted. Lost ${bets[i]}.")
                    players[player]["losses"] += 1
                elif result == "Blackjack":
                    continue
                else:
                    if dealer_value > 21 or result > dealer_value:
                        players[player]["balance"] += bets[i] * 2
                        print(f"✅ You win ${bets[i]}!")
                        players[player]["wins"] += 1
                    elif result < dealer_value:
                        print(f"❌ Dealer wins. Lost ${bets[i]}.")
                        players[player]["losses"] += 1
                    else:
                        players[player]["balance"] += bets[i]
                        print("⚖️ Tie. Bet returned.")
            players[player]["games_played"] += len(hands)

        print("\n=== Player Stats ===")
        for player in players:
            stats = players[player]
            print(f"{player}: ${stats['balance']} | Games: {stats['games_played']} | Wins: {stats['wins']} | Losses: {stats['losses']}")

        save_players(players)

        cont = input("\nPlay another round? (y/n): ").lower()
        if cont != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_blackjack()
