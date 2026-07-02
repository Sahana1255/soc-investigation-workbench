from pathlib import Path

from models.incident import Incident
from models.evidence import Evidence

from ingestion.classifier import EvidenceClassifier
from ingestion.parser_engine import ParserEngine

from services.investigation_service import InvestigationService
from services.database_service import DatabaseService

from correlation.correlation_engine import CorrelationEngine

from investigation.case_manager import CaseManager

from utils.logger import Logger
from utils.performance import timer


class SOCEngine:

    def __init__(self):

        self.logger = Logger.get_logger()

        self.classifier = EvidenceClassifier()

        self.parser = ParserEngine()

        self.investigation = InvestigationService()

        self.correlation = CorrelationEngine()

        self.case_manager = CaseManager()

        self.database = DatabaseService()

    def investigate(
        self,
        title,
        evidence_files,
        description="",
        analyst=None,
        max_events=None
    ):

        with timer("TOTAL INVESTIGATION"):

            self.logger.info(
                f"Starting investigation: {title}"
            )

            incident = Incident(

                title=title,

                description=description,

                assigned_analyst=analyst

            )

            self.logger.info(
                f"Received {len(evidence_files)} evidence file(s)."
            )

            # ----------------------------------------------------
            # Register Evidence
            # ----------------------------------------------------

            for file in evidence_files:

                path = Path(file)

                platform = self.classifier.classify(file)

                self.logger.info(
                    f"Evidence: {path.name} -> {platform}"
                )

                incident.evidence.append(

                    Evidence(

                        filename=path.name,

                        filepath=path,

                        file_type=path.suffix,

                        platform=platform

                    )

                )

            # ----------------------------------------------------
            # Parse Evidence
            # ----------------------------------------------------

            with timer("Parser"):

                events = self.parser.parse(
                    incident.evidence,
                    max_events=max_events
                )

            self.logger.info(
                f"Parsed {len(events)} event(s)."
            )

            # ----------------------------------------------------
            # Investigation
            # ----------------------------------------------------

            with timer("Investigation"):

                investigations = self.investigation.investigate(
                    events
                )

            self.logger.info(
                f"Generated {len(investigations)} investigation result(s)."
            )

            # ----------------------------------------------------
            # Correlation
            # ----------------------------------------------------

            with timer("Correlation"):

                correlation = self.correlation.correlate(
                    investigations
                )

            self.logger.info(

                f"Generated "
                f"{correlation.get('relationship_count', 0)} "
                f"relationship(s)."

            )

            # ----------------------------------------------------
            # Populate Incident
            # ----------------------------------------------------

            incident.events = [

                item.event

                for item in investigations

            ]

            incident.iocs = [

                ioc

                for item in investigations

                for ioc in item.iocs

            ]

            incident.relationships = correlation.get(

                "relationships",

                []

            )

            if investigations:

                incident.risk_score = max(

                    item.risk_score

                    for item in investigations

                )

                severity_order = [

                    "Low",

                    "Medium",

                    "High",

                    "Critical"

                ]

                incident.severity = max(

                    (

                        item.severity

                        for item in investigations

                    ),

                    key=severity_order.index

                )

            # ----------------------------------------------------
            # Case Management
            # ----------------------------------------------------

            case = self.case_manager.create(
                incident
            )

            # ----------------------------------------------------
            # Database
            # ----------------------------------------------------

            with timer("Database Save"):

                self.database.save_case(
                    case
                )

                self.database.save_incident(
                    incident
                )

            self.logger.info(

                f"Case {case['case_id']} saved."

            )

            self.logger.info(

                f"Incident {incident.incident_id} completed."

            )

            self.logger.info(

                f"Summary | "

                f"Events={len(incident.events)}, "

                f"IOCs={len(incident.iocs)}, "

                f"Risk={incident.risk_score}, "

                f"Severity={incident.severity}"

            )

            return {

                "case": case,

                "incident": incident,

                "investigations": investigations,

                "correlation": correlation

            }