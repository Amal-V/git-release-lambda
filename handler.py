import json
import git
import subprocess

user="admin"
password="password123"
release_tag="v3.0"
release_branch="master"
release_name="Last"
body=""

def callShell(cmd):
    pipe=subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output,error)=pipe.communicate()
    return output.replace('\n','')

def lambda_handler(event, context):
    git.Git().clone("https://github.com/neerajjose/temp.git")
    command="curl -s https://api.github.com/repos/geofffranks/spruce/releases/latest |jq \".tag_name\"|tr -d '\"' "
    latest_tag=callShell(command)
    # command="git -C ./temp/ log $(echo "+latest_tag+"|tr -d '"')..HEAD --oneline|grep OPS|cut -d " " -f2|tr -d '[]'"