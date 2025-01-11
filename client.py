import requests

def get_openai_response():
    response=requests.post("http://localhost:8000/poem/invoke",
                           json={'input':{'topic':"indian culture"}}
                           )
    return response.json()
if __name__=="__main__":
    print(get_openai_response())
