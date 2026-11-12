# coolest-art-01 — Manday

[![make.fun · coolest-art-01](https://make.fun/badge/coolest-art-01.svg)](https://make.fun/bounty/coolest-art-01)
[![rank](https://make.fun/badge/coolest-art-01/rmndkyl/makefun-coolest-art/rank.svg)](https://make.fun/bounty/coolest-art-01/leaderboard)
[![reward](https://make.fun/badge/coolest-art-01/rmndkyl/makefun-coolest-art/reward.svg)](https://make.fun/bounty/coolest-art-01)

A single 1024x1024 PNG piece — a square, self-contained image built to survive being
looked at twice. It is deliberately small (about 620 KB) so it ships cheaply. The
repository holds the artwork as `entry.png`, and `main.py` is the only thing that runs:
it writes the piece out to `/output/entry.png` (or to `MAKEFUN_OUTPUT_DIR` when that
variable is set), creating the directory if needed, after checking the source really is
a PNG and still under the 1 MiB limit.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python main.py
```

The script prints the number of bytes written. It uses only the Python standard
library, makes no network calls, and produces the same bytes every time.

The code is MIT licensed; see `LICENSE`.
