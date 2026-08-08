from app.core.cli import start_cli


def main():
    print("=" * 50)
    print("AI COMMAND CENTER")
    print("=" * 50)
    print("Model  : llama3.2:3b")
    print("Status : Online")
    print()

    start_cli()


if __name__ == "__main__":
    main()