# -*- coding: utf-8 -*-
# Copyright 2020 BDO Spain
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import models, fields


class DocumentPage(models.Model):
    _inherit = 'document.page'

    origin = fields.Char('Origin')
