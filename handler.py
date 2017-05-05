import json
import git
import subprocess
import os
import urllib2
import json
from collections import namedtuple

# from git.test.lib import TestBase
# from git.test.lib.helper import with_rw_directory

import os.path as osp

user="admin"
password="password123"
candidate="1.0.0"
release_tag="1.0.0"
release_branch="master"
release_name="Last"
body=""
github_token=""
github_org=""
github_repo=""

def callShell(cmd):
    pipe=subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output,error)=pipe.communicate()
    return output.replace('\n','')

def lambda_handler( event, context):
    try:
        repo=git.Repo.clone_from("https://" + github_token + "@github.com/" + github_org + '/' + github_repo +".git", osp.join(os.getcwd(), github_repo), branch="master")
    except:
        print "Already existing Repo"
        repo=git.Repo(osp.join(os.getcwd(), github_repo))
    repo.git.checkout("staging")
    # latest_tag="1.0.0"
    latest_release=urllib2.urlopen("https://api.github.com/repos/"+github_org+
        "/"+github_repo+"/releases/latest?access_token=" +github_token).read()
        
    latest_release_tag=json.loads(latest_release,object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    print str(latest_release_tag.tag_name)
    commits = list(repo.iter_commits(candidate + ".." + str(latest_release_tag.tag_name)))
    release_note=""
    for commit in commits:
        release_note+=commit.message + "\n"
    release_note=release_note.replace('\n','</br>')
    print release_note
lambda_handler("","")