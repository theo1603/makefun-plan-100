"""Write the plan to /output/entry.txt.

Deterministic, no network, no randomness: the same run always writes
the same text.
"""

import os

TEXT = (
    "Day 1: list a $49 Fiverr gig: 'your website into an AI chatbot in 24h.' "
    "$20 on API credits, $30 promoting it. One RAG template answers "
    "from client docs, ~40 min per bot. Email 50 Shopify stores daily "
    "via BuiltWith. A sale a day from day 7: likeliest day 30, "
    "~$850 kept."
)


def main() -> None:
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
