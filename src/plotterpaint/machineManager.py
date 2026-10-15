from gscrib import GCodeBuilder

g = GCodeBuilder(output="output.gcode")

g.set_axis(x=0, y=0, z=0)     # Set start position
g.rapid(z=5)                  # Move Z axis up quickly
g.rapid(x=10, y=10)           # Move to X=10, Y=10
g.tool_on("clockwise", 1000)  # Turn on the tool at 1000 RPM
g.move(x=20, y=20, F=1500)    # Move to X=20, Y=20 at feed rate 1500
g.tool_off()                  # Turn off the tool
g.teardown()                  # Finalize and save the file
