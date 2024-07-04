import pandas as pd
import os

# https://stackoverflow.com/a/68309347
def head(filename: str, n: int):
    try:
        with open(filename) as f:
            head_lines = [next(f).rstrip() for x in range(n)]
    except StopIteration:
        with open(filename) as f:
            head_lines = f.read().splitlines()
    return head_lines


def detect_delimiter(filename: str, n=2):
    sample_lines = head(filename, n)
    common_delimiters= [',',';','\t',' ','|',':']
    for d in common_delimiters:
        ref = sample_lines[0].count(d)
        if ref > 0:
            if all([ref == sample_lines[i].count(d) for i in range(1,n)]):
                return d
    return ','

def csv_file(file):
    try:
        delimiter = detect_delimiter("files/"+file)
        try:
            df = pd.read_csv("files/"+file, sep=delimiter)
        except:
            df = pd.read_csv("files/"+file, sep=delimiter, encoding="latin-1")
        if "Unnamed: 0" in df:
            df.drop("Unnamed: 0", axis=1, inplace=True)
        response = f"rows: {df.shape[0]}\tcolumns: {df.shape[1]}\n"
        for column in df.columns:
            posible_response = response + "\n" + column + "\n" + str(df[column].describe()) + "\n"
            if len(posible_response) > 4096: break
            response = posible_response
        name = os.path.splitext(os.path.basename("files/"+file))[0]
        df.to_json(f'files/{name}.json')
        return "csv2json", response
    except:
        try:
            df = pd.read_json("files/"+file)
            name = os.path.splitext(os.path.basename("files/"+file))[0]
            df.to_csv(f'files/{name}.csv')
            return "json2csv"
        except:
            return "other"