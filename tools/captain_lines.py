"""Make the sea captain's voice lines for the page.

Each stage gets one clip in assets/captain/<id>.mp3, made with the local Qwen3-TTS
studio (voice: sea-captain). The same text, minus delivery directions like
[pause 300], is written to assets/captain/lines.js so the page can show captions.

Usage:  python tools/captain_lines.py            # make every clip
        python tools/captain_lines.py map quests # remake just these
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "captain"
SPEAK = "C:/coding/QwenTTS_WSL/scripts/speak.py"
VOICE = "sea-captain"

LINES = {
    "top": "[excited] Ahoy, ye landlubbers! [pause 300] Gather 'round. Anthropic be handin' out a free year of Claude "
           "to small startup crews. Premium seats, API credits, the whole treasure chest. [pause 300] Robert has "
           "volunteered to do the paperwork, poor soul. Ye just grab a controller. [pause 300] Worst case, we level "
           "up for free. Best case, beer money. [pause 200] [excited] Now press start, ye scallywags!",
    "players": "Crew roster, lads. [pause 200] Robert's already aboard, mostly because somebody had to fill out the "
               "forms. [pause 300] There be up to five seats on this ship. Click an open slot, type yer name, and it's "
               "yours. [pause 300] Don't get too excited. Yer name only saves on yer own computer for now. So walk over "
               "and tell Robert in person, like it's nineteen eighty five.",
    "powerups": "Power-ups! [pause 200] Five premium seats, free for a year. That's about six thousand dollars of tools "
                "we'd never pay for ourselves, because we're cheap. [pause 300] A thousand dollars in API credits, "
                "which go bad in six months, like milk. [pause 200] Up to forty five thousand in partner perks, and "
                "office hours with the folks who built the thing. [pause 300] No equity, no quotas, nothin' to pay "
                "back. If they approve us. Which they might not. Ahem.",
    "inventory": "Yer inventory, matey. [pause 200] Claude Code be the big gun. It reads the code, writes the code, "
                 "tests the code, and never once asks for a raise. [pause 300] Agents that work while ye nap. "
                 "Connectors to plug into everything. Skills so the whole crew sails the same way. [pause 300] And a "
                 "browser bot that clicks through them awful old websites, so ye don't have to. [pause 200] Frankly, "
                 "it's more gear than this crew deserves.",
    "map": "Here's the map. Five levels, no dragons. [pause 300] Level one: ye say I'm in. [pause 200] Level two: ye "
           "get a work email. [pause 200] Level three: the application. Robert does the paperwork, because somebody "
           "has to, and it ain't gonna be me. [pause 200] Level four: we get approved, and everybody gets a seat. "
           "[pause 300] Level five: the boss fight. A real local business, a real problem, and we fix it. Or we sink "
           "tryin'.",
    "quests": "Side quests! [pause 200] The shops around here still run on paper, spreadsheets, and pure stubbornness. "
              "[pause 300] Bookings, invoices, dashboards, little tools, simple websites. Boring for them, easy loot "
              "for us. [pause 300] We pick one, we talk to a real owner, and we build somethin' that actually saves "
              "'em time. [pause 200] Novel idea, I know.",
    "endings": "Three endings, and nobody walks the plank. [pause 300] Ending one: we make nothin'. We still had a free "
               "year with the best tools on the seven seas, and we keep the experience. [pause 300] Ending two: beer "
               "money. Pizza and beer on the house. That be the realistic dream. [pause 300] Ending three: real "
               "treasure. Then we split it fair, in writing, and have ourselves some fun.",
    "manual": "Aye, the fine print. Every treasure's got a catch. [pause 300] It ain't guaranteed. They review every "
              "crew. [pause 200] After a year, we vote: keep it, shrink it, or scuttle it. No surprise charges. "
              "[pause 200] Seats have limits, so no infinite lives. [pause 200] And before any real paying customer, "
              "we put the split in writing. [pause 200] Nobody's sponsorin' us, either. It's just us and a pile of "
              "good tools.",
    "continue": "Continue? [pause 300] Insertin' a coin is easy. Ye just tell Robert, I'm in. In person, by text, by "
                "carrier pigeon, I don't care. [pause 300] Once two or three of ye sign on, the paperwork gets filed "
                "and the adventure begins. [pause 300] Or don't, and go back to copy-pastin' spreadsheets forever. "
                "[pause 200] Yer choice, sailor.",
}


def caption(text: str) -> str:
    """The spoken words without delivery directions."""
    return re.sub(r"\s+", " ", re.sub(r"\[[^\]]*\]", "", text)).strip()


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    wanted = sys.argv[1:] or list(LINES)
    for key in wanted:
        out = OUT / f"{key}.mp3"
        result = subprocess.run(
            [sys.executable, SPEAK, LINES[key], "--voice", VOICE, "--out", str(out)],
            capture_output=True, text=True,
        )
        print(f"{key}: {(result.stdout or result.stderr).strip().splitlines()[-1:]}", flush=True)
    captions = {k: caption(v) for k, v in LINES.items()}
    (OUT / "lines.js").write_text(
        "// Generated by tools/captain_lines.py. Edit the lines there, not here.\n"
        f"window.CAPTAIN_LINES = {json.dumps(captions, indent=2, ensure_ascii=False)};\n",
        encoding="utf-8",
    )
    print("captions written", flush=True)


if __name__ == "__main__":
    main()
