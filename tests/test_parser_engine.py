from ingestion.parser_engine import ParserEngine


def test_parser_exists():

    engine = ParserEngine()

    assert engine is not None