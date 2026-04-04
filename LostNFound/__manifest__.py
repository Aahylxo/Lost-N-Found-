{
    "name": 'Smart Lost & Found',
    "description":"""
        Campus Lost & Found ERP
        -Log found items with tracking IDs.
        -Students file lost claims.
        -Auto-match engine connects claims to found items based on category and date
            """,
    "depends":["base","mail"],
    "application": True,
    "data":[
        'security/ir.model.access.csv',
        'views/found_item_views.xml',
    ]
}
