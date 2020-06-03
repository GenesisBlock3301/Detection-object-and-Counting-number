import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-n","--name",required=True,help="name of the user")
args = vars(ap.parse_args())
print(f"Hi there {args['name']},it's nice to meet you!")
# >python command_line_argument.py --help
