"""One colour per subject, so students find a subject by colour before they read its name.

Related subjects share a family (every mathematics course is violet). Each colour carries a
white icon at 4.5:1 or better, so the tiles pass the 3:1 contrast needed for graphics.
"""

VIOLET = "#5B3FE4"      # mathematics
BLUE = "#2563EB"        # physics
TEAL = "#0D8478"        # chemistry
GREEN = "#1C8745"       # life sciences
INDIGO = "#3730A3"      # computing
CYAN = "#0E7490"        # earth and place
BROWN = "#B45309"       # history and citizenship
PURPLE = "#7E22CE"      # economics and business
ROSE = "#D0386F"        # English language
CRIMSON = "#9F1239"     # literature
ORANGE = "#C2410C"      # French
STONE = "#57534E"       # religion, philosophy and logic

BY_SLUG = {
    "mathematics": VIOLET, "additional-mathematics": VIOLET, "further-mathematics": VIOLET,
    "pure-mathematics-with-mechanics": VIOLET, "pure-mathematics-with-statistics": VIOLET,
    "physics": BLUE,
    "chemistry": TEAL,
    "biology": GREEN, "human-biology": GREEN, "food-and-nutrition": GREEN,
    "computer-science": INDIGO, "ict": INDIGO,
    "geography": CYAN, "geology": CYAN,
    "history": BROWN, "citizenship-education": BROWN,
    "economics": PURPLE, "business-studies": PURPLE, "commerce": PURPLE, "accounting": PURPLE,
    "principles-of-accounts": PURPLE, "office-practice": PURPLE,
    "english-language": ROSE,
    "literature-in-english": CRIMSON,
    "french": ORANGE,
    "religious-studies": STONE, "philosophy": STONE, "logic": STONE,
}

# Subjects added later fall back to a colour for their category.
BY_CATEGORY = {"sciences": BLUE, "humanities": BROWN, "languages": ROSE, "business": PURPLE}


def subject_colour(subject):
    return BY_SLUG.get(subject.slug) or BY_CATEGORY.get(subject.category) or VIOLET


def _rgb(hex_):
    h = hex_.lstrip("#")
    return [int(h[i:i + 2], 16) for i in (0, 2, 4)]


def mix(hex_, other, amount):
    """`hex_` moved `amount` (0 to 1) of the way towards `other`, as a #RRGGBB string."""
    a, b = _rgb(hex_), _rgb(other)
    return "#%02X%02X%02X" % tuple(round(x * (1 - amount) + y * amount) for x, y in zip(a, b))


def subject_shades(subject):
    """Every shade a subject card needs, as plain hex (no CSS colour functions, for older phones).

    base  tile, progress bar          dark  button background, white text 5.4:1 or better
    text  labels on the tint, 7.4:1+  tint  card background
    line  card border
    """
    base = subject_colour(subject)
    return {
        "base": base,
        "dark": mix(base, "#000000", .14),
        "text": mix(base, "#000000", .35),
        "tint": mix(base, "#FFFFFF", .93),
        "line": mix(base, "#FFFFFF", .55),
    }

