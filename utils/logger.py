import logging
from pathlib import Path


class Logger:

    _logger = None

    @classmethod
    def get_logger(cls):

        if cls._logger is not None:
            return cls._logger

        log_dir = Path("logs")

        log_dir.mkdir(
            exist_ok=True
        )

        logger = logging.getLogger(
            "SOCWorkbench"
        )

        logger.setLevel(
            logging.INFO
        )

        if not logger.handlers:

            formatter = logging.Formatter(

                "%(asctime)s | %(levelname)s | %(message)s"

            )

            file_handler = logging.FileHandler(
                log_dir / "soc_workbench.log",
                encoding="utf-8"
            )

            file_handler.setFormatter(
                formatter
            )

            console_handler = logging.StreamHandler()

            console_handler.setFormatter(
                formatter
            )

            logger.addHandler(
                file_handler
            )

            logger.addHandler(
                console_handler
            )

        cls._logger = logger

        return logger