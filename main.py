import argparse
from avatar.main_logic import main_logic

def main():
    parser = argparse.ArgumentParser(description="Real Avatar Script")
    parser.add_argument('--mode', type=str, choices=['train', 'inference'], required=True, help="Mode: 'train' or 'inference'")

    args = parser.parse_args()

    if args.mode == 'train':
        main_logic()
    elif args.mode == 'inference':
        # Add inference logic if needed
        pass
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()
