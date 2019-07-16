from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.views import View
from .models import Assets

import logging
logger = logging.getLogger("collect")

class CmdbView(View):
    def get(self,request,*args,**kwargs):
        objs = Assets.objects.all()
        print(objs)
        return render(request,'assets.html',context={'objects' : objs})

def CmdbDeleteView(request,*args,**kwargs):
    logger.debug(request)
    logger.info("args: {}".format(args))
    logger.info("kwargs : {}".format(kwargs))
    Assets.objects.get(id=kwargs['pk']).delete()
    return redirect('/api/v1/cmdb')

# class CollectHostInfo(View):
#     def get(self,request):
#         pass
#
#     def post(self,request):
#         import random
#         data = request.POST.dict()
#         data['hostname'] += str(random.randint(1, 100))
#         data['mac_address'] = "{} {}".format(str(random.randint(1, 100)), str(random.randint(1, 100)))
#         try:
#             Assets.objects.create(**data)
#         except Exception as e:
#             print(e)
#         return HttpResponse('succ')

class CollectHostInfo(View):

    def get(self, request):
        pass

    def post(self, request):
        # data = request.POST.dict()
        # try:
        #     Assets.objects.create(**data)
        # except Exception as e:
        #     print(e)
        # return HttpResponse('succccccccccc')
        import random
        data = request.POST.dict()
        data['hostname'] += str(random.randint(1, 100))
        data['mac_address'] = "{} {}".format(str(random.randint(1, 100)), str(random.randint(1, 100)))
        try:
            Assets.objects.create(**data)
        except Exception as e:
            print(e)
        return HttpResponse("succ.")

def AssetsView(request, *args, **kwargs):
    print(request)
    print("args: {}".format(args))
    print("kwargs : {}".format(kwargs))
    return HttpResponse("succ")