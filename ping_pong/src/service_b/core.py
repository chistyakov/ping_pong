from typing import Tuple, List, Optional


def get_avg_min_max(
    digits: Optional[List[int]],
) -> Tuple[Optional[float], Optional[int], Optional[int]]:
    if not digits:
        return None, None, None

    avg = sum(digits) / len(digits)
    min_digit = min(digits)
    max_digit = max(digits)
    return avg, min_digit, max_digit
