
# Temperature Data Analysis Program
# Description: This program processes multiple CSV files of temperature data from weather stations in Australia, calculates seasonal averages, 
# finds stations with the largest temperature range, and identifies the most stable and most variable stations.

import pandas as pd
import glob
import os

def main():
    # Folder containing all CSV files
    folder = "temperatures"

    # Load and combine all CSV files
    all_files = glob.glob(os.path.join(folder, "*.csv"))
    dfs = [pd.read_csv(file) for file in all_files]
    data = pd.concat(dfs, ignore_index=True)


    print(data)
    print("===============================================================================")

    # Keep only numeric month columns
    months = ["January","February","March","April","May","June",
            "July","August","September","October","November","December"]

    #1. Seasonal Average
    seasons = {
        "Summer": ["December", "January", "February"],
        "Autumn": ["March", "April", "May"],
        "Winter": ["June", "July", "August"],
        "Spring": ["September", "October", "November"],
    }

    seasonal_avgs = {}
    for season, cols in seasons.items():
        seasonal_avgs[season] = data[cols].stack().mean(skipna=True)

    with open("average_temp.txt", "w") as f:
        print("\n=== Seasonal Averages ===")
        for season, avg in seasonal_avgs.items():
            line = f"{season}: {avg:.2f}°C"
            print(line)
            f.write(line + "\n")

    #2. Largest Temperature Range
    data["MaxTemp"] = data[months].max(axis=1)
    data["MinTemp"] = data[months].min(axis=1)
    data["Range"] = data["MaxTemp"] - data["MinTemp"]

    max_range = data["Range"].max()
    largest_range_stations = data[data["Range"] == max_range]

    with open("largest_temp_range_station.txt", "w") as f:
        print("\n=== Largest Temperature Range Station(s) ===")
        for _, row in largest_range_stations.iterrows():
            line = (f"{row['STATION_NAME']}: Range {row['Range']:.2f}°C "
                    f"(Max: {row['MaxTemp']:.2f}°C, Min: {row['MinTemp']:.2f}°C)")
            print(line)
            f.write(line + "\n")

    #3. Temperature Stability 
    data["StdDev"] = data[months].std(axis=1)

    min_std = data["StdDev"].min()
    max_std = data["StdDev"].max()

    stable_stations = data[data["StdDev"] == min_std]
    variable_stations = data[data["StdDev"] == max_std]

    with open("temperature_stability_stations.txt", "w") as f:
        print("\n=== Temperature Stability ===")
        for _, row in stable_stations.iterrows():
            line = f"Most Stable: {row['STATION_NAME']}: StdDev {row['StdDev']:.2f}°C"
            print(line)
            f.write(line + "\n")
        for _, row in variable_stations.iterrows():
            line = f"Most Variable: {row['STATION_NAME']}: StdDev {row['StdDev']:.2f}°C"
            print(line)
            f.write(line + "\n")

    print("\n Analysis complete. Results saved to text files.")

if __name__ == "__main__":
    main()