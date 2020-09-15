"""quizproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from triviaapp import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.getname,name='getname'),
    path('playgame',views.playgame,name='playgame'),
    path('question1/$',views.question1,name='question1'),
    path('question1/(?P<pk>\d+)/$',views.question1,name='question1'),
    path('question2',views.question2,name='question2'),
    path('summary',views.summary,name='summary'),
    path('history',views.history,name='history'),

]