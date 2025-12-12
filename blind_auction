import art
import sys
import platform
import subprocess


def clear_terminal():
    """Clear terminal screen (works in terminal and IDE)."""
    try:
        if sys.stdout.isatty():
            command = 'cls' if platform.system() == 'Windows' else 'clear'
            subprocess.run(command, shell=True)
        else:
            print("\n" * 150)
    except Exception:
        print("\n" * 150)


def get_bid_input(valid_bidders=None):
    """Prompt user for name and bid, ensuring valid input."""
    while True:
        name = input("What is your name? ").strip()
        if valid_bidders and name not in valid_bidders:
            print("❌ Sorry, you're not part of this round.")
            continue
        break

    while True:
        try:
            bid = float(input("What is your bid? $"))
            if bid < 0:
                raise ValueError
            break
        except ValueError:
            print("❌ Invalid bid. Please enter a positive number.")

    return name, bid


def add_bid(bidding_dict, name, bid):
    """Add or update a bidder in the dictionary."""
    bidding_dict[name] = bid


def get_highest_bidders(bidding_dict):
    """Return all bidders with the highest bid."""
    if not bidding_dict:
        return [], 0.0

    max_bid = max(bidding_dict.values())
    winners = [name for name, bid in bidding_dict.items() if bid == max_bid]
    return winners, max_bid


def run_bidding_round(participants=None):
    """Run one full round of bidding."""
    bids = {}
    continue_bidding = True

    while continue_bidding:
        name, bid = get_bid_input(valid_bidders=participants)
        add_bid(bids, name, bid)

        next_bidder = input("Are there any other bidders? (yes/no): ").strip().lower()
        clear_terminal()

        if next_bidder == "no":
            continue_bidding = False

    return bids


def handle_tie_breaker(existing_bids, tied_bidders):
    """Handle tie-breaker rounds where bidders add to their existing bids."""
    round_number = 1
    current_bidders = tied_bidders
    bids = existing_bids.copy()

    while len(current_bidders) > 1:
        print(f"\n⚔️  Tie-breaker Round {round_number}! Current top bid: ${bids[current_bidders[0]]:.2f}")
        print(f"Bidders: {', '.join(current_bidders)}\n")

        # Each tied bidder adds to their existing bid
        for bidder in current_bidders:
            print(f"👉 {bidder}, your current bid is ${bids[bidder]:.2f}.")
            while True:
                try:
                    add_amount = float(input("How much would you like to add? $"))
                    if add_amount < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("❌ Please enter a valid positive number.")
            bids[bidder] += add_amount
            clear_terminal()

        current_bidders, top_bid = get_highest_bidders(bids)

        if len(current_bidders) == 1:
            winner = current_bidders[0]
            print(f"🏆 {winner} wins the tie-breaker with a total bid of ${top_bid:.2f} 🎉")
            return winner, top_bid

        print("😮 It's still a tie! Let's go another round...")
        round_number += 1
        clear_terminal()

    # Fallback — should never hit if logic above runs
    return current_bidders[0], bids[current_bidders[0]]


def main():
    """Main auction logic."""
    clear_terminal()
    print(art.logo)
    print("🎉 Welcome to the Silent Auction! Place your bids below.\n")

    # === Initial Bidding ===
    bids = run_bidding_round(participants=None)
    winners, top_bid = get_highest_bidders(bids)

    # === Handle Winner or Tie ===
    if len(winners) == 1:
        print(f"🏆 The winner is {winners[0]} with a bid of ${top_bid:.2f} 🎉")
    else:
        print(f"\n🤝 It's a tie! Each of these bidders offered ${top_bid:.2f}:")
        print(", ".join(winners))
        print("\nInitiating a tie-breaker round where bidders add to their existing bids...\n")
        clear_terminal()
        winner, amount = handle_tie_breaker(bids, winners)
        print(f"🏁 Final Winner: {winner} with ${amount:.2f} 🏁")


if __name__ == "__main__":
    main()
