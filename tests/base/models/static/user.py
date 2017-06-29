from byte.table import Model, Property

from datetime import datetime


class User(Model):
    class Options:
        slots = True

    id = Property(int, primary_key=True)

    username = Property(str)
    password = Property(str)

    created_at = Property(datetime, default=lambda: datetime.now())
    updated_at = Property(datetime, default=lambda: datetime.now())
