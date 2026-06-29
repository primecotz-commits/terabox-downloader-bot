"""
=========================================
Gezx Downloader
utils.py
=========================================
"""

import math
import re


def is_terabox_link(link: str) -> bool:
    """
    Check whether a link looks like a public TeraBox link.
    """

    if not link:
        return False

    patterns = [
        r"terabox\.com",
        r"1024tera\.com",
        r"teraboxapp\.com",
        r"nephobox\.com",
        r"freeterabox\.com",
        r"terasharelink\.com"
    ]

    link = link.lower()

    return any(re.search(pattern, link) for pattern in patterns)


def format_size(size: int) -> str:
    """
    Convert bytes into KB, MB, GB...
    """

    if size is None:
        return "Unknown"

    if size == 0:
        return "0 B"

    units = ["B", "KB", "MB", "GB", "TB"]

    power = int(math.floor(math.log(size, 1024)))
    power = min(power, len(units) - 1)

    value = size / (1024 ** power)

    return f"{value:.2f} {units[power]}"


def format_speed(speed: float) -> str:
    """
    Convert bytes/sec to readable speed.
    """

    return f"{format_size(speed)}/s"


def format_duration(seconds: int) -> str:
    """
    Convert seconds to HH:MM:SS
    """

    if seconds is None:
        return "Unknown"

    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60

    return f"{h:02}:{m:02}:{s:02}"


def format_eta(seconds: int) -> str:
    """
    ETA formatting.
    """

    if seconds <= 0:
        return "0 sec"

    m = seconds // 60
    s = seconds % 60

    if m == 0:
        return f"{s} sec"

    return f"{m} min, {s} sec"


def progress_bar(percent: float, total_blocks: int = 18) -> str:
    """
    Generate:
    [■■■■□□□□□□□□□□□□□□]
    """

    percent = max(0, min(percent, 100))

    filled = round((percent / 100) * total_blocks)

    empty = total_blocks - filled

    return "[" + ("■" * filled) + ("□" * empty) + "]"


def safe_filename(name: str) -> str:
    """
    Remove invalid filename characters.
    """

    invalid = r'<>:"/\|?*'

    for char in invalid:
        name = name.replace(char, "_")

    return name.strip()


def get_extension(filename: str) -> str:
    """
    Return file extension.
    """

    if "." not in filename:
        return ""

    return filename.split(".")[-1].lower()
