# Standard Libraries
import sys
import traceback

# Custom Modules
from core.pyramid import Pyramid
from utils import file_utils


def stop():
    sys.exit(1)


def main():
    # Create necessary class objects
    pyramid = Pyramid()

    try:
        # Step #1: Load numbers from file
        loaded_numbers = file_utils.load_numbers_from_txt_file(file_path="files/input_16_10000.txt")

        # Step #2: Get medians
        medians = pyramid.get_medians(numbers=loaded_numbers)

        # Step #3: Print needed medians
        median_2015 = medians[2014]
        median_9876 = medians[9875]
        print(f"Median for iteration 2015: {median_2015}")
        print(f"Median for iteration 9876: {median_9876}")
    except KeyboardInterrupt:
        print("[ERROR] Failed: script interrupted by user (CTRL + C)")
        stop()
    except Exception as e:
        print(f"[ERROR] Failed: unexpected exception: {e}")
        traceback.print_exc()  # traceback included


if __name__ == '__main__':
    main()
