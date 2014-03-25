# coding: utf-8
from datetime import date

from unidecode import unidecode

import boundaries

# Generated by sets.rb
sets = {
    48028: [u"Acton Vale", u"districts"],
    31056: [u"Adstock", u"districts"],
    92030: [u"Albanel", u"districts"],
    93042: [u"Alma", u"districts"],
    78070: [u"Amherst", u"districts"],
    7047: [u"Amqui", u"districts"],
    55008: [u"Ange-Gardien", u"districts"],
    96020: [u"Baie-Comeau", u"districts"],
    16013: [u"Baie-Saint-Paul", u"districts"],
    88022: [u"Barraute", u"districts"],
    66107: [u"Beaconsfield", u"districts"],
    27028: [u"Beauceville", u"districts"],
    70022: [u"Beauharnois", u"districts"],
    19105: [u"Beaumont", u"districts"],
    57040: [u"Beloeil", u"districts"],
    52035: [u"Berthierville", u"districts"],
    73015: [u"Blainville", u"districts"],
    73005: [u"Boisbriand", u"districts"],
    21045: [u"Boischatel", u"districts"],
    58033: [u"Boucherville", u"districts"],
    46078: [u"Bromont", u"districts"],
    58007: [u"Brossard", u"districts"],
    76043: [u"Brownsburg-Chatham", u"districts"],
    67020: [u"Candiac", u"districts"],
    82020: [u"Cantley", u"districts"],
    4047: [u"Cap-Chat", u"districts"],
    34030: [u"Cap-Santé", u"districts"],
    57010: [u"Carignan", u"districts"],
    7018: [u"Causapscal", u"districts"],
    57005: [u"Chambly", u"districts"],
    2028: [u"Chandler", u"districts"],
    60005: [u"Charlemagne", u"districts"],
    67050: [u"Châteauguay", u"districts"],
    82025: [u"Chelsea", u"districts"],
    62047: [u"Chertsey", u"districts"],
    15035: [u"Clermont", u"districts"],
    42110: [u"Cleveland", u"districts"],
    3010: [u"Cloridorme", u"districts"],
    44071: [u"Compton", u"districts"],
    59035: [u"Contrecoeur", u"districts"],
    41038: [u"Cookshire-Eaton", u"districts"],
    66058: [u"Côte-Saint-Luc", u"districts"],
    71040: [u"Coteau-du-Lac", u"districts"],
    72010: [u"Deux-Montagnes", u"districts"],
    66142: [u"Dollard-Des Ormeaux", u"districts"],
    # Municipality has names. DGEQ doesn't.
    # 66087: [u"Dorval", u"districts"],
    49058: [u"Drummondville", u"districts"],
    46050: [u"Dunham", u"districts"],
    31122: [u"East Broughton", u"districts"],
    46112: [u"Farnham", u"districts"],
    22010: [u"Fossambault-sur-le-Lac", u"districts"],
    30025: [u"Frontenac", u"districts"],
    81017: [u"Gatineau", u"districts"],
    47017: [u"Granby", u"districts"],
    93020: [u"Hébertville", u"districts"],
    71100: [u"Hudson", u"districts"],
    61025: [u"Joliette", u"districts"],
    72802: [u"Kanesatake", u"districts"],
    # Municipality has names. DGEQ doesn't.
    # 66102: [u"Kirkland", u"districts"],
    23057: [u"L'Ancienne-Lorette", u"districts"],
    82005: [u"L'Ange-Gardien", u"districts"],
    93065: [u"L'Ascension-de-Notre-Seigneur", u"districts"],
    60028: [u"L'Assomption", u"districts"],
    60035: [u"L'Épiphanie", u"districts"],
    71060: [u"L'Île-Perrot", u"districts"],
    17078: [u"L'Islet", u"districts"],
    15013: [u"La Malbaie", u"districts"],
    82035: [u"La Pêche", u"districts"],
    67015: [u"La Prairie", u"districts"],
    90012: [u"La Tuque", u"districts"],
    7057: [u"Lac-au-Saumon", u"districts"],
    46075: [u"Lac-Brome", u"districts"],
    79078: [u"Lac-des-Écorces", u"districts"],
    77055: [u"Lac-des-Seize-Îles", u"districts"],
    30030: [u"Lac-Mégantic", u"districts"],
    22015: [u"Lac-Saint-Joseph", u"districts"],
    78095: [u"Lac-Supérieur", u"districts"],
    76020: [u"Lachute", u"districts"],
    52017: [u"Lanoraie", u"districts"],
    65005: [u"Laval", u"districts"],
    52007: [u"Lavaltrie", u"districts"],
    67055: [u"Léry", u"districts"],
    71050: [u"Les Cèdres", u"districts"],
    71033: [u"Les Coteaux", u"districts"],
    1023: [u"Les Îles-de-la-Madeleine", u"districts"],
    # Municipality has names. DGEQ doesn't.
    # 25213: [u"Lévis", u"districts"],
    58227: [u"Longueuil", u"districts"],
    32065: [u"Lyster", u"districts"],
    87058: [u"Macamic", u"districts"],
    45072: [u"Magog", u"districts"],
    89015: [u"Malartic", u"districts"],
    52095: [u"Mandeville", u"districts"],
    55048: [u"Marieville", u"districts"],
    64015: [u"Mascouche", u"districts"],
    8053: [u"Matane", u"districts"],
    57025: [u"McMasterville", u"districts"],
    67045: [u"Mercier", u"districts"],
    93012: [u"Métabetchouan—Lac-à-la-Croix", u"districts"],
    74005: [u"Mirabel", u"districts"],
    9077: [u"Mont-Joli", u"districts"],
    66072: [u"Mont-Royal", u"districts"],
    57035: [u"Mont-Saint-Hilaire", u"districts"],
    78102: [u"Mont-Tremblant", u"districts"],
    78055: [u"Montcalm", u"districts"],
    18050: [u"Montmagny", u"districts"],
    66023: [u"Montréal", u"districts"],
    66007: [u"Montréal-Est", u"districts"],
    30045: [u"Nantes", u"districts"],
    71065: [u"Notre-Dame-de-l'Île-Perrot", u"districts"],
    30010: [u"Notre-Dame-des-Bois", u"districts"],
    61030: [u"Notre-Dame-des-Prairies", u"districts"],
    37235: [u"Notre-Dame-du-Mont-Carmel", u"districts"],
    72032: [u"Oka", u"districts"],
    57030: [u"Otterburn Park", u"districts"],
    2005: [u"Percé", u"districts"],
    71070: [u"Pincourt", u"districts"],
    32040: [u"Plessisville", u"districts"],
    96030: [u"Pointe-aux-Outardes", u"districts"],
    72020: [u"Pointe-Calumet", u"districts"],
    66097: [u"Pointe-Claire", u"districts"],
    96025: [u"Pointe-Lebel", u"districts"],
    82030: [u"Pontiac", u"districts"],
    2047: [u"Port-Daniel—Gascons", u"districts"],
    75040: [u"Prévost", u"districts"],
    32033: [u"Princeville", u"districts"],
    23027: [u"Québec", u"districts"],
    96040: [u"Ragueneau", u"districts"],
    62037: [u"Rawdon", u"districts"],
    60013: [u"Repentigny", u"districts"],
    55057: [u"Richelieu", u"districts"],
    42098: [u"Richmond", u"districts"],
    71133: [u"Rigaud", u"districts"],
    10043: [u"Rimouski", u"districts"],
    12072: [u"Rivière-du-Loup", u"districts"],
    55037: [u"Rougemont", u"districts"],
    86042: [u"Rouyn-Noranda", u"districts"],
    47047: [u"Roxton Pond", u"districts"],
    94068: [u"Saguenay", u"districts"],
    33045: [u"Saint-Agapit", u"districts"],
    62025: [u"Saint-Alphonse-Rodriguez", u"districts"],
    94255: [u"Saint-Ambroise", u"districts"],
    61040: [u"Saint-Ambroise-de-Kildare", u"districts"],
    76008: [u"Saint-André-d'Argenteuil", u"districts"],
    69070: [u"Saint-Anicet", u"districts"],
    12015: [u"Saint-Antonin", u"districts"],
    17055: [u"Saint-Aubert", u"districts"],
    23072: [u"Saint-Augustin-de-Desmaures", u"districts"],
    34038: [u"Saint-Basile", u"districts"],
    57020: [u"Saint-Basile-le-Grand", u"districts"],
    93030: [u"Saint-Bruno", u"districts"],
    85045: [u"Saint-Bruno-de-Guigues", u"districts"],
    58037: [u"Saint-Bruno-de-Montarville", u"districts"],
    63055: [u"Saint-Calixte", u"districts"],
    55023: [u"Saint-Césaire", u"districts"],
    19097: [u"Saint-Charles-de-Bellechasse", u"districts"],
    39060: [u"Saint-Christophe-d'Arthabaska", u"districts"],
    69017: [u"Saint-Chrysostome", u"districts"],
    42100: [u"Saint-Claude", u"districts"],
    75005: [u"Saint-Colomban", u"districts"],
    29057: [u"Saint-Côme—Linière", u"districts"],
    67035: [u"Saint-Constant", u"districts"],
    49070: [u"Saint-Cyrille-de-Wendover", u"districts"],
    54017: [u"Saint-Damase", u"districts"],
    62075: [u"Saint-Damien", u"districts"],
    94245: [u"Saint-David-de-Falardeau", u"districts"],
    42025: [u"Saint-Denis-de-Brompton", u"districts"],
    54060: [u"Saint-Dominique", u"districts"],
    62060: [u"Saint-Donat", u"districts"],
    63030: [u"Saint-Esprit", u"districts"],
    72005: [u"Saint-Eustache", u"districts"],
    10070: [u"Saint-Fabien", u"districts"],
    78047: [u"Saint-Faustin—Lac-Carré", u"districts"],
    62007: [u"Saint-Félix-de-Valois", u"districts"],
    32013: [u"Saint-Ferdinand", u"districts"],
    21010: [u"Saint-Ferréol-les-Neiges", u"districts"],
    33052: [u"Saint-Flavien", u"districts"],
    42020: [u"Saint-François-Xavier-de-Brompton", u"districts"],
    94235: [u"Saint-Fulgence", u"districts"],
    52080: [u"Saint-Gabriel", u"districts"],
    93035: [u"Saint-Gédéon", u"districts"],
    29073: [u"Saint-Georges", u"districts"],
    49048: [u"Saint-Germain-de-Grantham", u"districts"],
    19068: [u"Saint-Henri", u"districts"],
    93070: [u"Saint-Henri-de-Taillon", u"districts"],
    94240: [u"Saint-Honoré", u"districts"],
    54048: [u"Saint-Hyacinthe", u"districts"],
    52045: [u"Saint-Ignace-de-Loyola", u"districts"],
    26063: [u"Saint-Isidore", u"districts"],
    57033: [u"Saint-Jean-Baptiste", u"districts"],
    56083: [u"Saint-Jean-sur-Richelieu", u"districts"],
    75017: [u"Saint-Jérôme", u"districts"],
    27043: [u"Saint-Joseph-de-Beauce", u"districts"],
    72025: [u"Saint-Joseph-du-Lac", u"districts"],
    58012: [u"Saint-Lambert", u"districts"],
    71105: [u"Saint-Lazare", u"districts"],
    50042: [u"Saint-Léonard-d'Aston", u"districts"],
    63048: [u"Saint-Lin—Laurentides", u"districts"],
    70035: [u"Saint-Louis-de-Gonzague", u"districts"],
    57045: [u"Saint-Mathieu-de-Beloeil", u"districts"],
    37230: [u"Saint-Maurice", u"districts"],
    68050: [u"Saint-Michel", u"districts"],
    93045: [u"Saint-Nazaire", u"districts"],
    67010: [u"Saint-Philippe", u"districts"],
    54008: [u"Saint-Pie", u"districts"],
    72043: [u"Saint-Placide", u"districts"],
    68055: [u"Saint-Rémi", u"districts"],
    63035: [u"Saint-Roch-de-l'Achigan", u"districts"],
    15058: [u"Saint-Siméon", u"districts"],
    70040: [u"Saint-Stanislas-de-Kostka", u"districts"],
    61027: [u"Saint-Thomas", u"districts"],
    35027: [u"Saint-Tite", u"districts"],
    16055: [u"Saint-Urbain", u"districts"],
    71025: [u"Saint-Zotique", u"districts"],
    77022: [u"Sainte-Adèle", u"districts"],
    66117: [u"Sainte-Anne-de-Bellevue", u"districts"],
    53065: [u"Sainte-Anne-de-Sorel", u"districts"],
    4037: [u"Sainte-Anne-des-Monts", u"districts"],
    73035: [u"Sainte-Anne-des-Plaines", u"districts"],
    22045: [u"Sainte-Brigitte-de-Laval", u"districts"],
    67030: [u"Sainte-Catherine", u"districts"],
    45060: [u"Sainte-Catherine-de-Hatley", u"districts"],
    22005: [u"Sainte-Catherine-de-la-Jacques-Cartier", u"districts"],
    19055: [u"Sainte-Claire", u"districts"],
    68020: [u"Sainte-Clotilde", u"districts"],
    52040: [u"Sainte-Geneviève-de-Berthier", u"districts"],
    59010: [u"Sainte-Julie", u"districts"],
    63060: [u"Sainte-Julienne", u"districts"],
    72015: [u"Sainte-Marthe-sur-le-Lac", u"districts"],
    61050: [u"Sainte-Mélanie", u"districts"],
    75028: [u"Sainte-Sophie", u"districts"],
    73010: [u"Sainte-Thérèse", u"districts"],
    2010: [u"Sainte-Thérèse-de-Gaspé", u"districts"],
    70052: [u"Salaberry-de-Valleyfield", u"districts"],
    66127: [u"Senneville", u"districts"],
    97007: [u"Sept-Îles", u"districts"],
    36033: [u"Shawinigan", u"districts"],
    43027: [u"Sherbrooke", u"districts"],
    53052: [u"Sorel-Tracy", u"districts"],
    13073: [u"Témiscouata-sur-le-Lac", u"districts"],
    64008: [u"Terrebonne", u"districts"],
    31084: [u"Thetford Mines", u"districts"],
    37067: [u"Trois-Rivières", u"districts"],
    89008: [u"Val-d'Or", u"districts"],
    78010: [u"Val-David", u"districts"],
    82015: [u"Val-des-Monts", u"districts"],
    59020: [u"Varennes", u"districts"],
    71083: [u"Vaudreuil-Dorion", u"districts"],
    59025: [u"Verchères", u"districts"],
    39062: [u"Victoriaville", u"districts"],
    47025: [u"Waterloo", u"districts"],
    41098: [u"Weedon", u"districts"],
    77060: [u"Wentworth-Nord", u"districts"],
    66032: [u"Westmount", u"districts"],
    46080: [u"Cowansville", u"quartiers"],
    67025: [u"Delson", u"quartiers"],
    93005: [u"Desbiens", u"quartiers"],
    3005: [u"Gaspé", u"quartiers"],
    2015: [u"Grande-Rivière", u"quartiers"],
    69055: [u"Huntingdon", u"quartiers"],
    87090: [u"La Sarre", u"quartiers"],
    34120: [u"Lac-Sergent", u"quartiers"],
    83065: [u"Maniwaki", u"quartiers"],
    13095: [u"Pohénégamook", u"quartiers"],
    53050: [u"Saint-Joseph-de-Sorel", u"quartiers"],
    89040: [u"Senneterre", u"quartiers"],
    11040: [u"Trois-Pistoles", u"quartiers"],
}

