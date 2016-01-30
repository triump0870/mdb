from fabric.api import local

def deploy():
    local('git add .')
    print "Enter the git commit comment: "
    comment = raw_input()
    local(' git commit -m "%s"'%comment)
    local('git push origin master')
