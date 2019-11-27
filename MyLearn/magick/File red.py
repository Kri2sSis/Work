from tempfile import gettempdir
from os.path import join, exists


class File:
    def __init__(self, path):
        self.path = path
        self.current = 0
        if not exists(self.path):
            open(self.path, 'w').close()

    def __str__(self):
        return self.path

    def __add__(self, other):
        new_path = join(gettempdir(), 'new_file.txt')
        new_file = type(self)(new_path)
        new_file.write(self.read() + other.read())
        return new_file

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path, 'r') as f:
            f.seek(self.current)
            line = f.readline()
            if not line:
                self.current_position = 0
                raise StopIteration('EOF')
            self.current = f.tell()
            return line

    def write(self, text):
        with open(self.path, 'w') as f:
            return f.write(text)

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()


