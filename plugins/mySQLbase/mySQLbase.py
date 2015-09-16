## This plugin sets up a MySQL connection system that could potentially be used in the future

from __future__ import unicode_literals

import os
import logging
import MySQLdb as mdb
import sys

from pelican import signals
logger = logging.getLogger(__name__)


try:
    con = mdb.connect(DATABASESERVER,DATABASEUSER,DATABASEPASS,DATABASENAME);

    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    ver = cur.fetchone()
    
    print "Database version : %s " % ver
    
except mdb.Error, e:
  
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)

finally:    
        
    if con:    
        con.close()

def test(sender):
	print "Yay!" % sender


def register():
    signals.initialized.connect(test)
