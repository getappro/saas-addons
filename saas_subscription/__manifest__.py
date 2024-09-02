# Copyright 2020 Eugene Molotov <https://it-projects.info/team/em230418>
# License MIT (https://opensource.org/licenses/MIT).

{
    "name": """SaaS: Subscription""",
    "summary": """This module helps to create saas related Subscription. For example subscribtion""",
    "category": "Sales",
    "images": [],
    "version": "16.0.15.1.0",
    "application": False,
    "author": "WAHBI ACHRAF GetapPRO",
    "support": "support@getap.pro",
    "license": "Other OSI approved licence",  # MIT
    "depends": [
        "subscription_package",
        "saas",
        "saas_limit_max_users",
        "saas_build_admin",
        "saas_expiration"
    ],
    "data": [
        "views/subscription_package.xml",
        "views/saas_db_view.xml",
    ],
    "demo": [],
    "qweb": [],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,
    "auto_install": False,
    "installable": True,
}

