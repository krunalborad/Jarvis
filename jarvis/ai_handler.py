import requests


RAPIDAPI_KEY = "f7e538ddc1mshb8ab04a1559bd83p195056jsn3f2b861349b3" 
RAPIDAPI_HOST = "cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com"

def ask_rapidapi(query):
    url = "https://cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com/v1/chat/completions" 
    
    headers = {
        "Content-Type": "application/json",
        "x-rapidapi-host": RAPIDAPI_HOST,
        "x-rapidapi-key": RAPIDAPI_KEY
    }
    
    
    payload = {
        "messages": [{"role": "user", "content": query}],
        "model": "gpt-4o",  
        "temperature": 0.9,
        "max_tokens": 256
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
        
            return data['choices'][0]['message']['content']  
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return "Sorry, I could not get a response."
    except Exception as e:
        print(f"Exception occurred: {e}")
        return "Sorry, there was an error processing your request."