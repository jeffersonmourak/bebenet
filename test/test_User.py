import unittest
import json

from aux import Aux
from user_aux import UserAux

class UserTest(unittest.TestCase):

    aux = Aux()
    user_aux = UserAux()
    urlbase = "http://127.0.0.1:8000"

    def testPost(self):
        email = "apiteste1@teste.com"

        self.assertEqual(self.user_aux.createUser(email), 201)

        self.user_aux.deleteUser(email)

    def testGetByEmail(self):
        email = "apiteste2@teste.com"

        self.user_aux.createUser(email)

        url = "/user/email/" + email
        res = self.aux.getFunction(self.urlbase, url)
        self.assertEqual(json.loads(res)[0]['email'], email)

        self.user_aux.deleteUser(email)

    def testDelete(self):
        email = "apiteste3@teste.com"

        self.user_aux.createUser(email)

        url = "/user/email/" + email
        res = self.aux.getFunction(self.urlbase, url)
        idd = json.loads(res)[0]['id']
        url = "/user/"
        self.assertEqual( self.aux.deleteFunction(self.urlbase, url,idd), 200)

if __name__ == '__main__':
        unittest.main()
