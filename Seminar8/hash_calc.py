from os.path import join, abspath, dirname
import io, hashlib





def export_hash(in_file_name: str, out_file_name: str):
    with open(in_file_name, "rb") as f:
        digest = hashlib.file_digest(f, "sha256")
    hash_sum = digest.hexdigest()
    MAIN_DIR = abspath(dirname(__file__))
    full_name = join(MAIN_DIR, out_file_name + '.txt')
    with open(full_name, mode='a', encoding='utf-8') as file:
        file.write(f"Файл: {in_file_name} *** Хэш: {hash_sum}\n")


export_hash("phones11.csv","sha256_sum")
