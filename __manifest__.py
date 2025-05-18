{
    "name": "Commande Client",
    "version": "1.0",
    "author": "Jean-Louis",
    "category": "Custom",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/commande_views.xml"
    ],
    "assets": {
        "web.assets_backend": [
            "commande_client/static/src/css/style.css"
        ]
    },
    "installable": True,
    "application": True
}
