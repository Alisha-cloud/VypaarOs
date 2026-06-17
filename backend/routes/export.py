from fastapi import APIRouter
from fastapi.responses import FileResponse

from services.pdf_export import (
    generate_pdf
)

router = APIRouter()


@router.post("/export")

def export_pdf(
    data: dict
):

    path = generate_pdf(
        data["report"]
    )

    return FileResponse(
        path,
        filename="VyapaarOS_Report.pdf",
        media_type="application/pdf"
    )