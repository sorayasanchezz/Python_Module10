from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target: str, power: int) -> str:
        new_power: int = power * multiplier
        return base_spell(target, new_power)
    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def new_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return new_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def all_spells(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return all_spells


# Spell functions

def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


def strong_enough(target: str, power: int) -> bool:
    return power >= 20


def main() -> None:
    target = "Dragon"
    power = 10

    # Spell combiner
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined(target, power)

    r1 = result[0].split(" for")[0]
    r2 = result[1].split(" for")[0]
    print(f"Combined spell result: {r1}, {r2}")

    # Power amplifier
    print("\nTesting power amplifier...")
    amplified = power_amplifier(fireball, 3)

    print(f"Original: {power}, Amplified: {power * 3}")
    print(f"Spell result: {amplified(target, power)}\n")

    # Conditional caster
    print("Testing conditional caster...")
    conditional = conditional_caster(strong_enough, fireball)

    print("Low power:", conditional(target, 10))
    print("High power:", conditional(target, 30), "\n")

    # Spell sequence
    print("Testing spell sequence...")
    sequence = spell_sequence([fireball, heal])

    results = sequence(target, power)
    print("Sequence result:")
    for r in results:
        print("-", r)


if __name__ == "__main__":
    main()
    print()
