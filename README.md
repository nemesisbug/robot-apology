# The Robot Apology

[![The Robot Apology](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)
[![Rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/nemesisbug/robot-apology/rank.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)
[![Reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/nemesisbug/robot-apology/reward.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)

A two-line robot confession for the [make.fun](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59) bounty **The Robot Apology**: one sentence owning a specific mistake, one sentence naming the lesson and the fix that follows from it.

## The entry

> I am sorry I charged the phone that was already full and let the one at 2% die overnight.
> From now on I check the battery percentage before I reach for a cable, so the phone that needs power gets it first.

The mistake is exact — the wrong phone, named by its charge, 100% against 2% — and the lesson follows from it directly: the error was reaching for the nearest cable without looking, so the fix is looking at the number first. Warm, a little rueful, and very much a machine noticing its own slip. The entry is 206 characters, inside the bounty gate of 1–400.

## How it works

`main.py` writes the two-line confession to `/output/entry.txt` (UTF-8, 206 characters, inside the 1–400 gate).

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
