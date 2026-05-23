import sys

def main():
    phone_number = sys.stdin.read().strip()
    
    if phone_number.startswith("555"):
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()
