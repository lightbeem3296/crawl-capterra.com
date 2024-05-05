import json
import os
import traceback
from pathlib import Path

from slugify import slugify

from liblogger import log_err, log_inf

CUR_DIR = str(Path(__file__).parent.absolute())
OUTPUT_DIR = os.path.join(CUR_DIR, "output")


def main():
    damaged_file_count = 0

    category_dir_list = os.listdir(OUTPUT_DIR)
    for category_dir_name in category_dir_list:
        category_dir_path = os.path.join(OUTPUT_DIR, category_dir_name)
        if not os.path.isdir(category_dir_path):
            continue

        category_done_path = os.path.join(category_dir_path, "done")

        page_dir_list = os.listdir(category_dir_path)
        for page_dir_name in page_dir_list:
            page_dir_path = os.path.join(category_dir_path, page_dir_name)
            if not os.path.isdir(page_dir_path):
                continue

            log_inf(f"{category_dir_name} > {page_dir_name} ...")

            page_done_path = os.path.join(page_dir_path, "done")

            product_file_list = os.listdir(page_dir_path)
            for product_file_name in product_file_list:
                product_file_path = os.path.join(page_dir_path, product_file_name)
                if not os.path.isfile(product_file_path):
                    continue

                if not product_file_name.endswith(".json"):
                    continue

                is_valid = False
                with open(product_file_path, "r") as f:
                    try:
                        json.load(f)
                        is_valid = True
                    except:
                        traceback.print_exc()

                if not is_valid:
                    log_err(f"damaged: {category_dir_name} / {page_dir_name} / {product_file_name}")
                    damaged_file_count += 1
                    if os.path.isfile(product_file_path):
                        os.remove(product_file_path)
                    if os.path.isfile(page_done_path):
                        os.remove(page_done_path)
                    if os.path.isfile(category_done_path):
                        os.remove(category_done_path)
    if damaged_file_count == 0:
        log_inf("All files are valid.")
    else:
        log_err(f"{damaged_file_count} files are damaged. Do scraping again.")
        

if __name__ == "__main__":
    main()
    input("Press ENTER to exit.")
