{
    "name": "Blog Company Management",
    "version": "16.0.1.0.0",
    "category": "Website/Blog",
    "summary": "Company ownership on blogs and posts with hierarchical access",
    "license": "LGPL-3",
    "depends": ["website_blog", "base"],
    "data": [
        "security/ir.model.access.csv",
        "security/blog_company_rules.xml",
        "views/blog_views.xml",
    ],
    "installable": True,
}