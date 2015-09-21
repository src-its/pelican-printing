from pelican import signals
from pelican.readers import BaseReader

# Create a new reader class, inheriting from the pelican.reader.BaseReader
class NewReader(BaseReader):
    enabled = True  # Yeah, you probably want that :-)

    # The list of file extensions you want this reader to match with.
    # If multiple readers were to use the same extension, the latest will
    # win (so the one you're defining here, most probably).
    file_extensions = ['yeah']

    # You need to have a read method, which takes a filename and returns
    # some content and the associated metadata.
    def read(self, filename):
        metadata = {'title': 'Oh yeah',
                    'category': 'Foo',
                    'date': '2012-12-01'}

        parsed = {}
        for key, value in metadata.items():
            parsed[key] = self.process_metadata(key, value)

        return "Some content", parsed

def add_reader(readers):
    readers.reader_classes['yeah'] = NewReader

# This is how pelican works.
def register():
    signals.readers_init.connect(add_reader)
