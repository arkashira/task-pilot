import pytest
from src.task_pilot import TaskPilot, TemplateType

def test_get_template():
    task_pilot = TaskPilot()
    template = task_pilot.get_template(TemplateType.SPRINT)
    assert template.name == "Sprint"

def test_create_columns():
    task_pilot = TaskPilot()
    template = task_pilot.get_template(TemplateType.SPRINT)
    columns = task_pilot.create_columns(template)
    assert len(columns) == 3

def test_override_template():
    task_pilot = TaskPilot()
    template = task_pilot.get_template(TemplateType.SPRINT)
    new_columns = [template.columns[0], template.columns[1]]
    new_settings = {"iteration_length": 1}
    overridden_template = task_pilot.override_template(template, new_columns, new_settings)
    assert len(overridden_template.columns) == 2
    assert overridden_template.default_settings == new_settings

def test_main():
    task_pilot = TaskPilot()
    task_pilot.main()
    # No assertion, just checking that it runs without errors
