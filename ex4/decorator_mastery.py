from collections.abc import Callable
from typing import Any
from time import time, sleep
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kargs: Any):
        print(f"Casting {func.__name__}...")
        start = time()
        rtn: str = func(*args, **kargs)
        total_time = (time() - start)
        print(f"Spell completed in {total_time:.3f} seconds")
        return rtn
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            if len(args) >= 3:
                power = args[2]
            else:
                power = args[0]

            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == max_attempts:
                        return ("Spell casting failed after "
                                f"{max_attempts} attempts\n"
                                "Waaaaaaagh spelled !")
                    print("Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")
        return wrapper
    return decorator


@spell_timer
def fireball() -> str:
    return "Fireball cast!"


@power_validator(10)
def cast(power):
    return f"Spell cast with {power}"


@retry_spell(3)
def spell():
    raise ValueError()


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        sleep(0.1)
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")
    print(f"Result: {fireball()}\n")

    print(
        "Testing power validator...\n"
        f"Test (< 10): {cast(5)}\n"
        f"Test (>= 10): {cast(35)}\n")

    print("Testing retrying spell...")
    print(spell())

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Aeris"))
    print(MageGuild.validate_mage_name("A1"))

    mage = MageGuild()
    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Fireball", 5))


if __name__ == "__main__":
    main()
