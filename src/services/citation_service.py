class CitationService:
    
    def generate_apa(self, sources):

        citations = []

        for index, source in enumerate(sources, start=1):

            citations.append(
                f"{index}. {source['title']}. {source['link']}"
            )

        return citations

    def generate_mla(self, sources):

        citations = []

        for index, source in enumerate(sources, start=1):

            citations.append(
                f"{index}. \"{source['title']}\". {source['link']}"
            )

        return citations

    def generate_ieee(self, sources):

        citations = []

        for index, source in enumerate(sources, start=1):

            citations.append(
                f"[{index}] {source['title']}. Available: {source['link']}"
            )

        return citations


citation_service = CitationService()