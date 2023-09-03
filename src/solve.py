import pytesseract
import numpy as np


def solve(image: np.ndarray) -> str:
    for mode in [7, 10, 11, 12, 13]:
        result = normalize(
            pytesseract.image_to_string(
                image, lang="eng", config=f"--oem 3 --psm {mode}", timeout=0.5
            ).strip()
        )
        if result != "":
            return result

    return "not sure"


def normalize(s: str) -> str:
    print(s)
    if "\n" in s:
        return ""

    s = s.replace(" ", "").lower()

    if len(s) < 3:
        return ""

    # if first is number
    if s[0].isdigit() and s[2].isdigit():
        if s[1] in ["+", "4"]:
            return str(int(s[0]) + int(s[2]))
        elif s[1] in ["-", "_"]:
            return str(int(s[0]) - int(s[2]))
        else:
            return str(int(s[0]) * int(s[2]))

    # possible alphabet mapping
    mapping = {
        ")": "l",
        "¥": "y",
        "2": "z",
        "é": "e",
    }

    for k, v in mapping.items():
        s = s.replace(k, v)

    # if not all alphabet
    if not all([c.isalpha() for c in s]):
        return ""

    if len(s) != 4:
        return ""

    return s
