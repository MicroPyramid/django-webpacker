from django.core.management.base import BaseCommand
import json
import subprocess

try:
    from boto.s3.connection import S3Connection
    from boto.s3.key import Key
except:
    pass

from django.conf import settings
import mimetypes
import os


def call_subprocess(command):
    proc = subprocess.Popen(command,
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        )


def upload_to_s3(css_file):
    bucket_name = settings.AWS_BUCKET_NAME
    conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)

    folder = 'webpack_bundles/'
    bucket = conn.get_bucket(bucket_name=bucket_name)

    filename = css_file.split('/')[-1]
    file_obj = open(css_file, 'r')
    content = file_obj.read()

    key = folder + filename
    bucket = conn.get_bucket(bucket_name=bucket_name)
    mime = mimetypes.guess_type(filename)[0]
    k = Key(bucket)
    k.key = key  # folder + filename
    k.set_metadata("Content-Type", mime)
    k.set_contents_from_string(content)
    public_read = True
    if public_read:
        k.set_acl("public-read")



class Command(BaseCommand):
    args = '<filename>'
    help = 'Loads the initial data in to database'

    def handle(self, *args, **options):
        call_subprocess('./node_modules/.bin/webpack --config webpack.config.js')


        for each in settings.WEB_PACK_FILES:
            directory = settings.BASE_DIR + '/static/webpack_bundles/'
            css_file = max([os.path.join(directory, d) for d in os.listdir(directory) if d.startswith(each['webpack_js']) and d.endswith('css')], key=os.path.getmtime)
            js_file = max([os.path.join(directory, d) for d in os.listdir(directory) if d.startswith(each['webpack_js']) and d.endswith('js')], key=os.path.getmtime)

            if settings.ENABLE_DJANGO_WEBPACK_S3_STORAGES:
                upload_to_s3(css_file)
                upload_to_s3(js_file)

            import re
            regex = r'(.*?<link rel="stylesheet" type="text/css" href=")(.*?)(" id="packer_css"/>.*?<script id="packer_js" src=")(.*?)(" type="text/javascript"></script>.*)'

            with open(each['html_file_name'], 'r+') as f:
                content = f.read()
                m = re.match(regex, content, re.DOTALL)
                href = settings.STATIC_URL + css_file.split('/static/')[-1]
                src = settings.STATIC_URL + js_file.split('/static/')[-1]
                content = m.group(1) + href + m.group(3) + src + m.group(5)

            with open(each['html_file_name'], 'w') as f:
                f.write(content)

        result = {'message': "Successfully Created Compressed CSS, JS Files"}
        return json.dumps(result)
