import argparse


def main() -> None:
    parser = argparse.ArgumentParser(prog="huddle")
    subparsers = parser.add_subparsers(dest="command", required=True)

    coordinator_parser = subparsers.add_parser("coordinator")
    coordinator_parser.add_argument("action", choices=["start"])

    agent_parser = subparsers.add_parser("agent")
    agent_parser.add_argument("action", choices=["join"])
    agent_parser.add_argument("tunnel_url", nargs="?")
    agent_parser.add_argument("--token", default=None)

    args = parser.parse_args()

    if args.command == "coordinator":
        print("coordinator: not implemented yet")
    elif args.command == "agent":
        print("agent: not implemented yet")


if __name__ == "__main__":
    main()