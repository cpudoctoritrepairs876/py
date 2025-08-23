import argparse

parser = argparse.ArgumentParser(
    description="Provides a personal greetings."
)
    
parser.add_argument(
    "-n", "--name", metavar="name", 
    required=True, help="The name of the person to greet."
)    
    
args = parser.parse_args()    

msg = f"hello{args.name}!"
print(msg)