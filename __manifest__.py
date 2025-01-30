{
    'name': 'Restricción de Creación de Contactos',
    'version': '1.0',
    'summary': 'Restringe la creación de contactos a un grupo específico y administradores.',
    'category': 'Contactos',
    'author': 'Tu Nombre',
    'website': 'https://tu.sitio.web',
    'depends': ['base', 'contacts'],
    'data': [
        'security/contact_security.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}