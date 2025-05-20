import os
import time
import CustomWebDriverManager

from dotenv import load_dotenv
load_dotenv()

my_url = os.getenv("ADP_URL")
download_dir = os.getenv("DOWNLOAD_DIR")
browser = os.getenv("BROWSER")

def main():

    driver = CustomWebDriverManager.CustomWebDriverManager(my_url, download_dir, browser).create_driver()
    print("Done")


if __name__ == "__main__":
    main()
