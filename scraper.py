from selenium import webdriver
dr = webdriver.Edge('C:/Users/Mircea Timpuriu/Desktop/msedgedriver.exe')

locations = ["Alicante",
"Amsterdam",
"Ankara",
"Antalya",
"Atena",
"Baia Mare",
"Barcelona",
"Bari",
"Belgrad",
"Berlin",
"Berna",
"Bilbao",
"Bodrum",
"Bologna",
"Bonn",
"Bordeaux",
"Bratislava",
"Brest",
"Bruxelles",
"Bucuresti",
"Budapesta",
"Catania",
"Chisinau",
"Cluj-Napoca",
"Constanta",
"Copenhaga",
"Cork",
"Cracovia",
"Dortmund",
"Dublin",
"Dubrovnik",
"Florenta",
"Frankfurt",
"Geneva",
"Glasgow",
"Gran Canaria",
"Hamburg",
"Hanovra",
"Heraklion",
"Helsinki",
"Iasi",
"Ibiza",
"Innsbruck",
"Istanbul",
"Kiev",
"Koln",
"Larnaca",
"Lisabona",
"Londra",
"Lyon",
"Madrid",
"Malaga",
"Mallorca",
"Malta",
"Manchester",
"Marsilia",
"Milano",
"Montpellier",
"Munich",
"Mykonos",
"Nantes",
"Napoli",
"Nisa",
"Nuremberg",
"Oradea",
"Oslo",
"Palermo",
"Paphos",
"Paris",
"Pisa",
"Porto",
"Praga",
"Rennes",
"Rhodos",
"Rimini",
"Roma",
"Salonic",
"Salzburg",
"Seviliai",
"Sibiu",
"Sofia",
"Stockholm",
"Strasbourg",
"Stuttgart",
"Talin",
"Targu Mures",
"Tenerife",
"Timisoara",
"Tirana",
"Torino",
"Toulouse",
"Treviso",
"Valencia",
"Varsovia",
"Venetia",
"Verona",
"Viena",
"Zagreb",
"Zaragoza",
"Zurich"]

locations_abbr = ["ALC",
"AMS",
"ANK",
"AYT",
"ATH",
"BAY",
"BCN",
"BRI",
"BEG",
"BER",
"BRN",
"BIO",
"BXN",
"BLQ",
"BNJ",
"BOD",
"BTS",
"BES",
"BRU",
"BUH",
"BUD",
"CTA",
"KIV",
"CLJ",
"CND",
"CPH",
"ORK",
"KRK",
"DTM",
"DUB",
"DBV",
"FLR",
"FRA",
"GVA",
"GLA",
"LPA",
"HAM",
"HAJ",
"HER",
"HEL",
"IAS",
"IBZ",
"INN",
"IST",
"IEV",
"CGN",
"LCA",
"LIS",
"LON",
"LYS",
"MAD",
"AGP",
"PMI",
"MLA",
"MAN",
"MRS",
"MIL",
"MPL",
"MUC",
"JMK",
"NTE",
"NAP",
"NCE",
"NUE",
"OMR",
"OSL",
"PMO",
"PFO",
"PAR",
"PSA",
"OPO",
"PRG",
"RNS",
"RHO",
"RMI",
"ROM",
"SKG",
"SZG",
"SVQ",
"SBZ",
"SOF",
"STO",
"SXB",
"STR",
"TLL",
"TGM",
"TCI",
"TSR",
"TIA",
"TRN",
"TLS",
"TSF",
"VLC",
"WAW",
"VCE",
"VRN",
"VIE",
"ZAG",
"ZAZ",
"ZRH"]

for i in range(1):
    for j in range(2):
        if i != j:
            dr.get("http://vola.ro/flight_search/from/" + locations[i] + "/to/" + locations[j] + "/from_code/" + locations_abbr[i] + "/to_code/" + locations_abbr[j] + "/dd/2023-12-05/rd/2023-11-17/ad/1/ow/1")
            