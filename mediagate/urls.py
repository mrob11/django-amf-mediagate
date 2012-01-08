from django.conf.urls.defaults import patterns

urlpatterns += patterns('mediagate.amfgateway', 
    # AMF Gateway
    (r'^amf/', 'mediagateGateway'),
)

