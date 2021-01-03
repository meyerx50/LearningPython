import random
import statistics
### Global Variables ###
# Names the weapon types available in the game
weapon_type = ['Fist', 'Paw', 'Axe', 'Sword', 'Shield', 'Wand']
# Names all magic spells types in game
magic_type = ['Cure', 'Attack', 'Defense']

### Classes ###
class Spell:

    def __init__(self):
        self.data = []
        self.name = "Undefined"
        self.description = "Undefined"
        # What kind of spell is it?
        self.type = 0
        self.type_description = magic_type[self.type]
        # What is the minimum magic skill to use it?
        self.required_magic_skill = 0.0
        # How powerful is the spell?
        self.spell_power = 0.0
        # What is the base to calculate the spell outcome
        self.point_base = 0
        # How many mana points to use it?
        self.mana_cost = 0

    # All spells are a mean of the spell power and the player magic level
    def attack_damage(self, magic_level):
        damage_power = self.point_base * self.spell_power
        damage_skill = self.point_base * magic_level
        balanced_damage = statistics.mean([damage_skill, damage_power])
        return round(balanced_damage)

    def defense_block(self, magic_level):
        blocked_power = self.point_base * self.spell_power
        blocked_skill = self.point_base * magic_level
        balanced_blocked = statistics.mean([blocked_power, blocked_skill])
        return round(balanced_blocked)

    def cure(self, magic_level):
        cure_power = self.point_base * self.spell_power
        cure_skill = self.point_base * magic_level
        balanced_cure = statistics.mean([cure_power, cure_skill])
        return round(balanced_cure)

class Rune(Spell):
    def __init__(self):
        self.charges = 0

class Weapon:

    def __init__(self):
        self.data = []
        self.name = "Undefined"
        # Maximum damage delivered by the weapon considering the player skill 1.0
        self.damage = 0
        # Maximum protection delivered by the weapon considering the player skill 1.0
        self.protection = 0
        self.type = weapon_type[0]


class Creature:

    def __init__(self):
        # Basics
        self.data = []
        self.name = "Undefined"
        self.can_attack = False
        self.can_defend = False
        # Life
        self.life_points_max = 0
        self.life_points_current = 0
        # Magic
        self.mana_points_max = 0
        self.mana_points_current = 0
        self.magic_skill_set = []
        # > How good the player can use magic skills (e.g. Cure)
        self.magic_level = 0.0
        # Weapons
        self.left_hand = ""
        self.right_hand = ""
        # > How good the player can handle weapons. Increases attack and defense
        self.weapon_skills = 0.0


    # Calculates a random damage value a player can delivered based on weapons and skills
    def attack_damage(self):
        # Sum all weapons attack points and multiply by the skill factor
        total_attack = round((self.right_hand.damage + self.left_hand.damage) * self.weapon_skills)
        damage = random.randint(1, total_attack)
        return damage

    # Calculates a random block value a player can reduce from an attack based on weapons and skills
    def defense_block(self):
        # Sum all weapons defense points and multiply by the skill factor
        total_defense = round((self.right_hand.protection + self.left_hand.protection) * self.weapon_skills)
        block = random.randint(1, total_defense)
        return block

    # Delivers damage to a victim
    def engage(self, victim, damage):
        # Is the attacker alive?
        if self.alive() and self.can_attack:
            # Is the victim alive?
            if victim.alive():
                if damage >= 0:
                    result = damage
                else:
                    result = self.attack_damage()
                # Result can be minimized if the victim is able to defend him/herself
                if victim.can_defend:
                    result -= victim.defense_block()
                # Any harm?
                if (result > 0):
                    victim.life_points_current -= result
                    print(f'{victim.name} suffered an attack from {self.name} with damage'
                          f' of {result} hit points and has now {victim.life_points_current} life points.')
                    if victim.alive() == False:
                        print(f'{victim.name} is now dead')
                else:
                    print(f'{self.name} successfully blocked an attack from {victim.name}.')

    # Is the player still alive?
    def alive(self):
        if self.life_points_current > 0:
            return True
        else:
            return False

    # Does the play have enough mana?
    def enough_mana(self):
        if self.mana_points_current >= self.mana_for_cure:
            return True
        else:
            return False

    # Can the play cast this spell?
    def can_cast(self, spell):
        if self.magic_level >= spell.required_magic_skill:
            if self.mana_points_current >= spell.mana_cost:
                return True
            else:
                return False
        else:
            return False

    # Cast a magic spell
    def use_magic(self, spell, victim):
        if self.can_cast(spell):
            # Cure spells
            if spell.type == 0:
                cure = spell.cure(self.magic_level)
                if self.life_points_current + cure > self.life_points_max:
                    self.life_points_current = self.life_points_max
                else:
                    self.life_points_current += cure
                self.mana_points_current -= spell.mana_cost
                print(f'{self.name} has cured {cure} life points and has now {self.life_points_current}')
            # Attack spells
            elif spell.type == 1:
                damage = spell.attack_damage(self.magic_level)
                self.engage(victim, damage)
        else:
            print(f'{self.name} cannot cast the spell {spell.name}.')

