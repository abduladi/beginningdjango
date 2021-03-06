from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin

from coffeehouse.items.urls import urlpatterns as items_url_patterns
from django.conf import settings
from coffeehouse.stores.models import Special


urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name='homepage.html'), {"NODEJS_SOCKET_URL":settings.NODEJS_SOCKET_URL,"specials":Special.objects.all().order_by("-id")[:5]},name="homepage"),
    url(r'^about/', include('coffeehouse.about.urls',namespace="about")),
    url(r'^items/', include(items_url_patterns,namespace="items")),
    url(r'^stores/',include('coffeehouse.stores.urls',namespace="stores")),
    url(r'^online/',TemplateView.as_view(template_name='online/index.html'),name='online'),
    url(r'^admin/', admin.site.urls),

]
