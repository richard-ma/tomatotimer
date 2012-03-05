from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('tomatotimer.views',
    url(r'^$', 'index'),
    # Chrome Notification
    url(r'^chrome/popup-tomato/$', 'chrome_popup_tomato'),
    url(r'^chrome/popup-break/$', 'chrome_popup_break'),
    # Task Operation
    url(r'^task/create/$', 'task_create'),
    url(r'^task/update/(\d+)/$', 'task_update'),
    url(r'^task/read/all/$', 'task_read_all'),
    url(r'^task/read/(\d+)/$', 'task_read'),
    url(r'^task/delete/(\d+)/$', 'task_delete'),
)
