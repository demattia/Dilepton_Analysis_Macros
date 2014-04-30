sampleDataSet = '/Photon/Run2012A-22Jan2013-v1/AOD'

# original (i.e. RECO file) release,
# not the one we plan to process them with
sampleRelease = "CMSSW_5_3_7_patch5" 
# release used to create new files with
sampleProcessRelease = "CMSSW_5_3_8" 

sampleNumEvents = 13031092 # according to DBS, as of 13 October 2013

# global tag needs to be chosen to match release, trigger menu and alignment conditions.
# see https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions
sampleGlobalTag = 'FT_53_V21_AN4::All'

# data quality run/lumi section selection
sampleJSON = "https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions12/8TeV/Reprocessing/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt"

# restrict run range (mainly to get a sample with consistent trigger configuration)

# use checkAllFilesOpened whenever possible, and noDuplicateCheck when necessary
sampleDuplicateCheckMode = "checkAllFilesOpened"

# "DATA" or "MC"
sampleType = "DATA"


samplePatDBSName=""

sampleBaseDir="dcap://dcap.pp.rl.ac.uk///pnfs/pp.rl.ac.uk/data/cms/store/user/ejclemen//Photon/Data_Photon_Run2012A22Jan_pat_20130613/500b0fd5369d30864bfb27c034ab5148/"
samplePatFiles = [
sampleBaseDir+"PATtuple_192_6_tgs.root",
sampleBaseDir+"PATtuple_273_3_Nvz.root",
sampleBaseDir+"PATtuple_373_4_d4p.root",
sampleBaseDir+"PATtuple_407_3_hSO.root",
sampleBaseDir+"PATtuple_557_5_3vP.root",
sampleBaseDir+"PATtuple_319_3_el4.root",
sampleBaseDir+"PATtuple_248_3_AAJ.root",
sampleBaseDir+"PATtuple_180_3_G56.root",
sampleBaseDir+"PATtuple_133_3_OGE.root",
sampleBaseDir+"PATtuple_196_3_paP.root",
sampleBaseDir+"PATtuple_67_3_6WH.root",
sampleBaseDir+"PATtuple_125_3_ddc.root",
sampleBaseDir+"PATtuple_206_3_trw.root",
sampleBaseDir+"PATtuple_592_4_w3s.root",
sampleBaseDir+"PATtuple_526_4_Qun.root",
sampleBaseDir+"PATtuple_554_4_2Ef.root",
sampleBaseDir+"PATtuple_365_2_tBD.root",
sampleBaseDir+"PATtuple_302_2_dI3.root",
sampleBaseDir+"PATtuple_430_2_0Ft.root",
sampleBaseDir+"PATtuple_42_2_jJS.root",
sampleBaseDir+"PATtuple_24_2_H9j.root",
sampleBaseDir+"PATtuple_507_3_TE7.root",
sampleBaseDir+"PATtuple_506_3_s5j.root",
sampleBaseDir+"PATtuple_529_3_zab.root",
sampleBaseDir+"PATtuple_517_3_xGT.root",
sampleBaseDir+"PATtuple_560_3_0Zx.root",
sampleBaseDir+"PATtuple_509_3_DFT.root",
sampleBaseDir+"PATtuple_591_3_8Dm.root",
sampleBaseDir+"PATtuple_582_3_x0f.root",
sampleBaseDir+"PATtuple_584_3_i9G.root",
sampleBaseDir+"PATtuple_539_3_7nQ.root",
sampleBaseDir+"PATtuple_581_3_0UE.root",
sampleBaseDir+"PATtuple_461_1_Orz.root",
sampleBaseDir+"PATtuple_573_3_jJn.root",
sampleBaseDir+"PATtuple_586_3_N5R.root",
sampleBaseDir+"PATtuple_486_1_Lwe.root",
sampleBaseDir+"PATtuple_549_3_JHX.root",
sampleBaseDir+"PATtuple_556_3_H7L.root",
sampleBaseDir+"PATtuple_572_3_n0O.root",
sampleBaseDir+"PATtuple_474_1_glA.root",
sampleBaseDir+"PATtuple_419_1_ROh.root",
sampleBaseDir+"PATtuple_575_3_Y8X.root",
sampleBaseDir+"PATtuple_567_3_P5X.root",
sampleBaseDir+"PATtuple_485_1_D48.root",
sampleBaseDir+"PATtuple_495_1_hak.root",
sampleBaseDir+"PATtuple_563_3_XW8.root",
sampleBaseDir+"PATtuple_424_1_86f.root",
sampleBaseDir+"PATtuple_558_3_ivB.root",
sampleBaseDir+"PATtuple_578_3_WhD.root",
sampleBaseDir+"PATtuple_550_3_l50.root",
sampleBaseDir+"PATtuple_580_3_dPU.root",
sampleBaseDir+"PATtuple_454_1_M9f.root",
sampleBaseDir+"PATtuple_589_3_Gw1.root",
sampleBaseDir+"PATtuple_552_3_nIn.root",
sampleBaseDir+"PATtuple_416_1_CGv.root",
sampleBaseDir+"PATtuple_412_1_tNb.root",
sampleBaseDir+"PATtuple_543_3_53c.root",
sampleBaseDir+"PATtuple_577_3_NRo.root",
sampleBaseDir+"PATtuple_548_3_R1Q.root",
sampleBaseDir+"PATtuple_585_3_mVy.root",
sampleBaseDir+"PATtuple_568_3_eRO.root",
sampleBaseDir+"PATtuple_579_3_7Yn.root",
sampleBaseDir+"PATtuple_562_3_I6e.root",
sampleBaseDir+"PATtuple_525_3_l2c.root",
sampleBaseDir+"PATtuple_571_3_STr.root",
sampleBaseDir+"PATtuple_421_1_INu.root",
sampleBaseDir+"PATtuple_551_3_zrv.root",
sampleBaseDir+"PATtuple_477_1_Apv.root",
sampleBaseDir+"PATtuple_544_3_pvS.root",
sampleBaseDir+"PATtuple_490_1_n8b.root",
sampleBaseDir+"PATtuple_379_1_EDO.root",
sampleBaseDir+"PATtuple_523_3_6Y0.root",
sampleBaseDir+"PATtuple_593_3_blg.root",
sampleBaseDir+"PATtuple_559_3_bB4.root",
sampleBaseDir+"PATtuple_530_3_THK.root",
sampleBaseDir+"PATtuple_565_3_mbh.root",
sampleBaseDir+"PATtuple_504_3_sgr.root",
sampleBaseDir+"PATtuple_458_1_Pjp.root",
sampleBaseDir+"PATtuple_538_3_C71.root",
sampleBaseDir+"PATtuple_564_3_WSc.root",
sampleBaseDir+"PATtuple_542_3_4Jz.root",
sampleBaseDir+"PATtuple_464_1_dOr.root",
sampleBaseDir+"PATtuple_513_3_aZc.root",
sampleBaseDir+"PATtuple_561_3_s4f.root",
sampleBaseDir+"PATtuple_377_1_uTV.root",
sampleBaseDir+"PATtuple_528_3_OKK.root",
sampleBaseDir+"PATtuple_547_3_kYE.root",
sampleBaseDir+"PATtuple_524_3_NIr.root",
sampleBaseDir+"PATtuple_492_1_BAL.root",
sampleBaseDir+"PATtuple_534_3_opm.root",
sampleBaseDir+"PATtuple_408_1_iDA.root",
sampleBaseDir+"PATtuple_425_1_xwz.root",
sampleBaseDir+"PATtuple_476_1_lDL.root",
sampleBaseDir+"PATtuple_435_1_4WH.root",
sampleBaseDir+"PATtuple_376_1_lCE.root",
sampleBaseDir+"PATtuple_488_1_VTH.root",
sampleBaseDir+"PATtuple_348_1_70n.root",
sampleBaseDir+"PATtuple_405_1_Ezr.root",
sampleBaseDir+"PATtuple_375_1_YXH.root",
sampleBaseDir+"PATtuple_349_1_zaO.root",
sampleBaseDir+"PATtuple_448_1_WwL.root",
sampleBaseDir+"PATtuple_483_1_zMr.root",
sampleBaseDir+"PATtuple_344_1_cG1.root",
sampleBaseDir+"PATtuple_423_1_Pej.root",
sampleBaseDir+"PATtuple_369_1_8wx.root",
sampleBaseDir+"PATtuple_465_1_ZIx.root",
sampleBaseDir+"PATtuple_380_1_SNB.root",
sampleBaseDir+"PATtuple_501_3_ymO.root",
sampleBaseDir+"PATtuple_440_1_2lu.root",
sampleBaseDir+"PATtuple_398_1_BPg.root",
sampleBaseDir+"PATtuple_393_1_zI9.root",
sampleBaseDir+"PATtuple_450_1_uMX.root",
sampleBaseDir+"PATtuple_473_1_UVH.root",
sampleBaseDir+"PATtuple_426_1_Wha.root",
sampleBaseDir+"PATtuple_456_1_USK.root",
sampleBaseDir+"PATtuple_384_1_11V.root",
sampleBaseDir+"PATtuple_438_1_d6o.root",
sampleBaseDir+"PATtuple_362_1_pky.root",
sampleBaseDir+"PATtuple_396_1_SC5.root",
sampleBaseDir+"PATtuple_383_1_7S6.root",
sampleBaseDir+"PATtuple_402_1_B33.root",
sampleBaseDir+"PATtuple_386_1_KMc.root",
sampleBaseDir+"PATtuple_337_1_Bpl.root",
sampleBaseDir+"PATtuple_514_4_W98.root",
sampleBaseDir+"PATtuple_553_4_un6.root",
sampleBaseDir+"PATtuple_545_4_buV.root",
sampleBaseDir+"PATtuple_512_4_S6x.root",
sampleBaseDir+"PATtuple_587_4_2eg.root",
sampleBaseDir+"PATtuple_484_2_jEk.root",
sampleBaseDir+"PATtuple_357_2_IR8.root",
sampleBaseDir+"PATtuple_487_2_Vo6.root",
sampleBaseDir+"PATtuple_326_2_VJ9.root",
sampleBaseDir+"PATtuple_247_2_yis.root",
sampleBaseDir+"PATtuple_227_2_p5o.root",
sampleBaseDir+"PATtuple_467_2_LfV.root",
sampleBaseDir+"PATtuple_311_2_06m.root",
sampleBaseDir+"PATtuple_296_2_EVs.root",
sampleBaseDir+"PATtuple_437_1_dSL.root",
sampleBaseDir+"PATtuple_372_1_Cq0.root",
sampleBaseDir+"PATtuple_364_1_qt0.root",
sampleBaseDir+"PATtuple_350_1_4d8.root",
sampleBaseDir+"PATtuple_382_1_Jhl.root",
sampleBaseDir+"PATtuple_413_1_QFa.root",
sampleBaseDir+"PATtuple_388_1_2y2.root",
sampleBaseDir+"PATtuple_347_1_KCM.root",
sampleBaseDir+"PATtuple_371_1_9xx.root",
sampleBaseDir+"PATtuple_359_1_7eg.root",
sampleBaseDir+"PATtuple_136_1_rTi.root",
sampleBaseDir+"PATtuple_409_1_NPZ.root",
sampleBaseDir+"PATtuple_361_1_tyG.root",
sampleBaseDir+"PATtuple_334_1_OHc.root",
sampleBaseDir+"PATtuple_352_1_Whu.root",
sampleBaseDir+"PATtuple_355_1_ZU6.root",
sampleBaseDir+"PATtuple_428_1_gnz.root",
sampleBaseDir+"PATtuple_318_1_N3G.root",
sampleBaseDir+"PATtuple_336_1_Vbd.root",
sampleBaseDir+"PATtuple_353_1_I41.root",
sampleBaseDir+"PATtuple_418_1_yfG.root",
sampleBaseDir+"PATtuple_415_1_n1i.root",
sampleBaseDir+"PATtuple_417_1_319.root",
sampleBaseDir+"PATtuple_387_1_o0B.root",
sampleBaseDir+"PATtuple_443_1_R9f.root",
sampleBaseDir+"PATtuple_313_1_dLt.root",
sampleBaseDir+"PATtuple_436_1_IEL.root",
sampleBaseDir+"PATtuple_381_1_BZv.root",
sampleBaseDir+"PATtuple_401_1_wIh.root",
sampleBaseDir+"PATtuple_346_1_mRG.root",
sampleBaseDir+"PATtuple_391_1_Ww8.root",
sampleBaseDir+"PATtuple_239_1_XJM.root",
sampleBaseDir+"PATtuple_331_1_j6w.root",
sampleBaseDir+"PATtuple_342_1_hbV.root",
sampleBaseDir+"PATtuple_332_1_SDR.root",
sampleBaseDir+"PATtuple_185_1_ymG.root",
sampleBaseDir+"PATtuple_329_1_RUb.root",
sampleBaseDir+"PATtuple_279_1_ddC.root",
sampleBaseDir+"PATtuple_303_1_DIs.root",
sampleBaseDir+"PATtuple_390_1_33D.root",
sampleBaseDir+"PATtuple_294_1_62I.root",
sampleBaseDir+"PATtuple_340_1_D1x.root",
sampleBaseDir+"PATtuple_354_1_vR2.root",
sampleBaseDir+"PATtuple_335_1_9AB.root",
sampleBaseDir+"PATtuple_315_1_3wO.root",
sampleBaseDir+"PATtuple_374_1_ITl.root",
sampleBaseDir+"PATtuple_356_1_ThV.root",
sampleBaseDir+"PATtuple_320_1_CwW.root",
sampleBaseDir+"PATtuple_367_1_B5F.root",
sampleBaseDir+"PATtuple_299_1_l8C.root",
sampleBaseDir+"PATtuple_324_1_iJK.root",
sampleBaseDir+"PATtuple_330_1_ttt.root",
sampleBaseDir+"PATtuple_345_1_EX1.root",
sampleBaseDir+"PATtuple_173_1_j1J.root",
sampleBaseDir+"PATtuple_191_1_cXR.root",
sampleBaseDir+"PATtuple_111_1_HBo.root",
sampleBaseDir+"PATtuple_174_1_K89.root",
sampleBaseDir+"PATtuple_167_1_v73.root",
sampleBaseDir+"PATtuple_116_1_A5Z.root",
sampleBaseDir+"PATtuple_145_1_2jh.root",
sampleBaseDir+"PATtuple_156_1_sLl.root",
sampleBaseDir+"PATtuple_114_1_DIR.root",
sampleBaseDir+"PATtuple_113_1_HuZ.root",
sampleBaseDir+"PATtuple_164_1_9RB.root",
sampleBaseDir+"PATtuple_129_1_IdB.root",
sampleBaseDir+"PATtuple_151_1_0S3.root",
sampleBaseDir+"PATtuple_91_1_Eh7.root",
sampleBaseDir+"PATtuple_168_1_FBT.root",
sampleBaseDir+"PATtuple_128_1_LNT.root",
sampleBaseDir+"PATtuple_152_1_xTf.root",
sampleBaseDir+"PATtuple_154_1_vsg.root",
sampleBaseDir+"PATtuple_134_1_cc5.root",
sampleBaseDir+"PATtuple_93_1_2WQ.root",
sampleBaseDir+"PATtuple_139_1_4P1.root",
sampleBaseDir+"PATtuple_144_1_zId.root",
sampleBaseDir+"PATtuple_146_1_sYI.root",
sampleBaseDir+"PATtuple_155_1_KX8.root",
sampleBaseDir+"PATtuple_149_1_7QR.root",
sampleBaseDir+"PATtuple_121_1_3jw.root",
sampleBaseDir+"PATtuple_115_1_Et6.root",
sampleBaseDir+"PATtuple_159_1_dlC.root",
sampleBaseDir+"PATtuple_135_1_zO3.root",
sampleBaseDir+"PATtuple_574_3_rlr.root",
sampleBaseDir+"PATtuple_446_1_ZrE.root",
sampleBaseDir+"PATtuple_535_3_D6e.root",
sampleBaseDir+"PATtuple_583_3_cMO.root",
sampleBaseDir+"PATtuple_491_1_rfX.root",
sampleBaseDir+"PATtuple_566_3_HNC.root",
sampleBaseDir+"PATtuple_411_1_bEx.root",
sampleBaseDir+"PATtuple_541_3_dp1.root",
sampleBaseDir+"PATtuple_533_3_BzB.root",
sampleBaseDir+"PATtuple_590_3_nbT.root",
sampleBaseDir+"PATtuple_368_1_ISH.root",
sampleBaseDir+"PATtuple_521_3_iiu.root",
sampleBaseDir+"PATtuple_570_3_GaZ.root",
sampleBaseDir+"PATtuple_472_1_dG7.root",
sampleBaseDir+"PATtuple_478_1_ONq.root",
sampleBaseDir+"PATtuple_394_1_puS.root",
sampleBaseDir+"PATtuple_537_3_mm0.root",
sampleBaseDir+"PATtuple_503_3_uqu.root",
sampleBaseDir+"PATtuple_453_1_0WW.root",
sampleBaseDir+"PATtuple_576_3_1Yg.root",
sampleBaseDir+"PATtuple_497_1_rFU.root",
sampleBaseDir+"PATtuple_494_1_49V.root",
sampleBaseDir+"PATtuple_481_1_o4J.root",
sampleBaseDir+"PATtuple_496_1_U8Z.root",
sampleBaseDir+"PATtuple_475_1_MX3.root",
sampleBaseDir+"PATtuple_457_1_XFz.root",
sampleBaseDir+"PATtuple_432_1_o29.root",
sampleBaseDir+"PATtuple_328_1_v3r.root",
sampleBaseDir+"PATtuple_508_3_ZEZ.root",
sampleBaseDir+"PATtuple_511_3_3Ai.root",
sampleBaseDir+"PATtuple_510_3_cYO.root",
sampleBaseDir+"PATtuple_498_1_4vT.root",
sampleBaseDir+"PATtuple_519_3_fHA.root",
sampleBaseDir+"PATtuple_451_1_n2o.root",
sampleBaseDir+"PATtuple_555_3_vKA.root",
sampleBaseDir+"PATtuple_505_3_M5x.root",
sampleBaseDir+"PATtuple_366_1_i4d.root",
sampleBaseDir+"PATtuple_470_1_QM5.root",
sampleBaseDir+"PATtuple_333_1_hwV.root",
sampleBaseDir+"PATtuple_516_3_Ca0.root",
sampleBaseDir+"PATtuple_480_1_ffs.root",
sampleBaseDir+"PATtuple_434_1_N19.root",
sampleBaseDir+"PATtuple_404_1_WCk.root",
sampleBaseDir+"PATtuple_406_1_Yqc.root",
sampleBaseDir+"PATtuple_378_1_uUJ.root",
sampleBaseDir+"PATtuple_429_1_u7t.root",
sampleBaseDir+"PATtuple_462_1_o6N.root",
sampleBaseDir+"PATtuple_489_1_Om1.root",
sampleBaseDir+"PATtuple_482_1_6Ud.root",
sampleBaseDir+"PATtuple_444_1_1IZ.root",
sampleBaseDir+"PATtuple_410_1_IjI.root",
sampleBaseDir+"PATtuple_520_3_RoS.root",
sampleBaseDir+"PATtuple_439_1_N8b.root",
sampleBaseDir+"PATtuple_459_1_pN3.root",
sampleBaseDir+"PATtuple_399_1_YJM.root",
sampleBaseDir+"PATtuple_392_1_gZh.root",
sampleBaseDir+"PATtuple_468_1_ouz.root",
sampleBaseDir+"PATtuple_469_1_u9Q.root",
sampleBaseDir+"PATtuple_527_3_MtF.root",
sampleBaseDir+"PATtuple_455_1_pnz.root",
sampleBaseDir+"PATtuple_445_1_2N4.root",
sampleBaseDir+"PATtuple_351_1_ShH.root",
sampleBaseDir+"PATtuple_452_1_Q79.root",
sampleBaseDir+"PATtuple_363_1_9NF.root",
sampleBaseDir+"PATtuple_466_1_sn1.root",
sampleBaseDir+"PATtuple_370_1_c1m.root",
sampleBaseDir+"PATtuple_343_1_h1g.root",
sampleBaseDir+"PATtuple_463_1_YlG.root",
sampleBaseDir+"PATtuple_479_1_OT7.root",
sampleBaseDir+"PATtuple_358_1_BDy.root",
sampleBaseDir+"PATtuple_420_1_yzQ.root",
sampleBaseDir+"PATtuple_441_1_e3C.root",
sampleBaseDir+"PATtuple_433_1_n1P.root",
sampleBaseDir+"PATtuple_442_1_Zf2.root",
sampleBaseDir+"PATtuple_502_3_fWz.root",
sampleBaseDir+"PATtuple_360_1_tBr.root",
sampleBaseDir+"PATtuple_460_1_TqL.root",
sampleBaseDir+"PATtuple_500_1_alg.root",
sampleBaseDir+"PATtuple_422_1_LQn.root",
sampleBaseDir+"PATtuple_400_1_TPM.root",
sampleBaseDir+"PATtuple_471_1_OgT.root",
sampleBaseDir+"PATtuple_427_1_ft3.root",
sampleBaseDir+"PATtuple_403_1_ZDe.root",
sampleBaseDir+"PATtuple_127_1_jQR.root",
sampleBaseDir+"PATtuple_126_1_Seh.root",
sampleBaseDir+"PATtuple_148_1_mAy.root",
sampleBaseDir+"PATtuple_122_1_4Ep.root",
sampleBaseDir+"PATtuple_162_1_35r.root",
sampleBaseDir+"PATtuple_123_1_biY.root",
sampleBaseDir+"PATtuple_59_1_Dnp.root",
sampleBaseDir+"PATtuple_143_1_ijM.root",
sampleBaseDir+"PATtuple_141_1_iNr.root",
sampleBaseDir+"PATtuple_109_1_Muo.root",
sampleBaseDir+"PATtuple_157_1_Jcm.root",
sampleBaseDir+"PATtuple_110_1_Oq0.root",
sampleBaseDir+"PATtuple_75_1_PV1.root",
sampleBaseDir+"PATtuple_142_1_Sdk.root",
sampleBaseDir+"PATtuple_117_1_0yz.root",
sampleBaseDir+"PATtuple_140_1_CFu.root",
sampleBaseDir+"PATtuple_79_1_wXi.root",
sampleBaseDir+"PATtuple_98_1_XrI.root",
sampleBaseDir+"PATtuple_131_1_aNC.root",
sampleBaseDir+"PATtuple_92_1_ltY.root",
sampleBaseDir+"PATtuple_130_1_3Jr.root",
sampleBaseDir+"PATtuple_124_1_PNv.root",
sampleBaseDir+"PATtuple_158_1_thK.root",
sampleBaseDir+"PATtuple_137_1_Yej.root",
sampleBaseDir+"PATtuple_84_1_TcZ.root",
sampleBaseDir+"PATtuple_147_1_kIR.root",
sampleBaseDir+"PATtuple_119_1_lD6.root",
sampleBaseDir+"PATtuple_95_1_1B4.root",
sampleBaseDir+"PATtuple_132_1_XcY.root",
sampleBaseDir+"PATtuple_120_1_yHJ.root",
sampleBaseDir+"PATtuple_138_1_bQI.root",
sampleBaseDir+"PATtuple_86_1_7xE.root",
sampleBaseDir+"PATtuple_83_1_k27.root",
sampleBaseDir+"PATtuple_94_1_co6.root",
sampleBaseDir+"PATtuple_112_1_Nwm.root",
sampleBaseDir+"PATtuple_97_1_OI3.root",
sampleBaseDir+"PATtuple_118_1_hKz.root",
sampleBaseDir+"PATtuple_80_1_bUQ.root",
sampleBaseDir+"PATtuple_58_1_0Xo.root",
sampleBaseDir+"PATtuple_47_1_Lj1.root",
sampleBaseDir+"PATtuple_77_1_xCN.root",
sampleBaseDir+"PATtuple_108_1_lj4.root",
sampleBaseDir+"PATtuple_105_1_MSQ.root",
sampleBaseDir+"PATtuple_81_1_uNi.root",
sampleBaseDir+"PATtuple_106_1_djO.root",
sampleBaseDir+"PATtuple_103_1_7iw.root",
sampleBaseDir+"PATtuple_61_1_IYm.root",
sampleBaseDir+"PATtuple_99_1_8E0.root",
sampleBaseDir+"PATtuple_68_1_LxP.root",
sampleBaseDir+"PATtuple_107_1_DiG.root",
sampleBaseDir+"PATtuple_96_1_NKv.root",
sampleBaseDir+"PATtuple_65_1_HZz.root",
sampleBaseDir+"PATtuple_66_1_Sek.root",
sampleBaseDir+"PATtuple_85_1_Sec.root",
sampleBaseDir+"PATtuple_33_1_EcI.root",
sampleBaseDir+"PATtuple_46_1_l01.root",
sampleBaseDir+"PATtuple_72_1_SbB.root",
sampleBaseDir+"PATtuple_100_1_e8h.root",
sampleBaseDir+"PATtuple_90_1_YLQ.root",
sampleBaseDir+"PATtuple_54_1_tx4.root",
sampleBaseDir+"PATtuple_60_1_oRL.root",
sampleBaseDir+"PATtuple_64_1_gCA.root",
sampleBaseDir+"PATtuple_104_1_frk.root",
sampleBaseDir+"PATtuple_102_1_tTW.root",
sampleBaseDir+"PATtuple_44_1_aMs.root",
sampleBaseDir+"PATtuple_56_1_7a3.root",
sampleBaseDir+"PATtuple_71_1_qzg.root",
sampleBaseDir+"PATtuple_89_1_O0Y.root",
sampleBaseDir+"PATtuple_32_1_SWZ.root",
sampleBaseDir+"PATtuple_45_1_PIA.root",
sampleBaseDir+"PATtuple_52_1_JGw.root",
sampleBaseDir+"PATtuple_87_1_ylF.root",
sampleBaseDir+"PATtuple_57_1_Nka.root",
sampleBaseDir+"PATtuple_76_1_jji.root",
sampleBaseDir+"PATtuple_69_1_cKN.root",
sampleBaseDir+"PATtuple_78_1_8Sd.root",
sampleBaseDir+"PATtuple_82_1_vZV.root",
sampleBaseDir+"PATtuple_51_1_uSw.root",
sampleBaseDir+"PATtuple_29_1_Hzm.root",
sampleBaseDir+"PATtuple_73_1_RS8.root",
sampleBaseDir+"PATtuple_74_1_3oZ.root",
sampleBaseDir+"PATtuple_70_1_CFh.root",
sampleBaseDir+"PATtuple_546_3_Fvh.root",
sampleBaseDir+"PATtuple_532_3_vwP.root",
sampleBaseDir+"PATtuple_569_3_tdc.root",
sampleBaseDir+"PATtuple_522_3_hV3.root",
sampleBaseDir+"PATtuple_531_3_NTG.root",
sampleBaseDir+"PATtuple_515_3_ig5.root",
sampleBaseDir+"PATtuple_287_1_Api.root",
sampleBaseDir+"PATtuple_275_1_aNg.root",
sampleBaseDir+"PATtuple_385_1_mPo.root",
sampleBaseDir+"PATtuple_305_1_Dzq.root",
sampleBaseDir+"PATtuple_314_1_zrs.root",
sampleBaseDir+"PATtuple_397_1_kzH.root",
sampleBaseDir+"PATtuple_414_1_f6j.root",
sampleBaseDir+"PATtuple_338_1_pVS.root",
sampleBaseDir+"PATtuple_223_1_ahi.root",
sampleBaseDir+"PATtuple_309_1_1TP.root",
sampleBaseDir+"PATtuple_284_1_Gcq.root",
sampleBaseDir+"PATtuple_316_1_VHg.root",
sampleBaseDir+"PATtuple_300_1_lxQ.root",
sampleBaseDir+"PATtuple_283_1_EM6.root",
sampleBaseDir+"PATtuple_310_1_G6O.root",
sampleBaseDir+"PATtuple_274_1_2zZ.root",
sampleBaseDir+"PATtuple_170_1_K7z.root",
sampleBaseDir+"PATtuple_306_1_UEX.root",
sampleBaseDir+"PATtuple_278_1_TF2.root",
sampleBaseDir+"PATtuple_341_1_XNQ.root",
sampleBaseDir+"PATtuple_297_1_hRM.root",
sampleBaseDir+"PATtuple_327_1_Iy2.root",
sampleBaseDir+"PATtuple_312_1_9v3.root",
sampleBaseDir+"PATtuple_301_1_pxZ.root",
sampleBaseDir+"PATtuple_307_1_nC6.root",
sampleBaseDir+"PATtuple_339_1_pW4.root",
sampleBaseDir+"PATtuple_286_1_9Ke.root",
sampleBaseDir+"PATtuple_395_1_sZW.root",
sampleBaseDir+"PATtuple_295_1_9bC.root",
sampleBaseDir+"PATtuple_232_1_hu5.root",
sampleBaseDir+"PATtuple_321_1_Nsi.root",
sampleBaseDir+"PATtuple_231_1_WT9.root",
sampleBaseDir+"PATtuple_252_1_b1X.root",
sampleBaseDir+"PATtuple_281_1_KF0.root",
sampleBaseDir+"PATtuple_288_1_MFr.root",
sampleBaseDir+"PATtuple_323_1_xZ1.root",
sampleBaseDir+"PATtuple_199_1_TyA.root",
sampleBaseDir+"PATtuple_237_1_WbM.root",
sampleBaseDir+"PATtuple_280_1_f0y.root",
sampleBaseDir+"PATtuple_291_1_gqE.root",
sampleBaseDir+"PATtuple_244_1_54c.root",
sampleBaseDir+"PATtuple_304_1_EHh.root",
sampleBaseDir+"PATtuple_270_1_xDq.root",
sampleBaseDir+"PATtuple_285_1_F3Z.root",
sampleBaseDir+"PATtuple_325_1_fBq.root",
sampleBaseDir+"PATtuple_242_1_znj.root",
sampleBaseDir+"PATtuple_308_1_m4w.root",
sampleBaseDir+"PATtuple_317_1_59h.root",
sampleBaseDir+"PATtuple_228_1_QeO.root",
sampleBaseDir+"PATtuple_260_1_RtR.root",
sampleBaseDir+"PATtuple_245_1_qEA.root",
sampleBaseDir+"PATtuple_254_1_3Mc.root",
sampleBaseDir+"PATtuple_290_1_orj.root",
sampleBaseDir+"PATtuple_212_1_qeb.root",
sampleBaseDir+"PATtuple_282_1_MsL.root",
sampleBaseDir+"PATtuple_261_1_dTY.root",
sampleBaseDir+"PATtuple_188_1_meV.root",
sampleBaseDir+"PATtuple_214_1_fx5.root",
sampleBaseDir+"PATtuple_246_1_xL2.root",
sampleBaseDir+"PATtuple_241_1_4uA.root",
sampleBaseDir+"PATtuple_265_1_bOw.root",
sampleBaseDir+"PATtuple_298_1_GyF.root",
sampleBaseDir+"PATtuple_292_1_JJ6.root",
sampleBaseDir+"PATtuple_226_1_jvR.root",
sampleBaseDir+"PATtuple_203_1_ry9.root",
sampleBaseDir+"PATtuple_204_1_hXW.root",
sampleBaseDir+"PATtuple_234_1_CHb.root",
sampleBaseDir+"PATtuple_322_1_1rk.root",
sampleBaseDir+"PATtuple_253_1_1sJ.root",
sampleBaseDir+"PATtuple_251_1_i3S.root",
sampleBaseDir+"PATtuple_250_1_sbZ.root",
sampleBaseDir+"PATtuple_272_1_wFR.root",
sampleBaseDir+"PATtuple_269_1_vR5.root",
sampleBaseDir+"PATtuple_277_1_LSv.root",
sampleBaseDir+"PATtuple_266_1_epG.root",
sampleBaseDir+"PATtuple_235_1_na3.root",
sampleBaseDir+"PATtuple_289_1_UtB.root",
sampleBaseDir+"PATtuple_238_1_9iR.root",
sampleBaseDir+"PATtuple_249_1_WUu.root",
sampleBaseDir+"PATtuple_293_1_xxk.root",
sampleBaseDir+"PATtuple_257_1_2rj.root",
sampleBaseDir+"PATtuple_255_1_Hek.root",
sampleBaseDir+"PATtuple_258_1_ROH.root",
sampleBaseDir+"PATtuple_259_1_WSa.root",
sampleBaseDir+"PATtuple_267_1_KpE.root",
sampleBaseDir+"PATtuple_160_1_Kmv.root",
sampleBaseDir+"PATtuple_240_1_A8y.root",
sampleBaseDir+"PATtuple_163_1_qdZ.root",
sampleBaseDir+"PATtuple_230_1_tOu.root",
sampleBaseDir+"PATtuple_183_1_0cq.root",
sampleBaseDir+"PATtuple_233_1_V78.root",
sampleBaseDir+"PATtuple_177_1_SOH.root",
sampleBaseDir+"PATtuple_224_1_bNt.root",
sampleBaseDir+"PATtuple_184_1_AKt.root",
sampleBaseDir+"PATtuple_221_1_Ass.root",
sampleBaseDir+"PATtuple_262_1_95x.root",
sampleBaseDir+"PATtuple_197_1_22d.root",
sampleBaseDir+"PATtuple_256_1_9SP.root",
sampleBaseDir+"PATtuple_215_1_djY.root",
sampleBaseDir+"PATtuple_205_1_GO1.root",
sampleBaseDir+"PATtuple_178_1_Ksd.root",
sampleBaseDir+"PATtuple_211_1_kYW.root",
sampleBaseDir+"PATtuple_222_1_Lg6.root",
sampleBaseDir+"PATtuple_209_1_yuy.root",
sampleBaseDir+"PATtuple_198_1_S9u.root",
sampleBaseDir+"PATtuple_264_1_jUf.root",
sampleBaseDir+"PATtuple_216_1_Hr3.root",
sampleBaseDir+"PATtuple_194_1_CBI.root",
sampleBaseDir+"PATtuple_207_1_aW1.root",
sampleBaseDir+"PATtuple_101_1_Uwq.root",
sampleBaseDir+"PATtuple_208_1_3xG.root",
sampleBaseDir+"PATtuple_187_1_7Ae.root",
sampleBaseDir+"PATtuple_236_1_Vfi.root",
sampleBaseDir+"PATtuple_276_1_nMC.root",
sampleBaseDir+"PATtuple_213_1_rAW.root",
sampleBaseDir+"PATtuple_220_1_tSn.root",
sampleBaseDir+"PATtuple_190_1_hCM.root",
sampleBaseDir+"PATtuple_243_1_91m.root",
sampleBaseDir+"PATtuple_271_1_hmR.root",
sampleBaseDir+"PATtuple_200_1_eW4.root",
sampleBaseDir+"PATtuple_210_1_gl7.root",
sampleBaseDir+"PATtuple_219_1_oyV.root",
sampleBaseDir+"PATtuple_182_1_8fP.root",
sampleBaseDir+"PATtuple_176_1_xKg.root",
sampleBaseDir+"PATtuple_218_1_xDJ.root",
sampleBaseDir+"PATtuple_263_1_mYZ.root",
sampleBaseDir+"PATtuple_169_1_JAH.root",
sampleBaseDir+"PATtuple_165_1_m8F.root",
sampleBaseDir+"PATtuple_172_1_yZM.root",
sampleBaseDir+"PATtuple_229_1_8pF.root",
sampleBaseDir+"PATtuple_179_1_JBh.root",
sampleBaseDir+"PATtuple_88_1_Gbd.root",
sampleBaseDir+"PATtuple_189_1_iwE.root",
sampleBaseDir+"PATtuple_217_1_Cec.root",
sampleBaseDir+"PATtuple_171_1_Wf8.root",
sampleBaseDir+"PATtuple_268_1_lqa.root",
sampleBaseDir+"PATtuple_186_1_Xcf.root",
sampleBaseDir+"PATtuple_225_1_huK.root",
sampleBaseDir+"PATtuple_202_1_csh.root",
sampleBaseDir+"PATtuple_166_1_hCE.root",
sampleBaseDir+"PATtuple_201_1_OP5.root",
sampleBaseDir+"PATtuple_195_1_XlJ.root",
sampleBaseDir+"PATtuple_161_1_D6d.root",
sampleBaseDir+"PATtuple_193_1_bl3.root",
sampleBaseDir+"PATtuple_153_1_VZa.root",
sampleBaseDir+"PATtuple_150_1_vQU.root",
sampleBaseDir+"PATtuple_175_1_wMa.root",
sampleBaseDir+"PATtuple_181_1_RTK.root",
sampleBaseDir+"PATtuple_588_3_xHT.root",
sampleBaseDir+"PATtuple_493_1_f2S.root",
sampleBaseDir+"PATtuple_518_3_Hi2.root",
sampleBaseDir+"PATtuple_536_3_zLT.root",
sampleBaseDir+"PATtuple_540_3_T7z.root",
sampleBaseDir+"PATtuple_431_1_kFi.root",
sampleBaseDir+"PATtuple_449_1_zIk.root",
sampleBaseDir+"PATtuple_447_1_PiA.root",
sampleBaseDir+"PATtuple_499_1_PVK.root",
sampleBaseDir+"PATtuple_389_1_7UC.root",
sampleBaseDir+"PATtuple_48_1_euV.root",
sampleBaseDir+"PATtuple_40_1_ltu.root",
sampleBaseDir+"PATtuple_63_1_fAf.root",
sampleBaseDir+"PATtuple_39_1_9XX.root",
sampleBaseDir+"PATtuple_62_1_Xcx.root",
sampleBaseDir+"PATtuple_50_1_eHw.root",
sampleBaseDir+"PATtuple_49_1_Ya1.root",
sampleBaseDir+"PATtuple_53_1_mup.root",
sampleBaseDir+"PATtuple_34_1_gXf.root",
sampleBaseDir+"PATtuple_41_1_pOD.root",
sampleBaseDir+"PATtuple_21_1_nqw.root",
sampleBaseDir+"PATtuple_38_1_l3T.root",
sampleBaseDir+"PATtuple_17_1_t6b.root",
sampleBaseDir+"PATtuple_8_1_J2L.root",
sampleBaseDir+"PATtuple_43_1_St3.root",
sampleBaseDir+"PATtuple_20_1_Y26.root",
sampleBaseDir+"PATtuple_31_1_aXm.root",
sampleBaseDir+"PATtuple_55_1_MWr.root",
sampleBaseDir+"PATtuple_36_1_Dip.root",
sampleBaseDir+"PATtuple_35_1_d9o.root",
sampleBaseDir+"PATtuple_37_1_vac.root",
sampleBaseDir+"PATtuple_27_1_1u3.root",
sampleBaseDir+"PATtuple_7_1_xks.root",
sampleBaseDir+"PATtuple_30_1_HHl.root",
sampleBaseDir+"PATtuple_2_1_2sx.root",
sampleBaseDir+"PATtuple_6_1_PTx.root",
sampleBaseDir+"PATtuple_25_1_qG8.root",
sampleBaseDir+"PATtuple_22_1_AII.root",
sampleBaseDir+"PATtuple_28_1_Idf.root",
sampleBaseDir+"PATtuple_18_1_M13.root",
sampleBaseDir+"PATtuple_26_1_Y2l.root",
sampleBaseDir+"PATtuple_15_1_upI.root",
sampleBaseDir+"PATtuple_19_1_ySG.root",
sampleBaseDir+"PATtuple_4_1_lvt.root",
sampleBaseDir+"PATtuple_23_1_VJv.root",
sampleBaseDir+"PATtuple_10_1_Poj.root",
sampleBaseDir+"PATtuple_1_1_TkT.root",
sampleBaseDir+"PATtuple_9_1_MqA.root",
sampleBaseDir+"PATtuple_14_1_F84.root",
sampleBaseDir+"PATtuple_5_1_LpE.root",
sampleBaseDir+"PATtuple_3_1_T5V.root",
sampleBaseDir+"PATtuple_13_1_BzO.root",
sampleBaseDir+"PATtuple_16_1_wZn.root",
sampleBaseDir+"PATtuple_11_1_pp1.root",
sampleBaseDir+"PATtuple_12_1_bKy.root",
]