

# mags, lons, lats, eq_titles = [], [], [], []
# for eq_dict in all_eq_dicts:
#     mags.append(eq_dict['properties']['mag'])
#     lons.append(eq_dict['geometry']['coordinates'][0])
#     lats.append(eq_dict['geometry']['coordinates'][1])
#     eq_titles.append(eq_dict['properties']['title'])

# title = all_eq_data['metadata']['title']
# fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
#                      color=mags, color_continuous_scale='Viridis',
#                      labels={'color':'Magnitude'},
#                      projection='natural earth',
#                      hover_name=eq_titles,
#                      )
# fig.write_html('first_figure.html', auto_open