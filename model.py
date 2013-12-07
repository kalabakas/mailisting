from createsend import *
import settings

auth = {'api_key': settings.API_KEY}
listId = settings.LIST_ID

def listActiveSubscribers():
    listObj = List(auth,listId)
    return listObj.active().Results

def newSub(name, email):
    subObj = Subscriber(auth, listId)
    subObj.add(listId, email, name, '', False, True)
    return "{'email':"+email+"}"

def delSub(email):
    subObj = Subscriber(auth, listId, email)
    subObj.delete()
    return "{'email':"+email+"}"
