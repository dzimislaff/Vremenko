#!/usr/bin/env python
# -*- coding: 'UTF-8' -*-

BAZA = ('http://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/sl/'
        'observationAms_')
ZRAK = 'http://www.arso.gov.si/xml/zrak/ones_zrak_urni_podatki_zadnji.xml'

# slovar s kombinacijo povezav: osnova + končnica
KRAJI_URL = {
    'Ljubljana': (BAZA + 'LJUBL-ANA_BEZIGRAD_latest.xml'),
    'Novo mesto': (BAZA + 'NOVO-MES_latest.xml'),
    'Rogaška Slatina': (BAZA + 'ROGAS-SLA_latest.xml'),
    'Metlika': (BAZA + 'METLIKA_latest.xml'),
    'Črnomelj': (BAZA + 'CRNOMELJ_latest.xml'),
    'Koper': (BAZA + 'KOPER_KAPET-IJA_latest.xml'),
    'Celje': (BAZA + 'CELJE_MEDLOG_latest.xml'),
    'Kočevje': (BAZA + 'KOCEVJE_latest.xml'),
    'Maribor': (BAZA + 'MARIBOR_VRBAN-PLA_latest.xml'),
    'Podčetrtek': (BAZA + 'PODCE-TEK_ATOMS-TOP_latest.xml'),
    'Bilje pri Novi Gorici': (BAZA + 'NOVA-GOR_BILJE_latest.xml'),
    'Marinča vas': (BAZA + 'MARIN-VAS_latest.xml'),
    'Murska Sobota': (BAZA + 'MURSK-SOB_latest.xml'),
    'Trbovlje': (BAZA + 'TRBOVLJE_latest.xml'),
    'Krško': (BAZA + 'KRSKO_NEK_latest.xml'),
    'Nanos (1242 m)': (BAZA + 'NANOS_latest.xml'),
    'Rogla (1494 m)': (BAZA + 'ROGLA_latest.xml'),
    'Kredarica (2514 m)': (BAZA + 'KREDA-ICA_latest.xml'),
}

KRAJI_SKLONI = {
    'Ljubljana': 'Ljubljano',
    'Novo mesto': 'Novo mesto',
    'Rogaška Slatina': 'Rogaško Slatino',
    'Metlika': 'Metliko',
    'Črnomelj': 'Črnomelj',
    'Koper': 'Koper',
    'Celje': 'Celje',
    'Kočevje': 'Kočevje',
    'Maribor': 'Maribor',
    'Podčetrtek': 'Podčetrtek',
    'Bilje pri Novi Gorici': 'Bilje pri Novi Gorici',
    'Marinča vas': 'Marinčo vas',
    'Murska Sobota': 'Mursko Soboto',
    'Trbovlje': 'Trbovlje',
    'Krško': 'Krško',
    'Nanos (1242 m)': 'Nanos (1242 m)',
    'Rogla (1494 m)': 'Roglo (1494 m)',
    'Kredarica (2514 m)': 'Kredarico',
}

# slovarja z imenom kategorije in xpathom do podatka v XML-datoteki
XPATH_VREME = {
    'Opis vremena': '/data/metData/nn_icon-wwsyn_icon',
    'Temperatura': '/data/metData/t',
    'Relativna vlaga': '/data/metData/rh',
    'Tlak': '/data/metData/mslavg',
    'Povprečno sončno obsevanje': '/data/metData/gSunRadavg',
    'Vsota padavin': '/data/metData/rr_val',
}

XPATH_VETER = {
    'Smer vetra': '/data/metData/ddavg_longText',
    'Hitrost vetra': '/data/metData/ffavg_val',
    'Sunki vetra': '/data/metData/ffmax_val_kmh',
}

XPATH_ČAS = "/data/metData/tsValid_issued"

