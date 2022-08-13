from gphotospy.media import Media, MediaItem

from photo_sandbox.tasks.initialize_gphoto_spy import initialize_gphoto_spy


def fetch_photo_urls_from_photo_ids(photo_ids):
    """
    @param[list<int>] photo_ids Ids of photos

    @return [list<int>]
    """
    service = initialize_gphoto_spy()

    media_manager = Media(service)

    photos = (media_manager.get(id) for id in photo_ids)
    photos = (MediaItem(photo) for photo in photos)
    download_urls = (photo.get_url() for photo in photos)
    return list(download_urls)
