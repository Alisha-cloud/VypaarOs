import os
import pandas as pd

from fastapi import (
    APIRouter,
    UploadFile,
    File
)

from services.vector_store import (
    add_documents
)

from services.pdf_reader import (
    read_pdf
)

router = APIRouter()


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):

    content = await file.read()

    temp_path = f"temp_{file.filename}"

    with open(
        temp_path,
        "wb"
    ) as f:
        f.write(content)

    if file.filename.endswith(".pdf"):

        text = read_pdf(
            temp_path
        )

    elif file.filename.endswith(".csv"):

        df = pd.read_csv(
            temp_path
        )

        text = df.to_string()

    else:

        text = content.decode(
            "utf-8"
        )

    add_documents(
        [text]
    )

    os.remove(
        temp_path
    )

    return {
        "message":
        "Document indexed successfully"
    }