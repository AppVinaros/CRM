"""Simple CRM application."""

from .cli import main
from . import database

__all__ = ['main', 'database']
