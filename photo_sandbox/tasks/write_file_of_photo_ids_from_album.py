# import itertools
import csv

from gphotospy.album import Album
from gphotospy.media import Media

from photo_sandbox.tasks.initialize_gphoto_spy import initialize_gphoto_spy


def write_file_of_photo_ids_from_album():
    """
    Prompts for album name. Then fetches all of its media. Filters out the
    non-photos. For each photo, writes its id as a line to a file, named
    "ids_of_photos_in_album."

    @return [None]
    """
    service = initialize_gphoto_spy()

    # Init the album manager
    album_manager = Album(service)

    album_iterator = album_manager.list()

    # first_five_albums = itertools.islice(album_iterator, 5)
    #
    # # Print info about the first 5 most recent albums
    # for album in first_five_albums:
    #     print(album)

    # Find album by title
    album_title = input("Please enter the album title:\n")
    album = next(
        album for album in album_iterator if album.get("title").strip() == album_title
    )
    # print(json.dumps(album, indent=2))

    album_id = album.get("id")

    # Init the media manager
    media_manager = Media(service)

    # Get photos from album
    media_iterator = media_manager.search_album(album_id)
    photos = (
        media for media in media_iterator if media.get("mimeType").startswith("image")
    )
    # Get ids from photos
    ids = list(photo.get("id") for photo in photos)
    # Write ids to file, one per line
    with open("photo_sandbox/files/ids_of_photos_in_album", "w") as fw:
        csv.writer(fw).writerows([id] for id in ids)
