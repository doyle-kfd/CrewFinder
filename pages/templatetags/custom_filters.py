from django import template

register = template.Library()

@register.filter(name='secure')
def secure(url):
    print("Custom filters loaded!") 
    """Convert HTTP URLs to HTTPS."""
    if url and url.startswith("http://"):
        return url.replace("http://", "https://")
    return url