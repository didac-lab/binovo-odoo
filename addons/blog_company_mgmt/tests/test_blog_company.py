from odoo.tests.common import SavepointCase, tagged

@tagged('post_install', '-at_install')
class TestBlogCompany(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Company = cls.env['res.company']
        Users = cls.env['res.users']
        cls.parent = Company.create({'name': 'Parent Co'})
        cls.child = Company.create({'name': 'Child Co', 'parent_id': cls.parent.id})

        cls.user_parent = Users.create({
            'name': 'Parent User',
            'login': 'parentuser',
            'email': 'p@example.com',
            'company_id': cls.parent.id,
            'company_ids': [(6, 0, [cls.parent.id])],
        })

        cls.blog_child = cls.env['blog.blog'].sudo().create({
            'name': 'Child Blog',
            'company_id': cls.child.id,
        })
        cls.post_child = cls.env['blog.post'].sudo().create({
            'name': 'Child Post',
            'blog_id': cls.blog_child.id,
        })

    def test_user_sees_child_company_content(self):
        # record rule: child_of user's company -> includes descendants
        posts = self.env['blog.post'].with_user(self.user_parent).search([('id', '=', self.post_child.id)])
        self.assertTrue(posts, "Parent company user should see child company's posts")
        self.assertEqual(posts.company_id, self.child)