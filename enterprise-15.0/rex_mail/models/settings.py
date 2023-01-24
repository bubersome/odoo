#!/usr/bin/python3
# @Time    : 2021-08-06
# @Author  : Kevin Kong (kfx2007@163.com)

from odoo import api, fields, models, _


class res_config_settings(models.TransientModel):

    _inherit = "res.config.settings"

    using_catchall = fields.Boolean(
        string="Using Catch All", default=False, config_parameter="mail.catchall.enable")
    restrict_username = fields.Boolean(
        string="Restrict Username", default=False, config_parameter="mail.restrict.username")
