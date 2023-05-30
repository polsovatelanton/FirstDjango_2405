from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item

items = Item.objects.all()
#items = [
#   {"id": 1, "name": "Кроссовки abibas"},
#   {"id": 2, "name": "Куртка кожаная"},
#   {"id": 3, "name": "Coca-cola 1 литр"},
#   {"id": 4, "name": "Картофель фри"},
#   {"id": 5, "name": "Кепка"},
#]

def home(request):
#   text="""<h1>"Изучаем django"</h1>
#         <strong>Ученик</strong>: <i>Проскуряков А.В.</i>"""
#   return HttpResponse(text)
    context ={
        "name": 'Антон',
        "email": 'ap@mst.ru'
    }
    return render(request, "index.html", context)


def about(request):
    name = 'Anton'
    surname = 'Proskuryakov'
    email = 'ap@mst.ru'
    text=f""" <h1> name: {name} <br> surname: {surname} <br> email: {email} </h1> <a href='/'>На главную</a>"""
    return HttpResponse(text)

def item(request,id):
#    if (id > 0) and (id < 6):
#        text = f" <h1> Goodname: {items[id-1]['name']} <br> <a href='../../items/'>BACK</a> </h1>"
#    else:
#        text = f" <h1> There is no goodname with id = {id} </h1>"
#    return HttpResponse(text)
    context = {
        "items": items,
        "num": id
    }
    return render(request, "item.html", context)

def allitems(request):
#    newlist=[]
#    for i in range(5):
#        newlist.append(items[i]['name'])
#    text = f""" <h1> All goods:
#            <ol>
#             <li> <a href = '../item/1/'> {newlist[0]}</a> </li>
#             <li> <a href = '../item/2/'> {newlist[1]}</a> </li>
#             <li> <a href = '../item/3/'> {newlist[2]}</a> </li>
#            </ol>
#            </h1> """

#    return HttpResponse(text)
    context = {
        "items": items
    }
    return render(request, "items-list.html", context)



