from datetime import datetime as dt


# File class will represent each individual file within the file system
# Each file will have the properties
#   - Name
#   - Extension
#   - Rights (Read, Write, Execute)
#   - Date created (Current system time when object is created)


class File:
    def __init__(self, file_name, file_extension, file_rights=None):
        self.name = file_name
        self.extension = file_extension
        self.rights = ['R'] if file_rights is None else file_rights
        self.date_created = dt.now()

    def __str__(self):
        return self.name + self.extension


class Directory:
    def __init__(self, folder_name, folder_content=None):
        self.name = folder_name
        self.content = [] if folder_content is None else folder_content

    def __str__(self):
        return self.name + " " + self.content

    def insert_file(self, file):
        self.content.append(file)

    def get_content(self):
        file_str = ""
        dir_str = ""
        for file in self.content:
            if type(file) == File:
                file_str += file.name + file.extension + " "
            else:
                dir_str += file.name + " "
        return dir_str + file_str


class FileSystem:
    def __init__(self, root_folder_name, users=None):
        self.root = Directory(root_folder_name)
        self.users = ["Admin"] + users


#   Driver code
if __name__ == "__main__":
    fs = FileSystem("root", ["Jack"])
    print(fs.users)
    fs.root.insert_file(File("HolidayPic", ".jpg"))
    fs.root.insert_file(Directory("Music", File("BestSong", ".mp3")))
    print(fs.root.get_content())
