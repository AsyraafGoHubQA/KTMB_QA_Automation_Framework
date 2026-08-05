import spacy
from nlp.intents import INTENTS, SCENARIOS

nlp = spacy.load("en_core_web_sm")


def parse_command(command):

    doc = nlp(command.lower())

    # Generate tokens and lemmas
    tokens = [token.text.lower() for token in doc]
    lemmas = [token.lemma_.lower() for token in doc]

    result = {
        "intent": None,
        "scenario": None
    }

    # ------------------------
    # Detect Intent
    # ------------------------
    for intent, keywords in INTENTS.items():

        for keyword in keywords:

            keyword_tokens = keyword.lower().split()

            # Single word
            if len(keyword_tokens) == 1:

                if keyword_tokens[0] in tokens or keyword_tokens[0] in lemmas:
                    result["intent"] = intent
                    break

            # Multiple words
            else:

                if keyword.lower() in command.lower():
                    result["intent"] = intent
                    break

        if result["intent"]:
            break

    # ------------------------
    # Detect Scenario
    # ------------------------
    for scenario, keywords in SCENARIOS.items():

        for keyword in keywords:

            keyword_tokens = keyword.lower().split()

            # Single word
            if len(keyword_tokens) == 1:

                if keyword_tokens[0] in tokens or keyword_tokens[0] in lemmas:
                    result["scenario"] = scenario
                    break

            # Multiple words
            else:

                if keyword.lower() in command.lower():
                    result["scenario"] = scenario
                    break

        if result["scenario"]:
            break

    return result