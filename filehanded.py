class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def write_data(self, text):
        with open(self.filename, "w") as file:
            file.write(text)

    def read_data(self):
        with open(self.filename, "r") as file:
            return file.read()

    def append_data(self, text):
        with open(self.filename, "a") as file:
            file.write(text)

class ListManager:
    def __init__(self, data_list):
        self.data_list = data_list

    def get_element(self, index):
        try:
            return self.data_list[index]
        except IndexError as e:
            return f"Error: {e}"

file_obj = FileHandler("file1.txt")
file_obj.write_data("hello world")
print(file_obj.read_data())

file_obj.filename = "file.txt"
file_obj.append_data("python programming")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_obj = ListManager(numbers)
print(list_obj.get_element(10))

