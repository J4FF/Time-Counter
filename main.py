import json
import time

elapsed_time = 0

while True:
    current_time_in_seconds = time.time()
    updated_time_in_seconds = current_time_in_seconds + 3600

    updated_time = time.gmtime(updated_time_in_seconds)

    # Code, der alle 5 Minuten ausgeführt werden soll
    data = {
        "time": time.strftime("%Y-%m-%d %H:%M:%S", updated_time),
        "status": f"Der Raspberry PI lauft nun seit {elapsed_time} Minuten"
    }

    # Schreiben von Daten in eine JSON-Datei
    with open("testt.json", "w") as file:
        json.dump(data, file)

    time.sleep(300)
    elapsed_time += 5
