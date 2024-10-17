import os, requests, time
from dotenv import load_dotenv

load_dotenv()

# Ініціалізація бота
TG_BOT_TOKEN = os.getenv("BOT_TOKEN")
TG_BOT_BASE_URL = os.getenv("TG_URL")
TG_BOT_URL = f"{TG_BOT_BASE_URL}/bot{TG_BOT_TOKEN}/"

# Ініціалізація чата ЖПТ
CHATGPT_API_KEY = os.getenv("OPENAI_API_KEY")
CHATGPT_URL = os.getenv("OPENAI_URL")


# Функція отримання оновлень з бота
def get_updates(offset=None):
    url = TG_BOT_URL + "getUpdates"
    params = {"timeout" : 100, "offset" : offset}
    response = requests.get(url, params=params)
    return response.json()

# Функція надсилання юзеру повідомлення:
def send_message(chat_id, text):
    url = TG_BOT_URL + "sendMessage"
    params = {"chat_id" : chat_id, "text" : text}
    requests.get(url, params=params)

# Функція надислання запитання -- отримання відповіді від чату ЖПТ
def get_chatgpt_response(prompt): 
    headers = {
        'Authorization': f"Bearer {CHATGPT_API_KEY}",
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{
            'role': 'user',
            'content': prompt
        }],
        'max_tokens': 100
    }

    response = requests.post(CHATGPT_URL, headers=headers, json=data)
    if response.status_code == 200: 
        return response.json()['choices'][0]['message']['content']
        # return response.json()
    else: 
        return f'Помилка при звернені до ChatGPT: \n status code: {response.status_code} \n {response.json()}'

# Функція обробки повідомлень:
def main():
    last_update_id = None

    while True:
        updates = get_updates(offset=last_update_id)

        if "result" in updates:
            print(updates)
            for update in updates["result"]:
                if "message" in update:
                    chat_id = update["message"]["chat"]["id"]
                    text = update["message"].get("text", "")

                    send_message(chat_id, f"Запит до СhatGPT  в обробці")
                    gpt_response = get_chatgpt_response(text)
                    send_message(chat_id, f"Відповідь СhatGPT: \n{gpt_response}")
                    
                    last_update_id = update["update_id"] + 1
        time.sleep(1)

if __name__ == '__main__':
    main()