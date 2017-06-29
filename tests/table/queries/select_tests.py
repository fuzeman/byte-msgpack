from tests.base.core.fixtures import get_fixture_uri
from tests.base.models.dynamic.city import City

from byte.table import Table
from byte.formats.msgpack import MessagePackCollectionStructure
from hamcrest import *
import byte.compilers.operation
import byte.executors.file
import byte.formats.msgpack


def test_all_list():
    with get_fixture_uri('collections/list/cities.mpack') as artists_uri:
        cities = Table(
            City, artists_uri,
            format_structure=MessagePackCollectionStructure.List,
            plugins=[
                byte.compilers.operation,
                byte.executors.file,
                byte.formats.msgpack
            ])

        # Fetch all cities, and validate properties
        assert_that(list(cities.all().iterator()), all_of(
            has_length(23018),

            has_items(
                has_properties({
                    'id': '2179537',
                    'name': 'Wellington',

                    'country': 'New Zealand',
                    'subcountry': 'Wellington'
                }),
                has_properties({
                    'id': '2179670',
                    'name': 'Wanganui',

                    'country': 'New Zealand',
                    'subcountry': 'Manawatu-Wanganui'
                }),
                has_properties({
                    'id': '2181133',
                    'name': 'Timaru',

                    'country': 'New Zealand',
                    'subcountry': 'Canterbury'
                }),
                has_properties({
                    'id': '2181742',
                    'name': 'Taupo',

                    'country': 'New Zealand',
                    'subcountry': 'Waikato'
                }),
                has_properties({
                    'id': '2184155',
                    'name': 'Pukekohe East',

                    'country': 'New Zealand',
                    'subcountry': 'Auckland'
                }),
            )
        ))


def test_all_objects():
    with get_fixture_uri('collections/objects/cities.mpack') as artists_uri:
        cities = Table(
            City, artists_uri,
            format_structure=MessagePackCollectionStructure.Objects,
            plugins=[
                byte.compilers.operation,
                byte.executors.file,
                byte.formats.msgpack
            ])

        # Fetch all cities, and validate properties
        assert_that(list(cities.all().iterator()), all_of(
            has_length(23018),

            has_items(
                has_properties({
                    'id': '2179537',
                    'name': 'Wellington',

                    'country': 'New Zealand',
                    'subcountry': 'Wellington'
                }),
                has_properties({
                    'id': '2179670',
                    'name': 'Wanganui',

                    'country': 'New Zealand',
                    'subcountry': 'Manawatu-Wanganui'
                }),
                has_properties({
                    'id': '2181133',
                    'name': 'Timaru',

                    'country': 'New Zealand',
                    'subcountry': 'Canterbury'
                }),
                has_properties({
                    'id': '2181742',
                    'name': 'Taupo',

                    'country': 'New Zealand',
                    'subcountry': 'Waikato'
                }),
                has_properties({
                    'id': '2184155',
                    'name': 'Pukekohe East',

                    'country': 'New Zealand',
                    'subcountry': 'Auckland'
                }),
            )
        ))


def test_where_list():
    with get_fixture_uri('collections/list/cities.mpack') as artists_uri:
        cities = Table(
            City, artists_uri,
            format_structure=MessagePackCollectionStructure.List,
            plugins=[
                byte.compilers.operation,
                byte.executors.file,
                byte.formats.msgpack
            ])

        # Fetch cities, and validate properties
        assert_that(list(cities.select().where(City['country'] == 'New Zealand').iterator()), all_of(
            has_length(35),

            has_items(
                has_properties({
                    'id': '2179537',
                    'name': 'Wellington',

                    'country': 'New Zealand',
                    'subcountry': 'Wellington'
                }),
                has_properties({
                    'id': '2179670',
                    'name': 'Wanganui',

                    'country': 'New Zealand',
                    'subcountry': 'Manawatu-Wanganui'
                }),
                has_properties({
                    'id': '2181133',
                    'name': 'Timaru',

                    'country': 'New Zealand',
                    'subcountry': 'Canterbury'
                }),
                has_properties({
                    'id': '2181742',
                    'name': 'Taupo',

                    'country': 'New Zealand',
                    'subcountry': 'Waikato'
                }),
                has_properties({
                    'id': '2184155',
                    'name': 'Pukekohe East',

                    'country': 'New Zealand',
                    'subcountry': 'Auckland'
                }),
            )
        ))


def test_where_objects():
    with get_fixture_uri('collections/objects/cities.mpack') as artists_uri:
        cities = Table(
            City, artists_uri,
            format_structure=MessagePackCollectionStructure.Objects,
            plugins=[
                byte.compilers.operation,
                byte.executors.file,
                byte.formats.msgpack
            ])

        # Fetch artists, and validate properties
        assert_that(list(cities.select().where(City['country'] == 'New Zealand').iterator()), all_of(
            has_length(35),

            has_items(
                has_properties({
                    'id': '2179537',
                    'name': 'Wellington',

                    'country': 'New Zealand',
                    'subcountry': 'Wellington'
                }),
                has_properties({
                    'id': '2179670',
                    'name': 'Wanganui',

                    'country': 'New Zealand',
                    'subcountry': 'Manawatu-Wanganui'
                }),
                has_properties({
                    'id': '2181133',
                    'name': 'Timaru',

                    'country': 'New Zealand',
                    'subcountry': 'Canterbury'
                }),
                has_properties({
                    'id': '2181742',
                    'name': 'Taupo',

                    'country': 'New Zealand',
                    'subcountry': 'Waikato'
                }),
                has_properties({
                    'id': '2184155',
                    'name': 'Pukekohe East',

                    'country': 'New Zealand',
                    'subcountry': 'Auckland'
                }),
            )
        ))
