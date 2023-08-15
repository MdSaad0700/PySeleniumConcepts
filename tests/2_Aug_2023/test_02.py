import logging


def test_print_logger():
    LOGGER = logging.getLogger(__name__)

    LOGGER.info("This is info")
