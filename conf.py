import os

ABS_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABS_PATH)
DRIVER_DIR = os.path.join(BASE_DIR, "driver/chromedriver.exe")
DATA_DIR = os.path.join(BASE_DIR, "data")
SAMPLE_DIR = os.path.join(DATA_DIR, "samples")
SAMPLE_INPUTS = os.path.join(SAMPLE_DIR, "input/downloads")
SAMPLE_OUTPUTS = os.path.join(SAMPLE_DIR, 'output')
JAR_DIR = os.path.join(BASE_DIR, "jars")