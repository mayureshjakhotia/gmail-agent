import argparse
from core import event_agent

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--query", type=str, default="event")
    parser.add_argument("--mode", choices=["scan", "list"], default="list")

    args = parser.parse_args()
    event_agent.run(args.query, args.limit, args.mode)

if __name__ == "__main__":
    main()
