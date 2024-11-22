
class File:
    def __init__(self, name):
        self.name = name

    def open(self):
        pass

class PDFFile(File):
    def open(self):
        # از پکیج مربوط به کارهای فایلهای pdf استفاده کنم
        print('PDF file opened.')

class MusicFile(File):
    def open(self):
        # از کتابخانه مخصوص فایلهای موزیک و فایل را باز کن
        print('Music file opened.')

    def play(self):
        pass

my_file_name = 'sample.pdf'

file_name = my_file_name.split('.')[:len(my_file_name)]
file_extension = my_file_name.split('.')[-1]

if file_extension == 'pdf':
    my_file = PDFFile(my_file_name)
elif file_extension == 'mp3':
    my_file = MusicFile(my_file_name)

my_file.open() # Polymorphism چندریختی
my_file.play()



    

