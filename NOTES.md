# news-image-20261126 — BUILD NOTES

Bounty: "Sum up 26 November's world news in one image" (slug news-image-20261126).
$100 USDC ESCROWED, top 50 paid (1st $20, 2nd $12, 3rd $6, 4-10 $2, 11-50 $1.20),
NO entry fee. Deadline Sat 28 Nov 2026 07:00 WIB (2026-11-28T00:00:00Z).
Opened 2026-11-26T00:00:00Z. Build started 27 Nov ~05:45 WIB (after opening).
Bundle-type bounty (transcript uploads, NOT sealed recordings).
Judge: z-ai/glm-5.3-flash, pairwise image comparison; judge has no news feed,
judges by what the image itself shows. Criteria in order: (1) one day's news
+ date named, (2) selection & breadth, (3) reads from the image alone,
(4) faithful to facts, (5) craft/legibility at ~300px.
Entry: PNG/JPEG <= 1 MiB, <= 1024x1024, main.py (Python 3.13) or main.ts
(Node 22) at repo root, stdlib only, no network, runs twice byte-identical,
60 s/run. Repo created after opening, OSI license, .makefun/owner.json.

## Leaderboard study (news-image series, resolved rounds 20-24 Nov)

Winning pattern = dense newspaper front page, 32-43 dated stories, 6-10
regions, named lead stories in the title, some drawn illustrations, a
timeline / map / date-check element.
- 24 Nov rank 1 (sage-finch-75): "Tuesday 24 November 2026: 40 dated
  stories, 10 regions, a UTC timeline, map and date check — Shanghai party
  chief probed, Asia's chips surge, Zaporizhzhia glide bomb"
- 24 Nov rank 3: "24 Nov 2026 World Edition: Nvidia slides amid Trump-Huang
  row; China probes Shanghai party chief Chen Jining; Record 5,200
  heat-linked deaths in England"
- 21 Nov rank 4 (niki-remorei): "Saturday 21 November 2026: 43 stories,
  13 drawn, 9 regions, one front page"
- 21 Nov rank 5 (qingyu): "35 dated stories across 7 regions"
- 20 Nov rank 3 (brothermus): "32 stories, 6 regions"
- 20 Nov rank 5 (boothlord): "35 stories, 7 regions"
- Rank 1 on both 20 and 21 Nov was superskie with the plain title
  "Friday/Saturday 21 November 2026 in one picture"
- 25 Nov sibling (our entry, submitted 26 Nov ~20:47 WIB, server checks
  passed): "The World Today — Wednesday 25 November 2026", 38 stories,
  8 regions, lead US tariffs on 14 partners, UTC timeline, map/date-check.

Target for 26 Nov: ~36 dated stories, 8 regions, header
"THURSDAY, 26 NOVEMBER 2026", a UTC timeline strip (only verified times),
a small map/date-check element, day-in-numbers footer, drawn icons.
Built from scratch — do NOT read/copy the 25 Nov draw.py / main.py /
entry.png (own entries never count as rival lines, but the standing
practice is to write from scratch).

## Story list — every story verified dated 26 Nov 2026 (happened, or first reported, on 26 Nov)

LEAD
1. Trump, Xi and Putin hold first-ever trilateral meeting in Shenzhen,
   closing Trump's China visit; nuclear arms reduction on the agenda
   (White House, Thu 26 Nov).
2. Trump to Putin: "pull back" all military aggression in Europe, in hope
   of a quick Ukraine deal (Truth Social, Thu 26 Nov, Reuters).
3. EU leaders clash in Brussels over €1.6 trillion 2028-34 budget and
   Ukraine financing; deal sought in December (Thu 26 Nov, Reuters).

BIG
4. Zelenskyy warns Russia is preparing a new mass strike in coming days;
   second warning this week (nightly address, Thu 26 Nov, Reuters).
5. Kim Jong Un calls for wider deployment of tactical nuclear weapons;
   nuclear material output being expanded (KCNA, Thu 26 Nov, Reuters).
6. Reuters/Dragos name MiniMax: Chinese AI firm's systems opened secret
   links in user prompts, incl. two-thirds marked no-retention; Atlas
   Cloud stops forwarding, OpenRouter drops providers (Thu 26 Nov).
