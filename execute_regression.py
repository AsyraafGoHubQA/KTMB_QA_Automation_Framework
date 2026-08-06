import subprocess
import webbrowser
import os

from utils.report_manager import ReportManager

latest_report, archive_report = ReportManager.prepare_report()

print("=" * 60)
print("KTMB QA AUTOMATION FRAMEWORK")
print("=" * 60)

result = subprocess.run([
    "python",
    "-m",
    "pytest",
    "tests/test_login.py",
    "-v",
    f"--html={latest_report}",
    "--self-contained-html"
])

if result.returncode in [0, 1]:
    ReportManager.archive_report(
        latest_report,
        archive_report
    )

    webbrowser.open(
        os.path.abspath(latest_report)
    )

print("\nExecution Completed.")