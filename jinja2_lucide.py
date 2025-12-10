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

        # Parse optional keyword arguments
        kwargs = []
        while parser.stream.current.type != 'block_end':
            parser.stream.skip_if('comma')
            if parser.stream.current.type == 'name':
                name = next(parser.stream)
                parser.stream.expect('assign')
                value = parser.parse_expression()
                kwargs.append(nodes.Keyword(name.value, value))

        return nodes.Output(
            [self.call_method('_render_lucide', args + kwargs)],
            lineno=lineno
        )

    def _render_lucide(self, icon_name, **kwargs):
        if 'class_' in kwargs:
            kwargs['class'] = f"lucide lucide-{icon_name} {kwargs.pop('class_')}"
        try:
            # Create an icon instance using lucide.create_icon
            with document() as doc:
                icon_class_name = kebab_to_pascal(icon_name)
                icon_class = getattr(lucide, icon_class_name)

                with icon_class(**kwargs):
                    pass

            # Return the SVG string
            return doc.to_html()
        except Exception as e:
            # In case the icon name is invalid or another error occurs
            print(f"Error rendering lucide icon '{icon_name}': {e}")
            return f'<!-- lucide icon "{icon_name}" not found -->'