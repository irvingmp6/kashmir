from InputFile import InputFile

class FileInspectionCSV(InputFile):
    def __init__(self, file):
        super().__init__(file)
        self.extension_result = self._extension_check()

    def _extension_check(self):
        if self.file_extension == "csv":
            return True
        else:
            return False

    def _table_header_check(self):
    	with open(self.file_dir)

def main():
	pass

if __name__ == '__main__':
	main()