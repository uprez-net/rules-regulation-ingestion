from unstructured.partition.xlsx import partition_xlsx

def extract_elements_from_xlsx(filename: str):
    elements = partition_xlsx(filename=filename)
    return elements
