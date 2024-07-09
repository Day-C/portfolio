#!/usr/bin/python3
    """Define durg object attributes."""

    #if getenv("PHPSL_STORAGE_T") == "db":
    __tablename__ = "Reviews"

    name = Column("Drugs", String(128), nullable=False)
    description = Conlum("description", String(1024))
    active_ings = Column("active_ings", String(1024))
    inactive_ings = Column("inactive_ings", String(1024))
    strength = Column("stength", String(60))
    indication_usage = Column("usage", String(1024))
    dosage = Colum("dosage", String(1024))
    contradiction = Column("contradiction", String(1024))
    precautions = Column("precautions", String(1024))
    warning = Column("warning", String(1024))
    advers_react = Column("advers_reaction", String(1024))
    overdosage = Column("overdose", String(1024))
    pharmacology = Column("pharmacology"))
    package_ndc =Column("package_ndc", String(60))
    storage = Column("storage", String(400))

    name = ""
    description = ""
    active_ings = ""
    inactive_ings = ""
    strength = ""
    indication_usage = ""
    dosage = ""
    contradiction = ""
    precautions = ""
    warning = ""
    advers_react = ""
    overdosage = ""
    pharmacology = ""
    package_ndc = ""
    package_ndc = ""
