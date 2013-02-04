import sys, os
from warholm.session3 import CourseRepo, ContextManager

if len(sys.argv) != 2:
    print "You must provide a git repository directory as argument."
    sys.exit()
    
if not os.path.exists(sys.argv[1]):
    print "Directory "+sys.argv[1]+" does not exist."
    sys.exit()

repo_dir = sys.argv[1]
surname = filter(None,sys.argv[1].split("/"))[-1]

cm = ContextManager()
cm.__enter__(repo_dir)

inst = CourseRepo(surname)

if inst.check():
    print "PASS"
else:
    print "FAIL"

cm.__exit__()