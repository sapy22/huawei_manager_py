def content_preview(text: str) -> str:
    """
    Returns a preview of the first 40 characters of the input text, excluding newlines.

    Args:
        text (str): The input text.

    Returns:
        str: A string containing the first 40 characters of the input text,
        without newline characters. Returns an empty string if input is invalid.
    """
    try:
        return "".join(text.splitlines())[:40]
    except AttributeError:
        return ""