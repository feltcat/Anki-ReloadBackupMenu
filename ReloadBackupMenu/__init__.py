"""
Adds menu option to reload (which also backs up) the collection.
"""

from PyQt5.Qt import QAction
from PyQt5.QtGui import QKeySequence

from aqt import mw


def reloadCollection():
    mw.unloadCollection(mw.loadCollection)


# Create action
reload_action = QAction('&Reload (and back up) collection')
reload_action.setShortcut(QKeySequence('Ctrl+R'))
reload_action.triggered.connect(reloadCollection)
# Insert into menu
menu = mw.form.menuCol
before = mw.form.actionExit
menu.insertAction(before, reload_action)
menu.insertSeparator(before)