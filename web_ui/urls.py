"""
Copyright (c) 2018 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

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
