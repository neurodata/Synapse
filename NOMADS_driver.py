import sys
from NOMADS_pipeline import pipeline
from NOMADS_io import load_file, dump_file

if __name__ == '__main__':
    input_filepath = str(sys.argv[1])
    output_filepath = str(sys.argv[2])

    inpit_data = None
    try:
        input_data = load_file(input_filepath)
    except:
        print('ERROR in load_file: Is your filepath valid?')
        raise

    output_data = pipeline(input_data)
    dump_file(output_filepath, output_data)
