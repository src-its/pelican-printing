from __future__ import unicode_literals
import os
from pelican import signals

def test(sender):
    print "%s initialized !!" % sender

def register():
    signals.initialized.connect(test)


class MarkdownReader(BaseReader):
    enabled = bool(Markdown)

    def read(self, source_path):
        """Parse content and metadata of markdown files"""
        text = pelican_open(source_path)
        md = Markdown(extensions = ['meta', 'codehilite'])
        content = md.convert(text)

        metadata = {}
        for name, value in md.Meta.items():
            name = name.lower()
            meta = self.process_metadata(name, value[0])
            metadata[name] = meta
        return content, metadata
