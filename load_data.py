import sqlite3 as sql
import pandas as pd

select_all_query = "SELECT * FROM {0}"

class History:

    def __init__(self, db_dir):
        self.db_dir = db_directory
        self.connection = sql.connect(self.db_dir)

    def get_directory(self):
        return self.db_dir

    def set_directory(self, new_dir):
        self.db_dir = new_dir
        self.make_connection()

    def _make_connection(self):
        self.connection = sql.connect(self.db_dir)

class ChromeHistory(History):

    def load_meta(self):
        return pd.read_sql_query(select_all_query.format('meta'), self.connection)

    def load_visits(self):
        return pd.read_sql_query(select_all_query.format('visits'), self.connection)

    def load_visit_source(self):
        return pd.read_sql_query(select_all_query.format('visit_source'), self.connection)

    def load_keyword_search_terms(self):
        return pd.read_sql_query(select_all_query.format('keyword_search_terms'), self.connection)

    def load_downloads(self):
        return pd.read_sql_query(select_all_query.format('downloads'), self.connection)

    def load_downloads_url_chain(self):
        return pd.read_sql_query(select_all_query.format('downloads_url_chain'), self.connection)

    def load_downloads_slices(self):
        return pd.read_sql_query(select_all_query.format('downloads_slices'), self.connection)

    def load_segments(self):
        return pd.read_sql_query(select_all_query.format('segments'), self.connection)

    def load_urls(self):
        return pd.read_sql_query(select_all_query.format('urls'), self.connection)

    def load_typed_url_sync_metadata(self):
        return pd.read_sql_query(select_all_query.format('typed_url_sync_metadata'), self.connection)

    def load_segment_usage(self):
        return pd.read_sql_query(select_all_query.format('segment_usage'), self.connection)

    def load_sqlite_sequence(self):
        return pd.read_sql_query(select_all_query.format('sqlite_sequence'), self.connection)
        
