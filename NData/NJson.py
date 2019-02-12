import json


class NJsonPrimitive(object):

    def __init__(self, _json_filename=None):
        """
        :param _json_filename: the name of database file
        Initialize variables
        """
        self.metadata = dict()
        if _json_filename is None or isinstance(_json_filename, str):
            self.__filename_read = _json_filename
            self.__filename_write = _json_filename

    def read_from_file(self):
        """
        Load json data from file to metadata
        """
        if self.__filename_read is not None:
            try:
                with open(self.__filename_read, "r") as json_file:
                    self.metadata = json.load(json_file)
            except IOError as e:
                print("Error occurred while opening file: ", e)
        else:
            print("Read file is None")

    def write_to_file(self):
        """
        Write metadata to file
        """
        if self.__filename_write is not None:
            try:
                with open(self.__filename_write, "w") as jsonFile:
                    json.dump(self.metadata, jsonFile, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=True)
            except IOError as e:
                print("Error occurred while writing to file: ", e)
        else:
            print("Write file is None")

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
        if not isinstance(filename, str):
            print("Please use string while calling NJsonPrimitive.read")
            return
        try:
            with open(filename, "r") as f:
                return json.load(f)
        except IOError as e:
            print("Error occurred while opening file: ", e)

    @staticmethod
    def write(filename, data):
        """
        :param filename: the name of file
        :param data: the data you want to write to the file
        Static function to write data to json file
        """
        if not isinstance(filename, str):
            print("Please use string while calling NJsonPrimitive.write")
            return
        try:
            with open(filename, "w") as f:
                json.dump(data, f, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=True)
        except IOError as e:
            print("Error occurred while writing to file: ", e)
