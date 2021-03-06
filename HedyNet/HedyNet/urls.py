from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from .views import HomeTemplateView, VisitTemplateView

urlpatterns = patterns('',
    url(r'^$', HomeTemplateView.as_view(), name="home"),
    url(r'^visit$', VisitTemplateView.as_view(), name="visit"),

    url(r'^about$', TemplateView.as_view(template_name='about.html'), name="about"),
    url(r'^policies$', TemplateView.as_view(template_name='policies.html'), name="policies"),
    url(r'^codeofconduct$', TemplateView.as_view(template_name='codeofconduct.html'), name="codeofconduct"),
    url(r'^wishlist$', TemplateView.as_view(template_name="wishlist.html"), name="wishlist"),
    url(r'^sitemap$', TemplateView.as_view(template_name="sitemap.html"), name="sitemap"),
    url(r'^tos$', TemplateView.as_view(template_name="tos.html"), name="tos"),

    url(r'^membership$', TemplateView.as_view(template_name="membership.html"), name="membership"),    
    url(r'^friends$', TemplateView.as_view(template_name="friends.html"), name="friends"),
    url(r'^events$', TemplateView.as_view(template_name="events.html"), name="events"),
    
    url(r'^faq/', include('FAQ.urls')),
    url(r'^payments/', include('payments.urls')),
    url(r'^othersites/', include('othersites.urls')),
    url(r'^mailinglists/', include('mailchimp2.urls')),

    # Examples:
    # url(r'^$', 'HedyNet.views.home', name='home'),
    # url(r'^HedyNet/', include('HedyNet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'twilio.xml$', TemplateView.as_view(template_name="twilio.xml"), name="twilio_xml"),
)
