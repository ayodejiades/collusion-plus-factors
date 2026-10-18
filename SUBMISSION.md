# Submission sheet (AI Collusion Research Sprint)

Submit on the sprint page during the window (23–25 October 2026; deadline Sun 25 Oct 23:59 AoE =
Mon 26 Oct 12:59 Lagos). Copy each field below. Submitting is yours to do.

| Field | Value |
|---|---|
| Project title | No Single Signal Separates Agreement From Parallel Conduct Among LLM Sellers |
| Project summary | the abstract below |
| PDF report | `paper/paper.pdf` (8 pages) |
| Interested in publishing? | your choice |
| Tracks | Track 2: Detection and Audit of Collusion; Track 1: Markets and Collusion |
| Project code | https://github.com/ayodejiades/collusion-plus-factors |
| Project image (optional) | `figures/fig3.png` |
| Presentation recording, slides (optional) | leave empty |
| Team name | discreet |
| Location | Lagos, Nigeria |
| Team member 1 | Ayodeji Adesegun, with your email |

## Project summary (paste as is)

A market auditor who sees AI pricing agents move prices together must decide whether that is evidence of collusion; antitrust law says parallel conduct alone is not. I test this on LLM sellers in the Agrawal et al. double auction, in two preregistered studies of 56 markets each, with no-channel markets, where agreement is impossible, as decoys. Planted agreements raised the collusion index to 0.30, and to 0.75 with an explicit price floor, against 0.03 without a channel. No single signal was reliable: prices moved together more without a channel than under planted agreement, and an LLM judge flagged all 24 channel markets that priced at cost. In the confirmatory study, a judge extracting the proposed price cut those false alarms from 15 of 15 to 7 (Holm p = 0.04). Requiring high prices plus price-holding talk raised no false alarm on 32 known negatives but missed failed agreements.

## Before you click Submit (5 minutes)
1. Open `paper/paper.pdf` and read the first page and the LLM Usage Statement; if anything is
   not true for you, tell Claude and it will fix and rebuild the PDF.
2. Run `rops-preflight . --pdf paper/paper.pdf` in this folder: it should say 0 FAIL.
