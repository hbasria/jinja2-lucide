# Jinja2 Lucide

A Jinja2 extension to easily embed [Lucide](https://lucide.dev/) icons in your templates.

## Installation

```bash
pip install jinja2-lucide
```

## Usage

1.  Add the extension to your Jinja2 environment:

    ```python
    from jinja2 import Environment
    from jinja2_lucide import LucideExtension

    env = Environment(extensions=[LucideExtension])
    ```

2.  Use the `{% lucide %}` tag in your templates:

    ```jinja
    {% lucide "activity" %}
    ```

    This will render the "activity" icon as an inline SVG.

## Example

Here's a complete example of how to use the extension:

```python
from jinja2 import Environment
from jinja2_lucide import LucideExtension

# 1. Set up the Jinja2 environment
env = Environment(extensions=[LucideExtension])

# 2. Load your template
template_str = """
<!DOCTYPE html>
<html>
<head>
    <title>My Awesome Page</title>
</head>
<body>
    <h1>Welcome!</h1>
    <p>Here's a neat icon: {% lucide "github" %}</p>
</body>
</html>
"""
template = env.from_string(template_str)

# 3. Render the template
output = template.render()

# Print the output
print(output)
```

This will produce the following HTML:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Awesome Page</title>
</head>
<body>
    <h1>Welcome!</h1>
    <p>Here's a neat icon: <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-github"><path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"/></svg></p>
</body>
</html>
```

## How it Works

This extension provides a `{% lucide %}` tag that takes a single argument: the name of the icon you want to render. It uses the [lucide-python](https://pypi.org/project/lucide-python/) library to generate the SVG for the icon.

If an icon is not found, a comment `<!-- lucide icon "..." not found -->` will be rendered in its place.
