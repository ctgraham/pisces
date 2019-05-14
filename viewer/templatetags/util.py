from django import template
from .models import Note

register = template.Library()


@register.filter
def agent_filter(value):
    AGENT_MAP = {
        "agent_person": "Person",
        "agent_family": "Family",
        "agent_corporate_entity": "Organization",
        "agent_software": "Software",
    }
    return AGENT_MAP.get(value, value)


@register.filter
def term_type_filter(value):
    TERM_MAP = {
        "cultural_context": "Cultural context",
        "function": "Function",
        "geographic": "Geographic",
        "genre_form": "Genre / Form",
        "occupation": "Occupation",
        "style_period": "Style / Period",
        "technique": "Technique",
        "temporal": "Temporal",
        "topical": "Topic",
        "uniform_title": "Uniform Title",
        }
    return TERM_MAP.get(value, value)


@register.filter
def source_filter(value):
    SOURCE_MAP = {
        Note.ARCHIVESSPACE: "Rockefeller Archive Center",
        Note.CARTOGRAPHER: "Rockefeller Archive Center",
        Note.WIKIDATA: "Wikidata",
        Note.WIKIPEDIA: "Wikipedia",
        }
    return SOURCE_MAP.get(value, value)