### Game ###
# Creating game objects

# Creating magic spells
spl_cure = Spell()
spl_cure.name = "Light Cure"
spl_cure.description = "Restores a small amount of life points"
spl_cure.type = 0
spl_cure.required_magic_skill = 0.1
spl_cure.spell_power = 1.2
spl_cure.point_base = 10
spl_cure.mana_cost = 5

spl_death = Spell()
spl_death.name = "Sudden Death"
spl_death.description = "Delivers a huge amount of damage to the opponent"
spl_death.type = 1
spl_death.required_magic_skill = 3.0
spl_death.spell_power = 1.9
spl_death.point_base = 20
spl_death.mana_cost = 25

# Creating weapons
fst_bare = Weapon()
fst_bare.name = "Bare Fist"
fst_bare.type = weapon_type[0]
fst_bare.damage = 2
fst_bare.protection = 1

swd_justice = Weapon()
swd_justice.name = "Great Sword of Justice"
swd_justice.type = weapon_type[3]
swd_justice.damage = 18
swd_justice.protection = 2

shd_guardian = Weapon()
shd_guardian.name = "Guardian Shield"
shd_guardian.type = weapon_type[4]
shd_guardian.damage = 1
shd_guardian.protection = 15

shd_demon = Weapon()
shd_demon.name = "Demon Shield"
shd_demon.type = weapon_type[4]
shd_demon.damage = 1
shd_demon.protection = 20

paw_rabbit = Weapon()
paw_rabbit.name = "Sweet White Rabbit Paw"
paw_rabbit.type = weapon_type[2]
paw_rabbit.damage = 0
paw_rabbit.protection = 0

# Creating runes
# Runes are magic objects that can be only used a few times and require no mana
run_frozen = Rune()
run_frozen.name = "Frozen Avalanche Rune"
run_frozen.description = "Freezes your enemy's attack"
run_frozen.type = 2
run_frozen.required_magic_skill = 3.1
run_frozen.spell_power = 4
run_frozen.point_base = 1000
run_frozen.charges = 5

# Creating Players
# > Basics
Knight = Creature()
Knight.name = "Johnny Lawrence"
Knight.can_attack = True
Knight.can_defend = True
# > Life
Knight.life_points_max = 100
Knight.life_points_current = Knight.life_points_max
# > Weapons
Knight.right_hand = swd_justice
Knight.left_hand = shd_guardian
Knight.weapon_skills = 1.1
# > Magic
Knight.magic_level = 5
Knight.mana_points_max = 50
Knight.mana_points_current = 50
Knight.magic_skill_set = [spl_cure]

# > Basics
Hunter = Creature()
Hunter.name = "Daniel Larusso"
Hunter.can_attack = True
Hunter.can_defend = True
# > Life
Hunter.life_points_max = 100
Hunter.life_points_current = Hunter.life_points_max
# > Weapons
Hunter.right_hand = fst_bare
Hunter.left_hand = shd_demon
Hunter.weapon_skills = 10.2
# > Magic
Hunter.magic_level = 5
Hunter.mana_points_max = 50
Hunter.mana_points_current = 50
Hunter.magic_skill_set = [spl_cure, spl_death]

Rabbit = Creature()
Rabbit.name = "Innocent White Rabbit"
Rabbit.life_points_max = 10
Rabbit.life_points_current = Rabbit.life_points_max
Rabbit.right_hand = paw_rabbit
Rabbit.left_hand = paw_rabbit
Rabbit.can_attack = False
Rabbit.can_defend = False

# Fight!
Hunter.engage(Knight, -1)
Hunter.use_magic(Hunter.magic_skill_set[1], Knight)
Hunter.engage(Knight, -1)
Knight.use_magic(Knight.magic_skill_set[0], None)
Hunter.use_magic(Hunter.magic_skill_set[1], Knight)
