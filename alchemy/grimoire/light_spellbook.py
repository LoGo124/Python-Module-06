from typing import List


def light_spell_allowed_ingredients() -> List[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    status = validate_ingredients(ingredients)
    if "VALID" in status:
        return f"Spell recorded: {spell_name} ({status})"
    return f"Spell rejected: {spell_name} ({status})"
