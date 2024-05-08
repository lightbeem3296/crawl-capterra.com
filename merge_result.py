import json
import os
import sqlite3
from pathlib import Path

from slugify import slugify

from liblogger import log_err, log_inf, log_warn

CUR_DIR = str(Path(__file__).parent.absolute())
# OUTPUT_DIR = os.path.join(CUR_DIR, "output")
OUTPUT_DIR = r"C:\Users\alpha\Desktop\capterra.com\output"

from category_list import CATEGORY_LIST, SUBCATEGORY_LIST


def ensure_utf8(text: str) -> str:
    if text == None:
        return None
    else:
        return text.encode(
            encoding="utf-8",
            errors="xmlcharrefreplace",
        ).decode(
            encoding="utf-8",
            errors="ignore",
        )


def main():
    create_tables_query = """
    CREATE TABLE IF NOT EXISTS `Category` (
        `Category_ID` integer primary key NOT NULL UNIQUE,
        `Category_Name` TEXT,
        `Parent_Category_Name` TEXT,
        `Slug` TEXT
    );
    CREATE TABLE IF NOT EXISTS `Product` (
        `Product_ID` integer primary key NOT NULL UNIQUE,
        `Product_Name` TEXT,
        `Slug` TEXT,
        `Description` TEXT,
        `Rating_Score` REAL,
        `Reviews_Count` INTEGER,
        `URL` TEXT,
        `Recommendation_Percentage` REAL
    );
    CREATE TABLE IF NOT EXISTS `ProductCategory` (
        `id` integer primary key NOT NULL UNIQUE,
        `Product_ID` INTEGER NOT NULL,
        `Category_ID` INTEGER NOT NULL,
    FOREIGN KEY(`Product_ID`) REFERENCES `Product`(`Product_ID`),
    FOREIGN KEY(`Category_ID`) REFERENCES `Category`(`Category_ID`)
    );
    CREATE TABLE IF NOT EXISTS `Review` (
        `Review_ID` integer primary key NOT NULL UNIQUE,
        `User` TEXT,
        `Content` TEXT,
        `Rating` REAL,
        `Product_ID` INTEGER,
    FOREIGN KEY(`Product_ID`) REFERENCES `Product`(`Product_ID`)
    );
    """

    # initialize memory database
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    # create tables
    cur.executescript(create_tables_query)

    # load category list
    log_inf("load category list ...")
    category_list = []
    for category_str in CATEGORY_LIST:
        category_name = category_str.split(">", 1)[0].split(".", 1)[1].strip()
        category_link = category_str.split(">", 1)[1].strip()
        category_list.append(
            {
                "name": category_name,
                "url": category_link,
            }
        )

    # load category tree
    log_inf("load category tree ...")
    category_tree = {}
    for subcategory_str in SUBCATEGORY_LIST:
        words = subcategory_str.split(">")
        parent = words[1].strip()
        category_name = words[2].strip()
        category_link = words[3].strip()
        if parent in category_tree:
            category_tree[parent].append(
                {
                    "name": category_name,
                    "url": category_link,
                }
            )
        else:
            category_tree[parent] = {}
            category_tree[parent] = [
                {
                    "name": category_name,
                    "url": category_link,
                }
            ]

    # fill category table
    log_inf("fill category table ...")
    for category in category_list:
        category_name = category["name"]
        category_link = category["url"]
        parent_category_name = None
        for key in category_tree:
            for subcategory in category_tree[key]:
                if subcategory["url"] == category["url"]:
                    parent_category_name = key
                    break
            if parent_category_name != None:
                break
        slug = slugify(f"{category_name}")
        cur.execute(
            "INSERT INTO Category(Category_Name, Parent_Category_Name, Slug) VALUES (?, ?, ?)",
            (
                ensure_utf8(category_name),
                ensure_utf8(parent_category_name),
                ensure_utf8(slug),
            ),
        )
    conn.commit()

    # loop all products
    log_inf("loop all products ...")
    category_dir_list = os.listdir(OUTPUT_DIR)
    for category_dir_name in category_dir_list:
        category_dir_path = os.path.join(OUTPUT_DIR, category_dir_name)
        if not os.path.isdir(category_dir_path):
            continue

        category_name = category_dir_name.split(".", 1)[1].strip()
        category_id = cur.execute(
            "SELECT Category_ID FROM Category WHERE Category_Name = ?", (category_name,)
        ).fetchone()[0]

        page_dir_list = os.listdir(category_dir_path)
        for page_dir_name in page_dir_list:
            page_dir_path = os.path.join(category_dir_path, page_dir_name)
            if not os.path.isdir(page_dir_path):
                continue

            log_inf(f"category: {category_name}, page: {page_dir_name} ...")

            product_file_list = os.listdir(page_dir_path)
            for product_file_name in product_file_list:
                product_file_path = os.path.join(page_dir_path, product_file_name)
                if not os.path.isfile(product_file_path):
                    continue
                if not product_file_name.endswith(".json"):
                    continue

                with open(product_file_path, "r") as f:
                    product = json.load(f)

                    # check the product is new
                    row = cur.execute(
                        "SELECT Product_ID FROM Product WHERE Product_Name=? AND Description=? AND Rating_Score=?",
                        (
                            product["name"],
                            product["desc"],
                            product["rating_score"],
                        ),
                    ).fetchone()

                    if row != None:
                        product_id = row[0]
                        log_warn(f"duplicated product")
                        if (
                            cur.execute(
                                "SELECT * FROM ProductCategory WHERE Product_ID=? AND Category_ID =?",
                                (
                                    product_id,
                                    category_id,
                                ),
                            ).fetchone()
                            == None
                        ):
                            cur.execute(
                                "INSERT INTO ProductCategory(Product_ID, Category_ID) VALUES(?, ?)",
                                (
                                    product_id,
                                    category_id,
                                ),
                            )
                        else:
                            log_warn("duplicated product & category")
                    else:
                        cur.execute(
                            "INSERT INTO Product(Product_Name, Slug, Description, Rating_Score, Reviews_Count, URL, Recommendation_Percentage) VALUES(?, ?, ?, ?, ?, ?, ?)",
                            (
                                ensure_utf8(product["name"]),
                                slugify(f'{ensure_utf8(product["name"])}'),
                                ensure_utf8(product["desc"]),
                                product["rating_score"],
                                product["review_count"],
                                f'https://www.capterra.com{product["url"]}',
                                product["recommend"],
                            ),
                        )
                        product_id = cur.lastrowid
                        for review in product["reviews"]:
                            cur.execute(
                                "INSERT INTO Review(User, Content, Rating, Product_ID) VALUES(?, ?, ?, ?)",
                                (
                                    ensure_utf8(review["user"]),
                                    ensure_utf8(
                                        f'Overall: {review["overall"]}\nPros: {review["pros"]}\n: Cons: {review["cons"]}'
                                    ),
                                    review["rating"],
                                    product_id,
                                ),
                            )

                        # add product_category
                        cur.execute(
                            "INSERT INTO ProductCategory(Product_ID, Category_ID) VALUES(?, ?)",
                            (
                                product_id,
                                category_id,
                            ),
                        )

                conn.commit()
    conn.commit()

    # save into file
    out_db_path = os.path.join(OUTPUT_DIR, "result.sqlite3")
    if os.path.isfile(out_db_path):
        log_inf("old file exists. removing ...")
        os.remove(out_db_path)

    cur.execute(f"VACUUM INTO '{out_db_path}'")

    conn.close()


def test():
    print(ensure_utf8("Kyrylo \ud83d."))


if __name__ == "__main__":
    main()
    # test()
    input("Press ENTER to exit.")
