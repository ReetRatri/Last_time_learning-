import pytest
from django.urls import reverse
from concurrent.futures import ThreadPoolExecutor

@pytest.mark.django_db  # Allows database access in tests
def test_concurrent_form_submissions(client):
    url = reverse('form')  # Use the correct URL name

    # Sample data for different users
    form_data_list = [
        {"name": "Alice", "email": "alice@example.com", "password": "pass123", "gender": "female"},
        {"name": "Bob", "email": "bob@example.com", "password": "pass456", "gender": "male"},
        {"name": "Charlie", "email": "charlie@example.com", "password": "pass789", "gender": "male"},
    ]

    def submit_form(data):
        """Function to send a form submission."""
        response = client.post(url, data)
        return response.status_code

    # Simulating concurrent requests
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(submit_form, form_data_list))

    # Ensure all requests return 302 (redirect after form submission)
    assert all(status == 302 for status in results)
