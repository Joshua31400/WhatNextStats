from app import App
from data_fetch import DataFetch

if __name__ == "__main__":
    #DataFetch().update_cache(page_amount=500)
    app = App()
    app.run()
