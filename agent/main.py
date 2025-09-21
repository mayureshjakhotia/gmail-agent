import argparse
from core import event_agent

def main():
    parser = argparse.ArgumentParser(
        description="Gmail Event Agent: Scan or list events from Gmail",
        epilog="Example: python -m agent.main --mode show --query 'important' --limit 20"
    )
    parser.add_argument(
        "--limit", 
        type=int, 
        default=10, 
        help="Maximum number of events to retrieve or scan (default: 10)"
    )
    parser.add_argument(
        "--mode", 
        choices=["scan", "show"],
        default="show",
        help="Operation mode: 'scan' for detailed analysis, 'show' for showing events (default: show)"
    )

    args = parser.parse_args()
    event_agent.run(args.limit, args.mode)

if __name__ == "__main__":
    main()
