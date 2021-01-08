from endpoints.classes import Resource

from .post import DOC as get_doc
from .post import post

WRIST = [
    Resource("POST", "/wrist", post, "Used for creating data", "Create Data", get_doc)
]
