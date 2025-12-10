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
    <p>Here's another one, with custom attributes: {% lucide "activity", width=48, height=48, class_="text-red-500" %}</p>
    <p>This one doesn't exist: {% lucide "non-existent-icon" %}</p>
</body>
</html>
"""
template = env.from_string(template_str)

# 3. Render the template
output = template.render()

# Print the output
print(output)
