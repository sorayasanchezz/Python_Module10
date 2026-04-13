def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x["power"]["power"])
    min_power = min(mages, key=lambda x: x["power"]["power"])
    avg_power = round(sum(m["power"] for m in mages) / len(mages), 2)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


def main() -> None:
    artifacts = [
        {'name': 'Earth Shield', 'power': 102, 'type': 'relic'},
        {'name': 'Light Prism', 'power': 89, 'type': 'relic'}
    ]

    spells = ["fireball", "heal", "shield"]

    sorted_artifacts = artifact_sorter(artifacts)
    print(
        "\nTesting artifact sorter...\n"
        f"{sorted_artifacts[0]['name']} "
        f"({sorted_artifacts[0]['power']} power) "
        f"comes before {sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)")

    transformed_spells = spell_transformer(spells)
    print(
        "\nTesting spell transformer...\n",
        " ".join(transformed_spells))


if __name__ == "__main__":
    main()
