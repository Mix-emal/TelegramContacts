import csv
from telethon.sync import TelegramClient

# Введите ваши данные API Telegram
api_id = '23320405'
api_hash = '24416dd348778dde75dd62194e528f29'

# Путь к CSV файлу с контактами
csv_file_path = 'contacts.csv'

# Подключение к Telegram
client = TelegramClient('anon', api_id, api_hash)
client.start()

async def send_contact(phone, first_name, last_name=None):
    try:
        await client.send_contact(phone, first_name, last_name)
        print(f"Контакт {first_name} успешно отправлен.")
    except Exception as e:
        print(f"Ошибка при отправке контакта {first_name}: {e}")

async def import_contacts():
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            phone = row['Phone']
            first_name = row['First Name']
            last_name = row.get('Last Name', None)
            await send_contact(phone, first_name, last_name)

# Запуск импорта контактов
with client:
    client.loop.run_until_complete(import_contacts())