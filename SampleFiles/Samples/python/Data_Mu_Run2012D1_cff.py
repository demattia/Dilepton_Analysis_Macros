sampleDataSet = '/DoubleMu/Run2012D-PromptReco-v1/AOD'

# original (i.e. RECO file) release,
# not the one we plan to process them with
sampleRelease = "CMSSW_5_3_2_patch4" 
# release used to create new files with
sampleProcessRelease = "CMSSW_5_3_5" 

sampleNumEvents = 30748995 # according to DBS, as of 25 January 2013

# global tag needs to be chosen to match release, trigger menu and alignment conditions.
# see https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions
sampleGlobalTag = 'GR_P_V42_AN3::All'

# data quality run/lumi section selection
sampleJSON = "https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions12/8TeV/Prompt/Cert_190456-208686_8TeV_PromptReco_Collisions12_JSON_MuonPhys.txt"
        
# restrict run range (mainly to get a sample with consistent trigger configuration)
sampleRunRange = [190456-99999999]

# use checkAllFilesOpened whenever possible, and noDuplicateCheck when necessary
sampleDuplicateCheckMode = "checkAllFilesOpened"

# "DATA" or "MC"
sampleType = "DATA"






samplePatDBSName=""

sampleBaseDir="dcap://dcap.pp.rl.ac.uk///pnfs/pp.rl.ac.uk/data/cms/store/user/ejclemen//DoubleMu/Data_Mu_Run2012D1_pat_20130102/2a372f40071b596743f1b75f6fed579c/"
samplePatFiles = [
sampleBaseDir+"PATtuple_99_3_sPj.root",
sampleBaseDir+"PATtuple_373_6_DoB.root",
sampleBaseDir+"PATtuple_442_7_pXY.root",
sampleBaseDir+"PATtuple_453_6_w8J.root",
sampleBaseDir+"PATtuple_396_6_Ftv.root",
sampleBaseDir+"PATtuple_384_1_tbC.root",
sampleBaseDir+"PATtuple_355_6_N2t.root",
sampleBaseDir+"PATtuple_357_6_aVM.root",
sampleBaseDir+"PATtuple_254_4_CmD.root",
sampleBaseDir+"PATtuple_390_5_3EG.root",
sampleBaseDir+"PATtuple_394_6_59U.root",
sampleBaseDir+"PATtuple_393_6_fm8.root",
sampleBaseDir+"PATtuple_456_6_eSZ.root",
sampleBaseDir+"PATtuple_340_5_T7k.root",
sampleBaseDir+"PATtuple_127_3_FwU.root",
sampleBaseDir+"PATtuple_128_3_wYr.root",
sampleBaseDir+"PATtuple_136_3_TZ3.root",
sampleBaseDir+"PATtuple_451_6_Lo1.root",
sampleBaseDir+"PATtuple_509_6_Y43.root",
sampleBaseDir+"PATtuple_167_3_oo6.root",
sampleBaseDir+"PATtuple_455_6_WId.root",
sampleBaseDir+"PATtuple_508_6_z1y.root",
sampleBaseDir+"PATtuple_411_6_8UU.root",
sampleBaseDir+"PATtuple_512_6_Roz.root",
sampleBaseDir+"PATtuple_507_6_M8T.root",
sampleBaseDir+"PATtuple_364_6_X9V.root",
sampleBaseDir+"PATtuple_510_6_fqF.root",
sampleBaseDir+"PATtuple_194_3_C9D.root",
sampleBaseDir+"PATtuple_164_3_A8V.root",
sampleBaseDir+"PATtuple_398_6_zbY.root",
sampleBaseDir+"PATtuple_131_3_VAO.root",
sampleBaseDir+"PATtuple_457_6_81h.root",
sampleBaseDir+"PATtuple_454_6_ZEI.root",
sampleBaseDir+"PATtuple_511_6_Vl9.root",
sampleBaseDir+"PATtuple_356_6_xzG.root",
sampleBaseDir+"PATtuple_268_5_f2g.root",
sampleBaseDir+"PATtuple_383_6_XsM.root",
sampleBaseDir+"PATtuple_139_3_CD8.root",
sampleBaseDir+"PATtuple_303_4_FAX.root",
sampleBaseDir+"PATtuple_261_5_niG.root",
sampleBaseDir+"PATtuple_395_6_y9E.root",
sampleBaseDir+"PATtuple_129_3_vOg.root",
sampleBaseDir+"PATtuple_130_3_HJb.root",
sampleBaseDir+"PATtuple_365_6_7hg.root",
sampleBaseDir+"PATtuple_361_6_nXO.root",
sampleBaseDir+"PATtuple_277_5_3g6.root",
sampleBaseDir+"PATtuple_362_6_hI8.root",
sampleBaseDir+"PATtuple_272_5_BPx.root",
sampleBaseDir+"PATtuple_271_5_VXy.root",
sampleBaseDir+"PATtuple_276_5_kOy.root",
sampleBaseDir+"PATtuple_196_3_zWM.root",
sampleBaseDir+"PATtuple_360_5_Tnl.root",
sampleBaseDir+"PATtuple_337_5_p8p.root",
sampleBaseDir+"PATtuple_260_5_knD.root",
sampleBaseDir+"PATtuple_141_3_XND.root",
sampleBaseDir+"PATtuple_270_5_t5T.root",
sampleBaseDir+"PATtuple_259_5_QOJ.root",
sampleBaseDir+"PATtuple_339_5_Mfx.root",
sampleBaseDir+"PATtuple_275_5_cyr.root",
sampleBaseDir+"PATtuple_273_5_3vT.root",
sampleBaseDir+"PATtuple_138_3_fFA.root",
sampleBaseDir+"PATtuple_274_5_roT.root",
sampleBaseDir+"PATtuple_338_5_Hew.root",
sampleBaseDir+"PATtuple_279_5_4fl.root",
sampleBaseDir+"PATtuple_278_5_CcM.root",
sampleBaseDir+"PATtuple_280_5_e4j.root",
sampleBaseDir+"PATtuple_597_2_AeS.root",
sampleBaseDir+"PATtuple_323_2_n01.root",
sampleBaseDir+"PATtuple_385_2_F5M.root",
sampleBaseDir+"PATtuple_424_3_3IU.root",
sampleBaseDir+"PATtuple_578_2_F9J.root",
sampleBaseDir+"PATtuple_588_2_Teh.root",
sampleBaseDir+"PATtuple_621_3_vhT.root",
sampleBaseDir+"PATtuple_425_3_WUj.root",
sampleBaseDir+"PATtuple_241_1_gIo.root",
sampleBaseDir+"PATtuple_188_0_Usb.root",
sampleBaseDir+"PATtuple_215_1_Ztt.root",
sampleBaseDir+"PATtuple_299_1_n9X.root",
sampleBaseDir+"PATtuple_426_3_FwY.root",
sampleBaseDir+"PATtuple_461_3_Ns5.root",
sampleBaseDir+"PATtuple_321_2_EZQ.root",
sampleBaseDir+"PATtuple_244_1_A6Z.root",
sampleBaseDir+"PATtuple_462_3_dx7.root",
sampleBaseDir+"PATtuple_463_2_YSJ.root",
sampleBaseDir+"PATtuple_554_2_2jN.root",
sampleBaseDir+"PATtuple_486_2_ocY.root",
sampleBaseDir+"PATtuple_416_2_WVp.root",
sampleBaseDir+"PATtuple_484_2_qd3.root",
sampleBaseDir+"PATtuple_473_3_m5i.root",
sampleBaseDir+"PATtuple_322_2_bb7.root",
sampleBaseDir+"PATtuple_147_0_Twc.root",
sampleBaseDir+"PATtuple_105_0_9KA.root",
sampleBaseDir+"PATtuple_171_0_sjB.root",
sampleBaseDir+"PATtuple_202_1_8l5.root",
sampleBaseDir+"PATtuple_388_2_3Wm.root",
sampleBaseDir+"PATtuple_331_1_36C.root",
sampleBaseDir+"PATtuple_319_1_nxe.root",
sampleBaseDir+"PATtuple_158_0_B6p.root",
sampleBaseDir+"PATtuple_429_2_guK.root",
sampleBaseDir+"PATtuple_449_3_lwp.root",
sampleBaseDir+"PATtuple_419_2_JXA.root",
sampleBaseDir+"PATtuple_460_3_Brc.root",
sampleBaseDir+"PATtuple_487_2_N8g.root",
sampleBaseDir+"PATtuple_78_0_pV6.root",
sampleBaseDir+"PATtuple_94_0_3SG.root",
sampleBaseDir+"PATtuple_542_3_zB4.root",
sampleBaseDir+"PATtuple_226_1_59E.root",
sampleBaseDir+"PATtuple_20_2_GNo.root",
sampleBaseDir+"PATtuple_602_2_6Sn.root",
sampleBaseDir+"PATtuple_587_3_cUf.root",
sampleBaseDir+"PATtuple_427_3_HRN.root",
sampleBaseDir+"PATtuple_495_2_AlI.root",
sampleBaseDir+"PATtuple_428_3_b6U.root",
sampleBaseDir+"PATtuple_570_2_zOZ.root",
sampleBaseDir+"PATtuple_203_0_yDg.root",
sampleBaseDir+"PATtuple_489_2_Qsl.root",
sampleBaseDir+"PATtuple_37_4_8xq.root",
sampleBaseDir+"PATtuple_555_1_4wy.root",
sampleBaseDir+"PATtuple_221_0_b15.root",
sampleBaseDir+"PATtuple_144_1_s8c.root",
sampleBaseDir+"PATtuple_253_0_eBQ.root",
sampleBaseDir+"PATtuple_556_1_IYu.root",
sampleBaseDir+"PATtuple_475_3_tiQ.root",
sampleBaseDir+"PATtuple_21_2_5VK.root",
sampleBaseDir+"PATtuple_590_3_VSV.root",
sampleBaseDir+"PATtuple_483_2_poM.root",
sampleBaseDir+"PATtuple_466_2_j8e.root",
sampleBaseDir+"PATtuple_611_2_wHX.root",
sampleBaseDir+"PATtuple_44_4_6Xh.root",
sampleBaseDir+"PATtuple_210_0_GZD.root",
sampleBaseDir+"PATtuple_193_0_Rcf.root",
sampleBaseDir+"PATtuple_404_6_vuu.root",
sampleBaseDir+"PATtuple_400_6_KZv.root",
sampleBaseDir+"PATtuple_618_8_zeu.root",
sampleBaseDir+"PATtuple_125_3_AcR.root",
sampleBaseDir+"PATtuple_619_8_9yn.root",
sampleBaseDir+"PATtuple_263_5_mja.root",
sampleBaseDir+"PATtuple_282_6_Xa9.root",
sampleBaseDir+"PATtuple_517_6_gdA.root",
sampleBaseDir+"PATtuple_397_6_trC.root",
sampleBaseDir+"PATtuple_281_5_MHe.root",
sampleBaseDir+"PATtuple_250_4_xl8.root",
sampleBaseDir+"PATtuple_405_6_Rmr.root",
sampleBaseDir+"PATtuple_441_8_93M.root",
sampleBaseDir+"PATtuple_443_8_wis.root",
sampleBaseDir+"PATtuple_369_6_T64.root",
sampleBaseDir+"PATtuple_342_5_PjF.root",
sampleBaseDir+"PATtuple_284_6_LRT.root",
sampleBaseDir+"PATtuple_447_8_mXa.root",
sampleBaseDir+"PATtuple_209_3_cUs.root",
sampleBaseDir+"PATtuple_264_5_zTg.root",
sampleBaseDir+"PATtuple_446_8_edB.root",
sampleBaseDir+"PATtuple_444_8_iH3.root",
sampleBaseDir+"PATtuple_450_6_Kai.root",
sampleBaseDir+"PATtuple_190_1_gxP.root",
sampleBaseDir+"PATtuple_391_6_Iej.root",
sampleBaseDir+"PATtuple_407_6_xUc.root",
sampleBaseDir+"PATtuple_406_6_1fX.root",
sampleBaseDir+"PATtuple_402_6_M1e.root",
sampleBaseDir+"PATtuple_374_5_EDs.root",
sampleBaseDir+"PATtuple_370_6_q2f.root",
sampleBaseDir+"PATtuple_513_8_T9w.root",
sampleBaseDir+"PATtuple_347_6_ZK6.root",
sampleBaseDir+"PATtuple_478_6_FM5.root",
sampleBaseDir+"PATtuple_283_6_zwq.root",
sampleBaseDir+"PATtuple_445_8_gLU.root",
sampleBaseDir+"PATtuple_346_6_Eda.root",
sampleBaseDir+"PATtuple_126_3_4bX.root",
sampleBaseDir+"PATtuple_327_5_sYw.root",
sampleBaseDir+"PATtuple_353_6_PkO.root",
sampleBaseDir+"PATtuple_434_8_N64.root",
sampleBaseDir+"PATtuple_435_8_qOT.root",
sampleBaseDir+"PATtuple_247_4_Yn5.root",
sampleBaseDir+"PATtuple_408_6_tVm.root",
sampleBaseDir+"PATtuple_354_6_ogr.root",
sampleBaseDir+"PATtuple_162_1_BfT.root",
sampleBaseDir+"PATtuple_265_5_umg.root",
sampleBaseDir+"PATtuple_252_4_19I.root",
sampleBaseDir+"PATtuple_298_5_Mcx.root",
sampleBaseDir+"PATtuple_392_6_ajZ.root",
sampleBaseDir+"PATtuple_358_6_MUb.root",
sampleBaseDir+"PATtuple_137_3_Dvk.root",
sampleBaseDir+"PATtuple_345_6_JJI.root",
sampleBaseDir+"PATtuple_410_6_5zS.root",
sampleBaseDir+"PATtuple_134_3_ML7.root",
sampleBaseDir+"PATtuple_135_3_q9e.root",
sampleBaseDir+"PATtuple_285_5_g0S.root",
sampleBaseDir+"PATtuple_494_6_tk1.root",
sampleBaseDir+"PATtuple_375_6_rUZ.root",
sampleBaseDir+"PATtuple_371_6_hNr.root",
sampleBaseDir+"PATtuple_452_6_Dww.root",
sampleBaseDir+"PATtuple_217_3_uhW.root",
sampleBaseDir+"PATtuple_359_5_PGi.root",
sampleBaseDir+"PATtuple_267_5_Mtn.root",
sampleBaseDir+"PATtuple_501_2_pPq.root",
sampleBaseDir+"PATtuple_603_2_mgR.root",
sampleBaseDir+"PATtuple_538_1_2bC.root",
sampleBaseDir+"PATtuple_67_0_xFO.root",
sampleBaseDir+"PATtuple_625_2_LEe.root",
sampleBaseDir+"PATtuple_421_2_Qas.root",
sampleBaseDir+"PATtuple_318_2_fY2.root",
sampleBaseDir+"PATtuple_93_0_duw.root",
sampleBaseDir+"PATtuple_191_0_fCd.root",
sampleBaseDir+"PATtuple_458_2_nI2.root",
sampleBaseDir+"PATtuple_476_3_wY6.root",
sampleBaseDir+"PATtuple_224_0_fHD.root",
sampleBaseDir+"PATtuple_464_2_Al3.root",
sampleBaseDir+"PATtuple_295_1_KI6.root",
sampleBaseDir+"PATtuple_465_2_Mnn.root",
sampleBaseDir+"PATtuple_204_0_MN2.root",
sampleBaseDir+"PATtuple_243_0_a0J.root",
sampleBaseDir+"PATtuple_289_1_WUs.root",
sampleBaseDir+"PATtuple_218_0_E3u.root",
sampleBaseDir+"PATtuple_79_0_j3f.root",
sampleBaseDir+"PATtuple_612_2_y4V.root",
sampleBaseDir+"PATtuple_121_0_1qt.root",
sampleBaseDir+"PATtuple_219_0_6EI.root",
sampleBaseDir+"PATtuple_288_1_CuU.root",
sampleBaseDir+"PATtuple_503_2_A1W.root",
sampleBaseDir+"PATtuple_422_2_0xP.root",
sampleBaseDir+"PATtuple_46_4_AQV.root",
sampleBaseDir+"PATtuple_505_3_rHF.root",
sampleBaseDir+"PATtuple_605_3_KsB.root",
sampleBaseDir+"PATtuple_543_1_lEj.root",
sampleBaseDir+"PATtuple_143_0_pvA.root",
sampleBaseDir+"PATtuple_102_0_s28.root",
sampleBaseDir+"PATtuple_11_4_UK0.root",
sampleBaseDir+"PATtuple_610_3_NSc.root",
sampleBaseDir+"PATtuple_101_0_DCk.root",
sampleBaseDir+"PATtuple_70_0_Po0.root",
sampleBaseDir+"PATtuple_132_0_eQj.root",
sampleBaseDir+"PATtuple_230_0_RyV.root",
sampleBaseDir+"PATtuple_18_4_yFC.root",
sampleBaseDir+"PATtuple_245_0_XLd.root",
sampleBaseDir+"PATtuple_214_0_H6o.root",
sampleBaseDir+"PATtuple_480_2_IpY.root",
sampleBaseDir+"PATtuple_557_1_cC6.root",
sampleBaseDir+"PATtuple_502_2_wph.root",
sampleBaseDir+"PATtuple_119_0_rDE.root",
sampleBaseDir+"PATtuple_73_0_TJg.root",
sampleBaseDir+"PATtuple_6_4_jzm.root",
sampleBaseDir+"PATtuple_231_0_yEJ.root",
sampleBaseDir+"PATtuple_506_2_xGn.root",
sampleBaseDir+"PATtuple_106_0_omw.root",
sampleBaseDir+"PATtuple_227_0_qOY.root",
sampleBaseDir+"PATtuple_103_0_ZZ5.root",
sampleBaseDir+"PATtuple_482_2_7yS.root",
sampleBaseDir+"PATtuple_571_1_Z9k.root",
sampleBaseDir+"PATtuple_286_1_QQo.root",
sampleBaseDir+"PATtuple_68_0_9mK.root",
sampleBaseDir+"PATtuple_45_4_aVJ.root",
sampleBaseDir+"PATtuple_75_0_ZyC.root",
sampleBaseDir+"PATtuple_499_2_r7N.root",
sampleBaseDir+"PATtuple_558_1_tAJ.root",
sampleBaseDir+"PATtuple_23_4_R8Z.root",
sampleBaseDir+"PATtuple_107_0_CfY.root",
sampleBaseDir+"PATtuple_69_0_OF4.root",
sampleBaseDir+"PATtuple_148_0_dPP.root",
sampleBaseDir+"PATtuple_96_0_h6o.root",
sampleBaseDir+"PATtuple_117_0_oLn.root",
sampleBaseDir+"PATtuple_258_0_DwY.root",
sampleBaseDir+"PATtuple_63_0_W7j.root",
sampleBaseDir+"PATtuple_33_4_9Ku.root",
sampleBaseDir+"PATtuple_563_2_tJ6.root",
sampleBaseDir+"PATtuple_490_2_NAJ.root",
sampleBaseDir+"PATtuple_124_0_D3n.root",
sampleBaseDir+"PATtuple_123_0_9Sh.root",
sampleBaseDir+"PATtuple_72_0_7KH.root",
sampleBaseDir+"PATtuple_297_1_UxF.root",
sampleBaseDir+"PATtuple_493_2_Neh.root",
sampleBaseDir+"PATtuple_316_1_Dr2.root",
sampleBaseDir+"PATtuple_30_4_kZ0.root",
sampleBaseDir+"PATtuple_561_1_Uzj.root",
sampleBaseDir+"PATtuple_504_2_WgO.root",
sampleBaseDir+"PATtuple_55_4_pF9.root",
sampleBaseDir+"PATtuple_35_4_gUV.root",
sampleBaseDir+"PATtuple_636_8_Jjv.root",
sampleBaseDir+"PATtuple_637_8_eEU.root",
sampleBaseDir+"PATtuple_632_8_hf6.root",
sampleBaseDir+"PATtuple_439_8_NGj.root",
sampleBaseDir+"PATtuple_638_8_F7j.root",
sampleBaseDir+"PATtuple_351_8_QZr.root",
sampleBaseDir+"PATtuple_518_8_9UI.root",
sampleBaseDir+"PATtuple_350_8_GOm.root",
sampleBaseDir+"PATtuple_349_8_A3h.root",
sampleBaseDir+"PATtuple_409_7_geO.root",
sampleBaseDir+"PATtuple_526_8_U2Z.root",
sampleBaseDir+"PATtuple_521_8_UFP.root",
sampleBaseDir+"PATtuple_635_8_yA8.root",
sampleBaseDir+"PATtuple_628_8_pWj.root",
sampleBaseDir+"PATtuple_514_6_el3.root",
sampleBaseDir+"PATtuple_366_8_pgs.root",
sampleBaseDir+"PATtuple_413_6_pqb.root",
sampleBaseDir+"PATtuple_438_8_yUY.root",
sampleBaseDir+"PATtuple_448_8_Xnf.root",
sampleBaseDir+"PATtuple_524_8_apD.root",
sampleBaseDir+"PATtuple_633_8_eFE.root",
sampleBaseDir+"PATtuple_629_8_iQr.root",
sampleBaseDir+"PATtuple_436_8_J0r.root",
sampleBaseDir+"PATtuple_522_8_p8b.root",
sampleBaseDir+"PATtuple_527_8_L5c.root",
sampleBaseDir+"PATtuple_544_6_aFG.root",
sampleBaseDir+"PATtuple_344_8_RSs.root",
sampleBaseDir+"PATtuple_368_8_yjG.root",
sampleBaseDir+"PATtuple_630_8_M6n.root",
sampleBaseDir+"PATtuple_440_8_3D0.root",
sampleBaseDir+"PATtuple_399_6_8rP.root",
sampleBaseDir+"PATtuple_352_6_yTH.root",
sampleBaseDir+"PATtuple_620_8_LtR.root",
sampleBaseDir+"PATtuple_437_8_AMI.root",
sampleBaseDir+"PATtuple_530_8_qdV.root",
sampleBaseDir+"PATtuple_403_6_Csj.root",
sampleBaseDir+"PATtuple_516_6_TGt.root",
sampleBaseDir+"PATtuple_639_8_iKo.root",
sampleBaseDir+"PATtuple_414_6_1Js.root",
sampleBaseDir+"PATtuple_616_8_JOw.root",
sampleBaseDir+"PATtuple_615_8_YNF.root",
sampleBaseDir+"PATtuple_186_1_DTq.root",
sampleBaseDir+"PATtuple_239_0_oqo.root",
sampleBaseDir+"PATtuple_157_0_kbq.root",
sampleBaseDir+"PATtuple_387_2_Hdr.root",
sampleBaseDir+"PATtuple_59_0_3oj.root",
sampleBaseDir+"PATtuple_189_0_uUq.root",
sampleBaseDir+"PATtuple_92_0_IrV.root",
sampleBaseDir+"PATtuple_415_3_L7e.root",
sampleBaseDir+"PATtuple_601_3_q3E.root",
sampleBaseDir+"PATtuple_627_3_Vqu.root",
sampleBaseDir+"PATtuple_477_3_6jG.root",
sampleBaseDir+"PATtuple_606_3_Js5.root",
sampleBaseDir+"PATtuple_77_0_l7V.root",
sampleBaseDir+"PATtuple_539_1_xO5.root",
sampleBaseDir+"PATtuple_249_0_PJM.root",
sampleBaseDir+"PATtuple_320_2_yto.root",
sampleBaseDir+"PATtuple_418_3_ork.root",
sampleBaseDir+"PATtuple_479_2_BAC.root",
sampleBaseDir+"PATtuple_332_1_JcE.root",
sampleBaseDir+"PATtuple_60_0_YSb.root",
sampleBaseDir+"PATtuple_61_0_uIn.root",
sampleBaseDir+"PATtuple_423_2_apd.root",
sampleBaseDir+"PATtuple_290_1_oUa.root",
sampleBaseDir+"PATtuple_314_2_cAX.root",
sampleBaseDir+"PATtuple_242_0_6tw.root",
sampleBaseDir+"PATtuple_329_1_9iD.root",
sampleBaseDir+"PATtuple_248_0_0Fa.root",
sampleBaseDir+"PATtuple_237_0_YpR.root",
sampleBaseDir+"PATtuple_66_0_BCr.root",
sampleBaseDir+"PATtuple_17_2_4qN.root",
sampleBaseDir+"PATtuple_417_2_Crq.root",
sampleBaseDir+"PATtuple_238_0_K2o.root",
sampleBaseDir+"PATtuple_228_0_O7x.root",
sampleBaseDir+"PATtuple_80_0_Aac.root",
sampleBaseDir+"PATtuple_220_0_AJW.root",
sampleBaseDir+"PATtuple_172_0_fLP.root",
sampleBaseDir+"PATtuple_287_1_nYh.root",
sampleBaseDir+"PATtuple_294_1_vlF.root",
sampleBaseDir+"PATtuple_624_2_bdM.root",
sampleBaseDir+"PATtuple_567_2_G5I.root",
sampleBaseDir+"PATtuple_236_0_rOC.root",
sampleBaseDir+"PATtuple_420_2_fGc.root",
sampleBaseDir+"PATtuple_187_1_XTm.root",
sampleBaseDir+"PATtuple_581_1_1kG.root",
sampleBaseDir+"PATtuple_459_2_vKR.root",
sampleBaseDir+"PATtuple_328_2_ixV.root",
sampleBaseDir+"PATtuple_180_0_peQ.root",
sampleBaseDir+"PATtuple_212_1_aWc.root",
sampleBaseDir+"PATtuple_146_0_VfV.root",
sampleBaseDir+"PATtuple_474_2_gcZ.root",
sampleBaseDir+"PATtuple_113_0_5GJ.root",
sampleBaseDir+"PATtuple_64_0_Kfj.root",
sampleBaseDir+"PATtuple_71_0_73p.root",
sampleBaseDir+"PATtuple_109_0_k3B.root",
sampleBaseDir+"PATtuple_234_0_jbQ.root",
sampleBaseDir+"PATtuple_223_0_hNq.root",
sampleBaseDir+"PATtuple_545_1_7M6.root",
sampleBaseDir+"PATtuple_47_4_tsl.root",
sampleBaseDir+"PATtuple_42_4_BPA.root",
sampleBaseDir+"PATtuple_485_2_8Q0.root",
sampleBaseDir+"PATtuple_34_4_5Cv.root",
sampleBaseDir+"PATtuple_211_0_Uo9.root",
sampleBaseDir+"PATtuple_108_0_jUQ.root",
sampleBaseDir+"PATtuple_569_1_9Yf.root",
sampleBaseDir+"PATtuple_48_4_9ex.root",
sampleBaseDir+"PATtuple_31_4_Cr2.root",
sampleBaseDir+"PATtuple_28_4_oSf.root",
sampleBaseDir+"PATtuple_201_0_EaG.root",
sampleBaseDir+"PATtuple_49_4_Yhu.root",
sampleBaseDir+"PATtuple_65_0_DUh.root",
sampleBaseDir+"PATtuple_54_4_4M3.root",
sampleBaseDir+"PATtuple_213_0_d00.root",
sampleBaseDir+"PATtuple_110_0_U6I.root",
sampleBaseDir+"PATtuple_112_0_40C.root",
sampleBaseDir+"PATtuple_531_2_HNo.root",
sampleBaseDir+"PATtuple_111_0_pMU.root",
sampleBaseDir+"PATtuple_515_3_FBZ.root",
sampleBaseDir+"PATtuple_609_2_c0t.root",
sampleBaseDir+"PATtuple_104_0_lkn.root",
sampleBaseDir+"PATtuple_324_1_VQO.root",
sampleBaseDir+"PATtuple_229_0_PAb.root",
sampleBaseDir+"PATtuple_116_0_mJm.root",
sampleBaseDir+"PATtuple_262_2_W6F.root",
sampleBaseDir+"PATtuple_225_0_3tr.root",
sampleBaseDir+"PATtuple_246_0_CKi.root",
sampleBaseDir+"PATtuple_607_2_r8l.root",
sampleBaseDir+"PATtuple_293_2_5qJ.root",
sampleBaseDir+"PATtuple_313_1_pmF.root",
sampleBaseDir+"PATtuple_525_3_aau.root",
sampleBaseDir+"PATtuple_497_2_Afd.root",
sampleBaseDir+"PATtuple_500_2_2oK.root",
sampleBaseDir+"PATtuple_589_3_BVb.root",
sampleBaseDir+"PATtuple_330_2_LN3.root",
sampleBaseDir+"PATtuple_367_2_xWX.root",
sampleBaseDir+"PATtuple_118_0_fr2.root",
sampleBaseDir+"PATtuple_120_0_ePv.root",
sampleBaseDir+"PATtuple_496_2_WDW.root",
sampleBaseDir+"PATtuple_631_8_niu.root",
sampleBaseDir+"PATtuple_528_8_VNx.root",
sampleBaseDir+"PATtuple_389_5_FT8.root",
sampleBaseDir+"PATtuple_622_8_WGX.root",
sampleBaseDir+"PATtuple_529_8_fe1.root",
sampleBaseDir+"PATtuple_562_6_1Rd.root",
sampleBaseDir+"PATtuple_401_7_hOw.root",
sampleBaseDir+"PATtuple_523_8_lOz.root",
sampleBaseDir+"PATtuple_520_8_mLG.root",
sampleBaseDir+"PATtuple_163_0_OS5.root",
sampleBaseDir+"PATtuple_10_2_BVP.root",
sampleBaseDir+"PATtuple_122_0_KWW.root",
sampleBaseDir+"PATtuple_291_2_CTT.root",
sampleBaseDir+"PATtuple_430_3_YGL.root",
sampleBaseDir+"PATtuple_431_2_fF6.root",
sampleBaseDir+"PATtuple_174_0_c6S.root",
sampleBaseDir+"PATtuple_469_2_meM.root",
sampleBaseDir+"PATtuple_56_4_YsA.root",
sampleBaseDir+"PATtuple_498_2_sog.root",
sampleBaseDir+"PATtuple_317_2_f4M.root",
sampleBaseDir+"PATtuple_197_0_KTJ.root",
sampleBaseDir+"PATtuple_560_1_qc1.root",
sampleBaseDir+"PATtuple_582_1_TOk.root",
sampleBaseDir+"PATtuple_559_1_jaU.root",
sampleBaseDir+"PATtuple_251_0_h2h.root",
sampleBaseDir+"PATtuple_468_2_c0L.root",
sampleBaseDir+"PATtuple_257_0_IFm.root",
sampleBaseDir+"PATtuple_481_2_8Bx.root",
sampleBaseDir+"PATtuple_159_0_n9a.root",
sampleBaseDir+"PATtuple_598_2_Ens.root",
sampleBaseDir+"PATtuple_222_0_NFK.root",
sampleBaseDir+"PATtuple_348_2_kO7.root",
sampleBaseDir+"PATtuple_325_1_3cC.root",
sampleBaseDir+"PATtuple_333_2_lGk.root",
sampleBaseDir+"PATtuple_43_2_nBO.root",
sampleBaseDir+"PATtuple_604_2_oJG.root",
sampleBaseDir+"PATtuple_315_1_7c0.root",
sampleBaseDir+"PATtuple_266_2_QY0.root",
sampleBaseDir+"PATtuple_614_2_io7.root",
sampleBaseDir+"PATtuple_50_4_2Nb.root",
sampleBaseDir+"PATtuple_62_0_fRV.root",
sampleBaseDir+"PATtuple_36_4_5EL.root",
sampleBaseDir+"PATtuple_41_4_vIY.root",
sampleBaseDir+"PATtuple_86_0_rFP.root",
sampleBaseDir+"PATtuple_27_4_za7.root",
sampleBaseDir+"PATtuple_74_0_I02.root",
sampleBaseDir+"PATtuple_114_0_D4U.root",
sampleBaseDir+"PATtuple_115_0_jeq.root",
sampleBaseDir+"PATtuple_9_2_10W.root",
sampleBaseDir+"PATtuple_292_1_zGt.root",
sampleBaseDir+"PATtuple_343_2_Mvz.root",
sampleBaseDir+"PATtuple_133_0_2Rr.root",
sampleBaseDir+"PATtuple_412_2_CUG.root",
sampleBaseDir+"PATtuple_32_3_INA.root",
sampleBaseDir+"PATtuple_363_2_kYp.root",
sampleBaseDir+"PATtuple_372_2_oh1.root",
sampleBaseDir+"PATtuple_634_3_fFU.root",
sampleBaseDir+"PATtuple_600_2_u6Q.root",
sampleBaseDir+"PATtuple_568_1_Mzx.root",
sampleBaseDir+"PATtuple_95_0_m32.root",
sampleBaseDir+"PATtuple_40_2_ciB.root",
sampleBaseDir+"PATtuple_161_0_UHZ.root",
sampleBaseDir+"PATtuple_471_2_Hru.root",
sampleBaseDir+"PATtuple_519_2_msU.root",
sampleBaseDir+"PATtuple_98_0_F0z.root",
sampleBaseDir+"PATtuple_536_2_QxS.root",
sampleBaseDir+"PATtuple_57_3_rxw.root",
sampleBaseDir+"PATtuple_566_2_0ov.root",
sampleBaseDir+"PATtuple_100_0_ofu.root",
sampleBaseDir+"PATtuple_592_1_p06.root",
sampleBaseDir+"PATtuple_19_3_b63.root",
sampleBaseDir+"PATtuple_386_1_djI.root",
sampleBaseDir+"PATtuple_608_2_3ya.root",
sampleBaseDir+"PATtuple_22_3_l9d.root",
sampleBaseDir+"PATtuple_51_3_XFM.root",
sampleBaseDir+"PATtuple_599_2_c4D.root",
sampleBaseDir+"PATtuple_255_0_CL6.root",
sampleBaseDir+"PATtuple_326_1_nPZ.root",
sampleBaseDir+"PATtuple_579_1_YE0.root",
sampleBaseDir+"PATtuple_381_1_NNd.root",
sampleBaseDir+"PATtuple_432_2_Q7Z.root",
sampleBaseDir+"PATtuple_617_2_TEJ.root",
sampleBaseDir+"PATtuple_52_3_LJU.root",
sampleBaseDir+"PATtuple_377_1_6yB.root",
sampleBaseDir+"PATtuple_155_0_G1a.root",
sampleBaseDir+"PATtuple_81_0_cHV.root",
sampleBaseDir+"PATtuple_83_0_oAW.root",
sampleBaseDir+"PATtuple_470_2_6Yw.root",
sampleBaseDir+"PATtuple_491_2_mg6.root",
sampleBaseDir+"PATtuple_84_0_vH9.root",
sampleBaseDir+"PATtuple_256_0_MkQ.root",
sampleBaseDir+"PATtuple_232_0_kBS.root",
sampleBaseDir+"PATtuple_382_1_p5k.root",
sampleBaseDir+"PATtuple_376_1_fkl.root",
sampleBaseDir+"PATtuple_160_0_mRL.root",
sampleBaseDir+"PATtuple_300_1_60x.root",
sampleBaseDir+"PATtuple_165_0_jxy.root",
sampleBaseDir+"PATtuple_580_1_jg9.root",
sampleBaseDir+"PATtuple_12_1_Y2j.root",
sampleBaseDir+"PATtuple_533_2_0Xo.root",
sampleBaseDir+"PATtuple_29_2_NTJ.root",
sampleBaseDir+"PATtuple_535_2_gnA.root",
sampleBaseDir+"PATtuple_532_2_wAY.root",
sampleBaseDir+"PATtuple_534_2_nst.root",
sampleBaseDir+"PATtuple_1_1_UD8.root",
sampleBaseDir+"PATtuple_310_1_MmA.root",
sampleBaseDir+"PATtuple_301_1_rcg.root",
sampleBaseDir+"PATtuple_7_1_HM7.root",
sampleBaseDir+"PATtuple_492_2_WUr.root",
sampleBaseDir+"PATtuple_91_0_3Qs.root",
sampleBaseDir+"PATtuple_198_0_A3f.root",
sampleBaseDir+"PATtuple_541_1_X9e.root",
sampleBaseDir+"PATtuple_546_1_117.root",
sampleBaseDir+"PATtuple_311_1_L0G.root",
sampleBaseDir+"PATtuple_24_1_kOy.root",
sampleBaseDir+"PATtuple_540_1_c5L.root",
sampleBaseDir+"PATtuple_537_1_ATx.root",
sampleBaseDir+"PATtuple_302_1_vHx.root",
sampleBaseDir+"PATtuple_145_0_DMR.root",
sampleBaseDir+"PATtuple_216_0_lhV.root",
sampleBaseDir+"PATtuple_269_2_Pms.root",
sampleBaseDir+"PATtuple_623_2_0Kw.root",
sampleBaseDir+"PATtuple_25_1_50t.root",
sampleBaseDir+"PATtuple_575_1_dRT.root",
sampleBaseDir+"PATtuple_307_1_3UY.root",
sampleBaseDir+"PATtuple_596_1_fbj.root",
sampleBaseDir+"PATtuple_312_1_2dz.root",
sampleBaseDir+"PATtuple_547_1_Oqw.root",
sampleBaseDir+"PATtuple_309_1_GPe.root",
sampleBaseDir+"PATtuple_379_1_VK9.root",
sampleBaseDir+"PATtuple_564_1_6Yi.root",
sampleBaseDir+"PATtuple_380_1_q4V.root",
sampleBaseDir+"PATtuple_594_1_ZSd.root",
sampleBaseDir+"PATtuple_305_1_0QI.root",
sampleBaseDir+"PATtuple_179_0_4Zx.root",
sampleBaseDir+"PATtuple_586_1_GRf.root",
sampleBaseDir+"PATtuple_378_1_bYs.root",
sampleBaseDir+"PATtuple_551_1_7cF.root",
sampleBaseDir+"PATtuple_58_3_FUs.root",
sampleBaseDir+"PATtuple_173_0_mi1.root",
sampleBaseDir+"PATtuple_82_0_6iy.root",
sampleBaseDir+"PATtuple_140_0_PDM.root",
sampleBaseDir+"PATtuple_548_1_3Sc.root",
sampleBaseDir+"PATtuple_150_0_QKJ.root",
sampleBaseDir+"PATtuple_553_1_ZTz.root",
sampleBaseDir+"PATtuple_306_1_8vC.root",
sampleBaseDir+"PATtuple_149_0_QEq.root",
sampleBaseDir+"PATtuple_585_1_viK.root",
sampleBaseDir+"PATtuple_308_1_erY.root",
sampleBaseDir+"PATtuple_87_0_tSq.root",
sampleBaseDir+"PATtuple_168_0_a1b.root",
sampleBaseDir+"PATtuple_550_1_TMW.root",
sampleBaseDir+"PATtuple_626_2_0uo.root",
sampleBaseDir+"PATtuple_53_3_qR5.root",
sampleBaseDir+"PATtuple_584_1_L1n.root",
sampleBaseDir+"PATtuple_233_0_2Lu.root",
sampleBaseDir+"PATtuple_576_1_pZH.root",
sampleBaseDir+"PATtuple_205_0_drj.root",
sampleBaseDir+"PATtuple_4_2_Glh.root",
sampleBaseDir+"PATtuple_206_0_H6C.root",
sampleBaseDir+"PATtuple_235_0_y7v.root",
sampleBaseDir+"PATtuple_181_0_gD5.root",
sampleBaseDir+"PATtuple_8_1_Qgo.root",
sampleBaseDir+"PATtuple_192_0_TCZ.root",
sampleBaseDir+"PATtuple_595_1_mYr.root",
sampleBaseDir+"PATtuple_5_1_uhr.root",
sampleBaseDir+"PATtuple_97_0_R5m.root",
sampleBaseDir+"PATtuple_549_1_OV3.root",
sampleBaseDir+"PATtuple_182_0_qqG.root",
sampleBaseDir+"PATtuple_583_1_WIa.root",
sampleBaseDir+"PATtuple_15_1_oAv.root",
sampleBaseDir+"PATtuple_195_0_n16.root",
sampleBaseDir+"PATtuple_574_1_YBF.root",
sampleBaseDir+"PATtuple_183_0_8cD.root",
sampleBaseDir+"PATtuple_573_1_sCi.root",
sampleBaseDir+"PATtuple_26_1_G7J.root",
sampleBaseDir+"PATtuple_577_1_8Ba.root",
sampleBaseDir+"PATtuple_176_0_iev.root",
sampleBaseDir+"PATtuple_13_1_ZrK.root",
sampleBaseDir+"PATtuple_151_0_C2Q.root",
sampleBaseDir+"PATtuple_3_1_Lsd.root",
sampleBaseDir+"PATtuple_336_1_mTU.root",
sampleBaseDir+"PATtuple_175_0_X03.root",
sampleBaseDir+"PATtuple_85_0_53t.root",
sampleBaseDir+"PATtuple_16_1_Qde.root",
sampleBaseDir+"PATtuple_2_1_RCu.root",
sampleBaseDir+"PATtuple_335_1_3FJ.root",
sampleBaseDir+"PATtuple_88_0_bCq.root",
sampleBaseDir+"PATtuple_14_1_G0M.root",
sampleBaseDir+"PATtuple_166_0_XfS.root",
sampleBaseDir+"PATtuple_552_1_6YL.root",
sampleBaseDir+"PATtuple_200_0_7ER.root",
sampleBaseDir+"PATtuple_154_0_HgY.root",
sampleBaseDir+"PATtuple_156_0_nMj.root",
sampleBaseDir+"PATtuple_208_0_g3C.root",
sampleBaseDir+"PATtuple_207_0_0Pb.root",
sampleBaseDir+"PATtuple_142_0_dUr.root",
sampleBaseDir+"PATtuple_240_0_2Oq.root",
sampleBaseDir+"PATtuple_467_2_94Q.root",
sampleBaseDir+"PATtuple_38_2_cp8.root",
sampleBaseDir+"PATtuple_39_2_UnL.root",
sampleBaseDir+"PATtuple_572_2_57l.root",
sampleBaseDir+"PATtuple_488_2_ZPu.root",
sampleBaseDir+"PATtuple_565_2_CEc.root",
sampleBaseDir+"PATtuple_304_1_fZ5.root",
sampleBaseDir+"PATtuple_593_2_grK.root",
sampleBaseDir+"PATtuple_334_1_Sxj.root",
sampleBaseDir+"PATtuple_613_2_abY.root",
sampleBaseDir+"PATtuple_433_2_xjn.root",
sampleBaseDir+"PATtuple_591_1_tqP.root",
sampleBaseDir+"PATtuple_153_0_WNS.root",
sampleBaseDir+"PATtuple_152_0_UXo.root",
sampleBaseDir+"PATtuple_170_0_XTt.root",
sampleBaseDir+"PATtuple_178_0_AAe.root",
sampleBaseDir+"PATtuple_199_0_Ps6.root",
sampleBaseDir+"PATtuple_184_0_W0N.root",
sampleBaseDir+"PATtuple_177_0_ZJt.root",
sampleBaseDir+"PATtuple_169_0_Gsm.root",
sampleBaseDir+"PATtuple_76_0_Ib2.root",
sampleBaseDir+"PATtuple_90_0_7RK.root",
sampleBaseDir+"PATtuple_185_0_ts2.root",
sampleBaseDir+"PATtuple_89_0_zSL.root",
]