def convert_bytes(num: str) -> str:
    """
    Convert bytes to the appropriate unit (KB, MB, GB, etc.).

    Args:
        num (str): The number of bytes as a string.

    Returns:
        str: The converted value with the appropriate unit, rounded to one decimal place.
             Returns an empty string if the input cannot be converted to a float.
    """
    step_unit = 1024
    try:
        num = float(num)
        for unit in ["bytes", "KB", "MB", "GB", "TB"]:
            if num < step_unit:
                return f"{num:.1f} {unit}"
            num /= step_unit
    except (ValueError, TypeError):
        return ""


def convert_to_mb(num: str) -> float:
    """
    Converts bytes to megabits per second (Mbps).

    Args:
        num (str): The number of bytes as a string.

    Returns:
        float: The equivalent value in Mbps, rounded to two decimal places.
               Returns 0.0 if the input cannot be converted to a float.
    """
    try:
        num = float(num)
        return round((num / 1024 / 1024) * 8, 2)
    except (ValueError, TypeError):
        return 0.0