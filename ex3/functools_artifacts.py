from typing import Any
from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    ops: dict[str, Callable] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min}
    if not spells:
        return 0
    try:
        result = reduce(ops[operation], spells)
    except KeyError:
        raise KeyError("[ERROR]: Unknown operation")
    return result


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "water": partial(base_enchantment, 50, "water"),
        "fire": partial(base_enchantment, 50, "fire"),
        "air": partial(base_enchantment, 50, "air")}


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def spell(x: Any) -> str:
        return "Unknown spell type"

    @spell.register(int)
    def _(x: int) -> str:
        return f"Damage spell: {x} damage"

    @spell.register(str)
    def _(x: str) -> str:
        return f"Enchantment: {x}"

    @spell.register(list)
    def _(x: list) -> str:
        return f"Multi-cast: {len(x)} spells"

    return spell


# Utils

def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{target} has been enchanted with {power} {element}"


def main() -> None:

    # Spell reducer
    try:
        print(
            "\nTesting spell reducer...\n",
            f"Sum: {spell_reducer([20, 30, 50], 'add')}\n",
            f"Product: {spell_reducer([2, 12, 10000], 'multiply')}\n",
            f"Max: {spell_reducer([20, 10, 40, 30], 'max')}")
    except KeyError as e:
        print(e)

    # Partial enchanter
    enchants = partial_enchanter(base_enchantment)
    print(
        "\nTesting partial enchanter...\n",
        f"{enchants['fire']('enemy')}\n",
        f"{enchants['water']('sword')}\n",
        f"{enchants['air']('armor')}")

    # Fibonacci
    print(
        "\nTesting memoized fibonacci...\n",
        f"Fib(0): {memoized_fibonacci(0)}\n",
        f"Fib(1): {memoized_fibonacci(1)}\n",
        f"Fib(10): {memoized_fibonacci(10)}\n",
        f"Fib(15): {memoized_fibonacci(15)}\n")

    # Spell dispatcher
    ft_dispatch = spell_dispatcher()
    print(
        "Testing spell dispatcher...\n",
        f"{ft_dispatch(42)}\n",
        f"{ft_dispatch('fireball')}\n",
        f"{ft_dispatch([1, 2, 3])}\n",
        f"{ft_dispatch(None)}\n")


if __name__ == "__main__":
    main()
