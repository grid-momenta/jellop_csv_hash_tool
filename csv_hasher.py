import hashlib
import os
import sys

import pandas as pd

VALID_HASH_TYPES = ["sha256", "sha1", "md5"]


def hash_csv(csv_path, hash_method):
    if csv_path == "":
        raise Exception("empty csv path")
    if not os.path.exists(csv_path):
        raise Exception("path does not exist")

    col_names = ["IDs", "Email", "Country", "State", "City", "Full name", "G", "H", "I", "J"]

    df = pd.read_csv(csv_path, encoding="ISO-8859-1", names=col_names, engine="python")

    # hashing the first column
    if hash_method == "sha256":
        df["IDs"] = df["IDs"].apply(
            lambda x: hashlib.sha256(str(x).encode("utf-8")).hexdigest()
        )
    elif hash_method == "sha1":
        df["IDs"] = df["IDs"].apply(
            lambda x: hashlib.sha1(str(x).encode("utf-8")).hexdigest()
        )
    elif hash_method == "md5":
        df["IDs"] = df["IDs"].apply(
            lambda x: hashlib.md5(str(x).encode("utf-8")).hexdigest()
        )

    dir_name = os.path.dirname(csv_path)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    _, tail = os.path.split(csv_path)
    file_name, file_extension = os.path.splitext(tail)

    save_file = f"{dir_name}/{file_name}_hashed{file_extension}"

    # writing the new CSV output
    df.to_csv(save_file, columns=["IDs", "Email", "Country", "State", "City", "Full name"], index=False)
    return save_file


def main():
    csv_path = sys.argv[1]
    hash_type = sys.argv[2]

    if not os.path.exists(csv_path):
        print("Bad CSV path \n")
        return 1

    if hash_type not in VALID_HASH_TYPES:
        print("Bad hash type \n")
        return 1
    saved_file = hash_csv(csv_path, hash_type)

    print(f"File saved to: {saved_file}")
    return 0


if __name__ == "__main__":
    main()
