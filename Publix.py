#!/bin/python3

import requests

from typing import List, Optional, KeysView
from enum import Enum


class State(Enum):
    GA = "Georgia"
    FL = "Florida"
    SC = "South Carolina"


class Publix:
    def __init__(self):
        # Publix County Script
        self.county_script: str = "https://www.publix.com/covid-vaccine/assets/scripts/retrieveCountyStatus.js"
        self.hiding: bool = self.check_if_hiding()

        # API Endpoints
        self.georgia: str = "https://www.publix.com/covid-vaccine/georgia/georgia-county-status.txt"
        self.florida: str = "https://www.publix.com/covid-vaccine/florida/florida-county-status.txt"
        self.south_carolina: str = "https://www.publix.com/covid-vaccine/south-carolina/south-carolina-county-status.txt"

        # Human Endpoints
        self.georgia_page: str = "https://www.publix.com/covid-vaccine/georgia"
        self.florida_page: str = "https://www.publix.com/covid-vaccine/florida"
        self.south_carolina_page: str = "https://www.publix.com/covid-vaccine/south-carolina"

        self.states: dict = {
            State.GA: {
                "api": self.georgia,
                "human": self.georgia_page
            },
            State.FL: {
                "api": self.florida,
                "human": self.florida_page
            },
            State.SC: {
                "api": self.south_carolina,
                "human": self.south_carolina_page
            }
        }

    def check_if_hiding(self) -> bool:
        response: requests.Response = requests.get(url=self.county_script, stream=False)
        content: str = response.text

        check_sub: str = "!row[1].toLowerCase().includes('none available')) ? status"

        return check_sub in content

    def supported_states(self) -> KeysView:
        return self.states.keys()

    def supported_states_string(self) -> List[str]:
        states: List[str] = []
        for state in self.supported_states():
            states.append(state.value)

        return states

    def vaccine_availability(self, state: State) -> Optional[dict]:
        # Not Needed
        headers: dict = {
            "Content-Type": "text/plain; charset=utf-8",
            "User-Agent": "Chrome/90"
        }

        response: requests.Response = requests.get(url=self.states[state]["api"], stream=True)
        content: str = response.content
        results: dict = {}

        for line in str(content.decode("utf-16-le")).splitlines():
            clean: str = line.strip().strip("\ufeff")
            split: List[str] = clean.rsplit("|")

            if self.hiding and "none available" not in split[1].lower():
                results[split[0]] = "Fully Booked (Completamente reservado)"
            else:
                results[split[0]] = split[1]

        return results
