"""One colour per subject, so students find a subject by colour before they read its name.

Related subjects share a family (every mathematics course is violet). Each colour carries a
white icon at 4.2:1 or better, so the tiles pass the 3:1 contrast needed for graphics.
"""

VIOLET = "#5B3FE4"      # mathematics
BLUE = "#2563EB"        # physics
TEAL = "#0F8A7E"        # chemistry
GREEN = "#1E8E4A"       # life sciences
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
