import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_agente1_get(client):
    response = client.get('/agente1')
    assert response.status_code == 200
    assert 'Criação de ideias de conteúdo' in response.get_data(as_text=True)
