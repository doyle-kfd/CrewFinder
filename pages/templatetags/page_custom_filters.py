"""
Template Tags
This module defines custom template tags and filters to extend
the functionality of Django templates. It includes utilities for
transforming and manipulating data
to suit specific template needs.

Filters:
1. secure: Converts HTTP URLs to HTTPS for enhanced security.

Key Features:
- Improves security by ensuring URLs use HTTPS instead of HTTP.
- Easily integrates into templates for seamless transformation.

Dependencies:
- Django's template system for registering custom filters.
"""

from django import template

# Register the template library to define custom template tags and filters
register = template.Library()


@register.filter(name='secure')
def secure(url):
    """
    Converts HTTP URLs to HTTPS for enhanced security.

    Parameters:
    - url (str): The URL to be transformed.

    Returns:
    - str: The transformed URL with HTTPS if it originally used HTTP.
           If the URL does not start with "http://", it is returned unchanged.
    """
    # Check if the URL starts with "http://"
    if url and url.startswith("http://"):
        # Replace "http://" with "https://"
        return url.replace("http://", "https://")
    return url  # Return the original URL if no transformation is needed
