#!/usr/bin/python3
try:
    from alchemy.grimoire.dark_spellbook import dark_spell_record
except Exception as e:
    print(f"BOOOM!!!: {e}")

if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Using grimoire module directly")
    try:
        result: str = dark_spell_record(
            "Fantasy", "Earth, wind and fire"
        )
        print(f"Testing record dark spell: {result}")
    except Exception as e:
        print(f"KABOOOM!!!: {e}")
