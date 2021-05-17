# FUNCTION "run" IS RUN A SPECIFIC PYTHON PROGRAM WITH IN A SCRIPT

def run(runfile):
  with open(runfile, "r") as rnf:
    exec(rnf.read())

# BY SREEKUMAR HARIDAS ON 17/05/2021