import sys
import os
import pytest
from app import app, get_bot_response

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page():
    """Test that the home page loads correctly"""
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'ChatBot AI' in response.data
        assert b'preguntas y respuestas' in response.data

def test_health_endpoint():
    """Test that the health endpoint returns correct data"""
    with app.test_client() as client:
        response = client.get('/health')
        assert response.status_code == 200
        data = response.get_json()
        assert data['status'] == 'healthy'
        assert data['service'] == 'andres-flask-app'
        assert data['version'] == '1.0.5'

def test_saludo_endpoint():
    """Test that the saludo endpoint works with a name"""
    with app.test_client() as client:
        response = client.get('/saludo/Andres')
        assert response.status_code == 200
        assert b'Hola Andres!' in response.data
        assert b'puglla.byronrm.com' in response.data

def test_ask_endpoint_success():
    """Test that the ask endpoint responds to questions"""
    with app.test_client() as client:
        response = client.post('/ask', 
                              json={'question': 'hola'},
                              content_type='application/json')
        assert response.status_code == 200
        data = response.get_json()
        assert 'answer' in data
        assert len(data['answer']) > 0

def test_ask_endpoint_empty_question():
    """Test that the ask endpoint handles empty questions"""
    with app.test_client() as client:
        response = client.post('/ask', 
                              json={'question': ''},
                              content_type='application/json')
        assert response.status_code == 400

def test_ask_endpoint_no_json():
    """Test that the ask endpoint handles missing JSON"""
    with app.test_client() as client:
        response = client.post('/ask', 
                              data='invalid json',
                              content_type='application/json')
        assert response.status_code == 500

def test_bot_response_function():
    """Test that the bot response function works correctly"""
    # Test known responses
    assert 'Hola' in get_bot_response('hola')
    assert 'Hello' in get_bot_response('hello')
    assert 'ayudarte' in get_bot_response('¿cómo estás?')
    
    # Test that it returns some response for any input
    response = get_bot_response('random question')
    assert isinstance(response, str)
    assert len(response) > 0