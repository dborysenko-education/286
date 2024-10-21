import os, requests, time, base64
from dotenv import load_dotenv

load_dotenv()

# Ініціалізація бота
TG_BOT_TOKEN = os.getenv("BOT_TOKEN")
TG_BOT_BASE_URL = os.getenv("TG_URL")
TG_BOT_URL = f"{TG_BOT_BASE_URL}/bot{TG_BOT_TOKEN}/"

# Ініціалізація чата ЖПТ
CHATGPT_API_KEY = os.getenv("OPENAI_API_KEY")
CHATGPT_URL = os.getenv("OPENAI_URL")

# Ініціалізація Google Vision AI
GOOGLE_VISION_API_KEY = os.getenv("GOOGLE_VISION_AI_API_KEY")
GOOGLE_VISION_URL = os.getenv("GOOGLE_VISION_AI_API_KEY")


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
        'max_tokens': 1000
    }

    response = requests.post(CHATGPT_URL, headers=headers, json=data)
    if response.status_code == 200: 
        return response.json()['choices'][0]['message']['content']
        # return response.json()
    else: 
        return f'Помилка при звернені до ChatGPT: \n status code: {response.status_code} \n {response.json()}'

# Функція для завантаження зображення
def download_file(file_id):
    # Отримуємо шлях до файлу
    file_url = f'{TG_BOT_URL}getFile?file_id={file_id}'
    file_response = requests.get(file_url)
    file_path = file_response.json()['result']['file_path']

    # Завантажуємо файл
    download_url = f'https://api.telegram.org/file/bot{TG_BOT_TOKEN}/{file_path}'
    file_data = requests.get(download_url)

    # Зберігаємо файл
    file_name = 'downloaded_image.jpg'
    with open(file_name, 'wb') as f:
        f.write(file_data.content)

    return file_name

#Функція для відправки зображення в Google Vision AI
def send_to_google_vision(image_content):
    url = GOOGLE_VISION_URL + GOOGLE_VISION_API_KEY
    image_base64 = base64.b64encode(image_content).decode('utf-8')
    request_data = {
        "requests": [
            {
                "image": {
                    "content": image_base64
                },
                "features": [
                    {
                        "type": "TEXT_DETECTION"  # Наприклад, розпізнавання тексту
                    }
                ]
            }
        ]
    }

    response = requests.post(url, json=request_data)
    return response.json()
    
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

                    message = update['message'] 
                    if 'photo' in message:
                        # Отримуємо ID найбільшої версії зображення
                        file_id = message['photo'][-1]['file_id']

                        # Завантажуємо зображення
                        file_path = download_file(file_id)

                        image_content = download_file(file_path)

                        # Відправляємо зображення до Google Vision для обробки
                        vision_result = send_to_google_vision(image_content)

                        # Отримуємо результат і надсилаємо його користувачу
                        if 'textAnnotations' in vision_result['responses'][0]:
                            detected_text = vision_result['responses'][0]['textAnnotations'][0]['description']
                            send_message(chat_id, f"Розпізнаний текст: {detected_text}")
                        else:
                            send_message(chat_id, "Текст не розпізнано")
        time.sleep(1)

if __name__ == '__main__':
    main()