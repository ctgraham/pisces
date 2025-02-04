"""Source resources and their fields.

The resources in this file come from RAC data sources, including ArchivesSpace
and Cartographer, as well as external sources such as Wikipedia and Wikidata.
It is assumed that data from multiple sources will have been merged it is used
to instantiate these resources.
"""

import odin

from . import configs


class SourceRef(odin.Resource):
    """A reference to a related object."""
    ref = odin.StringField()
    type = odin.StringField(null=True)
    title = odin.StringField(null=True)


class SourceAncestor(odin.Resource):
    """A related SourceResource or SourceArchivalObject.

    SourceAncestors are parents of the current data object. Order is significant; they
    are listed from closest to furthest away (in other words the last ancestor
    will always be the top level of a collection).
    """
    ref = odin.StringField()
    level = odin.StringField()
    order = odin.StringField(null=True)
    title = odin.StringField(null=True)
    type = odin.StringField(null=True)
    subjects = odin.ArrayOf(SourceRef, null=True)
    dates = odin.StringField(null=True)


class SourceDate(odin.Resource):
    """Records the dates associated with an aggregation of archival records."""
    expression = odin.StringField(null=True)
    begin = odin.StringField(null=True)
    end = odin.StringField(null=True)
    date_type = odin.StringField(choices=configs.DATE_TYPE_CHOICES)
    label = odin.StringField(choices=configs.DATE_LABEL_CHOICES)


class SourceStructuredDateSingle(odin.Resource):
    """A structured representation of a single date"""
    date_expression = odin.StringField(null=True)
    date_standardized = odin.StringField(null=True)


class SourceStructuredDateRange(odin.Resource):
    """A structured representation of a date range"""
    begin_date_expression = odin.StringField(null=True)
    begin_date_standardized = odin.StringField(null=True)
    end_date_expression = odin.StringField(null=True)
    end_date_standardized = odin.StringField(null=True)


class SourceStructuredDate(odin.Resource):
    """An alternative representation of dates, currently associated only with agents."""
    date_label = odin.StringField(choices=configs.DATE_LABEL_CHOICES)
    date_type_structured = odin.StringField(choices=configs.DATE_TYPE_CHOICES)
    structured_date_single = odin.DictAs(SourceStructuredDateSingle, null=True)
    structured_date_range = odin.DictAs(SourceStructuredDateRange, null=True)


class SourceExtent(odin.Resource):
    """Records the size of an aggregation of archival records."""
    number = odin.StringField()
    container_summary = odin.StringField(null=True)
    portion = odin.StringField(choices=(('whole', 'Whole'), ('part', 'Part'))),
    extent_type = odin.StringField()


class SourceExternalId(odin.Resource):
    """Uniquely identifies a data object."""
    external_id = odin.StringField()
    source = odin.StringField()


class SourceAgentRecordIdentifier(odin.Resource):
    """Identifies an agent record in an external data source."""
    record_identifier = odin.StringField()
    source = odin.StringField()


class SourceLanguageAndScript(odin.Resource):
    """Records the language and scripts of archival records.

    Applies to resources post-ArchivesSpace v2.7 only.
    """
    language = odin.StringField(null=True)


class SourceLangMaterial(odin.Resource):
    """Records information about the languages of archival records.

    Applies to resources post-ArchivesSpace v2.7 only.
    """
    language_and_script = odin.DictAs(SourceLanguageAndScript, null=True)


class SourceSubcontainer(odin.Resource):
    """Provides detailed container information."""
    indicator_2 = odin.StringField(null=True)
    type_2 = odin.StringField(choices=configs.CONTAINER_TYPE_CHOICES, null=True)
    top_container = odin.DictAs(SourceRef)


class SourceInstance(odin.Resource):
    """The physical or digital instantiation of a group of records."""
    instance_type = odin.StringField(choices=configs.INSTANCE_TYPE_CHOICES)
    is_representative = odin.BooleanField()
    sub_container = odin.DictAs(SourceSubcontainer, null=True)
    digital_object = odin.DictAs(SourceRef, null=True)


class SourceLinkedAgent(odin.Resource):
    """A reference to a SourceAgentFamily, SourceAgentPerson or SourceAgentCorporateEntity."""
    role = odin.StringField(choices=configs.AGENT_ROLE_CHOICES)
    relator = odin.StringField(choices=configs.AGENT_RELATOR_CHOICES, null=True)
    ref = odin.StringField()
    type = odin.StringField()
    title = odin.StringField()


class SourceNameBase(odin.Resource):
    """Base class for structured representations of names.

    Subclassed by more specific representations SourceNameCorporateEntity,
    SourceNamePerson and SourceNameFamily.
    """
    sort_name = odin.StringField()
    authorized = odin.BooleanField()
    is_display_name = odin.BooleanField()
    # use_dates = odin.ArrayOf(SourceStructuredDate) # TODO: account for structured and nonstructured dates
    rules = odin.StringField(choices=configs.NAME_RULES_CHOICES, null=True)
    source = odin.StringField(choices=configs.NAME_SOURCE_CHOICES, null=True)


class SourceNameCorporateEntity(SourceNameBase):
    """A structured representation of an SourceAgentCorporateEntity's name."""
    primary_name = odin.StringField()


class SourceNameFamily(SourceNameBase):
    """A structured representation of a SourceAgentFamily's name."""
    family_name = odin.StringField()


