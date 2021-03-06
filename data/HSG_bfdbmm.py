
def load_bfdbmm(dbinstance):

    # cgenff/hsg_inte1.txt
    # 15 Mar 2017 commenting out CHARMM since CGenFF succeeds it
    #dbinstance.add_ReactionDatum(citation='bfdbmm', dbse='HSG', rxn=1, method='CHARMM', mode='', basis='na', value= -0.66888)
    #dbinstance.add_ReactionDatum(citation='bfdbmm', dbse='HSG', rxn=2, method='CHARMM', mode='', basis='na', value= -2.20172)
    #dbinstance.add_ReactionDatum(citation='bfdbmm', dbse='HSG', rxn=3, method='CHARMM', mode='', basis='na', value= -0.343247)
    #dbinstance.add_ReactionDatum(citation='bfdbmm', dbse='HSG', rxn=4, method='CHARMM', mode='', basis='na', value=-14.3922)
    #dbinstance.add_ReactionDatum(citation='bfdbmm', dbse='HSG', rxn=5, method='CHARMM', mode='', basis='na', value=-17.2401)
    #dbinstance.add_ReactionDatum(citation='bfdbmm', dbse='HSG', rxn=6, method='CHARMM', mode='', basis='na', value= -2.37916)
    #dbinstance.add_ReactionDatum(citation='bfdbmm', dbse='HSG', rxn=7, method='CHARMM', mode='', basis='na', value= -2.76727)
    #dbinstance.add_ReactionDatum(citation='bfdbmm', dbse='HSG', rxn=8, method='CHARMM', mode='', basis='na', value= -0.468104)
    #dbinstance.add_ReactionDatum(citation='bfdbmm', dbse='HSG', rxn=9, method='CHARMM', mode='', basis='na', value= -5.42821)
    #dbinstance.add_ReactionDatum(citation='bfdbmm', dbse='HSG', rxn=10, method='CHARMM', mode='', basis='na', value= -7.51519)
    #dbinstance.add_ReactionDatum(citation='bfdbmm', dbse='HSG', rxn=11, method='CHARMM', mode='', basis='na', value= -6.71113)
    #dbinstance.add_ReactionDatum(citation='bfdbmm', dbse='HSG', rxn=12, method='CHARMM', mode='', basis='na', value=  1.5176)
    #dbinstance.add_ReactionDatum(citation='bfdbmm', dbse='HSG', rxn=13, method='CHARMM', mode='', basis='na', value= -1.98802)
    #dbinstance.add_ReactionDatum(citation='bfdbmm', dbse='HSG', rxn=14, method='CHARMM', mode='', basis='na', value= -0.941816)
    #dbinstance.add_ReactionDatum(citation='bfdbmm', dbse='HSG', rxn=15, method='CHARMM', mode='', basis='na', value= -0.783307)
    #dbinstance.add_ReactionDatum(citation='bfdbmm', dbse='HSG', rxn=16, method='CHARMM', mode='', basis='na', value= -1.01255)
    #dbinstance.add_ReactionDatum(citation='bfdbmm', dbse='HSG', rxn=17, method='CHARMM', mode='', basis='na', value= -1.17488)
    #dbinstance.add_ReactionDatum(citation='bfdbmm', dbse='HSG', rxn=18, method='CHARMM', mode='', basis='na', value= -0.17763)
    #dbinstance.add_ReactionDatum(citation='bfdbmm', dbse='HSG', rxn=19, method='CHARMM', mode='', basis='na', value= -1.41111)
    #dbinstance.add_ReactionDatum(citation='bfdbmm', dbse='HSG', rxn=20, method='CHARMM', mode='', basis='na', value=  1.84467)

    # cgenff3.0.1/hsg/inte2.txt
    # newly run by Kenno V Feb 2017
    # above is earlier work, last datestamp 23 Sep 2015
    dbinstance.add_ReactionDatum(citation='merz3', dbse='HSG', rxn=1, method='CGENFF', mode='', basis='na', value=  -0.674224)
    dbinstance.add_ReactionDatum(citation='merz3', dbse='HSG', rxn=2, method='CGENFF', mode='', basis='na', value=  -2.18471)
    dbinstance.add_ReactionDatum(citation='merz3', dbse='HSG', rxn=3, method='CGENFF', mode='', basis='na', value=  -0.350405)
    dbinstance.add_ReactionDatum(citation='merz3', dbse='HSG', rxn=4, method='CGENFF', mode='', basis='na', value= -14.2531)
    dbinstance.add_ReactionDatum(citation='merz3', dbse='HSG', rxn=5, method='CGENFF', mode='', basis='na', value= -17.3035)
    dbinstance.add_ReactionDatum(citation='merz3', dbse='HSG', rxn=6, method='CGENFF', mode='', basis='na', value=  -2.3788)
    dbinstance.add_ReactionDatum(citation='merz3', dbse='HSG', rxn=7, method='CGENFF', mode='', basis='na', value=  -3.58571)  # diff
    dbinstance.add_ReactionDatum(citation='merz3', dbse='HSG', rxn=8, method='CGENFF', mode='', basis='na', value=  -0.601533)  # diff
    dbinstance.add_ReactionDatum(citation='merz3', dbse='HSG', rxn=9, method='CGENFF', mode='', basis='na', value=  -4.98325)  # diff
    dbinstance.add_ReactionDatum(citation='merz3', dbse='HSG', rxn=10, method='CGENFF', mode='', basis='na', value= -7.59517)
    dbinstance.add_ReactionDatum(citation='merz3', dbse='HSG', rxn=11, method='CGENFF', mode='', basis='na', value= -6.19271)  # diff
    dbinstance.add_ReactionDatum(citation='merz3', dbse='HSG', rxn=12, method='CGENFF', mode='', basis='na', value=  1.51758)
    dbinstance.add_ReactionDatum(citation='merz3', dbse='HSG', rxn=13, method='CGENFF', mode='', basis='na', value= -1.98962)
    dbinstance.add_ReactionDatum(citation='merz3', dbse='HSG', rxn=14, method='CGENFF', mode='', basis='na', value= -0.956435)
    dbinstance.add_ReactionDatum(citation='merz3', dbse='HSG', rxn=15, method='CGENFF', mode='', basis='na', value= -0.769564)
    dbinstance.add_ReactionDatum(citation='merz3', dbse='HSG', rxn=16, method='CGENFF', mode='', basis='na', value= -1.01149)
    dbinstance.add_ReactionDatum(citation='merz3', dbse='HSG', rxn=17, method='CGENFF', mode='', basis='na', value= -1.17308)
    dbinstance.add_ReactionDatum(citation='merz3', dbse='HSG', rxn=18, method='CGENFF', mode='', basis='na', value= -0.17828)
    dbinstance.add_ReactionDatum(citation='merz3', dbse='HSG', rxn=19, method='CGENFF', mode='', basis='na', value= -1.41111)
    dbinstance.add_ReactionDatum(citation='merz3', dbse='HSG', rxn=20, method='CGENFF', mode='', basis='na', value=  1.84467)
    # rxn=21 missing
    # bfdb.sql methodid 1
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=1,  method='AM1', mode='', basis='na', value= -0.27712845)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=2,  method='AM1', mode='', basis='na', value=  0.40890676)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=3,  method='AM1', mode='', basis='na', value= -0.08288232)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=4,  method='AM1', mode='', basis='na', value= -8.01670637)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=5,  method='AM1', mode='', basis='na', value= -8.29562715)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=6,  method='AM1', mode='', basis='na', value= -3.50011577)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=7,  method='AM1', mode='', basis='na', value= -0.48334816)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=8,  method='AM1', mode='', basis='na', value=  1.46391197)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=9,  method='AM1', mode='', basis='na', value= -2.51060333)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=10, method='AM1', mode='', basis='na', value= -4.14774058)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=11, method='AM1', mode='', basis='na', value= -3.39656303)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=12, method='AM1', mode='', basis='na', value=  0.56592457)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=13, method='AM1', mode='', basis='na', value=  0.3613397)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=14, method='AM1', mode='', basis='na', value=  0.07177427)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=15, method='AM1', mode='', basis='na', value= -0.03990452)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=16, method='AM1', mode='', basis='na', value= -0.04412513)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=17, method='AM1', mode='', basis='na', value=  0.41159197)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=18, method='AM1', mode='', basis='na', value= -0.14396521)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=19, method='AM1', mode='', basis='na', value=  1.00887402)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=20, method='AM1', mode='', basis='na', value=  0.6469583)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=21, method='AM1', mode='', basis='na', value= -7.0049977)
    # bfdb.sql methodid 2
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=1,  method='AM1FS1', mode='', basis='na', value= -2.43)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=2,  method='AM1FS1', mode='', basis='na', value= -2.79)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=3,  method='AM1FS1', mode='', basis='na', value= -3.44)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=4,  method='AM1FS1', mode='', basis='na', value= -10.66)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=5,  method='AM1FS1', mode='', basis='na', value= -11.01)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=6,  method='AM1FS1', mode='', basis='na', value= -5.22)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=7,  method='AM1FS1', mode='', basis='na', value= -3.21)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=8,  method='AM1FS1', mode='', basis='na', value= -0.99)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=9,  method='AM1FS1', mode='', basis='na', value= -4.26)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=10, method='AM1FS1', mode='', basis='na', value= -6.87)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=11, method='AM1FS1', mode='', basis='na', value= -5.56)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=12, method='AM1FS1', mode='', basis='na', value= -1.5)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=13, method='AM1FS1', mode='', basis='na', value= -2.73)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=14, method='AM1FS1', mode='', basis='na', value= -4.16)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=15, method='AM1FS1', mode='', basis='na', value= -2.13)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=16, method='AM1FS1', mode='', basis='na', value= -1.47)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=17, method='AM1FS1', mode='', basis='na', value= -3.15)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=18, method='AM1FS1', mode='', basis='na', value= -2.26)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=19, method='AM1FS1', mode='', basis='na', value= -2.14)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=20, method='AM1FS1', mode='', basis='na', value= -1.99)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=21, method='AM1FS1', mode='', basis='na', value= -8.37)
    # bfdb.sql methodid 16
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=1,  method='GAFF', mode='', basis='na', value=  -0.3672)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=2,  method='GAFF', mode='', basis='na', value=  -2.2041)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=3,  method='GAFF', mode='', basis='na', value=   0.1246)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=4,  method='GAFF', mode='', basis='na', value= -14.7348)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=5,  method='GAFF', mode='', basis='na', value= -17.5012)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=6,  method='GAFF', mode='', basis='na', value=  -2.513)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=7,  method='GAFF', mode='', basis='na', value=  -2.6369)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=8,  method='GAFF', mode='', basis='na', value=  -0.4512)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=9,  method='GAFF', mode='', basis='na', value=  -5.9818)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=10, method='GAFF', mode='', basis='na', value=  -7.59)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=11, method='GAFF', mode='', basis='na', value=  -6.9928)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=12, method='GAFF', mode='', basis='na', value=   4.6517)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=13, method='GAFF', mode='', basis='na', value=  -1.9683)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=14, method='GAFF', mode='', basis='na', value=   0.6261)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=15, method='GAFF', mode='', basis='na', value=  -0.679)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=16, method='GAFF', mode='', basis='na', value=  -1.0034)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=17, method='GAFF', mode='', basis='na', value=  -0.9144)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=18, method='GAFF', mode='', basis='na', value=   0.9282)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=19, method='GAFF', mode='', basis='na', value=  -1.553)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=20, method='GAFF', mode='', basis='na', value=   2.2541)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=21, method='GAFF', mode='', basis='na', value=  -8.8698)
    # bfdb.sql methodid 35
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=1,  method='PDDG', mode='', basis='na', value=  -2.58823027)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=2,  method='PDDG', mode='', basis='na', value=  -0.87762465)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=3,  method='PDDG', mode='', basis='na', value=  -0.33096816)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=4,  method='PDDG', mode='', basis='na', value=  -1.61327119)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=5,  method='PDDG', mode='', basis='na', value= -10.00308486)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=6,  method='PDDG', mode='', basis='na', value=  -5.19722576)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=7,  method='PDDG', mode='', basis='na', value=  -1.68709639)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=8,  method='PDDG', mode='', basis='na', value=   0.85670932)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=9,  method='PDDG', mode='', basis='na', value=  -3.30759336)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=10, method='PDDG', mode='', basis='na', value=  -1.36097072)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=11, method='PDDG', mode='', basis='na', value=  -4.02745745)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=12, method='PDDG', mode='', basis='na', value=  -2.35666953)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=13, method='PDDG', mode='', basis='na', value=  -1.43383881)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=14, method='PDDG', mode='', basis='na', value=  -3.49140134)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=15, method='PDDG', mode='', basis='na', value=  -2.02295531)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=16, method='PDDG', mode='', basis='na', value=  -0.9776186)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=17, method='PDDG', mode='', basis='na', value=  -2.42455764)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=18, method='PDDG', mode='', basis='na', value=  -2.62079961)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=19, method='PDDG', mode='', basis='na', value=  -0.48527947)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=20, method='PDDG', mode='', basis='na', value=  -1.67330378)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=21, method='PDDG', mode='', basis='na', value=  -3.83094171)
    # bfdb.sql methodid 36
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=1,  method='PM3', mode='', basis='na', value=  -1.08104078)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=2,  method='PM3', mode='', basis='na', value=  -0.26068254)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=3,  method='PM3', mode='', basis='na', value=   0.00968399)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=4,  method='PM3', mode='', basis='na', value=  -8.20121791)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=5,  method='PM3', mode='', basis='na', value= -11.94473375)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=6,  method='PM3', mode='', basis='na', value=  -3.92435163)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=7,  method='PM3', mode='', basis='na', value=  -1.03887648)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=8,  method='PM3', mode='', basis='na', value=   1.0763624)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=9,  method='PM3', mode='', basis='na', value=  -3.02592008)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=10, method='PM3', mode='', basis='na', value=  -2.03982604)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=11, method='PM3', mode='', basis='na', value=  -3.36786299)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=12, method='PM3', mode='', basis='na', value=  -2.17782849)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=13, method='PM3', mode='', basis='na', value=  -0.75837208)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=14, method='PM3', mode='', basis='na', value=  -2.15093851)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=15, method='PM3', mode='', basis='na', value=  -0.92236294)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=16, method='PM3', mode='', basis='na', value=  -0.58767569)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=17, method='PM3', mode='', basis='na', value=  -0.83948196)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=18, method='PM3', mode='', basis='na', value=  -1.81439818)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=19, method='PM3', mode='', basis='na', value=   0.14487994)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=20, method='PM3', mode='', basis='na', value=  -0.75511105)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=21, method='PM3', mode='', basis='na', value=  -5.19335765)
    # bfdb.sql methodid 37
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=1,  method='PM6', mode='', basis='na', value=  -0.191634842)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=2,  method='PM6', mode='', basis='na', value=  -0.676561383)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=3,  method='PM6', mode='', basis='na', value=  -0.988269312)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=4,  method='PM6', mode='', basis='na', value=  -9.451010415)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=5,  method='PM6', mode='', basis='na', value= -12.73255522)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=6,  method='PM6', mode='', basis='na', value=  -3.447677736)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=7,  method='PM6', mode='', basis='na', value=  -1.556907755)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=8,  method='PM6', mode='', basis='na', value=   0.513683735)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=9,  method='PM6', mode='', basis='na', value=  -4.383734183)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=10, method='PM6', mode='', basis='na', value=  -5.671765325)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=11, method='PM6', mode='', basis='na', value=  -5.879986431)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=12, method='PM6', mode='', basis='na', value=  -0.327428168)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=13, method='PM6', mode='', basis='na', value=  -0.457393268)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=14, method='PM6', mode='', basis='na', value=  -0.798347466)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=15, method='PM6', mode='', basis='na', value=  -0.148576706)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=16, method='PM6', mode='', basis='na', value=  -0.211013201)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=17, method='PM6', mode='', basis='na', value=  -0.20467784)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=18, method='PM6', mode='', basis='na', value=  -0.28862244)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=19, method='PM6', mode='', basis='na', value=  -0.376258692)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=20, method='PM6', mode='', basis='na', value=   0.296813668)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=21, method='PM6', mode='', basis='na', value=  -7.337952875)
    # bfdb.sql methodid 38
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=1,  method='PM6DH2', mode='', basis='na', value=  -0.96148)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=2,  method='PM6DH2', mode='', basis='na', value=  -2.38197)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=3,  method='PM6DH2', mode='', basis='na', value=  -2.66411)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=4,  method='PM6DH2', mode='', basis='na', value= -18.52053)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=5,  method='PM6DH2', mode='', basis='na', value= -16.04034)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=6,  method='PM6DH2', mode='', basis='na', value=  -4.18911)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=7,  method='PM6DH2', mode='', basis='na', value=  -3.21063)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=8,  method='PM6DH2', mode='', basis='na', value=  -0.81651)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=9,  method='PM6DH2', mode='', basis='na', value=  -5.49869)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=10, method='PM6DH2', mode='', basis='na', value=  -7.60802)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=11, method='PM6DH2', mode='', basis='na', value=  -7.19089)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=12, method='PM6DH2', mode='', basis='na', value=  -1.34728)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=13, method='PM6DH2', mode='', basis='na', value=  -2.07949)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=14, method='PM6DH2', mode='', basis='na', value=  -2.46949)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=15, method='PM6DH2', mode='', basis='na', value=  -0.93054)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=16, method='PM6DH2', mode='', basis='na', value=  -0.98472)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=17, method='PM6DH2', mode='', basis='na', value=  -1.63048)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=18, method='PM6DH2', mode='', basis='na', value=  -1.14731)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=19, method='PM6DH2', mode='', basis='na', value=  -1.81607)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=20, method='PM6DH2', mode='', basis='na', value=  -0.40515)
    dbinstance.add_ReactionDatum(citation='1hsg', dbse='HSG', rxn=21, method='PM6DH2', mode='', basis='na', value=  -8.44892)
