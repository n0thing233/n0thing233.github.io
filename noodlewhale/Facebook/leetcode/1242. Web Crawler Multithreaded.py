#两种思路吧：
#1. queue + seen + multi thread seen 需要加lock,每个worker从queue里get一个元素，然后找到neighbor然后放到queue里。queue空算结束。queue.join() threads.join() 就可以return list(seen)了
#2. concurrent future。。。。掌握不了 。好吧。。。
#你因为htmlparser h大小写调了一小时的bug......

from queue import Queue
from threading import Lock,Thread
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def hostname(url):
            start = len("http://")
            i = start
            while i < len(url) and url[i] != "/":
                i += 1
            return url[start:i]      
        q = Queue()
        seen = {startUrl}
        lock = Lock()
        start_hostname = hostname(startUrl)
        def worker():
            while True:
                url = q.get()
                if url is None:
                    return
                
                for i in htmlParser.getUrls(url):
                    if i not in seen and hostname(i) == start_hostname:
                        lock.acquire()
                        if i not in seen:
                            seen.add(i)
                            q.put(i)                           
                        lock.release()
                q.task_done()
        
        num_of_workers = 8
        workers = []
        q.put(startUrl)
        
        for i in range(num_of_workers):
            t = Thread(target = worker)
            t.start()
            workers.append(t)     
        q.join()
        for i in range(num_of_workers):
            q.put(None)
        for t in workers:
            t.join()
            
        return list(seen)
