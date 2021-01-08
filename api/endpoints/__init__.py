"""Routing table, gather route to main router for API"""
from typing import List
from endpoints.classes import Resource

from .health import HEALTH
from .wrist import WRIST

RESOURCES: List[Resource] = HEALTH + WRIST
