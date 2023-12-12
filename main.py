import random

# List of Pokémon
pokemon_list = [
    "Bulbasaur", "Charmander", "Squirtle", "Pikachu", "Eevee",
    "Jigglypuff", "Snorlax", "Mewtwo", "Gengar", "Dragonite",
    "Vaporeon", "Espeon", "Umbreon", "Raichu", "Mew",
    "Lapras", "Gyarados", "Magikarp", "Zubat", "Ditto"
]

# List of cards that modify the gameplay
cards = [
    "Lucky Egg - Double your next Pokémon spin!",
    "Master Ball - Choose any Pokémon you want!",
    "Repel - Skip your next spin and keep your Pokémon from previous round.",
    "Potion - If your opponent gets a weak Pokémon, they must spin again!"
]

def spin_roulette():
    print("\nPress Enter to spin the roulette...")
    input()
    
    # Randomly select a Pokémon from the list
    selected_pokemon = random.choice(pokemon_list)
    
    print(f"You've got: {selected_pokemon}!")
    return selected_pokemon

def get_random_card():
    return random.choice(cards)

# Function to check if the player wants to play again
def ask_play_again():
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    return play_again == "yes"

# Main game loop
play_game = True

while play_game:
    # Game loop for two players to get 4 Pokémon each
    player_pokemon = []
    for i in range(2):  # Two players
        print(f"\nPlayer {i+1}, it's your turn.")
        pokemon_count = 0
        
        while pokemon_count < 4:
            selected_pokemon = spin_roulette()
            player_pokemon.append(selected_pokemon)
            pokemon_count += 1
        
        print(f"\nPlayer {i+1}, your Pokémon:")
        print(', '.join(player_pokemon[i*4:i*4+4]))
    
    # Card usage phase
    for i in range(2):
        random_card = get_random_card()
        print(f"\nPlayer {i+1}, your random card: {random_card}")
        
        use_card_option = input(f"Player {i+1}, do you want to use the card to affect the opponent's next spin? (yes/no): ").lower()
        if use_card_option == "yes":
            if "Potion" in random_card:  # Opponent must spin again if they get a weak Pokémon
                print(f"Player {i+2 if i==0 else 1}, you must spin again if you get a weak Pokémon on your next turn!")
            elif "Repel" in random_card:  # Opponent skips their next spin
                print(f"Player {i+2 if i==0 else 1}, your next spin is skipped.")
            elif "Lucky Egg" in random_card:  # Double the next spin
                print(f"Player {i+2 if i==0 else 1}, your next Pokémon spin will be doubled!")
            elif "Master Ball" in random_card:  # Choose any Pokémon
                chosen_pokemon = input(f"Player {i+1}, you have the Master Ball! Choose any Pokémon from the list: ")
                print(f"Player {i+1}, you've got: {chosen_pokemon}!")
    
    play_game = ask_play_again()

print("\nThanks for playing Pokémon Roulette! See you next time.")