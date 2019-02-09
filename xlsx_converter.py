import argparse
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description='Xlsx converter')
    parser.add_argument('file', type=str, 
        help='provide xlsx file name')
    parser.add_argument('sheet', type=str, 
        help='provide xlsx sheet name in file')
    parser.add_argument('index', type=str, 
        help='provide xlsx index column in sheet')
    parser.add_argument('--output', type=str, default='json', nargs='+',
        help='What need output format? [csv, json]')

    args = parser.parse_args()

    if 'json' in args.output :
        with open('df.json', 'w', encoding='utf-8') as file:
            df = pd.read_excel(args.file, sheet_name=args.sheet)
            print(df)
            df.to_json(file, force_ascii=False, orient='records')

    if 'csv' in args.output :
        with open('df.csv', 'w', encoding='utf-8') as file:
            df = pd.read_excel(args.file, sheet_name=args.sheet, index_col=args.index)
            print(df)
            df.to_csv(file)

if __name__=="__main__":
    main()