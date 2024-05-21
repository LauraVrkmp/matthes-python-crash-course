from city_functions import format_string_city_country
from population import format_string_city_country_population

def test_city_country():
    formatted_string = format_string_city_country('santiago', 'chile')
    assert formatted_string == "Santiago, Chile"

def test_city_country_population():
    formatted_string = format_string_city_country_population('santiago',
                                                             'chile', 5000000)
    assert formatted_string == "Santiago, Chile - population 5000000"