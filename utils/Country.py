import pycountry

CUSTOM_COUNTRY_FIXES = {
    "US": "United States",
    "USA": "United States",
    "U.S.": "United States",
    "United States of America": "United States",
    "UK": "United Kingdom",
    "U.K.": "United Kingdom",
    "Russia": "Russian Federation",
    "Korea, South": "Korea, Republic of",
    "Korea, North": "Korea, Democratic People's Republic of",
    "Iran": "Iran, Islamic Republic of",
    "Syria": "Syrian Arab Republic",
    "Venezuela": "Venezuela, Bolivarian Republic of",
    "Bolivia": "Bolivia, Plurinational State of",
    "Tanzania": "Tanzania, United Republic of",
    "Vietnam": "Viet Nam",
    "Laos": "Lao People's Democratic Republic",
    "Moldova": "Moldova, Republic of",
    "Brunei": "Brunei Darussalam",
    "Czechia": "Czech Republic",
    "Burma": "Myanmar",
    "Taiwan*": "Taiwan, Province of China",
    "Turkey": "Türkiye",
}


def country_to_iso3(country):
    if country != None:
        country = country.strip()
    # Apply manual fixes first
    country = CUSTOM_COUNTRY_FIXES.get(country, country)
    try:
        country = pycountry.countries.lookup(country)
        return country.alpha_3
    except LookupError:
        return None