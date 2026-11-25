from pathlib import Path

LINE = "She waved. Train left. Gone."


def main() -> None:
    assert isinstance(LINE, str)
    assert len(LINE) <= 32
    assert len(LINE) > 0
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
