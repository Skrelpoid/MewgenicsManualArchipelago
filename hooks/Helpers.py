from typing import Optional, Any
from BaseClasses import MultiWorld


# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    from ..Locations import location_name_groups
    if category_name in location_name_groups["GoalOption"]:
        # This category is the name of a GoalOpion
        from ..Helpers import get_option_value
        chosen_goals = get_option_value(multiworld, player, "goals")
        # Fallback if User chooses no Goal
        if len(chosen_goals) == 0:
            chosen_goals = ["The Caves Boss"]
        return category_name in chosen_goals
    return None

def before_is_item_enabled(multiworld: MultiWorld, player: int, item:  dict[str, Any]) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:
    if "GoalOption" in location["category"]:
        from ..Helpers import get_option_value
        chosen_goals = set(get_option_value(multiworld, player, "goals"))
        # Fallback if User chooses no Goal
        if len(chosen_goals) == 0:
            chosen_goals = {"The Caves Boss"}
        return bool(set(location["category"]) & chosen_goals)
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
