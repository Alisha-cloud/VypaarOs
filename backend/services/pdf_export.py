from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_pdf(
    report,
    output_path="report.pdf"
):

    doc = SimpleDocTemplate(
        output_path
    )

    styles = getSampleStyleSheet()

    content = [
        Paragraph(
            "VyapaarOS Business Report",
            styles["Title"]
        ),

        Spacer(1, 20),

        Paragraph(
            report.replace(
                "\n",
                "<br/>"
            ),
            styles["BodyText"]
        )
    ]

    doc.build(content)

    return output_path