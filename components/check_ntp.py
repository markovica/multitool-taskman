#from apps.components.base import BaseComponent
from .base_component import BaseComponent


# MINIMAL COMPONENT EXAMPLE
# This component is not doing anything useful
# It is here just to demonstrate how a Class should be organized in order to be loaded 

class NTPChecker(BaseComponent):
    description = "Component that checks NTP - this is a dummy component."
    input_type = "file_list"
    output_type = "list"



    #def __init__(self, files):
    #    self.files = files

    def check(self):
        output = []
        for f in self.files:
            if "ntp" in f:
                try:
                    with open(f, "r") as fh:
                        lines = fh.readlines()
                        for line in lines:
                            output.append(f"NTP Server found in {f}: {line.strip}")
                except Exception as e:
                    output.append(f"Error reading {f}: {e}")
        return "\n".join(output) if output else "No NTP config found."