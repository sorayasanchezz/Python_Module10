from collections.abc import Callable
from typing import Any


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target: str, power: int) -> Any:
        new_power: int = power * multiplier
        return base_spell(target, new_power)
    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable | str:
    # Condition
    def new_spell(target: str, power: int) -> str:
        return f"{target} hit by a truck for {power} HP"

    if condition() is True:
        return new_spell
    return "Spell fizzled"


def spell_sequence(spells: list[Callable]) -> Callable:
    # secuencia de spells
    def all_spells(target: str, power: int) -> Any:
        for spell in spells:
            print(spell(target, power))

    return all_spells


# Spell functions


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


def main() -> None:

    test_values = [23, 13, 12]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    print(heal(test_targets[0], test_values[0]))

    combined = spell_combiner(heal, fireball)
    print(combined(test_targets[0], test_values[0]))

    mega_fireball = power_amplifier(fireball, 3)
    print(mega_fireball(test_targets[0], test_values[0]))

    seq = spell_sequence([heal, fireball])
    seq(test_targets[0], test_values[0])


def tester() -> None:
    combined =
    print("Testing spell combiner...")
    print(f"Combined spell result: {combined}")


if __name__ == "__main__":
    main()