def namer(f):
    # @note Saint-Jérôme (2475017) has names for districts.
    if f.get('CO_MUNCP') == 23027:
        return {
            u'Cap-Rouge-Laurentien': u'Cap-Rouge—Laurentien',
            u'La Chute-Montmorency-Seigneurial': u'La Chute-Montmorency—Seigneurial',
            u'Lac-Saint-Charles-Saint-Émile': u'Lac-Saint-Charles—Saint-Émile',
            u'Montcalm-Saint-Sacrement': u'Montcalm—Saint-Sacrement',
            u'Monts': u'Les Monts',
            u'Plateau': u'Le Plateau',
            u'Pointe-de-Sainte-Foy': u'La Pointe-de-Sainte-Foy',
            u'Saint-Louis-Sillery': u'Saint-Louis—Sillery',
            u'Saint-Roch-Saint-Sauveur': u'Saint-Roch—Saint-Sauveur',
        }.get(f.get('NM_DIS'), f.get('NM_DIS'))
    elif f.get('CO_MUNCP') == 58227:
        return re.sub(r"\A(?:d'|de |du |des )", '', f.get('NM_DIS'))
    elif f.get('CO_MUNCP') == 66097:
        return f.get('NM_DIS').replace('/ ', '/')
    elif f.get('CO_MUNCP') == 81017:
        return {
            u'de Hull-Val-Tétreau': u'de Hull—Val-Tétreau',
            u'de Saint-Raymond-Vanier': u'de Saint-Raymond—Vanier',
            u'de Wright-Parc-de-la-Montagne': u'Wright—Parc-de-la-Montagne',
            u'du Plateau-Manoir-des-Trembles': u'du Plateau—Manoir-des-Trembles',
        }.get(f.get('NM_DIS'), f.get('NM_DIS'))
    else:
        if f.get('NM_DIS'):
            return f.get('NM_DIS')
        elif f.get('MODE_SUFRG') == 'Q':
            return u'Quartier %s' % int(f.get('NO_DIS'))
        else:
            return u'District %s' % int(f.get('NO_DIS'))

