"""
Tests for orders manager
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

import pytest
from store_manager import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    result = client.get('/health-checks')
    assert result.status_code == 200
    assert result.get_json() == {'status':'ok'}

def test_stock_flow(client):
    print(client)
    # - Créez un article (`POST /products`)
    # - Ajoutez 5 unités au stock de cet article (`POST /products_stocks`)
    # - Vérifiez le stock, votre article devra avoir 5 unités dans le stock (`GET /stocks/:id`)
    # - Faites une commande de l'article que vous avez créé, 2 unités (`POST /orders`)
    # - Vérifiez le stock encore une fois (`GET /stocks/:id`)
    assert "Le test n'est pas encore là" == 1