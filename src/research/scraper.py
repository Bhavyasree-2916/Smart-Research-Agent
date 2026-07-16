import trafilatura


def extract_text(url):
    """
    Download a webpage and extract clean article text.
    """

    try:
        downloaded = trafilatura.fetch_url(url)

        if downloaded is None:
            return "Unable to download webpage."

        text = trafilatura.extract(
            downloaded,
            include_comments=False,
            include_tables=False
        )

        if text is None:
            return "No readable content found."

        return text

    except Exception as e:
        return f"Error: {e}"