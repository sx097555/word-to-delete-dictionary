#!/usr/bin/env python3
"""The case for deleting PULCHRITUDE from the dictionary.

pulchritude (noun) — beauty. Pronounced PUL-kri-tood.

The problem: it is the only word in English whose sound is the exact
opposite of its meaning. It means beauty, and it sounds like a rash.
A word for beauty should not sound like something you need antibiotics for.

Verdict: delete it. Beauty keeps its other five names, and the dictionary
loses the one word for beauty that sounds like a disease.
"""

WORD = "pulchritude"
PRONUNCIATION = "PUL-kri-tood"
DEFINITION = "beauty"

# What the word sounds like, in everyday sentences.
SOUND_ALIKES = [
    ("a skin condition",
     "Have you seen a doctor about your pulchritude?"),
    ("a plumbing problem",
     "The plumber says the pulchritude is backed up again."),
    ("a medieval affliction",
     "He died of pulchritude in the winter of 1348."),
    ("a prescription drug",
     "Ask your doctor if Pulchritude is right for you. Side effects may include beauty."),
]

# Words we already have for the same meaning. None of them sounds like a rash.
REPLACEMENTS = ["beauty", "loveliness", "grace", "elegance", "charm"]


def sound_test():
    """Exhibit A: the word, used in sentences, sounds like everything but beauty."""
    print("EXHIBIT A — THE SOUND TEST")
    for label, line in SOUND_ALIKES:
        print(f"  Sounds like {label}:")
        print(f'    "{line}"')
    print()


def redundancy():
    """Exhibit B: the meaning is already covered, by prettier words."""
    print("EXHIBIT B — THE REDUNDANCY")
    print(f"  We already have {len(REPLACEMENTS)} words for this:")
    print("  " + ", ".join(REPLACEMENTS) + ".")
    print("  None of them sounds like a rash.")
    print()


def verdict():
    """The verdict: delete it, and beauty loses nothing."""
    print("VERDICT: DELETE")
    print(f"  The dictionary keeps one word for beauty that sounds like")
    print(f"  a disease. Strike '{WORD}'. Beauty keeps its other")
    print(f"  five names, and nobody has to say 'pulchritude' at a")
    print(f"  dinner party ever again.")


def main():
    print(f"THE WORD: {WORD}")
    print(f"Pronounced: {PRONUNCIATION}")
    print(f"Means: {DEFINITION}")
    print()
    print("THE PROBLEM")
    print("  It means beauty, and it sounds like something you need")
    print("  antibiotics for.")
    print()
    sound_test()
    redundancy()
    verdict()


if __name__ == "__main__":
    main()
