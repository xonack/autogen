# filename: arxiv_search.py

import arxiv

def search_arxiv(query, max_results=10):
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    for result in search.results():
        print(f"Title: {result.title}")
        print(f"Authors: {', '.join(a.name for a in result.authors)}")
        print(f"Published: {result.published}")
        print(f"Summary: {result.summary} \n")

search_arxiv("GPT-4")