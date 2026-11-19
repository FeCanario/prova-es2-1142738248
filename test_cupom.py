from cupom import desconto_valido


def test_percentual_igual_ao_limite_e_aceito():
    percentual = 28

    resultado = desconto_valido(percentual)

    assert resultado is True


def test_percentual_acima_do_limite_e_rejeitado():
    percentual = 29

    resultado = desconto_valido(percentual)

    assert resultado is False


def test_percentual_zero_e_rejeitado():
    percentual = 0

    resultado = desconto_valido(percentual)

    assert resultado is False


def test_percentual_nao_inteiro_e_rejeitado():
    percentual = 27.5

    resultado = desconto_valido(percentual)

    assert resultado is False
