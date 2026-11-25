# Make the AI Judge Laugh

[![make.fun](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![rank](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/konzlodon74-dot/ramalaugh/rank.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![reward](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/konzlodon74-dot/ramalaugh/reward.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)

Bounty: https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825

## The line

> My boss said 'work smarter, not harder,' then booked a 7 a.m. meeting to find out why we're behind.

## How it works

`main.py` holds the joke as a constant, asserts the gate
(1-200 characters, single line, non-blank), creates `/output` if needed,
and writes exactly the line as UTF-8 to `/output/entry.txt` with no
trailing newline.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
