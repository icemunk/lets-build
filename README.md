# Let's Build Something

One static page (`index.html`) that pitches the team on trying the Claude Startups program together, styled as a retro arcade game.
It has no build step, no tracking, no forms and no email links. People just tell you in person.

- The Sea Captain talks you through every stage. His lines live in `tools/captain_lines.py`. To change one, edit it there and run `python tools/captain_lines.py <stage>`. That remakes `assets/captain/<stage>.mp3` and the captions in `assets/captain/lines.js` (it needs the local Qwen3-TTS studio running). The ⚓ button turns automatic narration off, and each stage has a CAPTAIN'S TAKE replay button.
- It plays like a game menu: a title screen, then 8 stages shown one at a time. You move with NEXT / BACK, the ← → keys, swiping, or the ☰ MENU stage select. Each stage has its own link (for example `#powerups`), and the browser Back button works.
- Colleagues type their name into a player slot. Names are saved only in their own browser (`localStorage`) and aren't sent anywhere yet.
- All the interactive parts are in one inline script: 8-bit sound effects, the score, the CONTINUE? countdown, and the Konami code (or tap the logo 5 times). Without JavaScript, it falls back to one long scrolling page.

## Before sharing
- Re-check the program numbers at https://claude.com/programs/startups. They were last checked 2026-10-08.
- Keep `PROJECT_CONTEXT.md` out of the public repo. It contains internal and tax notes.

## Preview locally
Run `python -m http.server 8000` and go to http://localhost:8000.

## Publish on GitHub Pages
1. Create a repo (for example `icemunk/lets-build`) and push `index.html` and `README.md`.
2. Go to Settings → Pages → Deploy from branch → `main` / root.
3. The page goes live at `https://icemunk.github.io/<repo>/`.
