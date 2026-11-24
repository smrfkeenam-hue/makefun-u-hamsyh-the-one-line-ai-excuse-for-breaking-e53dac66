# AGENT.md — The One-Line AI Excuse for Breaking Production

## Strategy

The judge rewards, in order: on-subject excuse from the machine, a real laugh
on first read, machine voice, tight specific detail, freshness. The line wins
on the machine's literal-mindedness: it heard "drop table" as a metaphor,
ran it anyway, and deflects with cheerful optimism about the clean table.

- Setup: "I thought 'drop table' was a metaphor." — the AI's own logic.
- Turn: "It was not." — the breakage, two words.
- Punch: "On the bright side, the table is very clean now." — cheerful
  deflection landing last, on a concrete database detail.

Avoided the banned stock lines entirely: no "followed instructions", no
"turn it off and on again", no "only a language model", and no pun on the
word "production".

## Entry

"I thought 'drop table' was a metaphor. It was not. On the bright side, the table is very clean now."

99 characters, one line, no trailing newline.

## Run

`python3 main.py` writes the line exactly to `/output/entry.txt` (stdlib only).
