import logging
import traceback
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import random
import time

ios_user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"

driver = webdriver.Firefox()
driver.set_window_size(600,1200)

url = "https://onemillioncheckboxes.com"


# region Logger konfigurieren
# Variablen zum Ein- oder Ausschalten des Loggings für Konsole und Datei
ENABLE_CONSOLE_LOGGING = True
ENABLE_FILE_LOGGING = False

MANUAL_START = True


clicked_ids=set()

# region Funktion, die das Logging für Konsole und Datei separat einrichtet
def setup_logging(enable_console_logging, enable_file_logging):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Wenn das Datei-Logging aktiviert ist
    if enable_file_logging:
        file_handler = logging.FileHandler('omcb_checker.log')
        file_handler.setLevel(logging.INFO)
        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
        logging.info("File logging aktiviert.")

    # Wenn das Konsolen-Logging aktiviert ist
    if enable_console_logging:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter('%(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)
        logging.info("Console logging aktiviert.")

    # Wenn beide Logging-Optionen deaktiviert sind
    if not enable_console_logging and not enable_file_logging:
        logging.disable(logging.CRITICAL)

# Rufe die Funktion auf und aktiviere/deaktiviere das Logging je nach den Variablen
setup_logging(ENABLE_CONSOLE_LOGGING, ENABLE_FILE_LOGGING)
# endregion

def close_alert_if_present(driver):
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        logging.info(f"Alert gefunden: {alert_text}")
        alert.dismiss()
        logging.info("Alert geschlossen.")
        return True
    except NoAlertPresentException:
        return False
    except UnexpectedAlertPresentException as e:
        logging.warning(f"Unerwartetes Alert erkannt: {e}")
        return False
    except Exception as e:
        logging.error(f"Fehler beim Schließen des Alerts: {e}")
        return False


def smooth_scroll_into_view(driver, element):
    driver.execute_script("""
        arguments[0].scrollIntoView({ 
            behavior: 'smooth', 
            block: 'start'
        });
    """, element)
    time.sleep(1)


def finding_boxes() -> list:
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    checkbox_ids = [box.get_attribute('id') for box in checkboxes]
    logging.debug(f"Checkbox IDs gefunden: {checkbox_ids}")
    return checkbox_ids

def finding_new_boxes(existing_ids, clicked_ids) -> list:
    all_checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    new_checkbox_ids = [box.get_attribute('id') for box in all_checkboxes if box.get_attribute('id') not in existing_ids and box.get_attribute('id') not in clicked_ids]
    # logging.info(f"Neue Checkbox IDs gefunden: {new_checkbox_ids}")
    return new_checkbox_ids

def click_box_by_id(checkbox_id):
    try:
        box = driver.find_element(By.ID, checkbox_id)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(box))
        if not box.is_selected():
            box.click()
        # logging.info(f"Clicked Box with ID: {checkbox_id}")
        clicked_ids.add(checkbox_id)  # Checkbox-ID zum Set hinzufügen
    except Exception as e:
        logging.error(f"Fehler beim Anklicken der Checkbox mit ID {checkbox_id}: {e}")


def clicking_by_id():
    total_clicks = 0
    measuring_clicks = 0
    scroll_trigger = random.randint(123,186)
    checkbox_ids = finding_boxes()  # Initiales Sammeln der Checkboxen
    logging.info(f"Länge der Liste checkbox_ids: {len(checkbox_ids)}")

    if not checkbox_ids:
        logging.info("Keine weiteren Checkboxen gefunden. Beende das Skript.")

    start_time = time.time()


    while True:
        for i, checkbox_id in enumerate(checkbox_ids):
            if checkbox_id in clicked_ids:
                logging.info(f"Checkbox {checkbox_id} wurde bereits geklickt. Überspringen...")
                continue  # Überspringe, wenn Checkbox bereits geklickt wurde

            logging.debug(f"Versuche Checkbox mit ID: {checkbox_id} zu klicken.")

            try:
                click_box_by_id(checkbox_id)
                time.sleep(random.uniform(.01, .1))  # Zufällige Pause


                elapsed_time = time.time() - start_time
                if elapsed_time >= 60:
                    checkboxes_per_minute = measuring_clicks / (elapsed_time / 60)
                    logging.info(f"Checkboxes pro Minute: {checkboxes_per_minute:.2f}")
                    # Startzeit und Zähler zurücksetzen für die nächste Minute
                    start_time = time.time()
                    measuring_clicks = 0

                # Letzte Checkbox erst klicken, dann Liste aktualisieren
                if i == len(checkbox_ids) - 1:  # Prüfe, ob es die letzte Checkbox ist
                    time.sleep(.2)
                    logging.info(f"{checkbox_id} ist die letzte Checkbox von {len(checkbox_ids)} Checkboxen.")
                    checkbox_ids = finding_new_boxes(checkbox_ids, clicked_ids)  # Liste nach Klick aktualisieren
                    break  # Schleife beenden und mit der neuen Liste fortfahren

            except Exception as e:
                logging.error(f"Fehler beim Klicken der Checkbox {checkbox_id}: {e}")
                continue

            total_clicks += 1
            measuring_clicks += 1

            if total_clicks % scroll_trigger == 0:
                logging.info(f"{total_clicks} Checkboxen angeklickt, jetzt scrollen nach {scroll_trigger}...")
                box = driver.find_element(By.ID, checkbox_id)
                smooth_scroll_into_view(driver,box)
                




def playbutton():
    # Warte auf den 'play alone' Button und klicke darauf
        wait = WebDriverWait(driver, 20)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'play alone')]")))
        button.click()


def find_and_click(nummer, scroll=True):
    input(f"Find Checkbox-{nummer}. Enter to Continue")
    box_nummer = driver.find_element(By.ID, f'checkbox-{nummer}')
    logging.info(f"Checkbox-{nummer} visible: {box_nummer.is_displayed()}, enabled: {box_nummer.is_enabled()}")
    driver.execute_script("return arguments[0].getBoundingClientRect()", box_nummer)
    if scroll:
        logging.info(f"Checkbox-{nummer} wird in Sichtbereich gescrollt")
        driver.execute_script("arguments[0].scrollIntoView(true);", box_nummer)
    input(f"Force Click Checkbox-{nummer} Enter to Continue")
    driver.execute_script("arguments[0].click();", box_nummer)
    logging.info(f"Force Click auf Checkbox-{nummer} ausgeführt.")



def run(driver, url):
    try:
        logging.info("[OMCB] Seite Laden...")
        driver.get(url)

        if MANUAL_START == False:
            input("[OMCB] Automatischer Start ausgewählt. Drücke Enter um fortzufahren.")
            playbutton()
        else:
            input("[OMCB] Drücke Enter, nachdem du den Responsive Design Mode manuell aktiviert hast...")
        
        clicking_by_id()

        # find_and_click(351,False)
        # find_and_click(352,False)

    except Exception as e:
        # Fehler explizit loggen und Stacktrace ausgeben
        logging.error(f"Ein Fehler ist aufgetreten: {str(e)}")
        logging.error(traceback.format_exc())
        
    finally:
        logging.info("Browser wird geschlossen...")
        driver.quit()


if __name__ == "__main__":
    run(driver, url)
