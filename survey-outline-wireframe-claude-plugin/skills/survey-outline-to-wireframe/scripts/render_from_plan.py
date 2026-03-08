"""
Render a survey wireframe DOCX from a JSON plan.

Usage:
    python render_from_plan.py plan.json output.docx

The JSON plan must contain:
    cover: {
        title: str,
        subtitle: str (optional),
        date: str (optional)
    }
    overview: {
        objectives: list (optional),
        quotas: list (optional),
        survey_flow: list (optional),
        survey_flow_description: str (optional)
    }
    sections: [
        {
            name: str,
            objectives: list (optional),
            header_fill: str (optional),
            rows: [
                {"type": "message", "text": str|list, "message_label": str (optional)},
                {"type": "qualification_message", "text": str|list},
                {"type": "termination_message", "text": str|list},
                {"type": "subsection", "name": str, "objectives": list (optional), "header_fill": str (optional)},
                {
                    "type": "question",
                    "title": str,
                    "question_parts": list|str,
                    "instruction": str (optional),
                    "response_lines": list (optional),
                    "notes": list (optional),
                    "objective": str|list (optional),
                    "programming_notes": list (optional),
                    "sub_questions": list (optional),
                    "question_number": str|false (optional)
                }
            ]
        }
    ]
"""

import argparse
import json
from pathlib import Path

from wireframe_builder import WireframeBuilder


def _load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def _required(mapping, key, where):
    if key not in mapping or mapping[key] in (None, ""):
        raise ValueError(f"Missing required field '{key}' in {where}.")
    return mapping[key]


def render(plan, output_path):
    builder = WireframeBuilder()

    cover = plan.get("cover") or {}
    title = _required(cover, "title", "cover")
    builder.set_cover(
        title=title,
        subtitle=cover.get("subtitle", "Survey Wireframe"),
        date=cover.get("date", ""),
    )

    overview = plan.get("overview") or {}
    if overview:
        builder.add_overview(
            objectives=overview.get("objectives"),
            quotas=overview.get("quotas"),
            survey_flow=overview.get("survey_flow"),
            survey_flow_description=overview.get("survey_flow_description"),
        )

    sections = plan.get("sections") or []
    if not sections:
        raise ValueError("Plan must include at least one section.")

    for section_index, section in enumerate(sections, start=1):
        section_name = _required(section, "name", f"sections[{section_index}]")
        builder.start_section(
            section_name,
            objectives=section.get("objectives"),
            header_fill=section.get("header_fill"),
        )

        for row_index, row in enumerate(section.get("rows") or [], start=1):
            row_type = row.get("type", "question")
            where = f"sections[{section_index}].rows[{row_index}]"

            if row_type == "message":
                builder.add_message(
                    _required(row, "text", where),
                    message_label=row.get("message_label", "Message"),
                )
                continue

            if row_type == "qualification_message":
                builder.add_qualification_message(_required(row, "text", where))
                continue

            if row_type == "termination_message":
                builder.add_termination_message(_required(row, "text", where))
                continue

            if row_type == "subsection":
                builder.add_subsection(
                    _required(row, "name", where),
                    objectives=row.get("objectives"),
                    header_fill=row.get("header_fill"),
                )
                continue

            if row_type != "question":
                raise ValueError(f"Unsupported row type '{row_type}' in {where}.")

            builder.add_question(
                title=_required(row, "title", where),
                question_parts=row.get("question_parts", []),
                instruction=row.get("instruction"),
                response_lines=row.get("response_lines"),
                notes=row.get("notes"),
                objective=row.get("objective", ""),
                programming_notes=row.get("programming_notes"),
                sub_questions=row.get("sub_questions"),
                question_number=row.get("question_number", ""),
            )

    return builder.save(output_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("plan_path")
    parser.add_argument("output_path")
    args = parser.parse_args()

    plan = _load_json(args.plan_path)
    output = Path(args.output_path)
    render(plan, str(output))
    print(output)


if __name__ == "__main__":
    main()