def ider(f):
    if f.get('CO_MUNCP') == 43027:
        return '%d' % (int(f.get('NO_DIS') * 10))
    else:
        return int(f.get('NO_DIS'))

for geographic_code, (name, type) in sets.items():
    boundaries.register(u'%s %s' % (name, type),
        file='%s-24%05d.shp' % (unidecode(name), geographic_code),
        domain=u'%s, QC' % name,
        last_updated=date(2014, 2, 28),
        name_func=namer,
        id_func=ider,
        authority=u'Directeur général des élections du Québec',
        licence_url='http://www.electionsquebec.qc.ca/francais/conditions-d-utilisation-de-notre-site-web.php',
        encoding='iso-8859-1',
        metadata={'geographic_code': '24%05d' % geographic_code},
        ogr2ogr='''-where "CO_MUNCP='%d'"''' % geographic_code,
        base_file='Districts Elec Mun 2014-02-28_DetU_region.shp',
    )

boundaries.register(u'Paroisse de Plessisville districts',
    file='Plessisville-2432045.shp',
    domain=u'Plessisville, QC',
    last_updated=date(2014, 2, 28),
    name_func=namer,
    id_func=ider,
    authority=u'Directeur général des élections du Québec',
    licence_url='http://www.electionsquebec.qc.ca/francais/conditions-d-utilisation-de-notre-site-web.php',
    encoding='iso-8859-1',
    metadata={'geographic_code': '2432045'},
    ogr2ogr='''-where "CO_MUNCP='2432045'"''',
    base_file='Districts Elec Mun 2014-02-28_DetU_region.shp',
)

