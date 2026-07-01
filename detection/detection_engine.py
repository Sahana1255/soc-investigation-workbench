from detection.sigma_engine import SigmaEngine
from detection.yara_engine import YaraEngine
from detection.whitelist import WhiteList
from detection.blacklist import BlackList

from intelligence.reputation_engine import ReputationEngine
from intelligence.mitre_mapper import MitreMapper
from intelligence.risk_engine import RiskEngine


class DetectionEngine:

    def __init__(self):

        self.sigma = SigmaEngine()

        self.yara = YaraEngine()

        self.whitelist = WhiteList()

        self.blacklist = BlackList()

        self.reputation = ReputationEngine()

        self.mitre = MitreMapper()

        self.risk = RiskEngine()

    def detect(self, investigation):

        self.sigma.detect(
            investigation
        )

        self.yara.detect(
            investigation
        )

        investigation.iocs = [

            ioc

            for ioc in investigation.iocs

            if not self.whitelist.contains(ioc)

        ]

        for ioc in investigation.iocs:

            if self.blacklist.contains(ioc):

                ioc.reputation = "Malicious"

                ioc.confidence = 100

        self.reputation.enrich(
            investigation
        )

        technique = self.mitre.map(
            investigation.event
        )

        if technique:

            investigation.techniques.append(
                technique
            )

        self.risk.assess(
            investigation
        )

        return investigation