# slovar s prevodom vremenskih oznak za izpis
OPIS_VREMENA = {
    None: None,
    'clear': ('jasno', 'Jasno je'),
    'mostClear': ('pretežno jasno', 'Pretežno jasno je'),
    'slightCloudy': ('rahlo oblačno', 'Rahlo oblačno je'),
    'partCloudy': ('delno oblačno', 'Delno oblačno je'),
    'modCloudy': ('zmerno oblačno', 'Zmerno oblačno je'),
    'prevCloudy': ('pretežno oblačno', 'Pretežno oblačno je'),
    'overcast': ('oblačno', 'Oblačno je'),
    'FG': ('megla', 'Megla je'),
    'lightFG': ('redka megla', 'Redka megla je'),
    'modFG': ('zmerna megla', 'Zmerna megla je'),
    'heavyFG': ('gosta megla', 'Gosta megla je'),
    'DZ': ('rosenje', 'Rosi'),
    'lightDZ': ('rahlo rosenje', 'Rahlo rosi'),
    'modDZ': ('zmerno rosenje', 'Zmerno rosi'),
    'heavyDZ': ('močno rosenje', 'Močno rosi'),
    'FZDZ': ('rosenje, ki zmrzuje', 'Rosenje, ki zmrzuje, je'),
    'lightFZDZ': ('rosenje, ki zmrzuje', 'Rahlo rosenje, ki zmrzuje, je'),
    'modFZDZ': ('rosenje, ki zmrzuje', 'Zmerno rosenje, ki zmrzuje, je'),
    'heavyFZDZ': ('rosenje, ki zmrzuje', 'Močno rosenje, ki zmrzuje, je'),
    'RA': ('dež', 'Dežuje'),
    'lightRA': ('šibek dež', 'Šibko dežuje'),
    'modRA': ('dež', 'Zmerno dežuje'),
    'heavyRA': ('dež', 'Močno dežuje'),
    'FZRA': ('dež, ki zmrzuje', 'Pada dež, ki zmrzuje'),
    'lightFZRA': ('šibek dež, ki zmrzuje', 'Pada šibek dež, ki zmrzuje'),
    'modFZRA': ('zmeren dež, ki zmrzuje', 'Pada zmeren dež, ki zmrzuje'),
    'heavyFZRA': ('močan dež, ki zmrzuje', 'Pada močan dež, ki zmrzuje'),
    'RASN': ('dež s snegom', 'Dež s snegom je'),
    'lightRASN': ('šibekdež s snegom', 'Šibek dež s snegom je'),
    'modRASN': ('zmeren dež s snegom', 'Zmeren dež s snegom je'),
    'heavyRASN': ('močan dež s snegom', 'Močan dež s snegom je'),
    'SN': ('sneg', 'Sneži'),  # sneženje namesto sneg?
    'lightSN': ('rahel sneg', 'Šibko sneži'),
    'modSN': ('zmeren sneg', 'Zmerno sneži'),
    'heavySN': ('močan sneg', 'Močno sneži'),
    'SHRA': ('ploha dežja', 'Naliv je'),
    'lightSHRA': ('šibka ploha dežja', 'Šibka ploha dežja je'),
    'modSHRA': ('zmerna ploha dežja', 'Zmerna ploha dežja je'),
    'heavySHRA': ('močna ploha dežja', 'Močna ploha dežja je'),
    'SHRASN': ('ploha dežja s snegom', 'Ploha dežja s snegom je'),
    'lightSHRASN': ('šibka ploha dežja s snegom', 'Šibka ploha dežja s snegom je'),
    'modSHRASN': ('zmerna ploha dežja s snegom', 'Zmerna ploha dežja s snegom je'),
    'heavySHRASN': ('močna ploha dežja s snegom', 'Močna ploha dežja s snegom je'),
    'SHSN': ('snežna ploha', 'Snežna ploha je'),
    'lightSHSN': ('šibka snežna ploha', 'Šibka snežna ploha je'),
    'modSHSN': ('zmerna snežna ploha', 'Zmerna snežna ploha je'),
    'heavySHSN': ('močna snežna ploha', 'Močna snežna ploha je'),
    'SHGR': ('ploha toče', 'Toča je'),
    'lightSHGR': ('šibka ploha sodre', 'Šibka ploha sodre je'),
    'modSHGR': ('zmerna ploha sodre', 'Zmerna ploha sodre je'),
    'heavySHGR': ('močna ploha sodre', 'Močna ploha sodre je'),
    'TS': ('nevihta', 'Nevihta je'),
    'lightTS': ('šibka nevihta', 'Šibka nevihta je'),
    'modTS': ('zmerna nevihta', 'Zmerna nevihta je'),
    'heavyTS': ('močna nevihta', 'Močna nevihta je'),
    'TSRA': ('nevihta z dežjem', 'Nevihta z dežjem je'),
    'lightTSRA': ('šibka nevihta z dežjem', 'Šibka nevihta z dežjem je'),
    'modTSRA': ('zmerna nevihta z dežjem', 'Zmerna nevihta z dežjem je'),
    'heavyTSRA': ('močna nevihta z dežjem', 'Močna nevihta z dežjem je'),
    'TSRASN': ('nevihta z dežjem in snegom', 'Nevihta z dežjem in snegom je'),
    'lightTSRASN': ('šibka nevihta z dežjem in snegom', 'Šibka nevihta z dežjem in snegom je'),
    'modTSRASN': ('zmerna nevihta z dežjem in snegom', 'Zmerna nevihta z dežjem in snegom je'),
    'heavyTSRASN': ('močna nevihta z dežjem in snegom', 'Močna nevihta z dežjem in snegom je'),
    'TSSN': ('nevihta s sneženjem', 'Nevihta s sneženjem je'),
    'lightTSSN': ('šibka nevihta s sneženjem', 'Šibka nevihta s sneženjem je'),
    'modTSSN': ('zmerna nevihta s sneženjem', 'Zmerna nevihta s sneženjem je'),
    'heavyTSSN': ('močna nevihta s sneženjem', 'Močna nevihta s sneženjem je'),
    'TSGR': ('nevihta s točo', 'Nevihta s točo je'),
    'lightTSGR': ('šibka nevihta s točo', 'Šibka nevihta s točo je'),
    'modTSGR': ('zmerna nevihta s točo', 'Zmerna nevihta s točo je'),
    'heavyTSGR': ('močna nevihta s točo', 'Močna nevihta s točo je'),
    # kombinacije
    'prevCloudy_lightRA': ('pretežno oblačno z rahlim dežjem', 'Pretežno oblačno z rahlim dežjem je'),
    'overcast_lightRA': ('oblačno z rahlim dežjem', 'Oblačno z rahlim dežjem je'),
    'prevCloudy_modRA': ('pretežno oblačno z zmernim dežjem', 'Pretežno oblačno z zmernim dežjem je'),
    'overcast_modRA': ('oblačno z zmernim dežjem', 'Oblačno z zmernim dežjem je'),
    'prevCloudy_heavyRA': ('pretežno oblačno z močnim dežjem', 'Pretežno oblačno z močnim dežjem je'),
    'overcast_heavyRA': ('oblačno z močnim dežjem', 'Oblačno z močnim dežjem je'),
    'prevCloudy_lightSN': ('pretežno oblačno s šibkim sneženjem', 'Pretežno oblačno s šibkim sneženjem je'),
    'overcast_lightSN': ('oblačno s šibkim sneženjem', 'Oblačno s šibkim sneženjem je'),
    'overcast_modSN': ('oblačno z zmernim sneženjem', 'Oblačno z zmernim sneženjem je'),
    'prevCloudy_modSN': ('pretežno oblačno z zmernim sneženjem', 'Pretežno oblačno z zmernim sneženjem je'),
    'overcast_heavySN': ('oblačno z močnim sneženjem', 'Oblačno z močnim sneženjem je'),
    'prevCloudy_heavySN': ('pretežno oblačno z močnim sneženjem', 'Pretežno oblačno z močnim sneženjem je'),
}

# tuple za vpis smeri vetra v podatkovno bazo: severovzhodnik -> 1 ...
VETER_IZPIS = (
    None,
    'severovzhodnik',
    'vzhodnik',
    'jugovzhodnik',
    'južni veter',
    'jugozahodnik',
    'zahodnik',
    'severozahodnik',
    'severnik'

)

# slovar z imenom kraja in šifro
ZRAK_ŠIFRE = {
    'Ljubljana': 'E21',
    'Maribor': 'E22',
    'Celje': 'E23',
    'Murska Sobota': 'E24',
    'Nova Gorica': 'E25',
    'Trbovlje': 'E26',
    'Koper': 'E30',
    'Novo mesto': 'E418'
}

# slovar z z vrsto onesnaženja, enoto in mejno vrednostjo
ZRAK_KATEGORIJE = {
    'pm10': ('µg/m³', 50),  # 50 µg/m³ je povprečna dnevna mejna vrednost
    'pm2.5': ('µg/m³', 50),  # mejna vrednost ni določena
    'so2': ('µg/m³', 350),
    'co': ('mg/m³', 10),
    'o3': ('µg/m³', 180),
    'no2': ('µg/m³', 200),
}
