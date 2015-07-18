from models import region

__author__ = 'Andrew'


def get_region_by_slug(slug):
    """
    Creates a region object from the data within this .py file
    :param slug:
    :return:
    """
    # Create an empty region
    new_region = region.Region()

    # Giant switch statement for different regions
    # NOTE: Once a usable database is up and running, this should be ported to the database
    if slug == "oce":
        new_region.name = "Oceania"
        new_region.slug = slug
        new_region.locales = ["en_AU"]
        new_region.platform_id = "OC1"

    elif slug == "na":
        new_region.name = "North America"
        new_region.slug = slug
        new_region.locales = ["en_US"]
        new_region.platform_id = "NA1"

    elif slug == "euw":
        new_region.name = "Europe West"
        new_region.slug = slug
        new_region.locales = ['en_GB', 'de_DE', 'es_ES', 'fr_FR', 'it_IT']
        new_region.platform_id = "EUW1"

    elif slug == "eune":
        new_region.name = "Europe Nordic East"
        new_region.slug = slug
        new_region.locales = ['en_PL', 'pl_PL', 'el_GR', 'ro_RO', 'cs_CZ', 'hu_HU']
        new_region.platform_id = "EUN1"

    elif slug == "lan":
        new_region.name = "Latin America North"
        new_region.slug = slug
        new_region.locales = ['es_MX']
        new_region.platform_id = "LA1"

    elif slug == "las":
        new_region.name = "Latin America South"
        new_region.slug = slug
        new_region.locales = ['es_AR']
        new_region.platform_if = "LA2"

    elif slug == "br":
        new_region.name = "Brazil"
        new_region.slug = slug
        new_region.locales = ['pt_BR']
        new_region.platform_id = "BR1"

    elif slug == "tr":
        new_region.name = "Turkey"
        new_region.slug = slug
        new_region.locales = ['tr_TR']
        new_region.platform_id = "TR1"

    elif slug == "ru":
        new_region.name = "Russia"
        new_region.slug = slug
        new_region.locales = ['ru_RU']
        new_region.platform_id = "RU"

    elif slug == "kr":
        new_region.name = "Korea"
        new_region.slug = slug
        new_region.locales = ['ko_KR']
        new_region.platform_id = "KR"

    # Return the region specified
    return new_region
