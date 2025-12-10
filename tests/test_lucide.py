import unittest
from jinja2 import Environment
from jinja2_lucide import LucideExtension

class LucideExtensionTest(unittest.TestCase):
    def setUp(self):
        self.env = Environment(extensions=[LucideExtension])

    def test_render_icon(self):
        template = self.env.from_string('{% lucide "github" %}')
        result = template.render()
        self.assertIn('<svg', result)
        self.assertIn('class="lucide lucide-github"', result)

    def test_render_icon_with_attrs(self):
        template = self.env.from_string('{% lucide "github", width=32, height=32, class_="my-class" %}')
        result = template.render()
        self.assertIn('width="32"', result)
        self.assertIn('height="32"', result)
        self.assertIn('class="lucide lucide-github my-class"', result)

    def test_non_existent_icon(self):
        template = self.env.from_string('{% lucide "non-existent-icon" %}')
        result = template.render()
        self.assertIn('<!-- lucide icon "non-existent-icon" not found -->', result)

if __name__ == '__main__':
    unittest.main()
