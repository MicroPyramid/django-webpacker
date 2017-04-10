from StringIO import StringIO

from django.test import TestCase
from django.core import management
from django.core.management.base import CommandError
from django.core.management import call_command


class CommandTests(TestCase):

    def test_command(self):
        call_command('compress_css_js_files', *[], **{})

        out = StringIO()
        management.call_command('compress_css_js_files', stdout=out)
        print (out.getvalue())
        self.assertEquals(out.getvalue(),
            "{'message': 'Successfully Created Compressed CSS, JS Files'}")
