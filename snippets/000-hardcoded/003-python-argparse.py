import argparse

def parse_arguments():
    """Parse command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='count', default=0,
                        help="Increases log verbosity for each occurrence")
    parser.add_argument('--src-csv-file', required=True,
                        help="Source CSV file exported from CSV")
    return parser.parse_args()


# --- MAIN ---
if __name__ == '__main__':
    args = parse_arguments()
    src_file = args.src_csv_file
