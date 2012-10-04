from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.market_data.views',
    #
    # Market URLs
    #

    # Quicklook
    url(r'^(?P<type_id>[0-9]+)/', 'market.market.quicklook', name = 'quicklook'),
    url(r'^tab/ask/(?P<type_id>[0-9]+)/(?P<min_sec>[0-9]+)/(?P<max_age>[0-9]+)/', 'market.market.quicklook_ask_filter', name = 'quicklook_filter_tab_ask'),
    url(r'^tab/bid/(?P<type_id>[0-9]+)/(?P<min_sec>[0-9]+)/(?P<max_age>[0-9]+)/', 'market.market.quicklook_bid_filter', name = 'quicklook_filter_tab_bid'),
    url(r'^region/(?P<region_id>[0-9]+)/(?P<type_id>[0-9]+)/', 'market.market.quicklook_region', name = 'quicklook_region'),
        
    # History JSON
    url(r'^history/(?P<region_id>[0-9]+)/(?P<type_id>[0-9]+)/', 'market.market.history_json', name = 'quicklook_history_json'),

    # Market browser
    url(r'^browse/tree/(?P<group>[0-9]+)/$', 'market.browser.tree', name = 'browser_tree_group_json'),
    url(r'^browse/tree/$', 'market.browser.tree', name = 'browser_tree'),
    
    url(r'^browse/(?P<group>[0-9]+)/', 'market.browser.browser', name = 'browser_preload'),
    url(r'^browse/panel/(?P<group>[0-9]+)/', 'market.browser.panel', name = 'browser_panel'),
    url(r'^browse/', 'market.browser.browser', name = 'browser'),
        
    # Scanners
    url(r'^scanner/random/', 'market.scanners.random', name = 'scanner_random'),
    url(r'^scanner/region/', 'market.scanners.region', name = 'scanner_region'),
        
    #
    # Trading URLs
    #
        
    # Station ranking
    url(r'^trading/station/ranking/', 'trading.station.ranking', name = 'station_ranking'),
    
)