class SourceNamePerson(SourceNameBase):
    """A structured representation of a SourceAgentPerson's name."""
    primary_name = odin.StringField()
    rest_of_name = odin.StringField(null=True)
    name_order = odin.StringField(choices=(('direct', 'Direct'), ('inverted', 'Inverted')))


class SourceSubnote(odin.Resource):
    """Contains note content."""
    jsonmodel_type = odin.StringField()
    content = odin.StringField(null=True)
    items = odin.ArrayField(null=True)


class SourceNote(odin.Resource):
    """Human-readable note.

    SourceNotes contain one or more SourceSubnotes.
    """
    jsonmodel_type = odin.StringField()
    type = odin.StringField(null=True)
    label = odin.StringField(null=True)
    subnotes = odin.ArrayOf(SourceSubnote, null=True)
    content = odin.StringField(null=True)
    items = odin.ArrayField(null=True)
    publish = odin.BooleanField()


class SourceGroup(odin.Resource):
    """Information about the highest-level collection containing the data object."""
    creators = odin.ArrayOf(SourceLinkedAgent, null=True)
    dates = odin.ArrayField(null=True)
    identifier = odin.StringField()
    title = odin.StringField()


class SourceTerm(odin.Resource):
    """A controlled term."""
    term_type = odin.StringField(choices=configs.TERM_TYPE_CHOICES)


class SourceSubject(odin.Resource):
    """A topical term."""
    external_ids = odin.ArrayOf(SourceExternalId)
    group = odin.DictAs(SourceGroup)
    publish = odin.BooleanField()
    source = odin.StringField(choices=configs.SUBJECT_SOURCE_CHOICES)
    terms = odin.ArrayOf(SourceTerm)
    title = odin.StringField()
    uri = odin.StringField()


class SourceComponentBase(odin.Resource):
    """Base class for archival components.

    Subclassed by SourceArchivalObject and SourceResource.

    Both language and lang_material need to exist in order to accomodate
    ArchivesSpace API changes between v2.6 and v2.7.
    """
    class Meta:
        abstract = True

    COMPONENT_TYPES = (
        ('archival_object', 'Archival Object'),
        ('resource', 'Resource')
    )

    dates = odin.ArrayOf(SourceDate)
    extents = odin.ArrayOf(SourceExtent)
    external_ids = odin.ArrayOf(SourceExternalId)
    group = odin.DictAs(SourceGroup)
    jsonmodel_type = odin.StringField(choices=COMPONENT_TYPES)
    lang_materials = odin.ArrayOf(SourceLangMaterial, null=True)
    language = odin.StringField(null=True)
    level = odin.StringField()
    linked_agents = odin.ArrayOf(SourceLinkedAgent)
    notes = odin.ArrayOf(SourceNote)
    publish = odin.BooleanField()
    subjects = odin.ArrayOf(SourceRef)
    suppressed = odin.StringField()
    title = odin.StringField(null=True)
    uri = odin.StringField()


class SourceArchivalObject(SourceComponentBase):
    """A component of a SourceResource."""
    position = odin.IntegerField()
    ref_id = odin.StringField()
    component_id = odin.StringField(null=True)
    display_string = odin.StringField()
    restrictions_apply = odin.BooleanField()
    ancestors = odin.ArrayOf(SourceAncestor)
    resource = odin.DictAs(SourceRef)
    has_unpublished_ancestor = odin.BooleanField()
    instances = odin.ArrayOf(SourceInstance)


class SourceResource(SourceComponentBase):
    """An aggregation of records."""
    position = odin.IntegerField()
    restrictions = odin.BooleanField()
    ead_id = odin.StringField(null=True)
    finding_aid_title = odin.StringField(null=True)
    finding_aid_filing_title = odin.StringField(null=True)
    id_0 = odin.StringField()
    id_1 = odin.StringField(null=True)
    id_2 = odin.StringField(null=True)
    ancestors = odin.ArrayOf(SourceAncestor, null=True)
    instances = odin.ArrayOf(SourceInstance)


class SourceAgentBase(odin.Resource):
    """A base class for agents.

    Subclassed by SourceAgentFamily, SourceAgentPerson and
    SourceAgentCorporateEntity.
    """
    class Meta:
        abstract = True

    AGENT_TYPES = (
        ('agent_corporate_entity', 'Organization'),
        ('agent_family', 'Family'),
        ('agent_person', 'Person')
    )

    agent_record_identifiers = odin.ArrayOf(SourceAgentRecordIdentifier, null=True)
    dates_of_existence = odin.ArrayField(null=True)
    group = odin.DictAs(SourceGroup)
    jsonmodel_type = odin.StringField(choices=AGENT_TYPES)
    notes = odin.ArrayOf(SourceNote)
    publish = odin.BooleanField()
    title = odin.StringField()
    uri = odin.StringField()


class SourceAgentCorporateEntity(SourceAgentBase):
    """An organization."""
    names = odin.ArrayOf(SourceNameCorporateEntity)
    display_name = odin.DictAs(SourceNameCorporateEntity)


class SourceAgentFamily(SourceAgentBase):
    """A family."""
    names = odin.ArrayOf(SourceNameFamily)
    display_name = odin.DictAs(SourceNameFamily)


class SourceAgentPerson(SourceAgentBase):
    """A person."""
    names = odin.ArrayOf(SourceNamePerson)
    display_name = odin.DictAs(SourceNamePerson)
