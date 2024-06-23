
# Асинхронный парсер PEP

Парсер документов PEP с официального сайта Python.


## Возможности

- Парсинг статусов версий и PEP
- Сохранение результатов в формате CSV


## Установка

1. Склонируйте проект:

```bash
  git clone git@github.com:basmdev/scrapy_parser_pep.git
```

2. Перейдите в папку проекта:

```bash
  cd scrapy_parser_pep
```

3. Создайте и активируйте виртуальное окружение:

```bash
  python -m venv venv
  source venv/Scripts/activate
```


4. Установите зависимости:

```bash
  pip install -r requirements.txt
```

## Использование

Запуск парсера:

```bash
scrapy crawl pep
```
Результаты сохраняются в папке results в формате CSV.

## Технологии

- Python
- Scrapy

## Автор

Mohammed Baskhanov (basmdev)