import os, sys
import pandas as pd
import hashlib

VALID_HASH_TYPES = ["sha256", "sha1", "md5"]


def hash_csv(csv_path, hash_method):
    if csv_path == "":
        raise Exception("empty csv path")
    if not os.path.exists(csv_path):
        raise Exception("path does not exist")

    df = pd.read_csv(csv_path, encoding="ISO-8859-1", on_bad_lines="skip")
    first_header = list(df.columns)[0]

    # hashing the first column
    if hash_method == "sha256":
        df[first_header] = df[first_header].apply(
            lambda x: hashlib.sha256(str(x).encode("utf-8")).hexdigest()
        )
    elif hash_method == "sha1":
        df[first_header] = df[first_header].apply(
            lambda x: hashlib.sha1(str(x).encode("utf-8")).hexdigest()
        )
    elif hash_method == "md5":
        df[first_header] = df[first_header].apply(
            lambda x: hashlib.md5(str(x).encode("utf-8")).hexdigest()
        )

    dir_name = os.path.dirname(csv_path)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    _, tail = os.path.split(csv_path)
    file_name, file_extension = os.path.splitext(tail)

    save_file = f"{dir_name}/{file_name}_hashed{file_extension}"

    # writing the new CSV output
    df.to_csv(save_file, index=False)
    return save_file


def main():
    csv_path = sys.argv[1]
    hash_type = sys.argv[2]

    if not os.path.exists(csv_path):
        print("Bad CSV path \n")
        return 1

    if not hash_type in VALID_HASH_TYPES:
        print("Bad hash type \n")
        return 1
    saved_file = hash_csv(csv_path, hash_type)

    print(f"File saved to: {saved_file}")
    return 0


if __name__ == "__main__":
    main()
