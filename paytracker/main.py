import os
from adp_gui_automation import download_adp_pdf
from organize_pdfs import organize_paychecks

from dotenv import load_dotenv

load_dotenv()



def main():
    """

    :return:
    """

    execute = organize_paychecks()

    return execute

if __name__ == "__main__":
    main()
