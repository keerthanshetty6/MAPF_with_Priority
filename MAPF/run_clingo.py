import subprocess

# Run clingo with the pathfinding model
for i in range(5,10):
    command = ["clingo", "priority.lp","test-instance.lp","-c lasttime=n"]
    result = subprocess.run(command, capture_output=True, text=True)

    # Get the clingo output (stdout)
    output = result.stdout
    print(output)

    # Find all lines containing 'path_length' and parse them
    path_lengths = []
    for line in output.splitlines():
        if "Optimization" in line:
            # Parse path_length(Agent, Length)
            parts = line.split(":")
            print(parts)