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
        self.surname = surname

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self.required = ['.git', 'setup.py', 'LICENSE.txt', 'README.txt', 'scripts/check_repo.py', 'scripts/getting_data.py', value+'/__init__.py', value+'/session3.py']
        self._surname = value

    def check(self):
        for f in self.required:
            # print self.required # debug
            if not os.path.exists(os.getcwd()+"/"+f):
                # print os.getcwd()+"/"+f # debug
                return False
        return True