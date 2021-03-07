#!/bin/python3

from Publix import Publix, State

if __name__ == "__main__":
    publix: Publix = Publix()
    publix_states: str = ", ".join(publix.supported_states_string())

    print(f"Supported States: {publix_states}")

    print("----------------------------------------")
    for state in publix.supported_states():
        vaccine_available: bool = False
        results: dict = publix.vaccine_availability(state=state)

        print(f"State: {state.value}")
        print("----------------------------------------")
        for county in results.keys():
            result: str = results[county]

            if "fully booked" in result.lower() or "none available" in result.lower():
                continue

            vaccine_available: bool = True

            print(f"{county}: {result}")

        if not vaccine_available:
            print("No Vaccines Are Available")

        print("----------------------------------------")
