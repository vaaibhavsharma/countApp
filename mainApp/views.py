from django.shortcuts import render
from django.http import JsonResponse
from .models import count

# Create your views here.
def main(request):

    data = count.objects.get(id=1)
    context = {'data': data}
    return render(request, 'main.html', context)

def countHandler(request):
    data = None
    if request.method == 'GET':
        like = request.GET.get("like", None)
        post = request.GET.get("dislike", None)

        if like:
            obj = count.objects.get(id=1)
            obj.likeCount = obj.likeCount + 1
            data = obj.likeCount
            obj.save()
        elif post:
            obj = count.objects.get(id=1)
            obj.dislikeCount = obj.dislikeCount + 1
            data = obj.dislikeCount
            obj.save()


    return JsonResponse(data, safe=False)