from AccessControl import ClassSecurityInfo
from Products.CMFCore.permissions import View
from Products.Archetypes import atapi
from Products.ATContentTypes.content.base import registerATCT
from Products.PloneFormGen.content.fieldsBase import (
    finalizeFieldSchema,
    BaseFormField,
    BaseFieldSchemaStringDefault,
)
from . import config


email_schema = BaseFieldSchemaStringDefault.copy() + atapi.Schema((
))


del starrating_schema['hidden']
del starrating_schema['serverSide']


finalizeFieldSchema(starrating_schema, folderish=True, moveDiscussion=False)


class FormEmailField(BaseFormField):
    """Email Field.
    """
    meta_type = 'FormEmailField'
    security = ClassSecurityInfo()
    schema = email_schema

    def __init__(self, oid, **kwargs):
        BaseFormField.__init__(self, oid, **kwargs)

        # set a preconfigured field as an instance attribute
        self.fgField = StringField('fg_email_field',
            searchable=0,
            required=0,
            write_permission=View,
            #validators=('isNotTooLong',),
            )


registerATCT(FormEmailField, config.PROJECTNAME)
