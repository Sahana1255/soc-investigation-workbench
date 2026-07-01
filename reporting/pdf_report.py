from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer


class PDFReport:

    def generate(self, incident, investigations, filename):

        document = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        story = []

        story.append(
            Paragraph("SOC Investigation Report", styles["Title"])
        )

        story.append(Spacer(1, 20))

        story.append(
            Paragraph(f"<b>Incident:</b> {incident.title}", styles["BodyText"])
        )

        story.append(
            Paragraph(f"<b>Status:</b> {incident.status}", styles["BodyText"])
        )

        story.append(
            Paragraph(f"<b>Priority:</b> {incident.priority}", styles["BodyText"])
        )

        story.append(
            Paragraph(f"<b>Severity:</b> {incident.severity}", styles["BodyText"])
        )

        story.append(
            Paragraph(f"<b>Total Events:</b> {len(incident.events)}", styles["BodyText"])
        )

        story.append(
            Paragraph(f"<b>Total IOCs:</b> {len(incident.iocs)}", styles["BodyText"])
        )

        story.append(Spacer(1, 20))

        story.append(
            Paragraph("Investigation Timeline", styles["Heading2"])
        )

        for event in incident.events[:50]:

            story.append(

                Paragraph(

                    f"{event.timestamp} | Event ID {event.event_code} | "
                    f"{event.username} | {event.hostname}",

                    styles["BodyText"]

                )

            )

        story.append(Spacer(1, 20))

        story.append(
            Paragraph("Recommendations", styles["Heading2"])
        )

        recommendations = [

            "Review suspicious authentication attempts.",

            "Investigate privileged account activity.",

            "Validate PowerShell execution.",

            "Review newly created user accounts.",

            "Verify all extracted IOCs."

        ]

        for recommendation in recommendations:

            story.append(
                Paragraph(f"• {recommendation}", styles["BodyText"])
            )

        document.build(story)