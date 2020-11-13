#!/usr/bin/env python
# -*- coding: 'UTF-8' -*-

import pytest
import vremenko.vreme
import vremenko.nastavitve as n
import vremenko.poštar

kraji = vremenko.nastavitve.KRAJI_URL.keys()


@pytest.mark.parametrize('kraj', kraji)
def test_vreme_podatki(kraj):
    stran = vremenko.poštar.pridobi_vremenske_podatke(n.KRAJI_URL[kraj])
    podatki = vremenko.vreme.vreme_podatki(stran)
    assert type(podatki.ura) == str
    assert type(podatki.temperatura) == str
    assert type(podatki.relativna_vlaga) == str
    assert podatki.temperatura_enota == "°C"
    assert podatki.relativna_vlaga_enota == "%"
    assert podatki.tlak_enota == "hPa"
    assert podatki.sončno_obsevanje_enota == "W/m2"
    assert podatki.vsota_padavin_enota == "mm"
    assert (podatki.opis_vremena is None) or (
        type(podatki.opis_vremena) == str)
    assert (podatki.tlak is None) or type(podatki.tlak) == str
    assert (podatki.sončno_obsevanje is None) or (
        type(podatki.sončno_obsevanje) == str)
    assert (podatki.vsota_padavin is None) or (
        type(podatki.vsota_padavin) == str)
