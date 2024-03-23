from sabirac import sabirac

def test_sabirac():
    iSabirac = sabirac(16)
    assert iSabirac.saberi(1, 2) == 3
    assert iSabirac.saberi(1, 6) == 7
    assert iSabirac.saberi(2, 5) == 7
    assert iSabirac.saberi(15, 1) == 0
    

    
    