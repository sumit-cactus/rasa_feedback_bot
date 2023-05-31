from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher

class ValidateFeedBackForm(FormValidationAction):
        def name(self) -> Text:
            return "validate_feedback_form"
        
        def is_int(self, value):
                try:
                    int(value)
                    return True
                except ValueError:
                    return False

        def validate_rating(self, slot_value, dispatcher, tracker, domain):
                if not self.is_int(slot_value):
                    dispatcher.utter_message("Please enter a valid rating between 1 and 5.")
                    return {"rating": None}
                if int(slot_value) > 5 or int(slot_value) < 1:
                    dispatcher.utter_message("Please enter a rating between 1 and 5.")
                    return {"rating": None}
                return {"rating": slot_value}

        def validate_feature(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> Dict[Text, Any]:
                if slot_value is None:
                    return {"feature": None}
                else:
                    return {"feature": slot_value}

        def validate_improvement(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> Dict[Text, Any]:
                if slot_value is None:
                    return {"improvement": None}
                else:
                    return {"improvement": slot_value}
        
class ActionSubmitFeedback(Action):
    def name(self) -> Text:
        return "action_submit_feedback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        rating = tracker.get_slot("rating")
        feature = tracker.get_slot("feature")
        improvement = tracker.get_slot("improvement")
        dispatcher.utter_message(template="utter_thanks_feedback")
        return []

