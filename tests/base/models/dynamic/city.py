from byte.table import Model, Property


class City(Model):
    id = Property(str, name='geonameid', primary_key=True)

    name = Property(str)

    country = Property(str)
    subcountry = Property(str)
