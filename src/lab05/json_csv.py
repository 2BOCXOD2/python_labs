def json_to_csv(json_path: str, csv_path: str):
    from pathlib import Path
    if Path(json_path).exists():
        if json_path[-5:] == ".json":
            f = open(json_path, "r", encoding="utf-8")
            st = f.read()
            f.close()
            if len(st) == 0:
                raise ValueError
            else:
                pass

        else:
            raise ValueError
    else:
        raise FileNotFoundError
    
a = json_to_csv("././data/samples/people.json", "123")