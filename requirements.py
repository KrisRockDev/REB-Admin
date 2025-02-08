import subprocess


def upgrade_pip():
    try:
        # Выполнение команды pip install --upgrade pip setuptools python-dotenv
        subprocess.run(["pip", "install", "--upgrade", "pip", "setuptools", "python-dotenv"], check=True)
        print("Пакеты 'pip' и 'setuptools' успешно обновлены.")
    except subprocess.CalledProcessError as e:
        print(f"Произошла ошибка: {e}")


def save_requirements():
    try:
        # Выполнение команды pip freeze и запись в файл requirements.txt
        with open("requirements.txt", "w") as f:
            subprocess.run(["pip", "freeze"], stdout=f, check=True)
        print("Файл requirements.txt успешно создан.")
    except subprocess.CalledProcessError as e:
        print(f"Произошла ошибка: {e}")


def install_requirements():
    try:
        # Выполнение команды pip install -r requirements.txt
        print("Устанавливаю зависимости из requirements.txt")
        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
        print("Зависимости из requirements.txt установлены")
    except subprocess.CalledProcessError as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    # upgrade_pip()
    save_requirements()
    # install_requirements()