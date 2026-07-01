from ingestion.classifier import EvidenceClassifier


def test_windows():

    classifier = EvidenceClassifier()

    assert classifier.classify(
        "Security.evtx"
    ) == "Windows"


def test_linux():

    classifier = EvidenceClassifier()

    assert classifier.classify(
        "auth.log"
    ) == "Linux"


def test_email():

    classifier = EvidenceClassifier()

    assert classifier.classify(
        "mail.eml"
    ) == "Email"


def test_csv():

    classifier = EvidenceClassifier()

    assert classifier.classify(
        "events.csv"
    ) == "CSV"