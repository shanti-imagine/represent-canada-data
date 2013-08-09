from datetime import date

import boundaries

boundaries.register('Caledon wards',
    domain='Caledon, ON',
    last_updated=date(2012, 2, 24),
    name_func=lambda f: 'Ward %s' % f.get('WARDNUM'),
    id_func=boundaries.attr('WARDNUM'),
    authority='Region of Peel',
    source_url='http://opendata.peelregion.ca/data-categories/regional-geography/ward-boundaries-(2010-2014).aspx',
    licence_url='http://opendata.peelregion.ca/terms-of-use.aspx',
    data_url='http://opendata.peelregion.ca/media/2549/wardboundary20102014_shp_04.2012.zip',
    additional_commands="""ogr2ogr -f "ESRI Shapefile" -where "MUNIC='10'" Caledon.shp wardbnd_1014.shp""",
    encoding='iso-8859-1',
    geographic_code='3521024',
)
