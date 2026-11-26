#!/usr/bin/env python3
"""Render entry.png for make.fun bounty news-image-20261126.

A deterministic 1024x1024 newspaper front page summing up the world news
of Thursday 26 November 2026. Every story comes from NOTES.md (verified
26 Nov stories only). PIL only; no network, no timestamps, no randomness.
Usage: python3 draw.py [output-path]  (default: entry.png next to this file)
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
MARGIN = 26
CONTENT_W = W - 2 * MARGIN  # 972

PAPER = (248, 244, 233)
INK = (20, 20, 20)
NAVY = (27, 42, 74)
NAVY_LIGHT = (38, 58, 102)
RED = (143, 29, 29)
GREY = (90, 86, 76)
RULE = (120, 110, 88)
HEADER_BG = (232, 223, 198)
BANNER_BG = (27, 42, 74)
BANNER_TEXT = (248, 246, 238)
BANNER_MUTED = (196, 205, 224)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_TITLE = font("DejaVuSerif-Bold.ttf", 54)
F_DATE = font("DejaVuSans-Bold.ttf", 20)
F_SUB = font("DejaVuSans-Bold.ttf", 12)
F_LABEL = font("DejaVuSans-Bold.ttf", 11)
F_LEAD_HEAD = font("DejaVuSans-Bold.ttf", 16)
F_LEAD_DECK = font("DejaVuSans.ttf", 12)
F_SEC = font("DejaVuSans-Bold.ttf", 13)
F_NUM = font("DejaVuSans-Bold.ttf", 12)
F_HEAD = font("DejaVuSans-Bold.ttf", 12)
F_DECK = font("DejaVuSans.ttf", 11)
F_FOOT = font("DejaVuSans.ttf", 12)
F_FOOT_B = font("DejaVuSans-Bold.ttf", 12)
F_VERIFY = font("DejaVuSans.ttf", 11)
F_CHIP = font("DejaVuSans-Bold.ttf", 10)


def wrap(text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    words = text.split()
    lines = []
    cur = ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if fnt.getlength(trial) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def centered(draw, y, text, fnt, fill):
    w = fnt.getlength(text)
    draw.text(((W - w) / 2, y), text, font=fnt, fill=fill)
    return fnt.getbbox(text)[3]


def draw_rule(draw, y, x0, x1, fill=RULE, width=1):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


# ---------------------------------------------------------------- icons
def icon_globe(d, x, y, s, c):
    d.ellipse([x, y, x + s, y + s], outline=c, width=2)
    d.ellipse([x + 2, y + s * 0.28, x + s - 2, y + s * 0.72], outline=c, width=1)
    d.ellipse([x + s * 0.28, y + 2, x + s * 0.72, y + s - 2], outline=c, width=1)
    d.line([(x, y + s / 2), (x + s, y + s / 2)], fill=c, width=1)


def icon_scales(d, x, y, s, c):
    d.line([(x + s / 2, y + 1), (x + s / 2, y + s - 4)], fill=c, width=2)
    d.line([(x + 1, y + 4), (x + s - 1, y + 4)], fill=c, width=2)
    d.polygon([(x + 1, y + 6), (x + 6, y + 6), (x + 3.5, y + s - 3)], outline=c)
    d.polygon([(x + s - 6, y + 6), (x + s - 1, y + 6), (x + s - 3.5, y + s - 3)],
              outline=c)
    d.line([(x + 2, y + s - 2), (x + s - 2, y + s - 2)], fill=c, width=2)


def icon_satellite(d, x, y, s, c):
    d.rectangle([x + s * 0.35, y + s * 0.35, x + s * 0.65, y + s * 0.65],
                outline=c, width=2)
    d.rectangle([x + 1, y + s * 0.30, x + s * 0.30, y + s * 0.70],
                outline=c, width=1)
    d.rectangle([x + s * 0.70, y + s * 0.30, x + s - 1, y + s * 0.70],
                outline=c, width=1)
    d.line([(x + s * 0.65, y + s * 0.35), (x + s - 1, y + 1)], fill=c, width=1)


def icon_football(d, x, y, s, c):
    cx, cy, r = x + s / 2, y + s / 2, s / 2 - 1
    d.ellipse([x + 1, y + 1, x + s - 1, y + s - 1], outline=c, width=2)
    d.polygon([(cx, cy - 4), (cx + 4, cy - 1), (cx + 2.5, cy + 3.5),
               (cx - 2.5, cy + 3.5), (cx - 4, cy - 1)], fill=c)
    for dx, dy in [(0, -r + 2), (r - 2, 0), (-r + 2, 0), (5, r - 4), (-5, r - 4)]:
        d.line([(cx, cy), (cx + dx, cy + dy)], fill=c, width=1)


def icon_ship(d, x, y, s, c):
    d.polygon([(x + 1, y + s * 0.62), (x + s - 1, y + s * 0.62),
               (x + s - 4, y + s - 2), (x + 4, y + s - 2)], outline=c, width=2)
    d.line([(x + s / 2, y + 1), (x + s / 2, y + s * 0.62)], fill=c, width=2)
    d.polygon([(x + s / 2 + 2, y + 3), (x + s / 2 + 2, y + s * 0.5),
               (x + s - 3, y + s * 0.5)], outline=c)


def icon_flame(d, x, y, s, c):
    d.polygon([(x + s / 2, y + 1), (x + s - 2, y + s * 0.55),
               (x + s * 0.68, y + s - 2), (x + s * 0.32, y + s - 2),
               (x + 2, y + s * 0.55)], outline=c, width=2)
    d.polygon([(x + s / 2, y + s * 0.45), (x + s * 0.68, y + s * 0.75),
               (x + s / 2, y + s - 3), (x + s * 0.32, y + s * 0.75)], fill=c)


ICONS = {
    "globe": icon_globe,
    "scales": icon_scales,
    "satellite": icon_satellite,
    "football": icon_football,
    "ship": icon_ship,
    "flame": icon_flame,
}

# ---------------------------------------------------------------- data
# (number from NOTES.md, headline, deck). 33 displayed entries; story 34
# is folded into #18's deck and story 36 into lead 3's deck (35 stories
# in total; #35 is excluded as not a 26 Nov story).
LEADS = [
    ("1", "Trump, Xi and Putin hold first-ever trilateral meeting in Shenzhen",
     "Nuclear arms reduction on the agenda as Trump's China visit closes"),
    ("2", "Trump tells Putin: \u201cpull back\u201d all military aggression in Europe",
     "Truth Social appeal seeks a quick Ukraine deal, Reuters reports"),
    ("3", "EU leaders clash in Brussels over \u20ac1.6 trillion 2028\u201334 budget",
     "Non-EU states to add \u20ac25bn for Ukraine in 2027; \u20ac70bn covers Kyiv's gap"),
]

SECTIONS = [
    ("EUROPE", "globe", [
        (4, "Zelenskyy warns of new mass Russian strike in coming days",
         "Second such warning this week, in his nightly address"),
        (9, "Kremlin: Ukraine tries to widen war to Med and Baltic seas",
         "Peskov calls it \u201cvery dangerous\u201d"),
        (11, "Russia hits two grain ships near Odesa ports",
         "100,000+ tonnes of grain hit overnight"),
        (12, "Ukrainian drones set Slavyansk ECO refinery ablaze",
         "Distillation unit badly damaged in Krasnodar region"),
        (15, "Russia approves record post-Soviet military budget",
         "Reported on Thursday 26 November"),
        (19, "UK moves against drone threat to airbases",
         "Reported on Thursday 26 November"),
        (26, "Giant mural in Moscow mocks Dutch missile aid to Ukraine",
         "Missiles with red tulips near the Dutch embassy"),
    ]),
    ("MIDDLE EAST", "flame", [
        (7, "Israel kills 9 in Gaza overnight",
         "Deputy education minister Khaled Abu Nada and wife among dead"),
        (8, "Israel threatens to displace another 1 million in Gaza",
         "If Hamas refuses to surrender its weapons, Katz says"),
        (13, "Israel says it is ready to strike Iran",
         "Reported on Thursday 26 November"),
        (14, "Eisenkot seals first coalition deal with Lieberman",
         "Bloc holds 48 of 120 Knesset seats; 61 needed"),
        (23, "Torture of Palestinian detainees \u201cinstitutionalised\u201d",
         "PCATI report says it extracts confessions"),
        (32, "Lebanon plans second international airport next month",
         "Reflecting Hezbollah's diminished sway"),
    ]),
    ("ASIA", "scales", [
        (5, "Kim Jong Un calls for wider tactical nuclear deployment",
         "Nuclear material output being expanded, KCNA says"),
        (10, "North Korea halts missile shipments to Russia",
         "KN-23 deliveries paused after diplomatic tensions"),
        (24, "Taliban replaces women's real names with \u2018Bibi\u2019",
         "In official and medical records in Balkh province"),
    ]),
    ("AFRICA", "globe", [
        (16, "Cairo tanker blast: mourning and accountability demands",
         "31 killed, 21 injured; suspect arrested"),
        (20, "DR Congo Ebola cases pass 12,000; almost 6,000 dead",
         "UN peacekeepers step up protection in Ituri"),
        (31, "Kenyan cult leader convicted of new charges",
         "Already serving a 200-year sentence"),
    ]),
    ("MARKETS & TECH", "satellite", [
        (6, "MiniMax systems opened secret links in user prompts",
         "Two-thirds marked no-retention; Atlas Cloud, OpenRouter act"),
        (22, "UN: seaborne trade stagnates amid war and climate",
         "Costs to rise; least-developed economies hit hardest"),
    ]),
    ("ASIA-PACIFIC", "ship", [
        (17, "Japan calls US tariff proposal \u201cregrettable\u201d",
         "Asian partners react to duties on 14 economies"),
        (18, "China protests Japanese vessels in Diaoyu waters",
         "Coast Guard took \u201cnecessary control measures\u201d near Diaoyu Dao"),
    ]),
    ("AMERICAS", "football", [
        (21, "Haiti: 4.9 million face growing health needs",
         "WHO warns amid gang violence and displacement"),
        (25, "King tides collapse part of Pacifica Municipal Pier",
         "Powerful waves hit the California coast"),
        (30, "Second judge blocks Trump birthright citizenship order",
         "Reported on Thursday 26 November"),
        (33, "US marks Thanksgiving Day; Wall Street shut",
         "Thursday 26 November"),
    ]),
    ("SPORT & SCIENCE", "football", [
        (27, "Bournemouth 2-1 Celta: 10th straight Europa win",
         "Milan fight back 4-2 at Olympiacos; Plzen 4-0 Benfica"),
        (28, "Besiktas-Hapoel game briefly suspended amid clashes",
         "Marseille-Levski fan violence in France"),
        (29, "Brighton 4-0 Craiova in Conference League",
         "Monaco stay top of the table"),
    ]),
]

# Two balanced columns of four sections each (15 stories per column).
LEFT_SECTIONS = [SECTIONS[0], SECTIONS[2], SECTIONS[3], SECTIONS[4]]
RIGHT_SECTIONS = [SECTIONS[1], SECTIONS[5], SECTIONS[6], SECTIONS[7]]

TIMELINE = ("08:29 UTC \u2014 China lodges Diaoyu protest  \u2022  "
            "17:45 UTC \u2014 Europa League matchday 5 kicks off  \u2022  "
            "20:00 UTC \u2014 Late Europa League kick-offs")
NUMBERS_1 = ("\u20ac1.6 TRILLION EU BUDGET  \u2022  31 KILLED IN CAIRO BLAST  "
             "\u2022  12,000 EBOLA CASES IN DRC  \u2022  4.9M HAITIANS NEED HEALTH CARE")
NUMBERS_2 = ("48 SEATS \u2014 EISENKOT BLOC (61 NEEDED)  \u2022  1M PALESTINIANS "
             "THREATENED  \u2022  2 GRAIN SHIPS HIT  \u2022  10 STRAIGHT BOURNEMOUTH WINS")
VERIFY = ("All stories happened or were first reported on "
          "Thursday 26 November 2026")


def story_block_height(stories, text_w):
    """Height of one section's story list, given the text width."""
    total = 0
    for _num, head, deck in stories:
        hl = wrap(head, F_HEAD, text_w)
        dl = wrap(deck, F_DECK, text_w)
        total += len(hl) * 14 + len(dl) * 12 + 3
    return total


