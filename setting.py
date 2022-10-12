#!/bin/env python
#coding=utf-8
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/vendor/')
#os.chdir(os.path.dirname(os.path.abspath(__file__)))

import logging
import uuid


settings = {
    'debug': True,
    'autoreload': True,
    "static_path": os.path.join(os.path.dirname(__file__), "static/"),
    "cookie_secret": "RyanKiu",
    "cookie_domain": "",
    "QiniuAccessKey": "WyKOXI0j_IA4WY3NYLuyJmm18oWsN3cxnEBylM6A",
    "QiniuSecretKey": "LjMeeTet0sCYcnDyUIBH_vjregSOHLbYSgDkMSKm",
}

try:
    import vendor
    import vendor.torndb as database
    conn = database.Connection("127.0.0.1:3306", "jiao1", "root", "Kiu422?!")
    conn1 = database.Connection("127.0.0.1:3306", "jiao2", "root", "Kiu422?!")
    conn2 = database.Connection("127.0.0.1:3306", "jiao3", "root", "Kiu422?!")
    ring = [conn1, conn2]
except:
    pass
