import os

class ContextManager(object):
    def __enter__(self,target_dir):
        self.target_dir = target_dir
        self.old_dir = os.getcwd()
        os.chdir(self.target_dir)
    
    def __exit__(self):
        os.chdir(self.old_dir)

class CourseRepo(object):
    def __init__(self,surname):
        self.required = surname

    @property
    def required(self):
        return self._required
    
    @required.setter
    def required(self, surname):
        self._required = ['.git', 'setup.py', 'LICENSE.txt', 'README.txt', 'scripts/check_repo.py', 'scripts/getting_data.py', surname+'/__init__.py', surname+'/session3.py']

    def check(self):
        for f in self._required:
            if not os.path.exists(os.getcwd()+"/"+f): return False
        return True