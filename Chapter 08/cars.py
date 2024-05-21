def car_info(manufacturer, model, **info):
    info['manufacturer'] = manufacturer
    info['model'] = model
    return info

car = car_info('subaru', 'outback', color='blue', tow_package=True)
print(car)