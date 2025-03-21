# Main ETL script placeholder
from etl.extract import fetch_data
from etl.transform import transform_data
from etl.load_sqlserver import load_to_sqlserver

if __name__ == "__main__":
    fetch_data(pages=3)
    transform_data()
    load_to_sqlserver()
