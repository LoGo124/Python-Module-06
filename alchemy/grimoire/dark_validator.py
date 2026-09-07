from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients = dark_spell_allowed_ingredients()
    for ingredient in allowed_ingredients:
        if ingredient.lower() in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
