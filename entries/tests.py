
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class Access_to_user_list(TestCase):
    def test_authorized_access(self):
        """
        Authorized access to user list should return status code 200
        """
        with self.settings(AXES_ENABLED = False):
            # see django-axes 
            # this will disable the credential prevention protection
            # TODO find a way to pass "request" to the authentication. See:
            # https://docs.djangoproject.com/en/4.1/topics/testing/tools/#overriding-settings
            superuser = User.objects.create_superuser('admin', 'x@x.com','superuser')
            self.client.login(username='admin', password='superuser')
            response = self.client.get('/entries/users/') 
            self.assertEqual(response.status_code, 200, "Status code should be 200")

    def test_non_authorized_access(self):
        """
        Non uthorized access to user list should return status code 403 (Forbidden)
        """
        with self.settings(AXES_ENABLED = False):
            # see above
            superuser = User.objects.create_superuser('admin', 'x@x.com','superuser')
            normaluser = User.objects.create_user('normal','y@y.com', 'normal')
            self.client.login(username='normal', password='normal')
            response = self.client.get('/entries/users/') 
            self.assertEqual(response.status_code, 403, "Status code should be 403")
        
