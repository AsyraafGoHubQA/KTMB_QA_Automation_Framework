import os
import shutil
import subprocess
import webbrowser
from datetime import datetime

from nlp.command_parser import parse_command
from nlp.scenario_mapping import SCENARIO_MAPPING


def create_report_path():

    today = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H-%M-%S")

    # Latest Report Folder
    latest_folder = os.path.join("reports", "Latest")

    # Archive Folder
    archive_folder = os.path.join("reports", "Archive", today)

    os.makedirs(latest_folder, exist_ok=True)
    os.makedirs(archive_folder, exist_ok=True)

    latest_report = os.path.join(
        latest_folder,
        "KTMB_LoginAutomation_Latest.html"
    )

    archive_report = os.path.join(
        archive_folder,
        f"KTMB_LoginAutomation_{current_time}.html"
    )

    return latest_report, archive_report


print("=" * 70)
print("        KTMB Intelligent Automation Assistant")
print("=" * 70)

while True:

    command = input("\nEnter your command (or type 'exit'): ")

    if command.lower() == "exit":
        print("\nThank you. Goodbye!")
        break

    result = parse_command(command)

    print("\n========== NLP Result ==========")
    print(f"Intent   : {result['intent']}")
    print(f"Scenario : {result['scenario']}")

    tc = SCENARIO_MAPPING.get(
        (result["intent"], result["scenario"])
    )

    if tc:

        print(f"\nMatched Test Case : {tc}")
        print("Launching Playwright Automation...\n")

        os.environ["SELECTED_TC"] = tc

        latest_report, archive_report = create_report_path()

        subprocess.run([
            "pytest",
            "tests/test_login.py",
            "-v",
            "-s",
            f"--html={latest_report}",
            "--self-contained-html"
        ])

       # Copy Latest Report to Archive only if it exists
if os.path.exists(latest_report):
    shutil.copy2(latest_report, archive_report)
    print("\nArchive report created successfully.")
else:
    print("\nERROR: Latest report was not generated.")
    

        print("\n" + "=" * 70)
        print("Automation Execution Completed")
        print("=" * 70)

        print(f"\nLatest Report :")
        print(latest_report)

        print(f"\nArchive Report :")
        print(archive_report)

        webbrowser.open(os.path.abspath(latest_report))

    else:

        print("\nNo matching test case found.")