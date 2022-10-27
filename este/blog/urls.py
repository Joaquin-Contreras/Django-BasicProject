from django.urls import path
from .views import Posts,PostDetalle,crearPost

app_name = 'blog'

urlpatterns = [
    path('', Posts, name='posts'),
    path('<int:post_id>', PostDetalle, name="postdetalle"),
    path('crearPost', crearPost, name="crearPost"),
    path('<str:tema>', Posts)
]