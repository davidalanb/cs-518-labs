
try:
    from db_manager import DBManager
    from profile_models import *
except ModuleNotFoundError:
    from profiles.data.db_manager import DBManager
    from profiles.data.profile_models import *    

class ProfileManager:
    '''
    The profile manager takes and returns model objects
    The DBManager works with plain python objects'''

    #================ THESE ARE IMPLEMENTED ================

    def __init__(self, dbm: DBManager):
        '''connect to db server and set self.col'''
    
        self.dbm = dbm
        self.dbm.create_index("profile_name")

    def delete_all(self):
        '''delete all profiles'''

        return self.dbm.delete_all()

    def create(self, p: Profile):
        '''create profile'''

        return self.dbm.create(p.model_dump())
    
    def read_all(self) -> ProfileCollection:
        '''read all profiles'''

        r = self.dbm.read_all()
        return ProfileCollection(profiles=r)
    
    #=================IMLEMENT THESE================

    #-------------------- READS ----------------------

    def read(self,query: ProfileQuery)->ProfileCollection:
        '''read profile by query'''

        # need to exclude None so that you can query by any of the optional fields
        q = query.model_dump(exclude_none=True)

        ''' now do the query'''

    def read_by_id(self,id: str) -> Profile:
        '''read profile by id'''
    
    def read_by_profile_name(self,name:str) -> Profile:
        '''read profile by profile_name'''
    
    def read_by_username(self,uname:str) -> ProfileCollection:
        '''read all profiles by username'''

    #---------------- UPDATES ----------------------
        
    def add_skills(self, pid, skills: ProfileSkills):
        '''add skills to profile'''



