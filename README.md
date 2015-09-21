## Printing Pelican

This experiment works to eventually print files through linked databases and CSV files.


## Dependencies

* Python
* Pelican
* Fabric

## Current Operation

Currently, the only supported command is to create an article page. The fdollowing command will allow you to create an article with a specified title:

	fab make_entry:"TITLE","CONTENT","CATEGORY"


You may also read a CSV file by using the following notation:

	fab read_csv:TITLE.csv

Currently all the CSV reader will do is spit out data.

## Further Development

Using [Click me!](http://nafiulis.me/making-a-static-blog-with-pelican.html "this guide") as a template for fabfiles.
