from django.conf.urls.defaults   import *
from django.views.generic.simple import direct_to_template

from views import DATA

urlpatterns = patterns('',

  # url(
  #     r'^$',
  #     direct_to_template,
  #     {'template': 'edu.html',
  #      'extra_context': {}
  #     },
  #     name='people'
  # ),

    url(
        r'^json/info/$',
        DATA.info,
        name='json.info'
    ),

)

if __name__ == "__main__":

    pass

else:

    from svc.urls import data_urlpatterns
    from models   import *

    urlpatterns += data_urlpatterns (EDUCATION)
