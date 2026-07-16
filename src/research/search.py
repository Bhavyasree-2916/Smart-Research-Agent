from ddgs import DDGS


def search_topic(topic, max_results=5):
    """
    Search the web for a given topic.
    Returns a list of search results.
    """

    results = []

    with DDGS() as ddgs:
        search_results = ddgs.text(topic, max_results=max_results)

        for item in search_results:
            results.append({
                "title": item["title"],
                "link": item["href"],
                "snippet": item["body"]
            })

    return results