import os

class InputFile():

    def __init__(self, file_dir_input):
        
        self.file_dir_input = file_dir_input
        self.file_location = self._get_file_location()
        self.file_basename = self._get_file_basename()
        self.file_basename_parts = self._parse_file_name()
        self.file_extension = self._get_file_extension()
        self.file_rootname = self._get_file_rootname()

    def _get_file_location(self):
        file_location = os.path.split(self.file_dir_input)[0]
        return file_location

    def _get_file_basename(self):
        file_basename = os.path.basename(self.file_dir_input)
        return file_basename

    def _parse_file_name(self):
        file_basename_parts = self.file_basename.split(".")
        return file_basename_parts

    def _get_file_extension(self):
        file_extension = self.file_basename_parts[-1].lower()
        return file_extension

    def _get_file_rootname(self):
        extension_length = len(self.file_extension) + 1
        file_rootname = self.file_basename[:-extension_length]
        return file_rootname


def main():
	pass

if __name__ == '__main__':
    main()