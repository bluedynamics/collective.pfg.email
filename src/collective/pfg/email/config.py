from Products.CMFCore.permissions import setDefaultRoles


PROJECTNAME = 'collective.pfg.email'
ADD_PERMISSIONS = {
    'FormEmailField': 'collective.pfg.email: Add FormEmailField',
}
setDefaultRoles(
    ADD_PERMISSIONS['FormEmailField'],
    ('Manager', 'Owner', 'Contributor', 'Site Administrator')
)