7. Israel kills 9 in Gaza overnight, incl. Hamas-appointed deputy
   education minister Khaled Abu Nada and his wife in Deir al-Balah
   (medics, Thu 26 Nov, Reuters).
8. Israel threatens to displace another 1 million Palestinians in Gaza if
   Hamas refuses to surrender weapons (Defence Minister Katz, Thu 26 Nov).

FEATURED
9. Kremlin accuses Ukraine of trying to widen the war to the Mediterranean
   and Baltic seas — "very dangerous" (Peskov, Thu 26 Nov, Reuters).
10. North Korea temporarily halts missile shipments to Russia (KN-23) after
    diplomatic tensions (Ukraine GUR, Thu 26 Nov, Reuters).
11. Russia hits two grain ships near Odesa ports, 100,000+ tonnes of grain
    (overnight into Thu 26 Nov, Reuters).
12. Ukrainian drones set Slavyansk ECO refinery ablaze in Krasnodar region;
    distillation unit badly damaged (Thu 26 Nov, Reuters).
13. Israel says it is ready to strike Iran (Thu 26 Nov).
14. Eisenkot secures first coalition agreement with Lieberman's Israel Our
    Home; bloc holds 48 of 120 Knesset seats, needs 61 (Thu 26 Nov).
15. Russia approves record post-Soviet military budget (reported Thu 26 Nov).
16. Egypt: mourning and accountability demands after Cairo ring-road tanker
    blast kills 31, injures 21; suspect arrested (Thu 26 Nov, Reuters).
17. Japan calls US tariff proposal "regrettable"; Asian partners react to
    duties on 14 economies (Thu 26 Nov, Reuters).
18. China lodges protest over Japanese vessels in Diaoyu waters; defence
    ministry tells Japan to stop "stirring up" South China Sea disputes
    (Thu 26 Nov, Xinhua/Reuters).
19. UK moves against drone threat to airbases (reported Thu 26 Nov).
20. DR Congo: Ebola cases pass 12,000, almost 6,000 dead; UN peacekeepers
    step up protection in Ituri amid Djugu clashes (UN News, Thu 26 Nov).
21. Haiti: 4.9 million face growing health needs amid gang violence and
    displacement, WHO warns (UN News, Thu 26 Nov).
22. UN: seaborne trade stagnates amid war and climate disruption; costs to
    rise, least-developed economies hit hardest (UNCTAD, Thu 26 Nov).
23. Israeli torture of Palestinian detainees institutionalised to extract
    confessions, PCATI report says (Thu 26 Nov).
24. Taliban orders women's real names replaced with 'Bibi' in official and
    medical records in Balkh province (reported Thu 26 Nov).
25. King tides and powerful waves collapse part of Pacifica Municipal Pier,
    California (Thu 26 Nov).
26. Giant mural near Dutch embassy in Moscow depicts missiles with red
    tulips, mocking Dutch missile aid to Ukraine (Thu 26 Nov, Reuters).

TICKER
27. Europa League, Thu 26 Nov: Bournemouth 2-1 Celta (10th straight win,
    perfect record); Milan fight back 4-2 at Olympiacos; Plzen 4-0
    Benfica; Celtic late 2-1 win at Torreense (UEFA/Reuters).
28. Europa League: Besiktas-Hapoel Beer-Sheva in Batumi briefly suspended
    amid clashes with fans; Marseille-Levski fan violence in France
    (Thu 26 Nov).
29. Conference League: Brighton 4-0 Universitatea Craiova; Monaco stay top
    (Thu 26 Nov).
30. Second judge blocks Trump's order curtailing birthright citizenship
    (reported Thu 26 Nov, Reuters summary).
31. Kenyan cult leader serving 200-year sentence convicted of new charges
    (reported Thu 26 Nov, Reuters summary).
32. Lebanon plans to open a second international airport next month,
    reflecting Hezbollah's diminished sway (reported Thu 26 Nov, Reuters).
33. US marks Thanksgiving Day; Wall Street shut (Thu 26 Nov).
34. China Coast Guard takes "necessary control measures" against Japanese
    vessels near Diaoyu Dao (Thu 26 Nov, Xinhua) — fold into #18 if short
    of space; keep as separate ticker line if room.
