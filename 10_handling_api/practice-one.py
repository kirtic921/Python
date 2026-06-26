import requests

def fetch_jokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        info = data["data"]
        content = info["data"][0]["content"]
        return content
    else:
        EXCEPTION("Failed in fetching data!")
        
def main():
    try:
        joke = fetch_jokes()
        print(joke)
    except Exception as e:
        print(str(e))
        
if __name__ == "__main__":
    main()
    