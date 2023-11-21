import time

import pytest
from timer.core.tracker import Tracker


class TestTraker:
    """
    Test class for the Tracker class.
    """
    def test_start(self):
        """
        Test the start method of the Tracker class.
        """
        tracker = Tracker()
        tracker.start()

        # Assert that the start time is set
        assert tracker.start_time is not None

    def test_stop(self):
        """
        Test the stop method of the Tracker class.
        """
        tracker = Tracker()
        tracker.stop()
        assert tracker.end_time is not None

    def test_content(self):
        """
        Test the content property of the Tracker class.
        """
        tracker = Tracker(content="Test content")
        assert tracker.content == "Test content"

    def test_get_time(self):
        """
        Test the get_time method of the Tracker class.
        """
        tracker = Tracker()
        tracker.start()
        tracker.stop()
        assert tracker.get_time() >= 0

    def test_get_time_with_content(self):
        """
        Test the get_time method of the Tracker class with content.
        """
        tracker = Tracker(content="Test content")
        tracker.start()
        tracker.stop()
        assert tracker.get_time() >= 0

    def test_get_time_with_no_content(self):
        """
        Test the get_time method of the Tracker class with no content.
        """
        tracker = Tracker()
        tracker.start()
        time.sleep(1)
        tracker.stop()
        assert tracker.get_time() > 0

    def test_get_time_with_no_start(self):
        """
        Test the get_time method of the Tracker class with no start time.
        """
        tracker = Tracker()
        tracker.stop()
        tracker.start()
        assert tracker.get_time() <= 0

    def test_get_time_with_no_stop(self):
        """
        Test the get_time method of the Tracker class with no stop time.
        """
        tracker = Tracker()
        tracker.start()
        tracker.stop()
        assert tracker.get_time() > 0

    def test_get_content(self):
        """
        Test the get_content method of the Tracker class.
        """
        tracker = Tracker(content="Test content")
        assert tracker.get_content() == "Test content"

    def test_get_content_with_no_content(self):
        """
        Test the get_content method of the Tracker class with no content.
        """
        tracker = Tracker()
        assert tracker.get_content() == ""

    def test_register_content(self):
        """
        Test the register_content method of the Tracker class.
        """
        tracker = Tracker(content="Test content")
        registered_content = {"Conteúdo": tracker.content}
        tracker.register_content()
        assert tracker.register_content() == registered_content

    def test_register_content_with_no_content(self):
        """
        Test the register_content method of the Tracker class with no content.
        """
        tracker = Tracker()
        registered_content = {"Conteúdo": None}
        tracker.register_content()
        assert tracker.register_content() != registered_content

    def test_register_content_with_no_registered_content(self):
        """
        Test the register_content method of the Tracker class with no registered content.
        """
        tracker = Tracker(content="Test content")
        registered_content = {}
        tracker.register_content()
        assert tracker.register_content() != registered_content

    def test_register_subcontent(self):
        """
        Test the register_subcontent method of the Tracker class.
        """
        tracker = Tracker(content="Test content")
        registered_subcontent = {tracker.content: {"Subconteúdo": "subcontent",}}
        tracker.register_subcontent()
        assert tracker.register_subcontent() == registered_subcontent

    def test_register_subcontent_without_subcontent(self):
        """
        Test the register_subcontent method of the Tracker class without subcontent.
        """
        tracker = Tracker(content="Test content")
        registered_subcontent = {"Test content": {None: None,}}
        tracker.register_subcontent()
        assert tracker.register_subcontent() != registered_subcontent

    def test_register_subcontent_without_content(self):
        """
        Test the register_subcontent method of the Tracker class without content.
        """
        tracker = Tracker(content="Test content")
        registered_subcontent = {None: {"Subconteúdo": "subcontent",}}
        tracker.register_subcontent()
        assert tracker.register_subcontent() != registered_subcontent

    def test_register_subcontent_without_content_and_subcontent(self):
        """
        Test the register_subcontent method of the Tracker class withou content and subcontent.
        """
        tracker = Tracker(content="Test content")
        registered_subcontent = {None: {None: None,}}
        tracker.register_subcontent()
        assert tracker.register_subcontent() != registered_subcontent



