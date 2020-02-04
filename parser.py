from argparse import ArgumentParser


def parser():
    # Create ArgumentParser object
    parser = ArgumentParser(description="year")
    # Add argument
    parser.add_argument("year",type="check")
    parser.add_argument("name", nargs="+")
    
    # Retrieve Arguments
    args = parser.parse_args()
    print(args)
    # Accessing different variables in args
    year = args.year
    first_name, last_name = args.name

    
    return year, first_name, last_name
def check (x):
    if 2012<=x<=2018:
        return int (x)
    else:
        raise ValueError