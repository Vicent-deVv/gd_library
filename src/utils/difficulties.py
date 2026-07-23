from enum import Enum


class Difficulty(Enum):
    NA = "Unrated"
    AUTO = "Auto"
    EASY = "Easy"
    NORMAL = "Normal"
    HARD = "Hard"
    HARDER = "Harder"
    INSANE = "Insane"
    EASY_DEMON = "Easy Demon"
    MEDIUM_DEMON = "Medium Demon"
    HARD_DEMON = "Hard Demon"
    INSANE_DEMON = "Insane Demon"
    EXTREME_DEMON = "Extreme Demon"


def get_level_difficulty(
    dif_numerator: int,
    dif_denominator: int,
    is_demon: bool,
    is_auto: bool,
    demon_diff: int,
):

    if is_auto:
        return Difficulty.AUTO

    if is_demon:
        demon_dict = {
            3: Difficulty.EASY_DEMON,
            4: Difficulty.MEDIUM_DEMON,
            0: Difficulty.HARD_DEMON,
            5: Difficulty.INSANE_DEMON,
            6: Difficulty.EXTREME_DEMON,
        }
        return demon_dict.get(demon_diff, Difficulty.HARD_DEMON)

    if dif_denominator != 0:
        calculate_demon_dif = dif_numerator // dif_denominator
    else:
        calculate_demon_dif = 0

    level_dict = {
        0: Difficulty.NA,
        1: Difficulty.EASY,
        2: Difficulty.NORMAL,
        3: Difficulty.HARD,
        4: Difficulty.HARDER,
        5: Difficulty.INSANE,
    }

    return level_dict.get(calculate_demon_dif, Difficulty.NA)