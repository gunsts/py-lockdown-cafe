from .cafe import Cafe
from .errors import NotVaccinatedError
from .errors import OutdatedVaccineError
from .errors import NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    vaccinated_count = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            vaccinated_count += 1
        except NotWearingMaskError:
            masks_to_buy += 1
    if vaccinated_count != 0:
        return "All friends should be vaccinated"
    if masks_to_buy != 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
