from django.urls import path
# from .views import movie_list, movie_detail
from .views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamDetailAV, ReviewList, ReviewDetail

urlpatterns = [
    path('list/', WatchListAV.as_view(), name="movie-list"),
    path("<int:pk>", WatchDetailAV.as_view(), name="movie-detail"),
    path("stream/", StreamPlatformAV.as_view(), name="stream-list"),
    path("stream/<int:pk>/", StreamDetailAV.as_view(), name='streamplatform-detail'),
    path('review/', ReviewList.as_view(), name="review-list"),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail')
]
