logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


# Mapping rank and suit symbols for display
rank_display = {
    '2': '2', '3': '3', '4': '4', '5': '5',
    '6': '6', '7': '7', '8': '8', '9': '9',
    '10': '10', 'Jack': 'J', 'Queen': 'Q',
    'King': 'K', 'Ace': 'A'
}

suit_display = {
    'Hearts': '♥',
    'Diamonds': '♦',
    'Clubs': '♣',
    'Spades': '♠'
}

def card_art(rank, suit):
    """Return a list of strings that visually represent the card."""
    r = rank_display[rank]
    s = suit_display[suit]
    spacing = ' ' if len(r) == 1 else ''
    return [
        "┌─────────┐",
        f"│{s}{spacing}       │",
        "│         │",
        f"│    {r}    │",
        "│         │",
        f"│       {spacing}{s}│",
        "└─────────┘"
    ]

def hidden_card_art():
    """Return a list of strings representing a face-down card."""
    return [
        "┌─────────┐",
        "│░░░░░░░░░│",
        "│░░░░░░░░░│",
        "│░░░░░░░░░│",
        "│░░░░░░░░░│",
        "│░░░░░░░░░│",
        "└─────────┘"
    ]
