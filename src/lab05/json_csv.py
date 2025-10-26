def json_to_csv(json_path: str, csv_path: str):
    from pathlib import Path
    import json
    import csv
    if Path(json_path).exists():
        if json_path[-5:] == ".json" and csv_path[-4:] == ".csv":
            f = open(json_path, "r", encoding="utf-8")
            st = f.read()
            f.close()
            if len(st) == 0:
                raise ValueError
            else:
                with open(json_path, "r", encoding="utf-8") as fj:
                    data = json.load(fj)
                x = data[0].keys() # Сохраняем изначальный порядок колонок
                with open(csv_path, "w", newline='', encoding="utf-8") as fc:
                    writer = csv.DictWriter(fc, fieldnames=x, extrasaction="raise")
                    writer.writeheader()
                    writer.writerows(data)


        else:
            raise ValueError
    else:
        raise FileNotFoundError
    
a = json_to_csv("././data/samples/people.json", "././data/out/people.csv")

# data = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}]
# path = Path("././data/out/people.json")
# with open(path, "w", encoding="utf-8") as fj:
#     json.dump(data, fj,  ensure_ascii=False, indent=2)