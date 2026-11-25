"""Write one Wi-Fi network name (≤32 chars) to /output/entry.txt."""

from pathlib import Path

LINE = "SheLeftIKeptTheWiFi"


def main() -> None:
    assert isinstance(LINE, str) and LINE.strip() == LINE
    assert 1 <= len(LINE) <= 32
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
