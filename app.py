from analyse_genres import generer_box_plot_genres
from data_clean import DataCleaner
from data_fetch import DataFetch
from duration_per_year import DurationPerYear
from heat_map import HeatmapGenerator
from roi_per_genre import RoiPerGenre
from seasonality import Seasonality
from evolution_time import EvolutionTemporelle
from genre_products import GenresProduits


class App:
    def run(self):
        fetcher = DataFetch()
        movies = fetcher.load_cache(movie_amount=10000)

        cleaner = DataCleaner(movies)
        df_clean = cleaner.run_pipeline()

        print(f" Cleaned movies: {len(df_clean)}")
        print(f"Memory weight: {df_clean.memory_usage(deep=True).sum() / 1024:.2f} KB")
        #print(df_clean.to_string())

        Seasonality(df_clean).calculate_stats()
        RoiPerGenre(df_clean).calculate_stats()
        DurationPerYear(df_clean).calculate_stats()

        HeatmapGenerator(df_clean).generate()

        EvolutionTemporelle(df_clean).calculate_stats()
        GenresProduits(df_clean).calculate_stats()

        #generer_box_plot_genres(movies)


