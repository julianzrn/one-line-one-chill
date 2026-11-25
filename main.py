from pathlib import Path

ENTRY = (
    "My sleep app recorded six hours of me politely answering questions "
    "last night, ending with me spelling out, letter by letter, our new address."
)


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
