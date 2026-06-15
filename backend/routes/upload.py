from fastapi import (
    APIRouter,
    UploadFile,
    File
)

from services.vector_store import (
    add_documents
)

router = APIRouter()


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):

    content = await file.read()

    text = content.decode(
        "utf-8"
    )

    add_documents(
        [text]
    )

    return {
        "message":
        "Document indexed successfully"
    }