from django.conf.urls import include, url
from raku_bot.views import RakuBotView

urlpatterns = [
        url(r'^a92ef480ccf0e1e51082eb68cfe81ce2d963f4e4ce11133557/?$', RakuBotView.as_view())
        ]
