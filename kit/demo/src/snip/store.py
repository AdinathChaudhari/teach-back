"""snip.store: the one place that keeps short codes and their long URLs.

This file is a tiny fictional demo. It exists so the citation checker
has a real file to resolve `src/snip/store.py:42` against.
"""
import json
import os
import secrets
import string

ALPHABET = string.ascii_lowercase + string.digits
CODE_LENGTH = 6
DB_PATH = os.environ.get("SNIP_DB", "snip.json")


def _load():
    """Read the whole table from disk. A missing file is an empty table."""
    if not os.path.exists(DB_PATH):
        return {}
    with open(DB_PATH) as fh:
        return json.load(fh)


def _write(table):
    """Write the whole table back. No locking: one writer at a time."""
    with open(DB_PATH, "w") as fh:
        json.dump(table, fh)


def new_code():
    """Pick a random code. Collisions are checked by the caller."""
    return "".join(secrets.choice(ALPHABET) for _ in range(CODE_LENGTH))


def lookup(code):
    """Return the long URL for a code, or None."""
    return _load().get(code)


def save(url):
    """Store a long URL under a fresh code and return the code."""
    table = _load()
    code = new_code()
    while code in table:
        code = new_code()
    table[code] = url
    _write(table)
    return code
