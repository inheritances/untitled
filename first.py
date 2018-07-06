import os
import argparse

def main(database: str,url:str):
    print("We are db " + database)
    print("the URL is " + url)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db","--database",help="SqlLite File Name")
    parser.add_argument("-i","--inpu",help="File Containing urls to read")
    args = parser.parse_args()
    database_file = args.database
    input_file = args.inpu
    main(database = database_file,url=input_file)