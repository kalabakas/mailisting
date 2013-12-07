from createsend import *
import settings

auth = {'api_key': settings.API_KEY}
listId = settings.LIST_ID

def listActiveSubscribers():
    listObj = List(auth,listId)
    return listObj.active().Results

def newSub(name, email):
    subObj = Subscriber(auth, listId)
    subObj.add(list_id, email, name, '', False, True)
    return "{'email':"+email+"}"

def delSub(email):
    subObj = Subscriber(auth, list_id, email)
    subObj.delete()
    return "{'email':"+email+"}"
