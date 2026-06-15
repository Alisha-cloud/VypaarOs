import faiss
import numpy as np

from sentence_transformers import (
    SentenceTransformer
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

dimension = 384

index = faiss.IndexFlatL2(
    dimension
)

documents = []


def add_documents(texts):

    embeddings = model.encode(
        texts
    )

    index.add(
        np.array(
            embeddings,
            dtype=np.float32
        )
    )

    documents.extend(
        texts
    )


def search_documents(
    query,
    top_k=3
):

    query_embedding = model.encode(
        [query]
    )

    distances, indices = index.search(
        np.array(
            query_embedding,
            dtype=np.float32
        ),
        top_k
    )

    results = []

    for idx in indices[0]:

        if idx < len(documents):
            results.append(
                documents[idx]
            )

    return results