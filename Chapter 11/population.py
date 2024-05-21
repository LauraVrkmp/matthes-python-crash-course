def format_string_city_country_population(city, country, population):
    string = f"{city}, {country}"
    string = string.title()
    string += f" - population {population}"
    return string