from django.conf.urls import  url

from . import views

urlpatterns = [
    # url(r'^$', views.landing_page, name='landing_page'),

    # url(r'^get_model/$', views.get_model, name='get_model'),

    # element
    # url(r'^delete_element_from_db/$', views.delete_element_from_db, name='delete_element_from_db'),
    # url(r'^add_element_to_db/$', views.add_element_to_db, name='add_element_to_db'),
    # url(r'^update_element_to_db/$', views.update_element_to_db, name='update_element_to_db'),

    # data structure
    # url(r'^delete_datastructure_from_db/$', views.delete_datastructure_from_db, name='delete_datastructure_from_db'),
    # url(r'^add_datastructure_to_db/$', views.add_datastructure_to_db, name='add_datastructure_to_db'),

    #get data structure image
    # url(r'^get_image/$', views.get_image, name='get_image'),
    url(r'^data_calc/$', views.tomainpage, name='tomainpage'),
    url(r'^add_element_to_db/$', views.add_element_to_db, name='add_element_to_db'),
]
