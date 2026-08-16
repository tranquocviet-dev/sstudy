import pytest
from message_manager import messages, get_sender, get_recipient, get_subject, get_content

@pytest.fixture
def stock_messages():
	return messages

def test_get_sender(stock_messages):
	assert get_sender(1) == "A.Tutor@grandwich.ac.uk"
	assert get_sender(5) == "A.Student@grandwich.ac.uk"
	assert get_sender("four") == None
	assert get_sender(0) == None
	assert get_sender(10) == None

def test_get_subject(stock_messages):
	assert get_subject(3) == "Coffee"
	assert get_subject(4) == "Exam"
	assert get_subject("four") == None
	assert get_subject(0) == None
	assert get_subject(100) == None
