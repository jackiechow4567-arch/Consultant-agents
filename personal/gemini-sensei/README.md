# Gemini Sensei (Japanese only)

This Gem is a Japanese teacher. It does not use the work consultant agents, MBA notes, investment tools, or product PDFs.

Gemini cannot see Cursor. Upload only Japanese-lesson files.

## Upload to the Gem

1. Open [Gemini Gems](https://gemini.google.com/gems/view) on your **personal** Google account.
2. Gem name: `Sensei`.
3. Paste [gem-instructions.md](gem-instructions.md) into **Instructions**.
4. **Knowledge:** upload the markdown files in [upload-this/](upload-this/). Rebuild with `python pack_for_gemini.py`.
5. That pack is only:
   - the listening-lab clips (N5 / N4 / N3)
   - anything you drop in `personal/japanese-lessons/`
6. Open **this Gem**, then text or **Live**.

Do not upload other repo folders into this Gem.

## Add your own Japanese materials

Put lesson files (`.md`, `.txt`, `.pdf`) in `personal/japanese-lessons/`, run `python pack_for_gemini.py`, then upload the new `upload-this/` files.
