import subprocess as sp
import sys
import os
import time
import datetime 
import pysvn

# Usage: commit_id.py check <app_dir> (checks if git is present)
# Usage: commit_id.py gen <app_dir> <file_to_write> (generates commit id)


def getSVNRevisonNumber(svnPath):
    try: 
        client = pysvn.Client()
    
        LogList = client.log(svnPath, limit=1 )
        ReposInfo = LogList[0]

        ReposRevNumber = ReposInfo.revision.number
     
        return ReposRevNumber
    except:
        return "" 
        
def grab_output(command, cwd):
    return sp.Popen(command, stdout=sp.PIPE, shell=True, cwd=cwd).communicate()[0].strip()


def getSVNRevisonNumber(svnPath):
    try: 
        client = pysvn.Client() 
        entry = client.info(svnPath)
        return  entry.commit_revision.number
    except:
        return "" 
        
def getSVNRevisonDate(svnPath):
    try: 
        client = pysvn.Client() 
        entry = client.info(svnPath)
        ReposRevNumber = datetime.datetime.strftime(datetime.datetime.fromtimestamp(entry.commit_time),"%Y%m%d%H%M%S")
        return ReposRevNumber
    except:
        return ""         


operation = sys.argv[1]
cwd = sys.argv[2]

if operation == 'check':
	  #index_path = os.path.join(cwd, '.git', 'index')
    index_path = os.path.join(cwd, 'svncheck', 'index')
    if os.path.exists(index_path):
        print("1")
    else:
        print("0")
    sys.exit(0)


output_file = sys.argv[3]
commit_id_size = 12

try:
    #commit_id = grab_output('git rev-parse --short=%d HEAD' % commit_id_size, cwd)
    #commit_date = grab_output('git show -s --format=%ci HEAD', cwd)
    commit_id   = getSVNRevisonNumber(cwd)
    commit_date = getSVNRevisonDate(cwd)
except:
    commit_id = 'invalid-hash'
    commit_date = 'invalid-date'

hfile = open(output_file, 'w')

hfile.write('#define APP_COMMIT_HASH "%s"\n'    % commit_id)
hfile.write('#define APP_COMMIT_HASH_SIZE %d\n' % commit_id_size)
hfile.write('#define APP_COMMIT_DATE "%s"\n'    % commit_date)

hfile.close()