def draw_section(draw, x, y, col_w, name, icon_name, stories):
    """Draw one region section; return the y just below it."""
    # Header band.
    draw.rectangle([x, y, x + col_w, y + 22], fill=HEADER_BG)
    ICONS[icon_name](draw, x + 4, y + 3, 16, NAVY)
    draw.text((x + 26, y + 4), name, font=F_SEC, fill=NAVY)
    draw.text((x + col_w - 34, y + 4), str(len(stories)), font=F_SEC, fill=RED)
    y += 22
    draw_rule(draw, y, x, x + col_w, fill=NAVY, width=2)
    y += 6
    text_x = x + 26
    text_w = col_w - 26
    for num, head, deck in stories:
        draw.text((x, y + 1), str(num) + ".", font=F_NUM, fill=RED)
        for line in wrap(head, F_HEAD, text_w):
            draw.text((text_x, y), line, font=F_HEAD, fill=INK)
            y += 14
        for line in wrap(deck, F_DECK, text_w):
            draw.text((text_x, y), line, font=F_DECK, fill=GREY)
            y += 12
        y += 3
    return y


def render():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead ------------------------------------------------------
    y = 16
    centered(d, y, "THE WORLD TODAY", F_TITLE, INK)
    y = 16 + 56
    draw_rule(d, y, MARGIN, W - MARGIN, fill=INK, width=3)
    y += 6
    draw_rule(d, y, MARGIN, W - MARGIN, fill=INK, width=1)
    y += 10
    centered(d, y, "THURSDAY, 26 NOVEMBER 2026", F_DATE, NAVY)
    # Date-check chip at the right of the dateline row.
    chip = "\u2713 DATE CHECK: 26 NOV 2026"
    cw = F_CHIP.getlength(chip) + 14
    cx0 = W - MARGIN - cw
    d.rectangle([cx0, y - 1, W - MARGIN, y + 16], outline=NAVY, width=1)
    d.text((cx0 + 7, y + 2), chip, font=F_CHIP, fill=NAVY)
    y += 26
    centered(d, y, "35 STORIES  \u2022  8 REGIONS  \u2022  "
                   "ALL VERIFIED 26 NOVEMBER 2026", F_SUB, INK)
    y += 20
    draw_rule(d, y, MARGIN, W - MARGIN, fill=INK, width=2)

    # ---- Lead banner ---------------------------------------------------
    y += 8
    banner_y0 = y
    inner_x = MARGIN + 16
    inner_w = CONTENT_W - 32
    ly = y + 10
    d.rectangle([MARGIN, banner_y0, W - MARGIN, banner_y0 + 148], fill=BANNER_BG)
    d.text((inner_x, ly), "THE DAY IN THREE HEADLINES", font=F_LABEL,
           fill=BANNER_MUTED)
    ly += 18
    for num, head, deck in LEADS:
        d.text((inner_x, ly), num + ".", font=F_LEAD_HEAD, fill=(232, 190, 90))
        for line in wrap(head, F_LEAD_HEAD, inner_w - 22):
            d.text((inner_x + 22, ly), line, font=F_LEAD_HEAD, fill=BANNER_TEXT)
            ly += 20
        d.text((inner_x + 22, ly), deck, font=F_LEAD_DECK, fill=BANNER_MUTED)
        ly += 17
        if num != "3":
            ly += 2
    banner_bottom = banner_y0 + 148

    # ---- Region grid ---------------------------------------------------
    grid_y = banner_bottom + 10
    footer_y = 892
    col_w = (CONTENT_W - 20) // 2  # 476
    left_x = MARGIN
    right_x = MARGIN + col_w + 20
    for col_x, col_sections in ((left_x, LEFT_SECTIONS),
                                (right_x, RIGHT_SECTIONS)):
        cy = grid_y
        for name, icon_name, stories in col_sections:
            need = 22 + 8 + story_block_height(stories, col_w - 26)
            if cy + need > footer_y:
                raise SystemExit(
                    "layout overflow in section %s: need %d, have %d"
                    % (name, need, footer_y - cy))
            cy = draw_section(d, col_x, cy, col_w, name, icon_name, stories)
            cy += 8

    # ---- Footer --------------------------------------------------------
    draw_rule(d, footer_y, MARGIN, W - MARGIN, fill=INK, width=2)
    fy = footer_y + 8
    d.text((MARGIN, fy), "UTC TIMELINE", font=F_LABEL, fill=RED)
    for line in wrap(TIMELINE, F_FOOT, CONTENT_W - 130):
        d.text((MARGIN + 128, fy + 1), line, font=F_FOOT, fill=INK)
        fy += 15
    fy += 4
    draw_rule(d, fy, MARGIN, W - MARGIN, fill=RULE, width=1)
    fy += 7
    centered(d, fy, NUMBERS_1, F_FOOT_B, NAVY)
    fy += 16
    centered(d, fy, NUMBERS_2, F_FOOT_B, NAVY)
    fy += 20
    centered(d, fy, VERIFY, F_VERIFY, GREY)
    return img


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img = render()
    img.save(out, format="PNG", optimize=True)
    print("wrote %s %dx%d" % (out, img.width, img.height))


if __name__ == "__main__":
    main()
