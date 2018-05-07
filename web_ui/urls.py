"""
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
"""
URL mapping of the application
"""

from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),

    # Angular mappings
    url(r'^home/?$', views.index, name='home'),
    url(r'^ng/home/?$', views.home, name='home'),

    # APIs Mappings

    # Maps the URL web/api/pod to the method api_pod inside views.py
    url(r'^api/pod/?$', views.api_pod),
    # Maps the URL web/api/switch/ to the method api_switch inside views.py
    url(r'^api/switch/(?P<podDn>.*)/?$', views.api_switch),
    # Maps the URL web/api/interface/ to the method api_switch inside views.py
    url(r'^api/interface/(?P<switchDn>.*)/?$', views.api_interface),
    # Maps the URL web/api/epg to the method api_epg inside views.py
    url(r'^api/epgs/?$', views.api_epg),
    # Maps the URL web/api/deploy to the method api_deploy inside views.py
    url(r'^api/deploy/?$', views.api_deploy),

]
