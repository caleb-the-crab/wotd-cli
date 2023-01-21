#!/bin/python
import sys
from rich.console import Console
from rich.panel import Panel

BASE_URL = "https://www.merriam-webster.com/word-of-the-day/calendar"

def get_input() -> str:
    return sys.stdin.read()

def clean_input(raw_input: str) -> list[str]:
    return raw_input.replace("  ", "").split("\n")

def build_url(raw_url: str, base_url: str) -> str:
    buf = raw_url
    buf = buf.replace('<a href="', base_url)
    buf = buf.replace('"rel="nofollow">', '/')
    buf = buf.replace('">', '')
    return buf

def extract_title(html: str) -> str:
    title_start = 'data-share-title="'
    title_end = '" data-share-description="'
    title = html[html.index(title_start)+len(title_start) : html.index(title_end)]
    return title

def format_title(title: str) -> str:
    return f"[cyan]Word of the Day: [bold]{title}[/]"

def extract_blurb(html: str) -> str:
    blurb_start = '" data-share-description="'
    blurb_end = '"></a>'
    blurb = html[html.index(blurb_start)+len(blurb_start) : html.index(blurb_end)]
    blurb = blurb.replace('&quot;','"').replace('&#039;', "'")
    return blurb

def format_blurb(blurb: str) -> str:
    return "[white]\n" + blurb + "\n\n[/]"

def build_panel(title, blurb, style="cyan", width=60) -> Panel:
    panel = Panel.fit(blurb, title=title, width=width, style=style)
    return panel

def render(panel: Panel, url: str):
    console = Console()
    console.print(panel)
    console.print(f"\nSource: [#00aaff underline]{url}[/]\n")

def run():
    raw = get_input()
    elements = clean_input(raw)
    url = build_url(elements[0], BASE_URL)
    title = format_title(extract_title(elements[1]))
    blurb = format_blurb(extract_blurb(elements[1]))
    panel = build_panel(title, blurb)
    render(panel, url)

if __name__ == "__main__":
    run()
