# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
# from rasa_sdk.events import FollowupAction
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher


# class ActionOne(Action):

#     def name(self) -> Text:
#         return "action_one"

#     def run(self, dispatcher, tracker, domain):
#         dispatcher.utter_message(utter_res1)
#         return[]
