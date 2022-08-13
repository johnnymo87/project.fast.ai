import csv
import random

from photo_sandbox.tasks.fetch_photo_urls_from_photo_ids import (
    fetch_photo_urls_from_photo_ids,
)

with open("photo_sandbox/files/ids_of_all_photos_since_sept_2018", "r") as fr:
    ids_of_all_photos_since_sept_2018 = [row[0] for row in csv.reader(fr)]

with open("photo_sandbox/files/ids_of_photos_of_Livia", "r") as fr:
    ids_of_photos_of_Livia = [row[0] for row in csv.reader(fr)]

ids_of_photos_of_not_Livia = list(
    set(ids_of_all_photos_since_sept_2018).difference(set(ids_of_photos_of_Livia))
)

ids_of_photos_of_Livia = random.sample(ids_of_photos_of_Livia, 150)
ids_of_photos_of_not_Livia = random.sample(ids_of_photos_of_not_Livia, 150)

download_urls_of_photos_of_Livia = fetch_photo_urls_from_photo_ids(
    ids_of_photos_of_Livia
)
with open("photo_sandbox/files/sample_of_ids_of_photos_of_Livia", "w") as fw:
    csv.writer(fw).writerows([url] for url in download_urls_of_photos_of_Livia)

download_urls_of_photos_of_not_Livia = fetch_photo_urls_from_photo_ids(
    ids_of_photos_of_not_Livia
)
with open("photo_sandbox/files/sample_of_ids_of_photos_of_not_Livia", "w") as fw:
    csv.writer(fw).writerows([url] for url in download_urls_of_photos_of_not_Livia)
