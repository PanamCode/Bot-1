from datetime import datetime

import gspread
from google.oauth2.service_account import Credentials

from bot.config import settings

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


def get_worksheet():
    creds = Credentials.from_service_account_file(
        settings.google_credentials_path,
        scopes=SCOPES,
    )
    client = gspread.authorize(creds)
    spreadsheet = client.open_by_key(settings.spreadsheet_id)
    return spreadsheet.sheet1


def save_application(
    name: str,
    phone: str,
    comment: str,
    user_id: int,
    username: str | None,
) -> None:
    ws = get_worksheet()

    # Если таблица пустая — добавляем заголовки
    if not ws.get_all_values():
        ws.append_row(["Дата", "Имя", "Телефон", "Комментарий", "User ID", "Username"])

    now = datetime.now().strftime("%d.%m.%Y %H:%M")

    ws.append_row([
        now,
        name,
        phone,
        comment or "—",
        str(user_id),
        f"@{username}" if username else "—",
    ])
