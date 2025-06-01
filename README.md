# 🔷 Геометрическая Библиотека "ShapeMaster" 
## *v0.1.0*

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg?style=for-the-badge&logo=checkmarx&logoColor=white)](#запуск-тестов)
[![Code Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg?style=for-the-badge&logo=codecov&logoColor=white)](#запуск-тестов)

</div>

---

> **ShapeMaster** — это простая, но мощная Python-библиотека, предназначенная для вычисления геометрических характеристик различных фигур. Она создана с упором на точность, легкость использования и расширяемость.

---

## 🎯 **Особенности**

### ✨ **Точное вычисление площади:**
- **Круга** (по радиусу)
- **Треугольника** (по трем сторонам с использованием формулы Герона)

### 🔧 **Дополнительные утилиты для треугольника:**
- Проверка, является ли треугольник прямоугольным (с использованием теоремы Пифагора и учетом погрешностей)

### 🏗️ **Объектно-ориентированный дизайн:**
- Каждая фигура представлена отдельным классом
- Общий базовый класс `Shape` для всех фигур, обеспечивающий единый интерфейс

### 🛡️ **Надежность:**
- Встроенная валидация параметров фигур (например, радиус должен быть положительным, стороны должны образовывать треугольник)
- Информативные пользовательские исключения для обработки ошибок

### 🔄 **Гибкость и расширяемость:**
- **Легкое добавление новых фигур**: просто унаследуйте новый класс от `Shape` и реализуйте метод `area()` (См. [Расширение библиотеки](#-расширение-библиотеки-добавление-новых-фигур))
- **Вычисление площади без знания типа фигуры**: обрабатывайте список различных фигур и вызывайте `area()` для каждой, не беспокоясь о ее конкретном типе (полиморфизм)

### 👨‍💻 **Удобство использования:**
- Фабричная функция `create_shape()` для создания фигур на основе переданных параметров, когда тип фигуры может быть неизвестен заранее

### 💎 **Качество кода:**
- Полностью типизированный код (type hints) для лучшей читаемости и поддержки статическими анализаторами
- Подробные докстринги для всех классов и методов
- 100% покрытие кода юнит-тестами с использованием `pytest`

---

## ⚙️ **Установка**

### 📋 **Требования**
- **Python 3.8** или выше

### 📦 **Установка из исходников** *(рекомендуется для разработки или локального использования)*

1. **Клонируйте репозиторий** (или скачайте архив с исходным кодом):
   ```bash
   git clone https://github.com/ToMaTiKkk/geometry_library.git 
   cd geometry_library
   ```

2. **Установите библиотеку и ее зависимости** для разработки (включая `pytest` для тестов):
   ```bash
   pip install .[dev]
   ```
   
   Если вы хотите установить только библиотеку без dev-зависимостей:
   ```bash
   pip install .
   ```

### 🌐 **Установка через pip** *(когда/если библиотека будет опубликована на PyPI)*
```bash
pip install shapemaster
```

---

## 🚀 **Быстрый старт: Примеры использования**

Вот как легко и просто можно использовать библиотеку ShapeMaster:

```python
from geometry_lib import Circle, Triangle, create_shape, Shape
from geometry_lib.exceptions import (
    ShapeError, 
    InvalidShapeParametersError, 
    NonPositiveValueError,
    TriangleInequalityError
)
import math # Для примера с math.pi

def main():
    print("--- Демонстрация ShapeMaster ---")

    # --- Работа с Кругом ---
    try:
        print("\n[Круг]")
        # Создание круга
        circle1 = Circle(radius=5)
        print(f"  {circle1}") # Использует __str__
        print(f"  Площадь: {circle1.area():.4f}") # Вывод с 4 знаками после запятой
        # Пример: Circle(radius=5.0), Площадь: 78.5398

        # Попытка создать круг с некорректным радиусом
        # circle_invalid = Circle(0) # Это вызовет NonPositiveValueError
    except NonPositiveValueError as e:
        print(f"  Ошибка создания круга: {e}")
    except TypeError as e:
        print(f"  Ошибка типа при создании круга: {e}")


    # --- Работа с Треугольником ---
    try:
        print("\n[Треугольник]")
        # Прямоугольный треугольник (Египетский)
        triangle1 = Triangle(side_a=3, side_b=4, side_c=5)
        print(f"  {triangle1}")
        print(f"  Площадь: {triangle1.area():.4f}")
        print(f"  Прямоугольный? {triangle1.is_right_angled()}")
        # Пример: Треугольник со сторонами 3.0, 4.0, 5.0, Площадь: 6.0000, Прямоугольный? True

        # Другой треугольник
        triangle2 = Triangle(7, 10, 12) # s = 14.5, Area = sqrt(14.5*7.5*4.5*2.5) ~ 34.9039
        print(f"  {triangle2}")
        print(f"  Площадь: {triangle2.area():.4f}")
        print(f"  Прямоугольный? {triangle2.is_right_angled()}")
        # Пример: Треугольник со сторонами 7.0, 10.0, 12.0, Площадь: 34.9039, Прямоугольный? False
        
        # Попытка создать невозможный треугольник
        # triangle_invalid = Triangle(1, 2, 10) # Это вызовет TriangleInequalityError
    except (NonPositiveValueError, TriangleInequalityError, TypeError) as e:
        print(f"  Ошибка при работе с треугольником: {e}")

    # --- Использование фабрики create_shape и Полиморфизм ---
    print("\n[Фабрика create_shape и Полиморфизм]")
    try:
        figures: list[Shape] = [
            create_shape(radius=2.5),                    # Создаст Circle
            create_shape(5, 12, 13),                     # Создаст Triangle (прямоугольный)
            create_shape(side_a=2, side_b=2, side_c=2),  # Создаст Triangle (равносторонний)
            # Сюда можно добавить другие фигуры, если они будут реализованы
            # Например, create_shape(width=4, height=6) для Rectangle
        ]

        for i, fig in enumerate(figures):
            # ВАЖНО: Мы не проверяем тип fig (if isinstance...), а просто вызываем area()!
            # Python сам определяет, какой метод area() вызвать (из Circle или Triangle).
            # Это и есть "вычисление площади без знания типа фигуры в compile-time".
            print(f"  Фигура #{i+1} ({fig.__class__.__name__}):")
            print(f"    Параметры: {fig}") # Использует __str__ конкретной фигуры
            print(f"    Площадь: {fig.area():.4f}")
            
            # Если мы хотим использовать специфичный метод, например, is_right_angled для Triangle
            if isinstance(fig, Triangle):
                print(f"    Прямоугольный (проверка)? {fig.is_right_angled()}")
            
    except (ValueError, ShapeError) as e: # ValueError от create_shape, ShapeError от конструкторов
        print(f"  Ошибка при использовании фабрики или обработке фигур: {e}")

    # --- Обработка общих ошибок библиотеки ---
    print("\n[Обработка общих ошибок]")
    try:
        # Пример некорректного вызова, который может вызвать ошибку в create_shape или конструкторе
        unknown_shape = create_shape(10, 20) # Неизвестная конфигурация для create_shape
    except ShapeError as e: # Ловим базовое исключение нашей библиотеки
        print(f"  Произошла ошибка, связанная с фигурой: {e}")
    except ValueError as e: # Ловим ValueError, если create_shape не распознал фигуру
        print(f"  Произошла ошибка значения (например, от create_shape): {e}")
    except Exception as e: # Ловим любые другие непредвиденные ошибки
        print(f"  Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()
```

---

## 📖 **API Справка** *(Основные компоненты)*

### 🟦 **Классы Фигур**

Все фигуры наследуются от `geometry_lib.Shape`.

#### 🔵 `geometry_lib.Circle(radius: float)`
- **`radius`**: Радиус круга (должен быть > 0)

**Методы:**
- `area() -> float`: Возвращает площадь круга

#### 🔺 `geometry_lib.Triangle(side_a: float, side_b: float, side_c: float)`
- **`side_a, side_b, side_c`**: Длины сторон треугольника (каждая > 0, должны удовлетворять неравенству треугольника)

**Методы:**
- `area() -> float`: Возвращает площадь треугольника (по формуле Герона)
- `is_right_angled(tolerance: float | None = None) -> bool`: Возвращает `True`, если треугольник прямоугольный (с учетом погрешности tolerance)

### 🏭 **Фабричная Функция**

#### `geometry_lib.create_shape(*args: float, **kwargs: float) -> Shape`

Пытается создать объект фигуры (`Circle` или `Triangle`) на основе переданных аргументов.

**Примеры:**
- `create_shape(5.0)` → `Circle(radius=5.0)`
- `create_shape(radius=2.5)` → `Circle(radius=2.5)`
- `create_shape(3.0, 4.0, 5.0)` → `Triangle(side_a=3.0, side_b=4.0, side_c=5.0)`
- `create_shape(side_a=1, side_b=1, side_c=1)` → `Triangle(side_a=1.0, side_b=1.0, side_c=1.0)`

Выбрасывает `ValueError`, если не может определить тип фигуры, или пробрасывает исключения от конструкторов фигур (`NonPositiveValueError`, `TriangleInequalityError`, `TypeError`).

### ⚠️ **Исключения**

Находятся в модуле `geometry_lib.exceptions` (но также доступны напрямую из `geometry_lib`).

```
ShapeError(Exception)
└── InvalidShapeParametersError(ShapeError, ValueError)
    ├── NonPositiveValueError(InvalidShapeParametersError)
    └── TriangleInequalityError(InvalidShapeParametersError)
```

- **`ShapeError`**: Базовое исключение для всех ошибок библиотеки
- **`InvalidShapeParametersError`**: Общее исключение для некорректных параметров фигуры
  - **`NonPositiveValueError`**: Если параметр (например, радиус, сторона) не является положительным
  - **`TriangleInequalityError`**: Если стороны не могут образовать треугольник

---

## 🛠️ **Для Разработчиков**

### 📁 **Структура Проекта**

```
geometry_library/
│
├── geometry_lib/           # Исходный код библиотеки
│   ├── __init__.py         # Главный __init__, экспортирует публичный API
│   ├── shapes/             # Модуль с классами фигур
│   │   ├── __init__.py     # Экспорт фигур из этого модуля
│   │   ├── base.py         # Абстрактный класс Shape
│   │   ├── circle.py       # Класс Circle
│   │   └── triangle.py     # Класс Triangle
│   └── exceptions.py       # Пользовательские исключения
│
├── tests/                  # Юнит-тесты
│   ├── __init__.py
│   ├── test_circle.py
│   ├── test_triangle.py
│   └── test_factory_and_polymorphism.py
│
├── .gitignore
├── CHANGELOG.md            # История изменений
├── LICENSE                 # Лицензия MIT
├── README.md               # Этот файл
├── pyproject.toml          # Конфигурация сборки и инструментов
├── requirements-dev.txt    # Зависимости для разработки
├── requirements.txt        # Зависимости для работы (сейчас пусто)
└── setup.py                # Скрипт для сборки и установки
```

### 🧪 **Запуск Тестов**

Для запуска тестов и получения отчета о покрытии:

1. **Убедитесь, что вы установили dev-зависимости:**
   ```bash
   pip install .[dev]
   # или
   pip install -r requirements-dev.txt
   ```

2. **Выполните в корневой директории проекта:**
   ```bash
   pytest
   ```

3. **Для получения отчета о покрытии кода тестами:**
   ```bash
   pytest --cov=geometry_lib
   ```

4. **Для генерации HTML-отчета о покрытии** (откройте `htmlcov/index.html` в браузере):
   ```bash
   pytest --cov=geometry_lib --cov-report=html
   ```

> **💡 Примечание:** Конфигурация pytest также может быть указана в `pyproject.toml`.

### 🔧 **Расширение Библиотеки** *(Добавление Новых Фигур)*

Добавлять новые фигуры очень просто:

1. **Создайте класс для новой фигуры** в `geometry_lib/shapes/`, унаследовав его от `Shape`
   - Реализуйте конструктор `__init__` с необходимыми параметрами и их валидацией
   - Обязательно реализуйте метод `area(self) -> float`
   - Рекомендуется реализовать `__repr__` и `__str__`
   
   **Пример:** `geometry_lib/shapes/rectangle.py`

2. **Зарегистрируйте новую фигуру:**
   - Импортируйте и добавьте класс новой фигуры в `__all__` в файле `geometry_lib/shapes/__init__.py`
   - Импортируйте и добавьте класс новой фигуры в `__all__` в файле `geometry_lib/__init__.py`

3. **(Опционально)** Обновите фабричную функцию `create_shape()` в `geometry_lib/__init__.py`, чтобы она могла создавать вашу новую фигуру

4. **Напишите юнит-тесты** для новой фигуры в директории `tests/`

### 🎨 **Стиль Кода и Линтинг**

Проект стремится следовать стандартам **PEP 8**. Рекомендуется использовать инструменты для форматирования (например, **Black**) и линтинга (например, **Flake8** или **Pylint**) для поддержания качества кода. Конфигурации для этих инструментов можно добавить в `pyproject.toml`.

### 🌿 **Система Контроля Версий**

Мы используем **Git**. Рекомендуемая стратегия ветвления:

- **`main`**: Стабильные релизы, помеченные тегами
- **`develop`**: Основная ветка разработки, куда сливаются готовые фичи
- **`feature/<name>`**: Ветки для разработки новых фич (от `develop`)
- **`fix/<name>`** или **`hotfix/<name>`**: Ветки для исправления багов

---

## 📜 **История Изменений**

Подробности о каждом релизе смотрите в файле **`CHANGELOG.md`**.

---

## 🤝 **Вклад** *(Contributing)*

Мы приветствуем любой вклад в развитие **ShapeMaster**! Если вы хотите помочь:

1. **Сделайте форк репозитория**
2. **Создайте новую ветку** для вашей фичи или исправления:
   ```bash
   git checkout -b feature/ваша-фича develop
   ```
3. **Напишите код** и обязательно добавьте тесты для ваших изменений
4. **Убедитесь, что все тесты проходят:**
   ```bash
   pytest
   ```
5. **Отправьте Pull Request** в ветку `develop` основного репозитория с подробным описанием ваших изменений

> **💡 Совет:** Пожалуйста, старайтесь следовать стилю кода проекта и писать понятные сообщения коммитов.

---

## 📄 **Лицензия**

Этот проект лицензирован на условиях лицензии **MIT** - см. файл [`LICENSE`](LICENSE) для подробностей.

---

<div align="center">

### 💚 **Спасибо за использование ShapeMaster!**

*Мы надеемся, эта библиотека будет вам полезна.*

**Если у вас есть вопросы, предложения или вы нашли баг, пожалуйста, создайте Issue в репозитории проекта.**

---

**🔗 [GitHub Repository](#) | 📚 [Documentation](#) | 🐛 [Report Bug](#) | 💡 [Request Feature](#)**

</div>
