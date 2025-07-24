from abc import ABC, abstractmethod

# مرحله 1: کلاس پایه برای مدیریت فایل‌ها
class FileHandler(ABC):
    @abstractmethod
    def open_file(self, file_path):
        pass

    @abstractmethod
    def edit_file(self, content):
        pass

# مرحله 2: پیاده‌سازی برای فایل‌های JSON
class JsonFileHandler(FileHandler):
    def open_file(self, file_path):
        print(f"Opening JSON file: {file_path}")
        # کد واقعی برای باز کردن فایل JSON

    def edit_file(self, content):
        print(f"Editing JSON content: {content}")
        # کد واقعی برای ویرایش JSON

# مرحله 3: پیاده‌سازی برای فایل‌های XML
class XmlFileHandler(FileHandler):
    def open_file(self, file_path):
        print(f"Opening XML file: {file_path}")
        # کد واقعی برای باز کردن فایل XML

    def edit_file(self, content):
        print(f"Editing XML content: {content}")
        # کد واقعی برای ویرایش XML

# مرحله 4: Factory برای ایجاد شیء مناسب
class FileHandlerFactory:
    @staticmethod
    def create_file_handler(file_type: str) -> FileHandler:
        if file_type.lower() == "json":
            return JsonFileHandler()
        elif file_type.lower() == "xml":
            return XmlFileHandler()
        else:
            raise ValueError(f"Unsupported file type: {file_type}")

# مرحله 5: استفاده از Factory در برنامه
def main():
    file_type = input("Enter file type (json/xml): ")
    file_path = input("Enter file path: ")
    content = input("Enter content to edit: ")

    try:
        handler = FileHandlerFactory.create_file_handler(file_type)
        handler.open_file(file_path)
        handler.edit_file(content)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()