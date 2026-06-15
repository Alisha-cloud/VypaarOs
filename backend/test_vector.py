from services.vector_store import (
    add_documents,
    search_documents
)

add_documents([
    "Floral Kurti sales increased by 40 percent",
    "Raksha Bandhan campaign generated high engagement",
    "Price reduction improved conversion rates"
])

results = search_documents(
    "How can I increase sales?"
)

print(results)