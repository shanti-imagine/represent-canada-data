from datetime import date

import boundaries

boundaries.register('New Brunswick electoral districts',
    domain='New Brunswick',
    last_updated=date(2011, 3, 8),
    name_func=boundaries.attr('PED_Name_E'),
    # DIST_ID
    id_func=boundaries.attr('PED_Num'),
    authority='Her Majesty the Queen in Right of New Brunswick',
    # http://www.snb.ca/geonb1/e/DC/catalogue-E.asp
    source_url='http://www.gnb.ca/elections/10prov/10provmap-e.asp',
    # http://geonb.snb.ca/downloads/prov_electoral_districts/geonb_2014_ped-cep_shp.zip
    data_url='http://www.gnb.ca/elections/pdf/2010PEDMaps/NB_Electoral_Districts.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '13'},
)
