def search_trains(trains, source, destination, travel_class=None):
    """Return trains matching the route and optional travel class."""
    return [
        train
        for train in trains
        if train["source"] == source
        and train["destination"] == destination
        and (
            travel_class is None
            or travel_class in train["classes"]
        )
    ]