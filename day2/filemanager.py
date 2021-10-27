class FileManager():

    def __init__(self, filename, mode):
        self.filname = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filname, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with FileManager('test.txt','w') as f:
    f.write('dane testowe')

print(f.closed)