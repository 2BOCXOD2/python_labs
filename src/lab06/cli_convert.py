import argparse
import sys
import os
sys.path.insert(0, os.path.join(sys.path[0], '../lab05'))
import json_csv
import csv_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv", help="Преобразовать .json в .csv")
    p1.add_argument("--input", dest="input", required=True, help="Ссылка на json")
    p1.add_argument("--output", dest="output", required=True, help="Ссылка на csv")

    p2 = sub.add_parser("csv2json", help="Преобразовать .csv в .json")
    p2.add_argument("--input", dest="input", required=True, help="Ссылка на csv")
    p2.add_argument("--output", dest="output", required=True, help="Ссылка на json")

    p3 = sub.add_parser("csv2xlsx", help="Преобразовать .csv в .xlsx")
    p3.add_argument("--input", dest="input", required=True, help="Ссылка на csv")
    p3.add_argument("--output", dest="output", required=True, help="Ссылка на xlsx")

    args = parser.parse_args()

    if args.cmd == "json2csv":
        json_path = args.input # Считали ссылку на читаемый файл
        csv_path = args.output # Считали ссылку для записываемого файла
        otvet = json_csv.json_to_csv(json_path, csv_path) # Загружаем ссылки в функцию и выполняем её

    elif args.cmd == "csv2json":
        csv_path = args.input # Считали ссылку для записываемого файла
        json_path = args.output # Считали ссылку на читаемый файл
        otvet = json_csv.csv_to_json(csv_path, json_path) # Загружаем ссылки в функцию и выполняем её

    elif args.cmd == "csv2xlsx":
        csv_path = args.input # Считали ссылку для записываемого файла
        xlsx_path = args.output # Считали ссылку на читаемый файл
        otvet = csv_xlsx.csv_to_xlsx(csv_path, xlsx_path) # Загружаем ссылки в функцию и выполняем её

d = main()

# python src/lab06/cli_convert.py json2csv --input ././data/samples/people.json --output ././data/out/06json2csv.csv
# python src/lab06/cli_convert.py csv2json --input ././data/samples/people1.csv --output ././data/out/06csv2json.json
# python src/lab06/cli_convert.py csv2xlsx --input ././data/samples/people1.csv --output ././data/out/06csv2xlsx.xlsx