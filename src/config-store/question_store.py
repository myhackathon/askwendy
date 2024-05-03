"""Class to read text files related to interview questions."""

class TextFileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_rows(self):
        rows = []
        with open(self.file_path, 'r') as file:
            for line in file:
                rows.append(line.strip())
        return rows