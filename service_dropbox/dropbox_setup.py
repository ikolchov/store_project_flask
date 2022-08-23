import dropbox
from decouple import config


class DropboxServiceSetter:

    def __init__(self):
        self.key = config('DROPBOX_TOKEN')
        self.path = config('DROPBOX_PATH')
        self.shared_link = config('DROPBOX_SHARED_LINK')

setter = DropboxServiceSetter()

dbx = dropbox.Dropbox(setter.key)


