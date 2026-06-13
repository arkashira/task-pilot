import pytest
from src.axentx_product.chain_playbook import ChainPlaybook
from src.axentx_product.portfolio import Portfolio
from src.axentx_product.product import Product

def test_chain_playbook():
    chain_playbook = ChainPlaybook()
    assert chain_playbook.techniques == 18
    assert chain_playbook.outcomes == 6
    assert chain_playbook.go == 4
    assert chain_playbook.no_go == 0
    assert chain_playbook.get_winning_strateg() == "winning strategy"

def test_portfolio():
    portfolio = Portfolio()
    product = Product("Test Product")
    portfolio.add_product(product)
    assert len(portfolio.get_products()) == 1
    assert portfolio.get_products()[0].name == "Test Product"
