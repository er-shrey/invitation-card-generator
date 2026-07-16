# Invitation Card Generator

Generates personalized wedding/event invitation cards as PDFs by overlaying each recipient's address (read from a CSV file) onto a template image, then combining it with cover/back pages into a per-recipient PDF.

## Tech Stack

- Python 2 (uses `print` statements and `.read('rb')` mode — **not** Python 3 compatible as written)
- [Pillow](https://pypi.org/project/Pillow/) (`PIL`) — draws text onto the card image
- [fpdf](https://pypi.org/project/fpdf/) — assembles JPG pages into a PDF

## Project Contents

- `imageToText.py` — reads `address.csv`, draws each recipient's address onto a copy of `2.jpg` using the `Beyond Wonderland.ttf` font, saves it as `<filename>.jpg`, then stitches `1.jpg` + `<filename>.jpg` + `3.jpg` into `<filename>.pdf`.
- `imageToPdf.py` — same PDF assembly step alone (assumes the per-recipient JPGs already exist).
- `address.csv` — input data with columns `sno,name,address1,address2,address3,filename` (currently only the header row, no data).
- `1.jpg`, `2.jpg`, `3.jpg` — front cover, address page template, and back cover images for the card.
- `Beyond Wonderland.ttf` — decorative font used for the address text.

## Prerequisites

- Python 2.7 (the scripts use Python 2 `print` and binary-mode `open()` syntax; port to Python 3 first if you only have Python 3 available)

## Installation

```bash
pip install Pillow fpdf
```

## Usage

1. Fill in `address.csv` with one row per recipient: `sno,name,address1,address2,address3,filename`.
2. Generate the address images and PDFs:

```bash
python imageToText.py
```

This produces `<filename>.jpg` (address page) and `<filename>.pdf` (final 3-page invitation) for every row in `address.csv`.

3. If the address JPGs already exist and you only need to (re)build the PDFs:

```bash
python imageToPdf.py
```

## Notes

- Text position is hardcoded (`xAxis = 500`, y-offsets 900–1300) to match the layout of `2.jpg` — adjust these in `imageToText.py` if you use a different template image size.
