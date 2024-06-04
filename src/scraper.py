import sys

def main():
    username = sys.argv[1]
    
    if username[0] == '@':
        username = username[1:]

    print(f"Scraping threads for {username}...")

if __name__ == "__main__":
    main()