boroughs_quebec = {
    u'ocd-division/country:ca/csd:2423027/borough:1': [u'La Cité-Limoilou', u'LACITELIMOILOU'],
    u'ocd-division/country:ca/csd:2423027/borough:2': [u'Les Rivières', u'LESRIVIERES'],
    u'ocd-division/country:ca/csd:2423027/borough:3': [u'Sainte-Foy–Sillery–Cap-Rouge', u'SAINTFOYSILLERYCAPROUGE'],
    u'ocd-division/country:ca/csd:2423027/borough:4': [u'Charlesbourg', u'CHARLESBOURG'],
    u'ocd-division/country:ca/csd:2423027/borough:5': [u'Beauport', u'BEAUPORT'],
    u'ocd-division/country:ca/csd:2423027/borough:6': [u'La Haute-Saint-Charles', u'LAHAUTESAINTCHARLES'],
}

for ocd_division, (name, machine_name) in boroughs_quebec.items():
    boundaries.register(u'%s districts' % name,
        file=u'Quebec-%s.shp' % unidecode(name),
        domain=u'%s, Québec, QC' % name,
        last_updated=date(2014, 2, 28),
        name_func=namer,
        id_func=lambda f: int(f.get('NO_DIS')),
        authority=u'Directeur général des élections du Québec',
        licence_url='http://www.electionsquebec.qc.ca/francais/conditions-d-utilisation-de-notre-site-web.php',
        encoding='iso-8859-1',
        metadata={'ocd_division': ocd_division},
        ogr2ogr='''-where "CO_MUNCP='23027' AND NMTRI_ARON='%s'"''' % machine_name,
        base_file='Districts Elec Mun 2014-02-28_DetU_region.shp',
    )

