import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from pep_parse.settings import (
    BASE_DIR,
    DT_FORMAT,
    QTY,
    RESULTS,
    STATUS,
    STATUS_SUMMARY,
    TOTAL,
)


class PepParsePipeline:
    def __init__(self):
        self.results_dir = Path(BASE_DIR) / RESULTS
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.pep_statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.pep_statuses[item.get(STATUS)] += 1
        return item

    def close_spider(self, spider):
        date_time_now = datetime.now().strftime(DT_FORMAT)
        filename = f"{STATUS_SUMMARY}_{date_time_now}.csv"
        with open(self.results_dir / filename, "w", newline="") as csv_file:
            fieldnames = [STATUS, QTY]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            total_qty = sum(self.pep_statuses.values())
            writer.writeheader()
            for status, qty in self.pep_statuses.items():
                writer.writerow({STATUS: status, QTY: qty})
            writer.writerow({STATUS: TOTAL, QTY: total_qty})
