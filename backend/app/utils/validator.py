VALID_CATEGORIES = [
    "horror",
    "educational",
    "shorts",
    "hooks",
    "seo"
]

def validate_category(category: str):
    return category.lower() in VALID_CATEGORIES
