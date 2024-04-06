from . import views
from django.urls import path

urlpatterns = [
    #path('', views.main, name="main"),
    path('file/', views.kz_file, name="kz_file"),
    path('file/<str:test>/', views.main_test, name="main_test"),
    path('xz/', views.main_test2, name="main_test2"),
    path('session/', views.main_of_session, name="main_of_session"),
    path('', views.main, name="main"),
    path('logout/', views.logout, name="logout"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="registration"),
    path('Avatar/', views.ProfilePic, name="ProfilePic"),
    path('User/change_pass/', views.pass_Changing, name="Change_pass"),
    path('usr/photos/<int:usr>/', views.Dsp_user_images, name="dsusrpht"),
    path('contacts/', views.Contact, name="Contacts"),
    path('contacts/message/<int:usr_id>', views.Contact_messages, name="Contacts"),
    path('contacts/message/<int:usr_id>/<int:post_id>/', views.Contact_message_rem, name="removing_message"),
    path('rchatpost/<int:post_id>/', views.removing_chat_post, name="rm_chat_pot1q"),
    path('user/<int:us_id>/', views.User_Profile, name="usrDatas"),
]
