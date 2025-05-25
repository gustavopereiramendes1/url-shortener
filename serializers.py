def urlUnique(url) -> dict:
    return{
            "id": str(url["_id"]),
            "originalUrl": url["originalUrl"],
            "shortUrl": url["shortUrl"]
        }
    

def list_Urls(urls) -> list:
    return [urlUnique(url) for url in urls]
