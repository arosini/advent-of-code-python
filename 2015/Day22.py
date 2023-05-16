from util.Util import timeit


class Boss:
    def __init__(self, hp, damage):
        assert hp > 0
        assert damage > 0

        self.hp = hp
        self.damage = damage

    def __copy__(self):
        obj = type(self).__new__(self.__class__)
        obj.hp = self.hp
        obj.damage = self.damage
        return obj

    def __str__(self):
        return f"Boss - HP: {self.hp}, Damage: {self.damage}"

    def __repr__(self):
        return str(self)


class Player:
    def cast(self, spell, target):
        assert self.mana >= spell.mana_cost
        self.mana -= spell.mana_cost

        if spell.effect_duration > 0:
            assert spell not in self.active_spells
            self.active_spells[spell] = spell.effect_duration
            self.armor += spell.armor_while_active
        else:
            target.hp -= spell.damage
            self.hp += spell.heal

    # Right now, this is written to only be able to fight one other character (the boss). Really the damage over time
    # effects should be written onto the target.
    def proc_active_spells(self, target):
        for spell in list(self.active_spells):
            target.hp -= spell.damage
            self.hp += spell.heal
            self.mana += spell.mana_gain

            self.active_spells[spell] -= 1
            if self.active_spells[spell] == 0:
                del self.active_spells[spell]
                self.armor -= spell.armor_while_active

    def __init__(self, hp, mana, armor, spellbook):
        assert hp > 0
        assert mana > 0
        assert armor >= 0
        assert spellbook is not None

        self.hp = hp
        self.mana = mana
        self.armor = armor
        self.spellbook = spellbook
        self.active_spells = {}

    def __copy__(self):
        obj = type(self).__new__(self.__class__)
        obj.hp = self.hp
        obj.mana = self.mana
        obj.armor = self.armor
        obj.spellbook = self.spellbook
        obj.active_spells = {}
        obj.active_spells = self.active_spells.copy()
        return obj

    def __str__(self):
        return f"Character - HP: {self.hp}, Mana: {self.mana}, Spells: {self.active_spells}"

    def __repr__(self):
        return str(self)


class Spell:
    def __init__(self, name, mana_cost, damage, heal, armor_while_active, mana_gain, effect_duration):
        assert name is not None
        assert mana_cost >= 0
        assert damage >= 0
        assert heal >= 0
        assert armor_while_active >= 0
        assert mana_gain >= 0
        assert effect_duration >= 0

        self.name = name
        self.mana_cost = mana_cost
        self.damage = damage
        self.heal = heal
        self.armor_while_active = armor_while_active
        self.mana_gain = mana_gain
        self.effect_duration = effect_duration

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return str(self)


def get_mana_spent_in_win(spells_cast):
    global global_least_mana_spend, global_spells_cast

    mana_spend = sum(spell.mana_cost for spell in spells_cast)
    if global_least_mana_spend is None or (global_least_mana_spend > mana_spend):
        global_least_mana_spend = mana_spend
        global_spells_cast = spells_cast.copy()
    return mana_spend


def spent_too_much_mana(spells_cast):
    global global_least_mana_spend
    if global_least_mana_spend is None: return False
    return sum(spell.mana_cost for spell in spells_cast) >= global_least_mana_spend


def dfs_least_mana_spend(player, boss, spells_cast, turn, part_1):
    if spent_too_much_mana(spells_cast): return None

    # Apply part 2 effect.
    if not part_1:
        player.hp -= 1
        if player.hp <= 0: return None

    # Apply spell effects.
    player.proc_active_spells(boss)
    if boss.hp <= 0: return get_mana_spent_in_win(spells_cast)

    # Player turn.
    if turn % 2 != 0:
        least_mana_spend = None

        for spell in player.spellbook:
            if spell.mana_cost > player.mana: continue
            if spell in player.active_spells: continue

            player_copy = player.__copy__()
            boss_copy = boss.__copy__()
            spells_cast_copy = spells_cast.copy()
            spells_cast_copy.append(spell)

            player_copy.cast(spell, boss_copy)
            if boss_copy.hp <= 0: return get_mana_spent_in_win(spells_cast_copy)

            result = dfs_least_mana_spend(player_copy, boss_copy, spells_cast_copy, turn + 1, part_1)
            if least_mana_spend is None or (result is not None and result < least_mana_spend): least_mana_spend = result

        return least_mana_spend

    # Boss turn.
    else:
        player.hp -= (boss.damage - player.armor)
        if player.hp <= 0: return None
        return dfs_least_mana_spend(player, boss, spells_cast, turn + 1, part_1)


def run(part_1):
    hp = 50
    mana = 500
    armor = 0
    spellbook = [
        Spell("Magic Missile", 53, 4, 0, 0, 0, 0),
        Spell("Drain", 73, 2, 2, 0, 0, 0),
        Spell("Shield", 113, 0, 0, 7, 0, 6),
        Spell("Poison", 173, 3, 0, 0, 0, 6),
        Spell("Recharge", 229, 0, 0, 0, 101, 5)
    ]

    boss_stats = []
    with open("input/Day22.txt") as file:
        lines = file.readlines()
        for line in lines: boss_stats.append(int(line.strip().split(":")[1]))

    player = Player(hp, mana, armor, spellbook)
    boss = Boss(*boss_stats)

    print(dfs_least_mana_spend(player, boss, list(), 1, part_1))


global_least_mana_spend = None
global_spells_cast = None


@timeit
def part1():
    global global_least_mana_spend, global_spells_cast
    global_least_mana_spend = None
    run(True)
    print(global_spells_cast)


@timeit
def part2():
    global global_least_mana_spend
    global_least_mana_spend = None
    run(False)


part1()
print()
part2()
