from data_clean import DataCleaner
from data_fetch import DataFetch
from seasonality import Seasonality


class App:
    def run(self):
        fetcher = DataFetch()
        movies = fetcher.load_cache(movie_amount=20)

        cleaner = DataCleaner(movies)
        df_clean = cleaner.run_pipeline()

        Seasonality(df_clean).calculate_stats()

        print(f" Cleaned movies: {len(df_clean)}")
        print(f"Memory weight: {df_clean.memory_usage(deep=True).sum() / 1024:.2f} KB")
        print(df_clean.to_string())