from kubus import hitung_volume_kubus

def test_volume_kubus():
    sisi = 5
    hasil = hitung_volume_kubus(sisi)
    assert hasil == 125  # Volume kubus dengan sisi 5 adalah 5^3 = 125
