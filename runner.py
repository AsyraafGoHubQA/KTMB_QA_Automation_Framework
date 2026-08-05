import os
import subprocess

from nlp.command_parser import parse_command
from nlp.scenario_mapping import SCENARIO_MAPPING

print("=" * 60)
print("     KTMB Intelligent Automation Assistant")
print("=" * 60)

while True:

    command = input("\nEnter your command (or type 'exit'): ")

    if command.lower() == "exit":
        print("\nGoodbye!")
        break

    result = parse_command(command)

    print("\n========== NLP Result ==========")
    print(f"Intent   : {result['intent']}")
    print(f"Scenario : {result['scenario']}")

    tc = SCENARIO_MAPPING.get(
        (result["intent"], result["scenario"])
    )

    if tc:

        print(f"Matched Test Case : {tc}")
        print("\nLaunching Playwright Automation...\n")

        # Pass selected TC to pytest
        os.environ["SELECTED_TC"] = tc

        subprocess.run([
            "pytest",
            "tests/test_login.py",
            "-v",
            "-s"
        ])

    else:

        print("\nNo matching test case found.")