from django.shortcuts import render
import markdown2

from . import util


def index(request):
    if request.method == "POST":
        query = request.POST.get('q')
        if util.get_entry(query):
            return render(request, "encyclopedia/error.html", {
            "item": item
        }) 


    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, item):
    print(item)
    print(util.list_entries())

    if util.get_entry(item) == None:
        return render(request, "encyclopedia/error.html", {
            "item": item
        })
    return render(request, "encyclopedia/item.html", {
    "content": markdown2.markdown(util.get_entry(item)),
    "item": item
    })
 
