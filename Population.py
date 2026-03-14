def get_city_population(populations: dict, city: str):
        try:
            population = populations[city]
            return population
        except KeyError:
            raise KeyError(f"No such city found: {city}")