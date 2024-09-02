import datetime
from dateutil.relativedelta import relativedelta
from odoo import _, api, models, fields, SUPERUSER_ID
from odoo.exceptions import UserError


class SaaSDB(models.Model):
    """SaaS DB Model"""
    _inherit = 'saas.db'
    _description = 'Add Subscription to SaaS DB'

    is_subscription = fields.Boolean(string='Is Subscription', default=False)
    subscription_id = fields.Many2one('subscription.package',
                                      string='Subscription')
    sub_reference = fields.Char(string="Sub Reference Code", store=True,)