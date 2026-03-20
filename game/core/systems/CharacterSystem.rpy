# CharacterSystem.rpy — Character definitions and relationship tracking

# ═══ Character Definitions ═══
# Defined in init python so they capture store._ and can be pickled on save.
# Using define would create Characters in script context with a different _ reference.

init -1 python:
    # Ensure mc_name is a string (Ren'Py treats { as text tag)
    if not hasattr(store, 'mc_name') or not isinstance(store.mc_name, str):
        store.mc_name = "Alex"
    store.mc_name = store.mc_name.replace("{", "{{").replace("}", "}}")

init python:
    store.mc_char = Character("[mc_name]", color="#e5e349")
    store.diana = Character("Diana", color="#e1bdff", image="diana", callback=_diana_speak_callback)
    store.sophie = Character("Sophie", color="#89CFF0", image="sophie")
    store.marlene = Character("Marlene", color="#b088f9", image="marlene")
    store.candace = Character("Dr. Cole", color="#f0c27f", image="candace")
    store.harmon = Character("Harmon", color="#8b7355", image="harmon")
    store.jada = Character("Jada", color="#6b8e6b", image="jada")
    store.narrator_char = Character(None, kind=nvl_narrator)
    store.inner = Character("[mc_name]", color="#aaaaaa", what_prefix="(", what_suffix=")")

    # Whisper variants — smaller, italic text for hushed/nighttime dialogue
    store.mc_whisper = Character("[mc_name]", color="#c8c878", what_prefix="{size=-4}{i}", what_suffix="{/i}{/size}")
    store.diana_whisper = Character("Diana", color="#c9a0e0", what_prefix="{size=-4}{i}", what_suffix="{/i}{/size}", callback=_diana_speak_callback)
    store.sophie_whisper = Character("Sophie", color="#6aaddb", what_prefix="{size=-4}{i}", what_suffix="{/i}{/size}")
    store.inner_whisper = Character("[mc_name]", color="#777777", what_prefix="{size=-5}{i}(", what_suffix="){/i}{/size}")
