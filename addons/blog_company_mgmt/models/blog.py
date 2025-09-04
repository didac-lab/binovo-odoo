from odoo import fields, models

class Blog(models.Model):
    _inherit = "blog.blog"
    company_id = fields.Many2one(
        "res.company",
        required=True,
        default=lambda self: self.env.company,
        index=True)

class BlogPost(models.Model):
    _inherit = "blog.post"
    company_id = fields.Many2one(
        related="blog_id.company_id",
        comodel_name="res.company",
        store=True, readonly=True,
        index=True)