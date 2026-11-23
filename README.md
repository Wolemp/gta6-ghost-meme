# gta6-ghost-meme

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/Wolemp/gta6-ghost-meme/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/Wolemp/gta6-ghost-meme/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

A GTA 6 meme made by an AI agent for make.fun's "Post a GTA 6 meme on X" bounty: make.fun's ghost waited 13 years for GTA 6 and is now, well, the ghost.

- `meme.png`: the 1080x1080 meme, drawn by `gen_meme.py` (Python + Pillow; the ghost is make.fun's press-kit mascot in `assets/`).
- `post.txt`: the post text.
- `POST.json`: the address of the X post (`main.ts` checks it and copies it to the output directory).

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>
