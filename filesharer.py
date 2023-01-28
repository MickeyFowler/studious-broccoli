from filestack import Client


class FileShare:

    def __init__(self, filepath, api_key="AfL83AXoDRoybP8Z7dDqxz"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_file_link = client.upload(filepath=self.filepath)
        return new_file_link.url
