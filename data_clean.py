import pandas as pd
import re


class DataCleaner:
    def __init__(self, movie_list):
        self.df = pd.DataFrame(movie_list)

    def filter_columns(self):
        colonnes_utiles = ['id', 'title', 'original_language',
                           'release_date', 'popularity',
                           'vote_average', 'vote_count', 'genre_ids']

        colonnes_presentes = []
        for col in colonnes_utiles:
            if col in self.df.columns:
                colonnes_presentes.append(col)

        self.df = self.df[colonnes_presentes]

    def remove_duplicates(self):
        self.df = self.df.drop_duplicates(subset=['id'], keep='first')

    def normalize_types(self):
        self.df['release_date'] = pd.to_datetime(self.df['release_date'], errors='coerce')

        self.df['popularity']    = pd.to_numeric(self.df['popularity'],    errors='coerce')
        self.df['vote_average']  = pd.to_numeric(self.df['vote_average'],  errors='coerce')
        self.df['vote_count']    = pd.to_numeric(self.df['vote_count'],    errors='coerce')

        self.df['vote_count'] = self.df['vote_count'].astype('Int64')

    def clean_strings(self):
        colonnes_texte = ['title', 'original_language']

        for col in colonnes_texte:
            if col in self.df.columns:
                self.df[col] = self.df[col].str.strip()

                # Replace multiple spaces with a single space
                self.df[col] = self.df[col].apply(
                    lambda x: re.sub(r'\s+', ' ', x) if isinstance(x, str) else x
                )

    def handle_missing_values(self):
        self.df = self.df.dropna(subset=['id'])
        self.df = self.df.dropna(subset=['title'])
        self.df = self.df.dropna(subset=['release_date'])

        without_votes = (self.df['vote_average'] == 0) & (self.df['vote_count'] == 0)
        self.df = self.df[~without_votes]

    def run_pipeline(self):
        self.filter_columns()
        self.remove_duplicates()
        self.normalize_types()
        self.clean_strings()
        self.handle_missing_values()

        return self.df