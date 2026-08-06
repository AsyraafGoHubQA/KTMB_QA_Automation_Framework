import os
import shutil
from datetime import datetime


class ReportManager:

    @staticmethod
    def prepare_report():

        today = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().strftime("%H-%M-%S")

        latest_folder = os.path.join("reports", "Latest")
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

    @staticmethod
    def archive_report(latest_report, archive_report):

        if os.path.exists(latest_report):

            shutil.copy2(latest_report, archive_report)

            print("\nArchive Report Created")
            print(archive_report)

        else:

            print("\nLatest report not found.")