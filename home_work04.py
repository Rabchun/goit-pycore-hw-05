import json
import datetime

def save_contacts(contacts):
    with open("contacts.json", "w") as f:
        json.dump(contacts, f)


def load_contacts():
    try:
        with open("contacts.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            error_message = {
                KeyError: "Контакт не знайдений.",
                ValueError: "Неправильний формат вводу. Спробуйте ще раз.",
                IndexError: "Невірний індекс.",
            }.get(type(e), "Сталася помилка.")
            return error_message

    return inner


@input_error
def add_contact(name, phone):
    contacts[name] = phone
    save_contacts(contacts)
    return f"Контакт {name} з номером {phone} додано."


@input_error
def find_contact(name):
    return contacts.get(name, "Контакт не знайдено.")


@input_error
def list_contacts():
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "Список контактів порожній."


@input_error
def edit_contact(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        save_contacts(contacts)
        return f"Номер телефону контакту {name} змінено на {new_phone}."
    else:
        return "Контакт не знайдено."


@input_error
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        return f"Контакт {name} видалено."
    else:
        return "Контакт не знайдено."


@input_error
def search_contacts(substring):
    results = []
    for name, phone in contacts.items():
        if substring.lower() in name.lower() or substring.lower() in phone.lower():
            results.append(f"{name}: {phone}")
    if results:
        return "\n".join(results)
    else:
        return f"Контактів з підрядком '{substring}' не знайдено."


@input_error
def show_birthday(name):
    if name in contacts:
        try:
            birthday = datetime.datetime.strptime(contacts[name]["birthday"], "%Y-%m-%d").strftime("%d.%m.%Y")
            return f"День народження {name}: {birthday}"
        except KeyError:
            return f"У контакту {name} не вказано дату народження."
        except ValueError:
            return "Неправильний формат дати народження."
    else:
        return "Контакт не знайдено."


@input_error
def add_birthday(name, birthday):
    try:
        datetime.datetime.strptime(birthday, "%Y-%m-%d")
    except ValueError:
        return "Неправильний формат дати народження. (Використовуйте формат YYYY-MM-DD)"

    if name in contacts:
        contacts[name]["birthday"] = birthday
        save_contacts(contacts)
        return f"Додано день народження {birthday} для контакту {name}."
    else:
        return "Контакт не знайдено."


def exit_bot():
    print("До побачення!")
    return True


def get_command():
    command = input("Введіть команду: ").lower()
    return command.split()


def main():
    contacts = load_contacts()

    while True:
        command = get_command()

        if command[0] == "додати":
            if len(command) == 3:
                name, phone = command[1:]
                print(add_contact(name, phone))
            else:
                print("Неправильна кількість аргументів. Спробуйте: додати <ім'я> <номер телефону>")