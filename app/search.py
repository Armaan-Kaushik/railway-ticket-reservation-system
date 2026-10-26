def search_trains(trains, source, destination, date, travel_class=None):
    """Return trains matching route, journey date, and optional travel class."""
    return [
        train
        for train in trains
        if train["source"] == source
        and train["destination"] == destination
        and train["date"] == date
        and (
            travel_class is None
            or travel_class in train["classes"]
        )
    ]