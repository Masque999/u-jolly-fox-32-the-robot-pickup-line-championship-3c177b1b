import os

LINE = "Beep. I ran a full diagnostic on my heart and the only error is that you are not in my contacts yet."
MAX_CHARS = 200


def main():
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, limit {MAX_CHARS}"
    assert LINE == LINE.strip(), "leading/trailing whitespace"
    assert "\n" not in LINE, "must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(path, encoding="utf-8") as f:
        back = f.read()
    assert back == LINE, "read-back mismatch"
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
