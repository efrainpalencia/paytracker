import pyautogui
import time

def download_adp_pdf():
    """
    Automates the download of pay statements from the ADP web portal using pyautogui.

    Assumes:
    - The user has already logged into ADP and navigated to the Pay Statements page.
    - The user has manually clicked "Show More" to expose all statement items.
    - The first pay statement is aligned at a known screen position.

    This script:
    - Clicks each pay statement one by one
    - Clicks the 'Download PDF' button
    - Presses ESC to close the preview
    - Scrolls just enough to bring the next item into position
    """

    # ----------------------------
    # ⚙️ CONFIGURATION
    # ----------------------------

    first_item_pos = (633, 731)        # (X, Y) screen coordinates of the first pay statement item
    download_button_pos = (1623, 590)  # (X, Y) position of the "Download PDF" button
    num_items = 159                    # Total number of pay statements to process

    scroll_steps = 3                   # Number of small scrolls after each item
    scroll_per_step = -39             # Scroll distance per step (negative scrolls down)
    pause_between = 2                 # Seconds to wait between major actions

    # ----------------------------
    # 🚀 MAIN LOOP
    # ----------------------------

    print("You have 5 seconds to focus Edge with ADP open...")
    time.sleep(5)

    for i in range(num_items):
        print(f"[{i+1}/{num_items}] Clicking pay statement at: {first_item_pos}")

        # Click the current item
        pyautogui.moveTo(first_item_pos[0], first_item_pos[1], duration=0.3)
        pyautogui.click()
        time.sleep(pause_between + 1)

        # Click the "Download PDF" button
        print("Clicking 'Download PDF' button...")
        pyautogui.moveTo(download_button_pos[0], download_button_pos[1], duration=0.3)
        pyautogui.click()
        time.sleep(pause_between + 3)

        # Close the PDF viewer (if applicable)
        pyautogui.press("esc")
        time.sleep(1)

        # Scroll down in small increments to bring the next item into place
        pyautogui.moveTo(first_item_pos[0], first_item_pos[1])  # Ensure cursor is in scrollable area
        for _ in range(scroll_steps):
            pyautogui.scroll(scroll_per_step)
            time.sleep(0.3)

        # Reposition the mouse and click to focus the new item (helps with flaky UI behavior)
        pyautogui.moveTo(first_item_pos[0], first_item_pos[1], duration=0.3)
        pyautogui.click()
        time.sleep(0.3)

    print("✅ Done! All pay statements clicked + downloaded.")
