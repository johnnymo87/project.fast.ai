import csv
from datetime import date as python_date

from gphotospy.media import Media
from gphotospy.media import date as gphoto_date
from gphotospy.media import date_range as gphoto_date_range

from photo_sandbox.tasks.initialize_gphoto_spy import initialize_gphoto_spy


def write_file_of_photo_ids_since_sept_2018():
    service = initialize_gphoto_spy()

    # Init the media manager
    media_manager = Media(service)

    # Get all photos since 2018-09-01, which is approximately the date of my
    # earliest photos of Livia.
    today = python_date.today()
    start_date = gphoto_date(2019, 8, 1)
    end_date = gphoto_date(today.year, today.month, today.day)
    media_iterator = media_manager.search(
        gphoto_date_range(start_date=start_date, end_date=end_date)
    )
    photos = (
        media for media in media_iterator if media.get("mimeType").startswith("image")
    )
    # Get ids from photos
    ids = list(photo.get("id") for photo in photos)
    # Write ids to file, one per line
    with open("photo_sandbox/files/ids_of_all_photos_since_sept_2018", "w") as fw:
        csv.writer(fw).writerows([id] for id in ids)
