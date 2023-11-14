import requests
from io import StringIO
from pathlib import Path
import os


def page_saver(url, path):
    response = requests.get(url)
    if response.status_code == 200:
        print("response satus: 200")
        f_line = "ADDRESS,TYPE,DATE\n"
        with open(path, 'w') as f:
            for line in StringIO(response.text):
                if not line.startswith("#"):
                    f_line += line
            f.write(f_line)
            if os.path.exists(path):
                print("File is written: " + path)
        # [print(f) for f in os.walk("/usr/local/airflow")]
    else:
        raise Exception(f"Failed to fetch webpage. Status code: {response.status_code}")
