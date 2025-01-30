from odoo import models, api, exceptions, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, vals):
        user = self.env.user
        if not (user.has_group('contact_restriction.group_create_contact') or user._is_admin()):
            raise exceptions.AccessError(_("⚠️ No tienes permiso para crear contactos. Contacta al administrador."))
        return super(ResPartner, self).create(vals)