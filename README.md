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
    {# Simple icon #}
    {% lucide "activity" %}

    {# Icon with custom attributes #}
    {% lucide "github", width=32, height=32, class_="my-custom-class" %}
    ```

    This will render the icons as inline SVGs.

    **Note:** Use `class_` instead of `class` for CSS classes, as `class` is a reserved keyword in Python.

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
    <p>Here's a bigger, red one: {% lucide "heart", width=48, height=48, class_="text-red-500" %}</p>
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
    <p>Here's a bigger, red one: <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-heart text-red-500"><path d="M20.42 4.58a5.4 5.4 0 0 0-7.65 0l-.77.77-.77-.77a5.4 5.4 0 0 0-7.65 0C3.33 5.43 3 6.61 3 8.03c0 1.42.33 2.6 1.17 3.44l7.07 7.07 7.07-7.07A5.4 5.4 0 0 0 21 8.03c0-1.42-.33-2.6-1.17-3.45z"/></svg></p>
</body>
</html>
```

## How it Works

This extension provides a `{% lucide %}` tag that takes a single argument: the name of the icon you want to render. It uses the [lucide-python](https://pypi.org/project/lucide-python/) library to generate the SVG for the icon.

If an icon is not found, a comment `<!-- lucide icon "..." not found -->` will be rendered in its place.
