from extraction.extraction_engine import ExtractionEngine

from detection.detection_engine import DetectionEngine

from models.investigation_result import InvestigationResult


class InvestigationService:

    def __init__(self):

        self.extractor = ExtractionEngine()

        self.detector = DetectionEngine()

    def investigate(self, events):

        investigations = []

        for event in events:

            extracted = self.extractor.extract(
                event.raw_data
            )

            investigation = InvestigationResult(

                event=event,

                iocs=extracted["iocs"],

                users=extracted["users"],

                assets=extracted["assets"],

                processes=extracted["processes"],

                network=extracted["network"]

            )

            self.detector.detect(
                investigation
            )

            investigations.append(
                investigation
            )

        return investigations