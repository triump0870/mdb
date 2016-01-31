from fabric.api import local
import os

def heroku():
    local('heroku maintenance:on --app movie-task')
    local('git push heroku master')
    local('heroku maintenance:off --app movie-task')
 
def deploy():
    local('git add .')
    print "Enter the git commit comment: "
    comment = raw_input()
    local(' git commit -m "%s"'%comment)
    local('git push origin master')
    local('heroku maintenance:on --app movie-task')
    local('git push heroku master')
    local('heroku maintenance:off --app movie-task')

def runserver():
    local('python src/manage.py runserver 0.0.0.0:8000')

def migrate():
    local('python src/manage.py makemigrations')
    local('python src/manage.py migrate')
    local('python src/manage.py collectstatic')

def dump():
    from os.path import join,dirname,exists
    import environ
    env = environ.Env()

    # Ideally move env file should be outside the git repo
    # i.e. BASE_DIR.parent.parent
    env_file = join(dirname('src/movie_task/settings/'), 'local.env')
    if exists(env_file):
        environ.Env.read_env(str(env_file))
    DATABASE_NAME = env('DB_NAME')
    USERNAME = env('DB_USER')
    PASSWORD = env('DB_PASS')

    local('PGPASSWORD={0} pg_dump -Fc --no-acl --no-owner -h localhost -U {1} {2}  > {2}.dump'.format(PASSWORD,USERNAME,DATABASE_NAME))
    local("heroku config:set AWS_STORAGE_BUCKET_NAME=%s"%env('AWS_STORAGE_BUCKET_NAME'))
    local("heroku config:set AWS_ACCESS_KEY=%s"%os.environ['AWS_ACCESS_KEY'])
    local("heroku config:set AWS_SECRET_ACCESS_KEY=%s"%os.environ['AWS_SECRET_ACCESS_KEY'])
    S3_URL = 'https://{}.s3.amazonaws.com/{}.dump'.format(env('AWS_STORAGE_BUCKET_NAME'), DATABASE_NAME)
#    local('aws configure')
    S3_UPLOAD_URL = 's3://%s/'%(os.environ['AWS_STORAGE_BUCKET_NAME'])
    local('rm %s.dump'%DATABASE_NAME)
    local('aws s3 cp %s.dump %s'%(DATABASE_NAME, S3_UPLOAD_URL))
    local("heroku pg:backups restore '%s' DATABASE_URL --confirm movie-task"%(S3_URL))

def local_deploy():
    local('git add .')
    comment = raw_input("Enter the commit comment: ")
    local('git commit -m "%s"'%comment)
    local('git push origin master')
