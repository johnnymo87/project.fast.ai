# import itertools
import csv
import json
import os
from datetime import date as python_date

from dotenv import load_dotenv
from gphotospy import authorize
from gphotospy.album import Album
from gphotospy.media import Media  # , MediaItem
from gphotospy.media import date as gphoto_date
from gphotospy.media import date_range as gphoto_date_range

# Create the credentials file that gphotospy wants
load_dotenv()
PROJECT_ID = os.environ["PROJECT_ID"]
CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
credentials = {
    "web": {
        "project_id": PROJECT_ID,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    }
}
with open("credentials.json", "w") as f:
    json.dump(credentials, f)

# Get authorization and return a service object
service = authorize.init("credentials.json")

# Init the album manager
album_manager = Album(service)

album_iterator = album_manager.list()

# first_five_albums = itertools.islice(album_iterator, 5)
#
# # Print info about the first 5 most recent albums
# for album in first_five_albums:
#     print(album)

# Find album by title
# album_title = input("Please enter the album title:\n")
# album = next(
#     album for album in album_iterator if album.get("title").strip() == album_title
# )
# # print(json.dumps(album, indent=2))
#
# album_id = album.get("id")

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
with open("photo_sandbox/ids_of_all_photos_since_sept_2018", "w") as fw:
    csv.writer(fw).writerows([id] for id in ids)

# # Get photos from album
# media_iterator = media_manager.search_album(album_id)
# photos = (
#     media for media in media_iterator if media.get("mimeType").startswith("image")
# )
# # Get ids from photos
# ids = list(photo.get("id") for photo in photos)
# # Write ids to file, one per line
# with open("photo_sandbox/ids_of_photos_in_album", "w") as fw:
#     csv.writer(fw).writerows([id] for id in ids)

# first_five_media = itertools.islice(media_iterator, 5)
#
# # Print info about the first 5 photos
# for media in first_five_media:
#     print(json.dumps(media, indent=2))

# Get download urls from photos in album
# photos = (media for media in media_iterator if media.get("mimeType").startswith("image"))
# photos = (MediaItem(photo) for photo in photos)
# download_urls = (photo.get_url() for photo in photos)
# download_urls = list(download_urls)
#
# # Write download urls to file
# with open("photo_sandbox/download_urls", "w") as f:
#     f.writelines(download_urls)
#
# print(
#     f"Wrote {len(download_urls)} download URLs to photo_sandbox/download_urls"
# )
