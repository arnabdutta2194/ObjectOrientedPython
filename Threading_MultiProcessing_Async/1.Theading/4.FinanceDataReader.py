from workers.WikipediaReaderWorker import WikiPediaWorker
from workers.YahooFinanceWorker import YahooFinancePriceScheduler
from workers.PostgresWorker import PostgresMasterScheduler
import time
from multiprocessing import Queue


def main():
    symbol_queue = Queue() 
    postgres_queue = Queue()
    calc_start_time  = time.time()

    wikiWorker = WikiPediaWorker()

    yahoo_finance_price_scheduler_threads = []
    num_yahoo_finance_price_workers = 4
    for i in range(num_yahoo_finance_price_workers):
        yahooFinancePriceScheduler = YahooFinancePriceScheduler(input_queue=symbol_queue,output_queue = [postgres_queue])
        yahoo_finance_price_scheduler_threads.append(yahooFinancePriceScheduler)

    postgres_scheduler_threads = []
    num_postgres_workers = 2
    for i in range(num_postgres_workers):
        postgresScheduler = PostgresMasterScheduler(input_queue=postgres_queue)
        postgres_scheduler_threads.append(postgresScheduler)

    symbol_counter = 0
    for symbol in wikiWorker.get_sp_500_companies():
        print("Inserting Symbol")
        symbol_queue.put(symbol)
        symbol_counter += 1
        if symbol_counter >=5:
            break
    
    for threads in yahoo_finance_price_scheduler_threads:
        symbol_queue.put('DONE')

    for threads in yahoo_finance_price_scheduler_threads:
        threads.join()
    
    for posgres_threads in postgres_scheduler_threads:
        posgres_threads.join()

    calc_end_time  = time.time()
    print('Total Time : ',round(calc_end_time-calc_start_time,1))

if __name__ == '__main__':
    main()
