from datetime import datetime


class ExportService:

    def generate_markdown(
        self,
        topic,
        brief,
        citations=None,
        quiz=None
    ):

        report = f"# Smart Research Report\n\n"

        report += f"## Topic\n\n{topic}\n\n"

        report += f"Generated on: {datetime.now()}\n\n"

        report += "---\n\n"

        report += "## Research Brief\n\n"

        report += brief

        report += "\n\n---\n\n"

        if citations:

            report += "## Citations\n\n"

            for citation in citations:

                report += f"- {citation}\n"

            report += "\n"

        if quiz:

            report += "## Quiz\n\n"

            report += quiz

        return report


export_service = ExportService()