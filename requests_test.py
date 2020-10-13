import requests as r


url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/'
headers = {'token': 'ISXLkoppxlzAjWSsvSHGHptpzxHEaDRH'}
# limit = '?limit=1000'

'''
The following is a group of check functions. They increase in specificity the furhter down you go. All can be combined with optional endpoints which narrow down the results to specific time periods, locations, or observable events
'''

# There are 11 data sets, they include sets like Daily Summaries
check_datasets = r.get(url+'/datasets'+limit, headers=headers)

# There are 42 data categories, they include categories like Annual Temperature
check_datacategories = r.get(url+'/datacategories'+limit, headers=headers)

# There are 1535 data types, they include types like
# Highest soil temperature at observation time
check_datatypes = r.get(url+'/datatypes'+limit, headers=headers)


check_locationcategories = r.get(url+'/locationcategories', headers=headers)
# https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=PRECIP_15&stationid=COOP:010008&units=metric&startdate=2010-05-01&enddate=2010-05-31

