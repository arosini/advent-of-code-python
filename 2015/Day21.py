from util.Util import timeit
from enum import Enum
import itertools
import math


class Boss:
    def __init__(self, hp, damage, armor,):
        assert hp > 0
        assert damage > 0
        assert armor >= 0

        self.hp = hp
        self.damage = damage
        self.armor = armor

    def __str__(self):
        return f"Boss - HP: {self.hp}, Damage: {self.damage}, Armor: {self.armor}"

    def __repr__(self):
        return str(self)


class Character:
    def __init__(self, hp, weapon, armor, rings):
        assert hp > 0
        assert weapon.type == Item.Type.WEAPON
        assert armor is None or armor.type == Item.Type.ARMOR
        assert all(ring.type == Item.Type.RING for ring in rings)
        assert rings is not None
        assert len(rings) <= 2

        self.hp = hp
        self.weapon = weapon
        self.armor = armor
        self.rings = rings
        self.damage = weapon.damage + (armor.damage if armor else 0) + sum(ring.damage for ring in rings)
        self.armor = weapon.armor + (armor.armor if armor else 0) + sum(ring.armor for ring in rings)

    def __str__(self):
        return f"Character - HP: {self.hp}, Damage: {self.damage}, Armor: {self.armor}"

    def __repr__(self):
        return str(self)


class Item:
    class Type(Enum):
        WEAPON = "Weapon"
        ARMOR = "Armor"
        RING = "Ring"

    def __init__(self, item_type, name, cost, damage, armor):
        assert item_type is not None
        assert name is not None
        assert cost >= 0
        assert damage >= 0
        assert armor >= 0

        self.type = item_type
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor

    def __str__(self):
        return f"{self.type} {self.name} - Cost: {self.cost}, Damage: {self.damage}, Armor: {self.armor}"

    def __repr__(self):
        return str(self)


def character_wins_vs_boss(character, boss):
    boss_rounds = math.ceil(boss.hp / max(1, character.damage - boss.armor))
    character_rounds = math.ceil(character.hp / max(1, boss.damage - character.armor))
    return character_rounds >= boss_rounds


def find_gold_spent(part_1):
    hp = 100
    boss_stats = []
    items = {Item.Type.WEAPON: [], Item.Type.ARMOR: [], Item.Type.RING: []}

    with open("input/Day21.txt") as file:
        lines = file.readlines()
        current_item_type = None
        for line in lines:
            line = line.strip()
            if len(boss_stats) < 3:
                boss_stats.append(int(line.split(":")[1]))
            elif line == "":
                continue
            elif line.startswith("Weapons:"):
                current_item_type = Item.Type.WEAPON
            elif line.startswith("Armor:"):
                current_item_type = Item.Type.ARMOR
            elif line.startswith("Rings:"):
                current_item_type = Item.Type.RING
            else:
                item_info = line.split()
                items[current_item_type].append(Item(current_item_type, item_info[0],
                                                     int(item_info[1]), int(item_info[2]), int(item_info[3])))

    # Armor is optional
    items[Item.Type.ARMOR].append(None)

    # Anywhere from 0 to 2 rings can be used.
    ring_sets = list(itertools.combinations(items[Item.Type.RING], 1))
    ring_sets += list(itertools.combinations(items[Item.Type.RING], 2))
    ring_sets += ()

    gold = None

    for weapon in items[Item.Type.WEAPON]:
        for armor in items[Item.Type.ARMOR]:
            for ring_set in ring_sets:
                character_wins = character_wins_vs_boss(Character(hp, weapon, armor, ring_set), Boss(*boss_stats))
                cost = weapon.cost + (armor.cost if armor else 0) + sum(ring.cost for ring in ring_set)

                if part_1 and character_wins:
                     if gold is None or cost < gold: gold = cost

                if not part_1 and not character_wins:
                    if gold is None or cost> gold: gold = cost

    print(gold)


@timeit
def part1():
    find_gold_spent(True)


@timeit
def part2():
    find_gold_spent(False)


part1()
print()
part2()

