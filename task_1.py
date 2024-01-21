import queue
import time

def generate_request(request_queue, request_id):
    """Функція для генерації нових заявок"""
    request_id += 1
    request = f"Заявка {request_id}"
    request_queue.put(request)
    print(f"Генерування заявки та додавання до черги: {request}")
    return request_id

def process_request(request_queue):
    """Функція для обробки заявок"""
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Обробка заявки: {request}")
    else:
        print("Черга пуста")

# Ініціалізація черги заявок
request_queue = queue.Queue()
request_id = 0

# Головний цикл програми
try:
    while True:
        # Генерація нових заявок
        request_id = generate_request(request_queue, request_id)

        # Обробка заявок
        process_request(request_queue)

        # Імітація затримки між генерацією та обробкою заявок
        time.sleep(1)
except KeyboardInterrupt:
    print("Програма зупинена користувачем")
