import threading
from sqlalchemy import create_engine
import os
from sqlalchemy.sql import text
from queue import Empty
from urllib.parse import quote_plus
import logging
import traceback

# Enable SQLAlchemy logging
# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

class PostgresMasterScheduler(threading.Thread):
    def __init__(self, input_queue, **kwargs):
        super(PostgresMasterScheduler, self).__init__(**kwargs)
        self._input_queue = input_queue
        self.start()
    
    def run(self):
        while True:
            try:
                val = self._input_queue.get(timeout=10)
            except Empty:
                print('Timeout Reached. Stopping Postgres Scheduler')
                break
            if val == 'DONE':
                break
            symbol, price, extracted_time = val
            postgresWorker = PostgresWorker(symbol, price, extracted_time)
            try:
                postgresWorker.insert_into_db()
            except Exception as e:
                print(f"Error inserting data: {e}")
 
class PostgresWorker:
    def __init__(self, symbol, price, extracted_time):
        self._symbol = symbol
        self._price = price
        self._extracted_time = extracted_time

        self._PG_USER = os.environ.get('PG_USER') or 'postgres'
        self._PG_PW = os.environ.get('PG_PW') or 'arzm@nIA112'
        self._PG_HOST = os.environ.get('PG_HOST') or 'localhost'
        self._PG_DB = os.environ.get('PG_DB') or 'threading'
        encoded_password = quote_plus(self._PG_PW)

        self._engine = create_engine(
            f'postgresql://{self._PG_USER}:{encoded_password}@{self._PG_HOST}/{self._PG_DB}'
        )

    def _create_insert_query(self):
        sql = """INSERT INTO prices (symbol, price, extracted_time) 
                 VALUES (:symbol, :price, :extracted_time)"""
        return sql
    
    def insert_into_db(self):
        insert_query = self._create_insert_query()

        try:
            with self._engine.connect() as conn:
                transaction = conn.begin()
                conn.execute(
                    text(insert_query),
                    {'symbol': self._symbol, 'price': self._price, 'extracted_time': self._extracted_time}
                )
                transaction.commit()
                print(f"Inserted: {self._symbol}, {self._price}, {self._extracted_time}")
        except Exception as e:
            traceback.print_exc()
            print(f"Failed to insert into DB: {e}")
            transaction.rollback()

