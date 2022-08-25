import os

from dropbox.exceptions import ApiError, AuthError
from werkzeug.exceptions import ServiceUnavailable, BadGateway

from service_dropbox.dropbox_setup import dbx, setter
from service_dropbox.pd_file_generator import pd_file_generator
from utils.func_helpers import get_filename_generator


class ExportDataManager:
    @staticmethod
    def get_report(data):

        file_name, temp_dir_file = get_filename_generator(data)
        pd_file_generator(temp_dir_file, data["start_date"], data["end_date"])
        try:
            with open(temp_dir_file, "rb") as f:
                resp = dbx.files_upload(f.read(), f"{setter.path}{file_name}")
        except ApiError:
            raise ServiceUnavailable(
                "raise something went wrong try again later. If the issue persists contact admin!"
            )
        except AuthError:
            raise BadGateway("Service unavailable")
        finally:
            os.remove(temp_dir_file)
        return "Report created"
