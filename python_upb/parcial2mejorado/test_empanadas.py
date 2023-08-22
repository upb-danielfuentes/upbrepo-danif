import pytest
from empanadas import EmpanadaShop

@pytest.fixture
def empanada_shop():
    return EmpanadaShop()

def test_calculate_total_cost(empanada_shop, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2\nCarne\n3\nPollo\n")

    total_cost = empanada_shop.calculate_total_cost(2)
    assert total_cost == 13.0  # 2*2.5 + 3*2.0

def test_display_payment_info_nequi(capsys, empanada_shop, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Nequi\n")
    empanada_shop.show_payment_options()
    captured = capsys.readouterr()
    assert "Consigne a este número: 3013366588" in captured.out

if __name__ == "__main__":
    pytest.main()
