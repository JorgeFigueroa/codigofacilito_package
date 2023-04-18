from codigofacilito import unreleased
import logging

"""
INFO -> 10
DEBUG -> 20
WARNING -> 30
ERROR -> 40
CRITICAL -> 50
"""

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    logging.debug(">>> start paquete")
    workshops = unreleased()
    logging.debug("workshops:", workshops)
    print("workshops:", workshops)

    logging.debug(">>> end paquete")

