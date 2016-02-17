import MySQLdb as mdb
import json
import calendar
from tastypie.http import HttpBadRequest, HttpApplicationError
from tastypie.exceptions import NotFound, BadRequest, InvalidFilterError, HydrationError, InvalidSortError, ImmediateHttpResponse, Unauthorized
from django.http import HttpResponse,HttpResponseRedirect
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.resources import csrf_exempt
from tastypie import fields
from datetime import datetime
from django.utils import timezone
from django.db import connection, transaction, DatabaseError, IntegrityError
from tastypie.cache import SimpleCache
import time
from app.app.models.models import City,Sbpics,Sbimage
import json
import hmac
import base64,hashlib,urllib2
import smtplib
from django.conf import settings

class BranchAppResource(ModelResource):
    class Meta:
        collection_name="data"
        queryset = City.objects.all()
        resource_name = 'appbranch'
        authorization = Authorization()
        # limit = 0 #(unlimted)
        filtering = {
            "branch_flag": ALL,
            "branch_name":('exact', 'startswith','istartswith','icontains',),
            "cid":ALL,
        }
        cache = SimpleCache(timeout=60*60*24)


class PicsResource(ModelResource):
    class Meta:
        collection_name="data"
        queryset = Sbpics.objects.all()
        resource_name = 'pics'
        authorization = Authorization()
        # limit = 0 #(unlimted)
        # filtering = {
        #     "branch_flag": ALL,
        #     "branch_name":('exact', 'startswith','istartswith','icontains',),
        #     "cid":ALL,
        # }
        cache = SimpleCache(timeout=60*60*24)

class SbimageResource(ModelResource):
    class Meta:
        collection_name="data"
        queryset = Sbimage.objects.all()
        resource_name = 'sbimage'
        authorization = Authorization()
        # limit = 0 #(unlimted)
        # filtering = {
        #     "branch_flag": ALL,
        #     "branch_name":('exact', 'startswith','istartswith','icontains',),
        #     "cid":ALL,
        # }
        cache = SimpleCache(timeout=60*60*24)


