import pytest
import numpy as np
from mnogougao import *

@pytest.mark.parametrize("a", np.linspace(-1, 1, 20)  )
def test_kvadrat(a):
    try:
        kvadrat = Kvadrat(a)
        assert kvadrat.obim() == 4*a
        assert kvadrat.povrsina() == a**2
    except ValueError as e:
        assert a < 0


@pytest.mark.parametrize("a, b", [ (a,b) for a in np.linspace(0, 1, 20) for b in (0, 1, 20) ] )
def test_pravougli_trougao(a, b):
    trougao = PravougliTrougao(a, b)
    assert trougao.obim() == a + b + np.sqrt(a**2 + b**2)
    assert trougao.povrsina() == a*b/2






