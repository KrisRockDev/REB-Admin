import os
import sys
import fnmatch
from pathlib import Path

SCRIPT_NAME = os.path.basename(sys.argv[0])
OUTPUT_FILE = f"{SCRIPT_NAME[:-3]}.md"

# Игнорируемые папки и файлы по умолчанию
DEFAULT_IGNORE = [".git", ".idea", "__pycache__", "venv", "env", "node_modules", ".venv", ".gitignore", ".dockerignore", "LICENSE.md", "README.md", "requirements.txt", "requirements.py"]

# Файлы, которые нужно исключить из обработки
EXCLUDED_FILES = [OUTPUT_FILE, SCRIPT_NAME, "README.md", "requirements.txt", "requirements.py"]


def load_ignore_patterns(ignore_file):
    """Загружает шаблоны из файла .gitignore или .dockerignore."""
    if not os.path.exists(ignore_file):
        return []
    with open(ignore_file, "r", encoding="utf-8") as f:
        patterns = []
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                # Преобразуем шаблоны .gitignore/.dockerignore в формат, понятный fnmatch
                if line.startswith("/"):
                    line = line[1:]  # Убираем ведущий слэш
                if line.endswith("/"):
                    line = line[:-1]  # Убираем trailing слэш для директорий
                patterns.append(line)
        return patterns


def should_ignore(path, ignore_patterns):
    """Проверяет, должен ли файл или папка быть проигнорированы."""
    # Проверяем, находится ли файл в списке исключений
    if os.path.basename(path) in EXCLUDED_FILES:
        return True
    # Проверяем шаблоны из .gitignore, .dockerignore и DEFAULT_IGNORE
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(path, pattern) or fnmatch.fnmatch(os.path.basename(path), pattern):
            return True
        if "/" in pattern or "\\" in pattern:
            if fnmatch.fnmatch(path, pattern):
                return True
    return False


def collect_files(root_dir, gitignore_patterns, dockerignore_patterns):
    """Собирает все файлы, которые не должны быть проигнорированы."""
    collected_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Удаляем игнорируемые папки из списка для обхода
        dirnames[:] = [
            d for d in dirnames
            if not should_ignore(os.path.relpath(os.path.join(dirpath, d), root_dir),
                                 DEFAULT_IGNORE + gitignore_patterns + dockerignore_patterns)
        ]
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            relative_path = os.path.relpath(file_path, root_dir)
            if not should_ignore(relative_path, DEFAULT_IGNORE + gitignore_patterns + dockerignore_patterns):
                collected_files.append(relative_path)
    return collected_files


def create_markdown(root_dir):
    """Создает Markdown-документ с содержимым всех файлов."""
    gitignore_patterns = load_ignore_patterns(os.path.join(root_dir, ".gitignore"))
    dockerignore_patterns = load_ignore_patterns(os.path.join(root_dir, ".dockerignore"))

    files = collect_files(root_dir, gitignore_patterns, dockerignore_patterns)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as md_file:
        for file in files:
            md_file.write(f"### {file}\n```\n")
            try:
                with open(os.path.join(root_dir, file), "r", encoding="utf-8") as f:
                    md_file.write(f.read().strip())
            except UnicodeDecodeError:
                # Пропускаем бинарные файлы или файлы с неподдерживаемой кодировкой
                print("Бинарный файл или неподдерживаемая кодировка", file)
            md_file.write("\n```\n\n")


if __name__ == "__main__":
    project_root = os.getcwd()  # Корневой каталог проекта
    create_markdown(root_dir=project_root)
