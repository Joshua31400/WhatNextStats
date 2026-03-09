from data_clean import DataCleaner
from data_fetch import DataFetch


class App:
    def run(self):
        fetcher = DataFetch()
        movies = fetcher.fetch_data(page_amount=1)
        cleaner = DataCleaner(movies)
        df_clean = cleaner.run_pipeline()

        print(f" Cleaned movies: {len(df_clean)}")
        print(f"Memory weight: {df_clean.memory_usage(deep=True).sum() / 1024:.2f} KB")
        print(df_clean.head().to_string())