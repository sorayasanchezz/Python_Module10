from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    pass


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    pass


def spell_sequence(spells: list[Callable]) -> Callable:
    pass


# Spell functions


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


def main() -> None:
    spell1 = heal
    spell2 = fireball

    test_values = [23, 13, 12]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    print(spell2(test_targets[0], test_values[0]))

    combined = spell_combiner(spell1, spell2)
    print(combined(test_targets[0], test_values[0]))


if __name__ == "__main__":
    main()
