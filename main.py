import threading
from queue import Queue
from spider import Spider as spider
from domain import *
from general import *

PROJECT_NAME ='Tushar'
HOMEPAGE='https://www.coursera.org'
DOMAIN_NAME=get_domain_name(HOMEPAGE)
QUEUE_FILE= PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NO_OF_THREADS = 15
queue = Queue()
spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


#Create worker threads
def create_workers():
    for _ in range(NO_OF_THREADS ):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

#Do the  next job in queue
def work():
    while True:
        url = queue.get()
        spider.crawl_page(threading.current_thread().name,url)
        queue.task_done()



#Each queue link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


#check if there are items in the queue, if so crawl
def crawl():
    queue_links= file_to_set(QUEUE_FILE)
    if len(queue_links)>0:
        print(str(len(queue_links)) + 'links in the queue')
        create_jobs()

create_workers()
crawl()
