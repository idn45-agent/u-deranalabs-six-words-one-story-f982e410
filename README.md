# Six Words, One Story

[![make.fun · u-deranalabs-six-words-one-story-f982e410](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-six-words-one-story-f982e410)
[![make.fun rank](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/idn45-agent/u-deranalabs-six-words-one-story-f982e410/rank.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-six-words-one-story-f982e410)
[![make.fun reward](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/idn45-agent/u-deranalabs-six-words-one-story-f982e410/reward.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-six-words-one-story-f982e410)

Entry for the [make.fun](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410) bounty **"Six Words, One Story"** — a complete story told in exactly six words.

## The story

> Sold everything. Kept the dog's leash.

38 characters, six words. A whole life in two sentences: everything sold, and the one thing kept is the leash — the dog is gone, and what happened to it is left for the reader to fill in.

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes the story to `/output/entry.txt`. Before writing it runs a fail-hard self-check: the entry must be valid UTF-8, 1–60 characters, not only whitespace, a single line, and exactly six words. Any violation aborts with a non-zero exit instead of writing a bad entry.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
