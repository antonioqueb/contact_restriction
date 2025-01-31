from odoo import models, api, exceptions, _

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    # Se elimina la sobreescritura del método create
    # @api.model
    # def create(self, vals):
    #     if not self.env.user.has_group('contact_restriction.group_create_contact'):
    #         raise exceptions.AccessError(_("⚠️ No tienes permiso para crear contactos. Contacta al administrador."))
    #     return super().create(vals)