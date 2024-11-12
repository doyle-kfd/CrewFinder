from django import template

register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key):
    """Custom filter to get a dictionary value by key."""
    if isinstance(dictionary, dict):  # Check if dictionary is actually a dictionary
        return dictionary.get(key, 'Not Applied')  # Default to 'Not Applied' if key not found
    return 'Not Applied'  # If dictionary is None or not a dictionary, return 'Not Applied'
