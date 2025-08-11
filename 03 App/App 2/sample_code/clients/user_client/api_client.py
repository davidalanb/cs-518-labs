import requests as rq

class APIClient:
    ''' generic API client'''

    def __init__(self,url):
        self.url = url

    def create(self,body):
        res = rq.post(self.url,json=body) 
        res.raise_for_status()  
        return res.json()
        
    def read_all(self):
        res = rq.get(self.url)
        res.raise_for_status()  
        return res.json()
            
    def read_by_id(self,uid):
        res = rq.get(self.url + uid)
        res.raise_for_status()  
        return res.json()

    def read(self,query):
        res = rq.get(self.url,params=query)
        res.raise_for_status()  
        return res.json()        

    def update(self,uid,update):
        res = rq.put(self.url + uid,json=update)
        res.raise_for_status()  
        return res.json()
    
    def delete_all(self):
        res = rq.delete(self.url) 
        res.raise_for_status()  
        return res.json()

    def delete_by_id(self,uid):
        res = rq.delete(self.url + uid)
        res.raise_for_status()  
        return res.json()  