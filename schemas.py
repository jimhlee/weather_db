
# The intended primary key will always be listed first
tables = { 
    # Date is the primary key, along with stationid, we can pinpoint any event
    'weather_table': (
            ('eventid', 'serial'),
            ('date', 'date'),
            ('stationid', 'varchar'),
            ('name', 'varchar'),
            ('prcp', 'float'),
            ('snow', 'float'),
            ('snwd', 'float'),
            ('tmax', 'int'),
            ('tmin', 'int'),
        ),
    # stationid is the primary key
    'location_table': (
            ('stationid', 'int'),
            ('name', 'varchar'),
        ),
}