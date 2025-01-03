
# Git Commit Visualizer

Git Commit Visualizer — это Python-утилита для анализа истории коммитов в репозитории Git, связанных с конкретным файлом. Она также генерирует граф изменений коммитов, сохраняя его в формате PNG.

## Основные функции

- **Поиск коммитов**:
  - Определяет все коммиты, связанные с указанным хэшем файла.
- **Визуализация графа**:
  - Создаёт граф изменений в формате PNG с помощью Graphviz.

---

## Установка

1. **Клонирование репозитория**:
   ```bash
   git clone https://github.com/yourusername/git-commit-visualizer.git
   cd git-commit-visualizer
   ```

2. **Установка зависимостей**:
   Убедитесь, что у вас установлен Python 3.6 или выше, и выполните установку необходимых библиотек:
   ```bash
   pip install gitpython graphviz
   ```

3. **Установка Graphviz**:
   Убедитесь, что Graphviz установлен на вашей системе:
   - На Windows: [Graphviz Download](https://graphviz.org/download/)
   - На Linux:
     ```bash
     sudo apt install graphviz
     ```
   - На macOS:
     ```bash
     brew install graphviz
     ```

4. **Создание конфигурационного файла**:
   В корневой папке проекта создайте файл `config.ini` со следующим содержимым:
   ```ini
   [DEFAULT]
   repo_path = /path/to/your/repository
   file_hash = your_file_hash
   ```

---

## Использование

1. **Запуск утилиты**:
   Выполните скрипт:
   ```bash
   python main.py
   ```

2. **Результаты**:
   - Вывод коммитов с указанным хэшем файла появится в терминале.
   - Сгенерированный граф будет сохранён как `graph.png` в корневой папке проекта.

---

## Как это работает

1. **Анализ коммитов**:
   - Скрипт ищет все коммиты, связанные с указанным хэшем файла, через API библиотеки `gitpython`.

2. **Генерация графа**:
   - Создаёт граф с помощью `Graphviz`, показывающий связи между коммитами.

3. **Вывод графа**:
   - Сохраняет граф в формате PNG для удобного просмотра.

---

## Пример файла конфигурации

```ini
[DEFAULT]
repo_path = /home/user/myrepo
file_hash = abcdef1234567890abcdef1234567890abcdef12
```

---

## Лицензия

Этот проект распространяется под лицензией MIT.

---

## Автор

Проект разработан wallrat1.
