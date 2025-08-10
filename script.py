import requests

def main():
    try:
        r = requests.get("https://www.youtube.com", timeout=5)
        if r.status_code == 200:
            print("YouTube is reachable!")
        else:
            print(f"YouTube returned status code: {r.status_code}")
    except Exception as e:
        print(f"Error reaching YouTube: {e}")

if __name__ == "__main__":
    main()
