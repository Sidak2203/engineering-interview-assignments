def transform_data(races, results):
    """
    Transforms data by extracting required fields and merging datasets.

    Args:
        races (pd.DataFrame): Race details.
        results (pd.DataFrame): Race results.

    Returns:
        list: A list of tuples (year, transformed JSON data).
    """
    transformed_data = []

    # Iterate over unique years
    for year in races["year"].unique():
        yearly_races = races[races["year"] == year].copy()
        json_data = []

        for _, race in yearly_races.iterrows():
            race_id = race["raceId"]
            race_results = results[results["raceId"] == race_id]

            # Identify the winning driver (position 1)
            winner = race_results[race_results["position"] == 1]
            winning_driver_id = int(winner["driverId"].values[0]) if not winner.empty else None

            # Get fastest lap time (minimum fastestLapTime in this race)
            fastest_lap_time = (
                race_results["fastestLapTime"].dropna().min()
                if not race_results["fastestLapTime"].isna().all()
                else None
            )

            json_data.append({
                "Race Name": race["name"],
                "Race Round": race["round"],
                "Race Datetime": f"{race['date']}T{race.get('time', '00:00:00.000')}",
                "Race Winning driverId": winning_driver_id,
                "Race Fastest Lap": fastest_lap_time
            })

        transformed_data.append((year, json_data))

    return transformed_data  # List of (year, json_data)