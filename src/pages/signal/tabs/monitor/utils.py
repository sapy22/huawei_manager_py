def split_tx(value: str) -> str:
    """ 
    Split and return the value of PPusch and PPucch.
    input: PPusch:0dBm PPucch:0dBm PSrs:0dBm PPrach:0dBm
    split: ' ' and :
    return: 0dBm/0dBm or ''
    """
    try:
        value = value.split(" ")
        v1 = value[0].split(":")[1]
        v2 = value[1].split(":")[1]
        return f"{v1}/{v2}"
    except (IndexError, AttributeError):
        return ""


def split_k(value: str) -> int:
    """ input: 1850000kHz, return: 1850 or 0 """
    try:
        value = int(float(value.split("k")[0]))
        value = round(value/1000)
        return value
    except (ValueError, AttributeError):
        return 0


def split_d(value: str|None) -> int:
    """ input: 18.0dbm or -18dbm, return: 18 or -18 or 0 """
    try:
        v = [v for v in value if v in ("1","2","3","4","5","6","7","8","9","0",".","-")]
        return int(float("".join(v)))
        # return int(float(re.sub(r"[^\-\d\.]", "", value)))
        # return int(float(value.split("d")[0]))
    except (ValueError, TypeError):
        return 0