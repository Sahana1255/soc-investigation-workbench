from extraction.ioc_extractor import IOCExtractor


def test_ipv4():

    extractor = IOCExtractor()

    result = extractor.extract(
        "Connection from 192.168.1.100"
    )

    assert any(

        ioc.value == "192.168.1.100"

        for ioc in result

    )


def test_url():

    extractor = IOCExtractor()

    result = extractor.extract(
        "https://example.com/login"
    )

    assert any(

        ioc.type == "URL"

        for ioc in result

    )


def test_email():

    extractor = IOCExtractor()

    result = extractor.extract(
        "admin@test.com"
    )

    assert any(

        ioc.type == "Email"

        for ioc in result

    )