boroughs_montreal = {
    u'ocd-division/country:ca/csd:2466023/borough:ahuntsic-cartierville': [u"Ahuntsic-Cartierville", u'AHUNTSICCARTIERVILLE'],
    u'ocd-division/country:ca/csd:2466023/borough:anjou': [u"Anjou", u'ANJOU'],
    u'ocd-division/country:ca/csd:2466023/borough:côte-des-neiges~notre-dame-de-grâce': [u"Côte-des-Neiges—Notre-Dame-de-Grâce", u'COTEDESNEIGESNOTREDAMEDEGRACE'],
    u'ocd-division/country:ca/csd:2466023/borough:lachine': [u"Lachine", u'LACHINE'],
    u'ocd-division/country:ca/csd:2466023/borough:lasalle': [u"LaSalle", u'LASALLE'],
    u'ocd-division/country:ca/csd:2466023/borough:le_plateau-mont-royal': [u"Le Plateau-Mont-Royal", u'LEPLATEAUMONTROYAL'],
    u'ocd-division/country:ca/csd:2466023/borough:le_sud-ouest': [u"Le Sud-Ouest", u'LESUDOUEST'],
    u'ocd-division/country:ca/csd:2466023/borough:l~île-bizard~sainte-geneviève': [u"L'Île-Bizard—Sainte-Geneviève", u'LILEBIZARDSAINTGENEVIEVE'],
    u'ocd-division/country:ca/csd:2466023/borough:mercier~hochelaga-maisonneuve': [u"Mercier—Hochelaga-Maisonneuve", u'MERCIERHOCHELAGAMAISONNEUVE'],
    u'ocd-division/country:ca/csd:2466023/borough:montréal-nord': [u"Montréal-Nord", u'MONTREALNORD'],
    u'ocd-division/country:ca/csd:2466023/borough:outremont': [u"Outremont", u'OUTREMONT'],
    u'ocd-division/country:ca/csd:2466023/borough:pierrefonds-roxboro': [u"Pierrefonds-Roxboro", u'PIERREFONDROXBORO'],
    u'ocd-division/country:ca/csd:2466023/borough:rivière-des-prairies~pointe-aux-trembles': [u"Rivière-des-Prairies—Pointe-aux-Trembles", u'RIVIEREDESPRAIRIESPOINTEAUXTREMBLES'],
    u'ocd-division/country:ca/csd:2466023/borough:rosemont~la_petite-patrie': [u"Rosemont—La Petite-Patrie", u'ROSEMONTLAPETITEPATRIE'],
    u'ocd-division/country:ca/csd:2466023/borough:saint-laurent': [u"Saint-Laurent", u'SAINTLAURENT'],
    u'ocd-division/country:ca/csd:2466023/borough:saint-léonard': [u"Saint-Léonard", u'SAINTLEONARD'],
    u'ocd-division/country:ca/csd:2466023/borough:verdun': [u"Verdun", u'VERDUN'],
    u'ocd-division/country:ca/csd:2466023/borough:ville-marie': [u"Ville-Marie", u'VILLEMARIE'],
    u'ocd-division/country:ca/csd:2466023/borough:villeray~saint-michel~parc-extension': [u"Villeray—Saint-Michel—Parc-Extension", u'VILLERAYSAINTMICHELPARCEXTENSION'],
}

for ocd_division, (name, machine_name) in boroughs_montreal.items():
    boundaries.register(u'%s districts' % name,
        file=u'Montreal-%s.shp' % unidecode(name),
        domain=u'%s, Montréal, QC' % name,
        last_updated=date(2014, 2, 28),
        name_func=namer,
        id_func=lambda f: int(f.get('NO_DIS')),
        authority=u'Directeur général des élections du Québec',
        licence_url='http://www.electionsquebec.qc.ca/francais/conditions-d-utilisation-de-notre-site-web.php',
        encoding='iso-8859-1',
        metadata={'ocd_division': ocd_division},
        ogr2ogr='''-where "CO_MUNCP='66023' AND NMTRI_ARON='%s'"''' % machine_name,
        base_file='Districts Elec Mun 2014-02-28_DetU_region.shp',
    )
