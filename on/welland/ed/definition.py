from datetime import date

import boundaries

boundaries.register('Welland wards',
    domain='Welland, ON',
    last_updated=date(2014, 4, 7),
    name_func=lambda f: 'Ward %s' % f.get('WARD'),
    id_func=boundaries.attr('WARD'),
    authority='City of Welland',
    source_url='http://www.welland.ca/open/OpendataResp.asp?utitle=Ward%20Boundaries',
    licence_url='http://www.welland.ca/open/OpendataTermUse.asp',
    data_url='http://www.welland.ca/open/Datasheets/Welland_ward_boundaries.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '3526032'},
    prj='http://spatialreference.org/ref/epsg/26917/prj/',
)
