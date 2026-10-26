def search_trains(trains, source, destination, date):
    """Return trains matching the route and journey date."""
    return [
        train
        for train in trains
        if train["source"] == source
        and train["destination"] == destination
        and train["date"] == date
    ]