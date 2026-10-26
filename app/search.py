def search_trains(trains, source, destination):
    """Return trains matching the requested source and destination."""
    return [
        train
        for train in trains
        if train["source"] == source
        and train["destination"] == destination
    ]