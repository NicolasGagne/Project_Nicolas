

from django.contrib.auth.models import User
from rest_framework import viewsets, renderers
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy
from .serializers import UserSerializer, BookmarkSerializer
from project_nicolas.app_bookmarks.models import Bookmark
from rest_framework import mixins
from django.http import HttpResponseRedirect, HttpResponse
import urllib
from datetime import datetime, timedelta
from django.shortcuts import redirect
from project_nicolas.settings_file.settings_local import DAY_BEFORE_ERASE
from django.db import IntegrityError
from django.contrib import messages
from rest_framework.exceptions import ValidationError
from django.utils import timezone

def full_url(url):
    if not (url.startswith('http://')) or not (url.startswith('https://')):
        url = 'http://' + url
    return url



def clic_link(request, id):
    """
    view to update the last used time
    """

    queryset = Bookmark.objects.filter(id=id)

    for bm in queryset:
        bm.last_active = datetime.utcnow()
        bm.save()

    url = full_url(bm.site_link)
    check_link(request)
    return redirect(url)

def check_link(request):
    """
    view to check if link are still valid
    """
    print('{timestamp} -- request started'.format(timestamp=datetime.utcnow().isoformat()))
    queryset = Bookmark.objects.all()
    print('{timestamp} --QUERYSET request ended'.format(timestamp=datetime.utcnow().isoformat()))
    for bm in queryset:

        url = full_url(bm.site_link)

        try:
            code = urllib.request.urlopen(url).getcode()
            print("Code: ", code, " ", bm.site_link)
            bm.last_check = timezone.now()
            bm.save()
            print('{timestamp} --TRY request ended'.format(timestamp=datetime.utcnow().isoformat()))
        except urllib.error.URLError:

            if bm.last_check < (timezone.now() - timedelta(days=DAY_BEFORE_ERASE)):
                messages.info(request,
                              bm.title + ',was deleted!, was not working the last ' + DAY_BEFORE_ERASE + ' days')
                bm.delete()

            elif bm.created > (timezone.now() - timedelta(seconds=60)):
                messages.info(request, bm.title + ' does not have a working link NOT ADDED TO THE LIST!')
                bm.delete()

            else:
                messages.info(request, bm.title + ' is not working at this moment')
            print('{timestamp} --EXCEPT request ended'.format(timestamp=datetime.utcnow().isoformat()))

    return HttpResponse(None)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class ListCreateBookmarkViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                viewsets.GenericViewSet):
    """
    A viewset that provides `create` & 'liste, actions.
    """
    renderer_classes = (renderers.TemplateHTMLRenderer,)
    template_name = 'bookmarks_list.html'
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

    def list(self, request, *args, **kwargs):

        response = super(ListCreateBookmarkViewSet, self).list(request, *args, **kwargs)
        serializer = BookmarkSerializer()
        renderer = renderers.HTMLFormRenderer()

        if request.accepted_renderer.format == 'html':
            return Response({'data': response.data, 'form_bookmark': renderer.render(serializer.data)})
        return response


    def create(self, request, *args, **kwargs):
        '''
        Override the create funtion in order to to return to the url list and check url valid
        '''

        url = request.POST["site_link"]
        if not urllib.parse.urlparse(url).scheme:
            url = 'http://' + url

        try:
            urllib.request.urlopen(url)
            super(ListCreateBookmarkViewSet, self).create(request, *args, **kwargs)

        except IntegrityError:
            messages.info(request, 'This URL all ready exist!')

        except ValidationError as error:
            messages.info(request, 'This TITLE all ready exist!')

        except urllib.error.URLError:
            messages.info(request, request.POST["site_link"] + ' is not a working link NOT ADDED TO THE LIST!')


        return HttpResponseRedirect(redirect_to=reverse_lazy('appBookmarks:bookmarks-list'))
