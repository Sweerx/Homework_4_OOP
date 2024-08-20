
# Homework from SkyPro

## Описание проекта

Данный проект является частью учебного задания в рамках курса SkyPro и предназначен для демонстрации навыков работы с объектно-ориентированным 
программированием (ООП) на языке Python.

### Основные улучшения:
1. **Добавлен класс-наследник `Smartphone` от `Product`**: Класс, представляющий смартфоны, расширяющий функциональность базового класса `Product`.
2. **Добавлен класс-наследник `LawnGrass` от `Product`**: Класс для представления газонной травы, также расширяющий функциональность базового класса `Product`.
3. **Доработан метод `__add__` в классах-наследниках**: Внесены изменения в метод `__add__` для обеспечения корректной работы сложения объектов этих классов.
4. **Тестирование**: Тесты были обновлены и дополнены для проверки новых методов. Проект проверен на соответствие стандартам кода с использованием `mypy` и `flake8`.


## Установка

Чтобы начать работу с проектом, выполните следующие шаги:

1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/Sweerx/Homework_4_OOP.git
   ```
   или с помощью SSH:
   ```bash
   git clone git@github.com:Sweerx/Homework_4_OOP.git
   ```

2. **Установите зависимости**:
   ```bash
   pip install -r requirements.txt
   ```

## Запуск проекта

Для запуска проекта выполните следующую команду в терминале:

```bash
python main.py
```

## Тестирование

Тесты расположены в директории `tests`. Для запуска всех тестов используйте команду:

```bash
pytest
```

## Линтинг и статический анализ

Перед сдачей проекта выполняю проверку качества кода с помощью следующих инструментов:

1. **mypy** - статический анализатор типов:
   ```bash
   mypy .
   ```

2. **flake8** - инструмент для проверки стиля кода:
   ```bash
   flake8 .
   ```
