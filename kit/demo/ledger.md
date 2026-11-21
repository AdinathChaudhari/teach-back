# snip, Level 1 ledger (demo)

Every claim on `kit/template.html` is listed here with the line that proves it.

- `save` reads the whole table first: `src/snip/store.py:42`
- A new code is re-rolled while it already exists: `src/snip/store.py:44`
- The code is stored next to its long URL: `src/snip/store.py:46`
- The table is written back to one JSON file: `src/snip/store.py:47`, `src/snip/store.py:26`
- A code is 6 characters from lowercase letters and digits: `src/snip/store.py:11`, `src/snip/store.py:12`
- A missing file counts as an empty table: `src/snip/store.py:18`
- A lookup returns the long URL, or None: `src/snip/store.py:37`
- `save` takes one long URL: `src/snip/store.py:40`
- The code comment assumes one writer at a time: `src/snip/store.py:25`
- A pitch takes about 30 seconds to say (a speaking target, not a code fact)
