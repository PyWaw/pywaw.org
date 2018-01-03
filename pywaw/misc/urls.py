from django.conf.urls import url

from . import views

app_name = 'misc'
urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^faq/$', views.FaqView.as_view(), name='faq'),
    # url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
]
