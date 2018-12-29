import json


class NJsonPrimitive(object):

    def __init__(self, _json_filename):
        """
        :param _json_filename: the name of database file
        Initialize variables
        """
        self.metadata = {'': 0}
        self.__filename_read = _json_filename
        self.__filename_write = _json_filename

    def read_from_file(self):
        """
        Load json data from file to metadata
        """
        with open(self.__filename_read, "r") as json_file:
            self.metadata = json.load(json_file)

    def write_to_file(self):
        """
        Write metadata to file
        """
        with open(self.__filename_write, "w") as jsonFile:
            json.dump(self.metadata, jsonFile, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=True)

    @property
    def filename_read(self):
        return self.__filename_read

    @filename_read.setter
    def filename_read(self, fn):
        if isinstance(fn, str):
            self.__filename_read = fn

    @property
    def filename_write(self):
        return self.__filename_write

    @filename_write.setter
    def filename_write(self, fn):
        if isinstance(fn, str):
            self.__filename_write = fn

    @property
    def metadata(self):
        return self.__metadata

    @metadata.setter
    def metadata(self, metadata):
        self.__metadata = metadata

    @staticmethod
    def read(filename):
        """
        :param filename: the name of file
        :return: python objects contained in the file using json format
        Static function to load data from json file
        """
        with open(filename, "r") as f:
            return json.load(f)

    @staticmethod
    def write(filename, data):
        """
        :param filename: the name of file
        :param data: the data you want to write to the file
        Static function to write data to json file
        """
        with open(filename, "w") as f:
            json.dump(data, f, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=True)
