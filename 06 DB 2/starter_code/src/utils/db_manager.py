class DBManager:
    def __init__(self,one, two, three):
        pass

    def create_index(self,ix, unique=True):
        self.col.create_index(ix, unique=unique) 

    '''
        include all of your other DBManager methods
    '''

    def add_to_set(self,pid: str,field: str,add_these: list[str]):
        '''take an id and a set fieldname, and add each item provided'''

        r = self.col.update_one({'_id':pid},
                { "$addToSet": { field: {'$each': add_these } }}
        )

        return r.modified_count   