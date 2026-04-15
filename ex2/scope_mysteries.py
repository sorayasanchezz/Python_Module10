from collections.abc import Callable


def mage_counter() -> Callable:
    i = 0

    def counter() -> int:
        nonlocal i
        i += 1
        return i
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    def accumulator(add_power: int) -> int:
        nonlocal initial_power
        initial_power += add_power
        return initial_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchantment


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, int] = {}

    def store(key: str, value: int) -> None:
        memory[key] = value

    def recall(key: str) -> int | str:
        return memory.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall}


def main() -> None:

    # Mage counter
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(
        "\nTesting mage counter...\n",
        f"counter_a call 1: {counter_a()}\n",
        f"counter_a call 2: {counter_a()}\n",
        f"counter_b call 1: {counter_b()}")

    # Spell acumulator
    ft_accumulator = spell_accumulator(100)
    print(
        "\nTesting spell accumulator...\n",
        f"Base 100, add 20: {ft_accumulator(20)}\n",
        f"Base 100, add 30: {ft_accumulator(30)}")

    # Enchantment factory
    ft_enchantment_a = enchantment_factory("Flaming")
    ft_enchantment_b = enchantment_factory("Frozen")

    print(
        "\nTesting enchantment factory...\n",
        f"{ft_enchantment_a('Sword')}\n",
        f"{ft_enchantment_b('Shield')}\n")

    # Memory vault
    memory = memory_vault()
    ft_store = memory['store']
    ft_recall = memory['recall']

    ft_store("secret", 42)

    print(
        "Testing memory vault...\n",
        "Store 'secret' = 42\n",
        f"Recall 'secret': {ft_recall('secret')}\n",
        f"Recall 'unknown': {ft_recall('unknown')}\n",)


if __name__ == "__main__":
    main()
