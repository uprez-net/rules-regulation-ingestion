from unstructured.chunking.title import chunk_by_title

def chunk_text(elements):
    return chunk_by_title(
        elements,
        combine_text_under_n_chars=100,
        max_characters=3000,
    )
