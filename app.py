from data_fetch import DataFetch


class App:
    def run(self):
        dataFetch = DataFetch()
        data = dataFetch.fetch_data()
        print(data)