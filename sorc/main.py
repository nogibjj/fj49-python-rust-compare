import polars as pl
import matplotlib.pyplot as plt


# Reading the data
def reader():
    df = pl.read_csv("spotify.csv")
    return df


spotify = reader()
# print(spotify)


# Basic stats
def mean():
    mean_duration = int(spotify["duration_ms"].mean())
    return mean_duration


def median():
    median_duration = int(spotify["duration_ms"].median())
    return median_duration


def mode():
    mode_duration = int(spotify["duration_ms"].mode()[0])
    return mode_duration


def std():
    std_duration = int(spotify["duration_ms"].std())
    return std_duration


# Making a plot
def viz():
    frequency_df = spotify.group_by("artist_name").agg(
        pl.col("artist_name").count().alias("frequency")
    )
    sorted_df = frequency_df.sort("frequency")
    top_10_frequencies = sorted_df.tail(10)
    # top_10_frequencies_pandas = top_10_frequencies.to_pandas()
    x = plt.figure(figsize=(20, 12))
    x = plt.bar(top_10_frequencies["artist_name"], top_10_frequencies["frequency"])
    print("the", type(x))
    # top_10_frequencies.plot(kind="bar", x="artist_name", y="frequency", figsize=(20, 12))
    x = plt.xlabel("Top Artists")
    x = plt.ylabel("Number of top tracks")
    x = plt.title("Which artists had the most top tracks in the last few years?")
    # x = plt.show()
    return x
