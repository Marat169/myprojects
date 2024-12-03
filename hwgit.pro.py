# Импортируем библиотеку subprocess
import subprocess

# Определяем функцию git_config_list
def git_config_list():
    try:
        # Выполняем команду Git с помощью subprocess.run
        result = subprocess.run(
            ["git", "config", "--global", "--list"],  # Команда Git
            capture_output=True,  # Захватываем вывод
            text=True,  # Вывод в текстовом формате
            check=True  # Проверка на успешное выполнение команды
        )
        # Выводим результат выполнения команды
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        # Выводим сообщение об ошибке, если команда завершилась с ошибкой
        print(f"Ошибка при выполнении команды: {e}")
    except FileNotFoundError:
        # Обрабатываем случай, если Git не установлен
        print("Git не установлен или не найден в PATH.")

# Вызываем функцию git_config_list
git_config_list()