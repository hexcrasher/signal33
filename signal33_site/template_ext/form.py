from cStringIO import StringIO
from flask import Blueprint

proc = Blueprint("form_processors", __name__)

FORM_URL_ENCODED = "application/x-www-form-urlencoded"
FORM_FILE_UPLOAD = "multipart/form-data"



@proc.context_processor
def begin_form(id, action, method="post", encoding_type=None):
    enctype = ""
    if encoding_type is not None:
        enctype = ' enctype="{0}"'.format(encoding_type)
    return '<form id="{0}" name="{0}" action="{1}" method="{2}"{3}>'.format(id, action, method, enctype)
@proc.context_processor
def end_form():
    return "</form>"

@proc.context_processor
def form_input(id, type="text", **attributes):
    attrs = StringIO()

    attrs.write(' ')

    for key in attributes.keys():
        attrs.write('{0}="{1} " '.format(key, attributes[key]))

    return '<input type="{0}" id="{1}" name="{1}"{2}/>'.format(type, id, attrs.getvalue())