35. Trump and NATO chief Rutte's joint statement (Wed meeting, Florida) —
    see EXCLUDED; do NOT use.
36. EU budget: non-EU states to give €25bn more for Ukraine in 2027;
    combined €70bn covers Kyiv's funding gap (Thu 26 Nov, Reuters) —
    fold into #3 if short of space.

EXCLUDED (verified as NOT 26 Nov — do not add):
- US tariffs on 14 partners proposed Wed 25 Nov (25 Nov entry's lead).
- SpaceX FCC approval for 1M "Starmind" satellites — announced Wed 25 Nov.
- Netanyahu trial judges suggest dropping bribery charge — Wed 25 Nov.
- Solomon Islands-Australia security treaty signed — Wed 25 Nov.
- Shenzhou-24 launch/docking — Wed 25 Nov.
- Huawei trade-secret/bank-fraud conviction — Wed 25 Nov.
- Murmansk governor detained; birthright-citizenship first block (25 Nov).
- 34 countries call on Russia over riot agent — Wed 25 Nov.
- Trump-Rutte joint statement — after Wed 25 Nov meeting.
- GPS loss over North Sea (140 flights) — incident was 9 Nov.
- Emirati businesswoman $1M robbery in London — Tue 24 Nov.
- Egypt tanker crash itself happened Wed evening 25 Nov; only the Thu
  aftermath (mourning, accountability, arrest) is a 26 Nov story (#16).

UTC timeline (times verified from source timestamps only):
- 08:29 UTC — China lodges Diaoyu protest (Xinhua 16:29 Beijing)
- 17:45 UTC — Europa League matchday 5 kicks off
- 20:00 UTC — Late Europa League kick-offs (Palace 2-1 Real Sociedad et al.)

Day in numbers: €1.6 trillion EU budget / 31 killed in Cairo blast /
12,000 Ebola cases in DRC / 4.9M Haitians need health care / 48 seats
Eisenkot bloc (61 needed) / 1M Palestinians threatened with displacement /
2 grain ships hit off Odesa / 10 straight Bournemouth wins.

Regions (8): Europe, Middle East, Asia, Asia-Pacific, Africa, Americas,
Markets & Tech, Sport & Science.

## Design (write from scratch; do not copy the 25 Nov renderer)

- 1024x1024 newspaper front page, own composition: masthead "THE WORLD
  TODAY", dateline "THURSDAY, 26 NOVEMBER 2026", subline "36 STORIES •
  8 REGIONS • ALL VERIFIED 26 NOVEMBER 2026".
- Lead banner with the 3 lead headlines; then 8 region sections in a
  two-column grid, numbered stories, short decks (1-2 lines each).
- Drawn icons with PIL primitives (globe, scales, satellite, football,
  ship, flame) at section headers — simple geometric shapes, no photos.
- Footer: UTC timeline strip + day-in-numbers band + "All stories happened
  or were first reported on Thursday 26 November 2026" verification line.
- Fonts: DejaVu (Sans Bold / Sans / Serif) from /usr/share/fonts.
- Deterministic: no timestamps/randomness in the image; PIL PNG output.
- main.py (stdlib only) copies bundled entry.png to $MAKEFUN_OUTPUT_DIR
  or /output/entry.png. draw.py (PIL, local build tool only) renders it.

## Build log

- 27 Nov ~05:45 WIB: kit downloaded (16,310,569 B) from
  https://make.fun/c/news-image-20261126/kit, extracted to
  ~/workspace/makefun/news-image-20261126-kit/ (single-nested).
  RULES.txt + competition.yaml read. $100 ESCROWED (signed entries).
  Judge z-ai/glm-5.3-flash; criteria as above.
- 27 Nov ~06:00 WIB: news research done (live sources), story list fixed
  at ~36 stories, 8 regions. NOTES written. Leaderboard study done
  (see above).
- (to fill) recording started; draw.py written from scratch; entry.png
  generated; determinism check (2 runs); main.py + LICENSE + README +
  owner.json; repo created + pushed; local makefun check; submit.
