# wotd-cli - Word of the Day
A simple, hackable application which pulls the Word of the Day from Merriam
Webster's Dictionary and displays it to the console in a Rich panel.

## Example
  Here is an example of the output as it appears when piped. The terminal will
display this with full colour and typeface styling.
```
$ wotd
╭────────────── Word of the Day: Exacerbate ───────────────╮
│                                                          │
│ The Latin adjective acer, meaning "sharp," forms the     │
│ basis of a number of English words. Acerbic ("having a   │
│ bitter temper or sour mood"), acrid ("having a sharp     │
│ taste or odor"), and acrimony ("a harsh manner or        │
│ disposition") are just the tip of the jagged iceberg.    │
│ First appearing in English in the 17th century,          │
│ exacerbate combines the Latin prefix ex- ("out of" or    │
│ "outside") with acer offspring acerbus, meaning "harsh"  │
│ or "bitter." Just as pouring salt in a wound worsens     │
│ pain, things that exacerbate cause a situation to go     │
│ from bad to worse. A pointed insult or cutting remark,   │
│ for example, might exacerbate tensions between two       │
│ bitter rivals. The legacy of acer isn&#039;t all         │
│ negative, however. The Latin name for the genus of maple │
│ trees and shrubs is Acer, owing to maples’               │
│ characteristically pointy leaves.                        │
│                                                          │
│                                                          │
╰──────────────────────────────────────────────────────────╯

Source: 
https://www.merriam-webster.com/word-of-the-day/calendar/word-of-the-day/exacerbate-2023-01-21
```

## Requirements
- python 3.X
- bash
- curl
- grep
- rich `pip install rich`
- internet connection

## Quickstart
1. Clone this repo wherever you would like `git clone https://github.com/caleb-the-crab/wotd-cli`.
2. Run the script `wotd-sh` to make sure it's working
3. Add the following line to your .bashrc, or whatever config file is used for your
terminal: `alias wotd="$HOME/<...>/wotd-cli/wotd-sh"`. Replace `<...>` with the
path to which you cloned the repo.
4. Close and re-open your terminal to apply the changes and type `wotd`.

