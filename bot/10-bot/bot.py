import os, requests, time
from dotenv import load_dotenv

load_dotenv()

# Ініціалізація бота
TG_BOT_TOKEN = os.getenv("BOT_TOKEN")
TG_BOT_BASE_URL = os.getenv("TG_URL")
TG_BOT_URL = f"{TG_BOT_BASE_URL}/bot{TG_BOT_TOKEN}/"

# Ініціалізація чата ЖПТ



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

                    send_message(chat_id, f"Ви надіслали: {text}")

                    last_update_id = update["update_id"] + 1
        time.sleep(1)

if __name__ == '__main__':
    main()