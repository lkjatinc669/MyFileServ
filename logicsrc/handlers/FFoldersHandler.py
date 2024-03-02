import os

class FFoldersHandler:
    def __init__(self, path) -> None:
        self.path = path

    def getFilesFolders(self):
        ff = os.listdir(self.path)
        files, folders = [], []
        for x in ff:
            if os.path.isfile(x):
                files.append(x)
            elif os.path.isdir(x):
                if x[0] == ".":
                    pass
                else:
                    folders.append(x)
        return {
            "files":files, "folders":folders
        }