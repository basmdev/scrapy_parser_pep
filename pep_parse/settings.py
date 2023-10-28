from pathlib import Path

BOT_NAME = "pep_parse"

SPIDER_MODULES = ["pep_parse.spiders"]
NEWSPIDER_MODULE = "pep_parse.spiders"
ROBOTSTXT_OBEY = True

ALLOWED_DOMAINS = [
    "peps.python.org",
]
BASE_DIR = Path(__file__).parent.parent

RESULTS = "results"
"""Имя директории, где будут храниться результаты скрапинга."""

NUMBER = "number"
"""Название поля, представляющего номер PEP."""

NAME = "name"
"""Название поля, представляющего имя PEP."""

STATUS = "status"
"""Название поля, представляющего статус PEP."""

QTY = "quantity"
"""Название поля, представляющего количество PEP."""

STATUS_SUMMARY = "status_summary"
"""Префикс имени файла для сводной информации о статусах PEP."""

TOTAL = "Total"
"""Название поля, представляющего общее количество PEP."""

DT_FORMAT = "%Y-%m-%d_%H-%M-%S"
"""Формат времени и даты для создания имен файлов."""

FEEDS = {
    f"{RESULTS}/pep_%(time)s.csv": {
        "format": "csv",
        "fields": [NUMBER, NAME, STATUS],
        "overwrite": True,
    },
}

ITEM_PIPELINES = {
    "pep_parse.pipelines.PepParsePipeline": 300,
}
