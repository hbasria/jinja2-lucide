import lucide
from jinja2 import nodes
from jinja2.ext import Extension
from tagflow import document


kebab_to_pascal = lambda s: ''.join(w.capitalize() for w in s.split('-'))


class LucideExtension(Extension):
    """
    Jinja2 extension to easily embed Lucide icons as SVG.
    
    Usage: {% lucide "icon-name" %}
    Example: {% lucide "github" %}
    """
    tags = {"lucide"}

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        
        # Expects a string literal (the icon name)
        args = [parser.parse_expression()]
        
        return nodes.Output(
            [self.call_method('_render_lucide', args)],
            lineno=lineno
        )

    def _render_lucide(self, icon_name):
        try:
            # Create an icon instance using lucide.create_icon
            with document() as doc:
                icon_class_name = kebab_to_pascal(icon_name)
                icon_class = getattr(lucide, icon_class_name)

                with icon_class():
                    pass

            # Return the SVG string
            return doc.to_html()
        except Exception as e:
            # In case the icon name is invalid or another error occurs
            print(f"Error rendering lucide icon '{icon_name}': {e}")
            return f'<!-- lucide icon "{icon_name}" not found -->'