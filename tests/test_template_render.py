"""Smoke test: template.html must render to a valid PDF via WeasyPrint."""
from pathlib import Path

import weasyprint

TEMPLATE = Path(__file__).parent.parent / "template.html"


def test_template_renders_to_valid_pdf(tmp_path):
    pdf_bytes = weasyprint.HTML(filename=str(TEMPLATE)).write_pdf()

    assert pdf_bytes.startswith(b"%PDF-")
    assert len(pdf_bytes) > 1000

    out = tmp_path / "out.pdf"
    out.write_bytes(pdf_bytes)
    assert out.stat().st_size > 0
