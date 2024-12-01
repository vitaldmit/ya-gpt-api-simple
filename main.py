"""
Простейшее приложение для получения ответа от модели YandexGPT Lite.
https://yandex.cloud/ru/docs/foundation-models/quickstart/yandexgpt#api_2
"""

import requests
from secret import IAM_TOKEN, FOLDER_ID


class YandexGPT:
    """
    Класс для работы с API YandexGPT.
    """

    def __init__(self, iam_token: str, folder_id: str) -> None:
        self.iam_token = iam_token
        self.folder_id = folder_id

        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.iam_token}'
        }

    def generate_text(self, prompt: str) -> dict:
        """
        Функция для генерации текста с помощью модели YandexGPT.
        """

        url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'

        data = {
            'modelUri': f'gpt://{self.folder_id}/yandexgpt-lite',
            'completionOptions': {
                'stream': False,
                'temperature': 0.6,
                'maxTokens': '2000'
            },
            'messages': [
                {
                    'role': 'system',
                    'text': (
                        'Найди ошибки в тексте и исправь их. Просто верни '
                        'верни исправленный текст без лишних комментариев.'
                    )
                },
                {
                    'role': 'user',
                    'text': prompt
                }
            ]
        }

        resp = requests.post(
            url, headers=self.headers, json=data, timeout=10
        )

        return resp.json()


# Пример использования
if __name__ == '__main__':
    yandex_gpt = YandexGPT(IAM_TOKEN, FOLDER_ID)

    PROMPT = (
        'Ламинат подойдет для укладки на кухне или в детской комнате – он '
        'не боится влаги и механических повреждений благодаря защитному '
        'слою из облицовочных меламиновых пленок толщиной 0,2 мм '
        'и обработанным воском замкам.'
    )

    response = yandex_gpt.generate_text(PROMPT)

    print(response['result']['alternatives'][0]['message']['text'])
