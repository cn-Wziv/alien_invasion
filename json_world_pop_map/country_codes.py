from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    # 返回国别码
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # 没找到制定国家则返回None
    return None

print(get_country_code('Andorra'))
print(get_country_code('United Arab Emirates'))
print(get_country_code('Afghanistan'))