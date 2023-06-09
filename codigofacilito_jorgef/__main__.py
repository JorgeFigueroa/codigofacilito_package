from codigofacilito_jorgef import unreleased
import logging

"""
INFO -> 10
DEBUG -> 20
WARNING -> 30
ERROR -> 40
CRITICAL -> 50
"""

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logging.debug(">>> start paquete")
    # workshops = unreleased()
    logging.debug(help(unreleased.__doc__))

    logging.debug(">>> end paquete")
