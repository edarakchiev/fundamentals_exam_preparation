def cast_spell(heroes, hero_name, mp_needed, spell_name):
    if heroes[hero_name]['MP'] >= mp_needed:
        heroes[hero_name]['MP'] -= mp_needed
        print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['MP']} MP!")
    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")


def take_damage(heroes, hero_name, damage, attacker):
    heroes[hero_name]["HP"] -= damage
    if heroes[hero_name]["HP"] > 0:
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
    else:
        heroes.pop(hero_name)
        print(f"{hero_name} has been killed by {attacker}!")


def recharge(heroes, hero_name, amount):
    heroes[hero_name]['MP'] += amount
    if heroes[hero_name]['MP'] > 200:
        difference = heroes[hero_name]['MP'] - 200
        amount -= difference
        heroes[hero_name]['MP'] = 200
    print(f"{hero_name} recharged for {amount} MP!")


def heal(heroes, hero_name, amount):
    heroes[hero_name]['HP'] += amount
    if heroes[hero_name]['HP'] > 100:
        difference = heroes[hero_name]['HP'] - 100
        amount = amount - difference
        heroes[hero_name]['HP'] = 100
    print(f"{hero_name} healed for {amount} HP!")


n = int(input())
heroes = {}

for _ in range(n):
    name, hp, mp = input().split()
    hp = int(hp)
    mp = int(mp)
    heroes[name] = {}
    heroes[name] = {"HP": hp, "MP": mp}

while True:
    data = input()
    if data == "End":
        break
    data = data.split(" - ")
    command = data[0]
    hero_name = data[1]
    if command == "CastSpell":
        mp_needed = int(data[2])
        spell_name = data[3]
        cast_spell(heroes=heroes, hero_name=hero_name, mp_needed=mp_needed, spell_name=spell_name)
    elif command == "TakeDamage":
        damage = int(data[2])
        attacker = data[3]
        take_damage(heroes=heroes, hero_name=hero_name, damage=damage, attacker=attacker)
    elif command == "Recharge":
        amount = int(data[2])
        recharge(heroes=heroes, hero_name=hero_name, amount=amount)
    elif command == "Heal":
        amount = int(data[2])
        heal(heroes=heroes, hero_name=hero_name, amount=amount)

for hero, value in sorted(heroes.items(), key=lambda x: (-x[1]["HP"], x[0])):
    print(f"{hero}")
    print(f'  HP: {value["HP"]}')
    print(f'  MP: {value["MP"]}')