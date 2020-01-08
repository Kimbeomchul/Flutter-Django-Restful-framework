from django.test import TestCase
from django.db.utils import ProgrammingError
from south.db import db

exists = False
db.start_transaction()
try:
    # Will fail if the destination table does not exist. 
    # Any typo here will yield incorrect results. Be careful.
    db.execute("select count(*) from auth_user")
    # If we get here, the table exists
    exists = True
except ProgrammingError:
    pass

# Always end the transaction we started, rollback or commit shouldn't matter.
db.rollback_transaction()

if exists:
    db.rename_table...
else:
    # The table does not exist, create new one.
    db.create_table...