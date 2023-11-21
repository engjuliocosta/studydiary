"""
    Class Tracker: able to track time
    Usage:
        API Tracker: able to track time
        It's going to interage with system and intenet
        to return the time in the format HH:MM:SS, to register the content
        on the CSV file
"""
from time import time

class Tracker:
    """Class API Tracker: able to track time
       It's going to interage with system
    """

    def __init__(self, content: str = ''):
        self.content = content
        self.start_time = None
        self.end_time = None

    def start(self):
        """
        Start the timer by setting the start time.
        """
        self.start_time = time()

    def stop(self):
        """
        Records the end time of the process.

        This method sets the `end_time` attribute of the current instance with the current time.
        """
        self.end_time = time()

    def get_time(self):
        """
        Get the current time.
        Returns:
            The current time in the format HH:MM:SS.
        """
        return self.end_time - self.start_time

    def get_content(self):
        """
        Get the content of the tracker.
        Returns:
            The content of the tracker.
        """
        self.content: str
        return self.content

    def register_content(self):
        """
        Register the content of the tracker.
        Returns:
            The content of the tracker.
        """
        registered_content = {"Conteúdo": self.content}
        return registered_content


    def register_subcontent(self):
        """
        Register the subcontent of the tracker.
        Returns:
            The subcontent of the tracker.
        """
        subcontents = self.content
        registered_subcontents = {subcontents: {"Subconteúdo": "subcontent",}}
        
        return registered_subcontents



