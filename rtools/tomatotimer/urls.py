from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('tomatotimer.views',
    url(r'^$', 'index'),
    # Chrome Notification
    url(r'^chrome/popup-tomato/$', 'chrome_popup_tomato'),
    url(r'^chrome/popup-break/$', 'chrome_popup_break'),
)

# for staticfiles
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)