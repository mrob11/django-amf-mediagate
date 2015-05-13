from django.conf.urls import patterns


urlpatterns = patterns(
    'mediagate.amfgateway',
    (r'^amf/', 'mediagateGateway'),
)
