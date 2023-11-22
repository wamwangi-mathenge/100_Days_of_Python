capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a List in a Dictionary
cities = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Munich", "Dortmund"],
}

# Nesting a Dictionary in a Dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
        "popular_sites": ["Eiffel Tower", "Stade de France", "Arc de Triomphe"],
    },
    "Germany": {
        "cities_visited": ["Berlin", "Munich", "Dortmund"],
        "total_visits": 26,
        "popular_sites": ["Bradenburg Gate", "Allianz Arena", "Signal Iduna Park"],
    }
}

# Nesting a Dictionary in a List
travel_log2 = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Dijon", "Lille"],
        "total_visits": 23,
        "popular_sites": ["Eiffel Tower", "Stade de France", "Arc de Triomphe"],
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Munich", "Dortmund"],
        "total_visits": 45,
        "popular_sites": ["Bradenburg Gate", "Allianz Arena", "Signal Iduna Park"],
    }
]