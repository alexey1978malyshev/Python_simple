from os.path import join, abspath, dirname
import io, hashlib




#функция для вычисления хэша файла:
def export_hash(in_file_name: str, out_file_name: str): # аргументами ф-ции приходят адреса исходного файла и файла с хэш-суммой , куда будем сохранять хэш
    with open(in_file_name, "rb") as f: # открываем исх.файл на чтение в бинарном режиме
        digest = hashlib.file_digest(f, "sha256") #возвращаем объект дайджеста
    hash_sum = digest.hexdigest()#возвращаем строкосый хэш
    MAIN_DIR = abspath(dirname(__file__))
    full_name = join(MAIN_DIR, out_file_name + '.txt')
    with open(full_name, mode='a', encoding='utf-8') as file:
        file.write(f"Файл: {in_file_name} *** Хэш: {hash_sum}\n") #записываем хэш в файл


export_hash("phones11.csv","sha256_sum")
