class NMarkdown(object):
    def __init__(self, _markdown_filename=None):
        """
        :param _markdown_filename: the name of markdown file
        Initialize variables
        """
        if _markdown_filename is None or isinstance(_markdown_filename, str):
            self.__markdown_filename = _markdown_filename

    @staticmethod
    def read_info(filename):
        content = str()
        if not isinstance(filename, str):
            print("Please use string while calling NMarkdown.read_info")
            return
        if not filename.endswith(".mk"):
            print("Please give the name of a markdown file while calling NMarkdown.read_info")
            return
        try:
            with open(filename, "r") as f:
                content = f.read()
        except IOError as e:
            print("Error occurred while reading file: ", e)
        for line in content.splitlines():
            print(line)
