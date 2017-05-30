import requests

import json

from aux import Aux

class UserAux:

    aux = Aux()
    urlbase = "http://127.0.0.1:8000"

    def createUser(self, email):
        self.deleteUser(email)
        url= "/user"
        json = { "name":"Teste1","email":email,"age":"21","password":"123456"}
        return self.aux.postFunction(self.urlbase, url, json)

    def deleteUser(self, email):
        url = "/user/email/" + email
        res = self.aux.getFunction(self.urlbase, url)

        if res == "[]":
            return
            
        idd = json.loads(res)[0]['id']

        url = "/user/"
        self.aux.deleteFunction(self.urlbase, url,idd)

    if __name__ == "__main__":
        print ("MAIN")
