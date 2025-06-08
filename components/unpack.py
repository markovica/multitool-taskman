# MINIMAL COMPONENT EXAMPLE
# This component is not doing anything useful
# It is here just to demonstrate how a Class should be organized in order to be loaded 

import os
import tarfile

from sqlalchemy import extract
from urllib3 import Retry
#from apps.components.base import BaseComponent
from .base_component import BaseComponent


class Unpacker(BaseComponent):
    description = "Component that upacks tar.gz archives"
    input_type = "file_url"
    output_type = "file_list"
    '''
    def __init__(self, input_archive="logs.tar.gz", output_dir="extracted"):
        self.input_archive = input_archive
        self.output_dir = output_dir

    def process(self):
        extracted_files = []
        if not tarfile.is_tarfile(self.input_archive):
            return f"{self.input_archive} is not a valid tar file."
        with tarfile.open(self.input_archive, "r:gz") as archive:
            archive.extractall(self.output_dir)
            extracted_files = [os.path.join(self.output_dir, name) for name in archive.getnames()]
        return extracted_files
    '''

def run(self):
    archive = self.input_data
    output_dir = self.params.get("output_dir", "extracted")
    os.makedirs(output_dir, exist_ok=True)
    extracted_files = []
    if not tarfile.is_tarfile(archive):
        return []
    with tarfile.open(archive, "r:gz") as tar:
        tar.extractall(output_dir)
        extracted_files = [os.path.join(output_dir, name) for name in tar.getnames()]
        return extracted_files


    