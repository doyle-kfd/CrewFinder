"""
Template Tags
This module defines custom template tags and filters to extend the
functionality
of Django templates. It provides utilities for accessing and manipulating data
within templates.

Filters:
1. get_item: A custom filter to retrieve a value from a dictionary by key.

Key Features:
- Simplifies data retrieval within templates.
- Handles cases where the input is not a dictionary or the key is not found.

Dependencies:
- Django's template system for registering custom filters.
"""

from django import template

# Register the template library to define custom template tags and filters
register = template.Library()


@register.filter(name='get_item')
def get_item(dictionary, key):
    """
    Custom filter to get a dictionary value by key.

    Parameters:
    - dictionary (dict): The dictionary from which to retrieve the value.
    - key (str): The key to look up in the dictionary.

    Returns:
    - The value associated with the key in the dictionary, or 'Not Applied'
      if the key is not found or the input is not a dictionary.
    """
    # Check if the provided input is a dictionary
    if isinstance(dictionary, dict):
        # Retrieve the value by key, default to 'Not Applied'
        # if key is not found
        return dictionary.get(key, 'Not Applied')
    # Return 'Not Applied' if the input is not a dictionary or is None
    return 'Not Applied'
