# Використовуючи модуль sqlite3 та модуль smtplib, реалізуйте реальне додавання користувачів до бази. Мають бути реалізовані
# такі функції та класи:
# ·        клас користувача, що містить у собі такі методи: get_full_name (ПІБ з поділом через пробіл: «Петров Ігор Сергійович»),
# get_short_name (формату ПІБ: «Петров І. С.»), get_age (повертає вік користувача, використовуючи поле birthday типу datetime.date);
# метод __str__ (повертає ПІБ та дату народження);
# ·        функція реєстрації нового користувача (приймаємо екземпляр нового користувача та відправляємо email на пошту
# користувача з листом подяки).
# ·        функція відправлення email з листом подяки.
# ·        функція пошуку користувачів у таблиці users за іменем, прізвищем і поштою.

# Протестувати цей функціонал, використовуючи заглушки у місцях надсилання пошти. Під час штатного запуску програми вона має
# відправляти повідомлення на вашу реальну поштову скриньку (необхідно налаштувати SMTP, використовуючи доступи від провайдера
# вашого email-сервісу).
import sqlite3
import datetime
import smtplib
from pathlib import Path
from email.message import EmailMessage


db_file = Path(__file__).parent / "reg_users.db"

# Налаштування SMTP (підстав свої дані)
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"


class User:
    def __init__(self, last_name: str, first_name: str,
                 middle_name: str, birthday: datetime.date,
                 email: str, user_id: int | None = None):
        self.id = user_id
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.birthday = birthday
        self.email = email

    # ---------- Getter / Setter ----------

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = self.__validate_name(value, "last name")

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = self.__validate_name(value, "first name")

    @property
    def middle_name(self):
        return self.__middle_name

    @middle_name.setter
    def middle_name(self, value):
        self.__middle_name = self.__validate_name(value, "middle name")

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, value):
        self.__birthday = self.__validate_birthday(value)

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = self.__validate_email(value)

    # ---------- Валідатори ----------

    @staticmethod
    def __validate_name(value, field_name):
        if not isinstance(value, str):
            raise ValueError(f"{field_name} must be a string")
        value = value.strip()
        if not value:
            raise ValueError(f"{field_name} cannot be empty")
        return value

    @staticmethod
    def __validate_birthday(value):
        if not isinstance(value, datetime.date):
            raise ValueError("birthday must be a datetime.date object")
        if value > datetime.date.today():
            raise ValueError("birthday cannot be in the future")
        return value

    @staticmethod
    def __validate_email(value):
        if not isinstance(value, str):
            raise ValueError("email must be a string")
        value = value.strip()
        if "@" not in value or "." not in value:
            raise ValueError("email is not valid")
        return value

    # ---------- Читання з бази ----------

    def _fetch_record(self) -> tuple | None:
        """Дістає рядок користувача з бази за його id."""
        if self.id is None:
            raise ValueError("User has no id — cannot fetch from database")

        with sqlite3.connect(db_file) as conn:
            return conn.execute(
                "SELECT * FROM users WHERE id = ?", (self.id,)
            ).fetchone()

    def get_full_name(self) -> str:
        row = self._fetch_record()
        if row is None:
            raise ValueError(f"User with id {self.id} not found")
        return f"{row[1]} {row[2]} {row[3]}"

    def get_short_name(self) -> str:
        row = self._fetch_record()
        if row is None:
            raise ValueError(f"User with id {self.id} not found")
        return (
            f"{row[1]} "
            f"{row[2][0].upper()}. "
            f"{row[3][0].upper()}."
        )

    def get_age(self) -> int:
        row = self._fetch_record()
        if row is None:
            raise ValueError(f"User with id {self.id} not found")

        birthday = datetime.date.fromisoformat(row[4])
        today = datetime.date.today()
        age = today.year - birthday.year
        if (today.month, today.day) < (birthday.month, birthday.day):
            age -= 1
        return age

    def __str__(self) -> str:
        return (
            f"{self.get_full_name()}, "
            f"дата народження: {self.birthday.strftime('%d.%m.%Y')}"
        )


# ---------- Робота з базою ----------

def init_db() -> None:
    with sqlite3.connect(db_file) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                last_name TEXT NOT NULL,
                first_name TEXT NOT NULL,
                middle_name TEXT NOT NULL,
                birthday TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)
        conn.commit()


def add_user_to_db(user: User) -> None:
    """Зберігає користувача в базу і присвоює йому id."""
    with sqlite3.connect(db_file) as conn:
        cursor = conn.execute(
            """
            INSERT INTO users (last_name, first_name, middle_name,
                               birthday, email)
            VALUES (?, ?, ?, ?, ?)
            """,
            (user.last_name, user.first_name, user.middle_name,
             user.birthday.isoformat(), user.email)
        )
        conn.commit()
        user.id = cursor.lastrowid   # ← ключовий момент: id тепер заповнений


# ---------- Відправлення email ----------

def send_thank_email(user: User) -> None:
    message = EmailMessage()
    message["Subject"] = "Дякуємо за реєстрацію!"
    message["From"] = SENDER_EMAIL
    message["To"] = user.email
    message.set_content(
        f"Шановний(а) {user.get_short_name()}!\n\n"
        f"Дякуємо за реєстрацію у нашій системі.\n"
        f"Ваші дані успішно збережено.\n\n"
        f"З повагою, команда підтримки."
    )

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(message)


# ---------- Реєстрація користувача ----------

def register_user(user: User) -> None:
    add_user_to_db(user)          # тепер user.id заповнений
    send_thank_email(user)
    print(f"Користувача {user.get_full_name()} зареєстровано, "
          f"лист надіслано на {user.email}")


# ---------- Пошук користувачів ----------

def search_users(last_name: str = "", first_name: str = "",
                 email: str = "") -> list[User]:
    query = "SELECT * FROM users WHERE 1=1"
    params = []

    if last_name:
        query += " AND last_name = ?"
        params.append(last_name)
    if first_name:
        query += " AND first_name = ?"
        params.append(first_name)
    if email:
        query += " AND email = ?"
        params.append(email)

    with sqlite3.connect(db_file) as conn:
        rows = conn.execute(query, params).fetchall()

    users = []
    for row in rows:
        users.append(User(
            last_name=row[1],
            first_name=row[2],
            middle_name=row[3],
            birthday=datetime.date.fromisoformat(row[4]),
            email=row[5],
            user_id=row[0],       # ← id заповнюється з бази
        ))
    return users


# ---------- Приклад використання ----------

if __name__ == "__main__":
    init_db()

    user = User(
        "Петров", "Ігор", "Сергійович",
        datetime.date(1990, 5, 15),
        "petrov@example.com"
    )

    # register_user(user)  # розкоментуй, щоб реально зареєструвати
    add_user_to_db(user)   # для тесту без email

    # Тепер user.id заповнений, методи читають з бази:
    print("ID:", user.id)
    print(user.get_full_name())   # Петров Ігор Сергійович
    print(user.get_short_name())  # Петров І. С.
    print("Вік:", user.get_age())
    print(user)

    # Пошук повертає об'єкти User з заповненим id
    found = search_users(last_name="Петров")
    for u in found:
        print("Знайдено:", u.get_full_name(), "(id", u.id, ")")