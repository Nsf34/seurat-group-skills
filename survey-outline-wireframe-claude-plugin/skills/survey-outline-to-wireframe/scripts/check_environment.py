"""
Lightweight environment check for the survey wireframe plugin.
"""

import sys


def main():
    try:
        import docx  # type: ignore
    except ModuleNotFoundError:
        print(
            "Missing dependency: python-docx. Install it in the local Python environment before "
            "running this skill."
        )
        return 1

    version = getattr(docx, "__version__", "unknown")
    print(f"python-docx available: {version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
