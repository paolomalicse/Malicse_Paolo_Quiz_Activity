class MagicCard:
  
    DEFAULT_SET = "Core Set"
    RARITY_LEVELS = ("Common", "Uncommon", "Rare", "Mythic Rare")

    def __init__(self, card_name, mana_cost, rarity, power=1):
        self.card_name = card_name
        self.mana_cost = mana_cost
        self.rarity = rarity
        self.power = power


card1 = MagicCard("Fire Elemental", "3RR", "Rare", 5)
card2 = MagicCard("Water Sprite", "1U", "Common", 2)

card1.power = 10

print(card1.card_name, "-", card1.mana_cost, "-", card1.rarity, "-", card1.power)
print(card2.card_name, "-", card2.mana_cost, "-", card2.rarity, "-", card2.power)

card2.DEFAULT_SET = "Dominaria Remastered"

print("MagicCard.DEFAULT_SET:", MagicCard.DEFAULT_SET)
print("card1.DEFAULT_SET:", card1.DEFAULT_SET)
print("card2.DEFAULT_SET:", card2.DEFAULT_SET)

# Bonus: additional class attribute related to the actual game
print("Rarity Levels:", MagicCard.RARITY_LEVELS)
