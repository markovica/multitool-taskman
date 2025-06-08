#from apps.components.base import BaseComponent
from .base_component import BaseComponent

class ReportAggregator(BaseComponent):
    description = "Report aggregator. Takes multiple inputs."

    input_type = "list|dict"
    output_type = "string"

    input_spec = {
        "inputs": "List or dictionary of worker outputs to aggregate"
    }
    output_spec = {
        "report": "Aggregated data"
    }

    def run(self):
        report_lines = []
        if isinstance(self.input_data, dict):
            for name, data in self.input_data.items():
                report_lines.append(f"\n## Result from {name}")
                report_lines.append(str(data))
        elif isinstance(self.input_data, list):
                for i, item in enumerate(self.input_data):
                    report_lines.append(f"\n## Input {i+1}")
                    report_lines.append(str(item))
        else:
             report_lines.append("Unsupported input format")
        return "\n".join(report_lines)