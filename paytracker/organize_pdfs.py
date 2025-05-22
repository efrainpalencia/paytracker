import os
import re
import shutil
from datetime import datetime

import dotenv
dotenv.load_dotenv()

# ----------------------------
# 🌐 Environment Variables
# ----------------------------
source_folder_env = os.getenv("SOURCE_FOLDER")
target_root_env = os.getenv("TARGET_ROOT")


# ----------------------------
# 📁 Paths
# ----------------------------

# Source folder where the raw paycheck PDFs are stored
source_folder = fr"{source_folder_env}"

# Target root directory for organized paychecks
target_root = fr"{target_root_env}"

# ----------------------------
# 🧠 Date Parsing Helper
# ----------------------------
def parse_date_from_filename(filename):
    """
    Extracts a date from a filename formatted like:
    'Statement for Apr 2, 2025.pdf'.

    Returns:
        datetime object if a date is successfully parsed,
        otherwise None.
    """
    match = re.search(r"Statement for (\w{3}) (\d{1,2}), (\d{4})", filename)
    if not match:
        return None

    month_str, day, year = match.groups()
    date_str = f"{month_str} {day}, {year}"

    try:
        return datetime.strptime(date_str, "%b %d, %Y")
    except ValueError:
        return None

# ----------------------------
# 🚀 Rename + Move PDFs
# ----------------------------
def organize_paychecks():
    """
    Organizes paycheck PDF files by:
    - Renaming each file to YYYY_MM_DD.pdf
    - Creating subdirectories for year and month (e.g. 2025/April/)
    - Moving each file into its appropriate folder
    """
    # Create the target Paychecks folder if it doesn't exist
    if not os.path.exists(target_root):
        os.makedirs(target_root)

    # Iterate through all files in the source folder
    for filename in os.listdir(source_folder):
        if not filename.lower().endswith(".pdf"):
            continue  # Skip non-PDF files

        full_path = os.path.join(source_folder, filename)
        date = parse_date_from_filename(filename)

        if not date:
            print(f"Skipping unrecognized file: {filename}")
            continue

        # Format the new filename as YYYY_MM_DD.pdf
        new_name = f"{date.year}_{date.month:02d}_{date.day:02d}.pdf"

        # Create subdirectories: year/MonthName (e.g. 2025/April)
        year_folder = os.path.join(target_root, str(date.year))
        month_name = date.strftime("%B")  # Full month name like "April"
        month_folder = os.path.join(year_folder, month_name)
        os.makedirs(month_folder, exist_ok=True)

        # Move the file to its new location with the new name
        target_path = os.path.join(month_folder, new_name)
        shutil.move(full_path, target_path)

        print(f"Moved: {filename} → {target_path}")

    print("✅ All paychecks organized by year and month name.")

# ----------------------------
# ▶️ Run
# ----------------------------
if __name__ == "__main__":
    organize_paychecks()
