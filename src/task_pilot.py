import json
from dataclasses import dataclass
from enum import Enum
from typing import List


class TemplateType(str, Enum):
    SPRINT = "sprint"
    KANBAN = "kanban"
    OKR = "okr"


@dataclass
class Column:
    name: str
    settings: dict


@dataclass
class Template:
    name: str
    columns: List[Column]
    default_settings: dict


class TaskPilot:
    """Core class that stores and manipulates workflow templates."""

    def __init__(self):
        self.templates = {
            TemplateType.SPRINT: Template(
                "Sprint",
                [
                    Column("To-Do", {}),
                    Column("In Progress", {}),
                    Column("Done", {}),
                ],
                {"iteration_length": 2},
            ),
            TemplateType.KANBAN: Template(
                "Kanban",
                [
                    Column("Backlog", {}),
                    Column("Ready", {}),
                    Column("In Progress", {}),
                    Column("Done", {}),
                ],
                {},
            ),
            TemplateType.OKR: Template(
                "OKR",
                [
                    Column("Objectives", {}),
                    Column("Key Results", {}),
                ],
                {},
            ),
        }

    # --------------------------------------------------------------------- #
    # Public API used by the test‑suite
    # --------------------------------------------------------------------- #

    def get_template(self, template_type: TemplateType) -> Template | None:
        """Return the template associated with *template_type* or ``None``."""
        return self.templates.get(template_type)

    def create_columns(self, template: Template) -> List[Column]:
        """Return a list of columns defined in *template*."""
        return template.columns

    def override_template(
        self, template: Template, new_columns: List[Column], new_settings: dict
    ) -> Template:
        """
        Replace *template*'s columns and default settings with the supplied
        values and return the modified template.
        """
        template.columns = new_columns
        template.default_settings = new_settings
        return template

    def main(self) -> None:
        """
        Entry‑point used by the test suite. Prints a JSON array containing the
        names of all available templates.
        """
        print(json.dumps([t.name for t in self.templates.values()], indent=4))
