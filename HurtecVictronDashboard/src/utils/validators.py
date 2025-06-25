"""Input validation utilities."""


def validate_url(url: str) -> bool:
    return url.startswith("http")
