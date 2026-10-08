# Blackjack Simulator (`Blackjack_simulator.py`)

---

## Overview

This repository contains an interactive command-line Blackjack game implemented in Python. The program simulates classic single-player Blackjack gameplay against an automated dealer using object-oriented principles to manage card decks, player hands, and scoring logic.

---

## Key Features & Rules

1. **Object-Oriented Architecture**
   * `Card`: Represents individual playing cards with suits and ranks.
   * `CardCollection`: Handles deck generation, card shuffling, drawing mechanics, and hand value calculations.

2. **Special Game Rules & Win Conditions**
   * **Dynamic Ace Calculation:** Aces dynamically count as 11 or 1 depending on whether the hand total exceeds 21.
   * **5-Card Charlie:** Automatically win the round upon successfully drawing 5 cards without busting.
   * **Dealer Logic:** The dealer automatically hits until reaching a minimum hand total of 17.

---

## How to Run

Execute the script directly from your terminal using Python 3:

```bash
python Blackjack_simulator.py
