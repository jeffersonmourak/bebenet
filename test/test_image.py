import unittest
import json
import base64

from aux import Aux
from user_aux import UserAux

class ImageTest(unittest.TestCase):

    aux = Aux()
    user_aux = UserAux()
    urlbase = "http://127.0.0.1:8000"

    def testPostAndGetImage(self):
        email = "apiteste1@teste.com"

        self.user_aux.createUser(email)

        #pega id do usuario
        url = "/user/email/" + email
        res = self.aux.getFunction(self.urlbase, url)
        id = json.loads(res)[0]['id']

        url = "/user/picture"

        with open("test/sample.jpg", "rb") as imageFile:
            str = base64.b64encode(imageFile.read())
            param = {"type": "jpg", "bytecode": str, "id_user": id};
            response = self.aux.postFunction(self.urlbase, url, param)
            self.assertEqual(response, 201)

        url = "/user/picture/%d" % (id)
        response = self.aux.getFunction(self.urlbase, url)
        response = json.loads(response)

        self.assertTrue(len(response['url']) > 0)

        self.user_aux.deleteUser(email)

if __name__ == '__main__':
        unittest.main()
