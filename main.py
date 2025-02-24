from partitioning.xlsx_partition import extract_elements_from_xlsx
from chunking.text_chunking import chunk_text
from ingestion.pipeline import ingest_data
from utils.helpers import elements_to_json

FILENAME = "data/Complaince.xlsx"

if __name__ == "__main__":
    elements = extract_elements_from_xlsx(FILENAME)
    print(elements[1].text)

    json_data = elements_to_json(elements)
    print(json_data)

    chunks = chunk_text(elements)

    data = [chunk.to_dict() for chunk in chunks]
    ingest_data(data)
