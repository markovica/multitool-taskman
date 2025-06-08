from ast import pattern
from .base_component import BaseComponent

import re


class DdnsDenyChecker(BaseComponent):
    description = "Component that checks syslog for DDNS deny. Can be used as simple template for developing other regex based searches"

    input_type = "file_list"
    output_type = "list"
    

    input_spec = {
        "file_list": "List of files to scan for 'deny' in syslog"
    }
    output_spec = {
        "matches": "List of matching lines with context"
    }

    def run(self):
        matches = []
        pattern = re.compile(r"deny\s+updates")

        for file in self.input_data:
            if "syslog" not in file:
                continue
            try:
                with open(file, "r") as f:
                    for line in f:
                        if pattern.search(line):
                            matches.append({"file": file, "line": line.strip()}) 
            except Exception as e:
                matches.append({"files": file, "error": str(e)})
        return matches

            

