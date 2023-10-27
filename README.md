
# Асинхронный парсер PEP

Парсер документов PEP с официального сайта Python.


## Возможности

- Парсинг статусов версий и PEP
- Сохранение результатов в формате CSV


## Установка

Склонируйте проект:

```bash
  git clone git@github.com:MAGFRG/scrapy_parser_pep.git
```

Перейдите в папку проекта:

```bash
  cd scrapy_parser_pep
```

Создайте и активируйте виртуальное окружение:

```bash
  python -m venv venv
  source venv/Scripts/activate
```


Установите зависимости:

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

- [Магомет Басханов](https://github.com/MAGFRG/)

