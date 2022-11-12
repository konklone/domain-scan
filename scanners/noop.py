import logging
from typing import Tuple
from utils.scan_utils import ArgumentParser, make_values_single

###
# Testing scan function. Does nothing time consuming or destructive,
# but exercises many of the main hooks of domain-scan.


# Set a default number of workers for a particular scan type.
# Overridden by a --workers flag.
workers = 2


# Optional one-time initialization for all scans.
# If defined, any data returned will be passed to every scan instance and used
# to update the environment dict for that instance
# Will halt scan execution if it returns False or raises an exception.
#
# Run locally.
def init(environment: dict, options: dict) -> dict:
    logging.debug("Init function.")
    return {'constant': 12345}


# Optional one-time initialization per-scan. If defined, any data
# returned will be passed to the instance for that domain and used to update
# the environment dict for that particular domain.
#
# Run locally.
def init_domain(domain: str, environment: dict, options: dict) -> dict:
    logging.debug("Init function for %s." % domain)
    return {'variable': domain}


# Required scan function. This is the meat of the scanner, where things
# that use the network or are otherwise expensive would go.
#
# Runs locally or in the cloud (Lambda).
def scan(domain: str, environment: dict, options: dict) -> dict:
    logging.debug("Scan function called with options: %s" % options)

    # Perform the "task".
    complete = True
    logging.warning("Complete!")

    return {
        'complete': complete,
        'constant': environment.get('constant'),
        'variable': environment.get('variable')
    }


# Required CSV row conversion function. Usually one row, can be more.
#
# Run locally.
def to_rows(data):
    return [
        [data['complete'], data['constant'], data['variable']]
    ]


# CSV headers for each row of data. Referenced locally.
headers = ["Completed", "Constant", "Variable"]
