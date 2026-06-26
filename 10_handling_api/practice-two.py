import requests

def fetch_products():
    url = "https://api.freeapi.app/api/v1/public/randomproducts?page=1&limit=10&inc=category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid&query=mens-watches"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        info = data["data"]
        cap = info["data"]
        products_list = [pro["category"] for pro in cap[0:3]]
        return products_list
    else:
        EXCEPTION("Failed to load data") 
        
def main():
    try:
        list = fetch_products()
        print(list)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()   