sampleDataSet = '/DoubleMuParked/Run2012D-22Jan2013-v1/AOD'

# original (i.e. RECO file) release,
# not the one we plan to process them with
sampleRelease = "CMSSW_5_3_7_patch5" 
# release used to create new files with
sampleProcessRelease = "CMSSW_5_3_8" 

sampleNumEvents = 38006513 # according to DBS, as of 13 October 2013

# global tag needs to be chosen to match release, trigger menu and alignment conditions.
# see https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions
sampleGlobalTag = 'FT_53_V21_AN3::All'

# data quality run/lumi section selection
sampleJSON = "https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions12/8TeV/Reprocessing/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON_MuonPhys.txt"

# restrict run range (mainly to get a sample with consistent trigger configuration)

# use checkAllFilesOpened whenever possible, and noDuplicateCheck when necessary
sampleDuplicateCheckMode = "checkAllFilesOpened"

# "DATA" or "MC"
sampleType = "DATA"





samplePatDBSName=""

sampleBaseDir="file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Data_Mu_Run2012D22Jan_pat_20140327/demattia//DoubleMuParked/Data_Mu_Run2012D22Jan_pat_20140327/ce2ef5771b8bd3b63b0f9db075cc5761/"
samplePatFiles = [
sampleBaseDir+"PATtuple_100_1_mzH.root",
sampleBaseDir+"PATtuple_100_1_y5p.root",
sampleBaseDir+"PATtuple_101_1_ZMt.root",
sampleBaseDir+"PATtuple_102_1_So3.root",
sampleBaseDir+"PATtuple_103_1_k5x.root",
sampleBaseDir+"PATtuple_104_1_rSB.root",
sampleBaseDir+"PATtuple_105_1_Szb.root",
sampleBaseDir+"PATtuple_106_1_k6J.root",
sampleBaseDir+"PATtuple_107_1_9Vj.root",
sampleBaseDir+"PATtuple_108_1_SVv.root",
sampleBaseDir+"PATtuple_109_1_oVp.root",
sampleBaseDir+"PATtuple_10_2_LLd.root",
sampleBaseDir+"PATtuple_110_1_yH9.root",
sampleBaseDir+"PATtuple_111_1_EKz.root",
sampleBaseDir+"PATtuple_112_1_hYP.root",
sampleBaseDir+"PATtuple_113_1_T6R.root",
sampleBaseDir+"PATtuple_114_2_Rp0.root",
sampleBaseDir+"PATtuple_115_1_ziW.root",
sampleBaseDir+"PATtuple_116_1_Ikc.root",
sampleBaseDir+"PATtuple_117_1_e5Y.root",
sampleBaseDir+"PATtuple_118_1_GaN.root",
sampleBaseDir+"PATtuple_119_1_9ni.root",
sampleBaseDir+"PATtuple_11_1_GsP.root",
sampleBaseDir+"PATtuple_120_1_eQL.root",
sampleBaseDir+"PATtuple_121_1_6V3.root",
sampleBaseDir+"PATtuple_122_1_HEk.root",
sampleBaseDir+"PATtuple_123_1_QDb.root",
sampleBaseDir+"PATtuple_124_1_ZuP.root",
sampleBaseDir+"PATtuple_125_1_2BT.root",
sampleBaseDir+"PATtuple_126_1_5PT.root",
sampleBaseDir+"PATtuple_127_1_wbf.root",
sampleBaseDir+"PATtuple_127_1_yhZ.root",
sampleBaseDir+"PATtuple_128_1_oGE.root",
sampleBaseDir+"PATtuple_129_1_oB4.root",
sampleBaseDir+"PATtuple_12_1_qAK.root",
sampleBaseDir+"PATtuple_130_1_01A.root",
sampleBaseDir+"PATtuple_131_1_fGg.root",
sampleBaseDir+"PATtuple_131_1_k7x.root",
sampleBaseDir+"PATtuple_132_1_GdV.root",
sampleBaseDir+"PATtuple_132_2_yRB.root",
sampleBaseDir+"PATtuple_133_1_2Eg.root",
sampleBaseDir+"PATtuple_133_1_wsg.root",
sampleBaseDir+"PATtuple_134_1_MVa.root",
sampleBaseDir+"PATtuple_134_1_xWp.root",
sampleBaseDir+"PATtuple_135_1_4q7.root",
sampleBaseDir+"PATtuple_135_1_JjV.root",
sampleBaseDir+"PATtuple_136_1_tlW.root",
sampleBaseDir+"PATtuple_137_1_q2w.root",
sampleBaseDir+"PATtuple_138_1_ZtC.root",
sampleBaseDir+"PATtuple_138_1_ZxS.root",
sampleBaseDir+"PATtuple_139_1_pdK.root",
sampleBaseDir+"PATtuple_139_2_hUK.root",
sampleBaseDir+"PATtuple_13_1_8Sc.root",
sampleBaseDir+"PATtuple_140_1_IJV.root",
sampleBaseDir+"PATtuple_140_1_ySz.root",
sampleBaseDir+"PATtuple_141_1_v58.root",
sampleBaseDir+"PATtuple_142_1_QTf.root",
sampleBaseDir+"PATtuple_142_1_R0w.root",
sampleBaseDir+"PATtuple_143_1_Rny.root",
sampleBaseDir+"PATtuple_144_1_Ciy.root",
sampleBaseDir+"PATtuple_144_1_fV4.root",
sampleBaseDir+"PATtuple_145_2_z38.root",
sampleBaseDir+"PATtuple_146_1_10u.root",
sampleBaseDir+"PATtuple_146_1_OeJ.root",
sampleBaseDir+"PATtuple_147_1_MER.root",
sampleBaseDir+"PATtuple_147_1_whm.root",
sampleBaseDir+"PATtuple_148_1_HwW.root",
sampleBaseDir+"PATtuple_148_1_V33.root",
sampleBaseDir+"PATtuple_149_1_0Na.root",
sampleBaseDir+"PATtuple_149_1_4Ih.root",
sampleBaseDir+"PATtuple_14_1_AvS.root",
sampleBaseDir+"PATtuple_150_1_4ur.root",
sampleBaseDir+"PATtuple_150_1_5fN.root",
sampleBaseDir+"PATtuple_151_1_OkC.root",
sampleBaseDir+"PATtuple_151_1_cmg.root",
sampleBaseDir+"PATtuple_152_1_lww.root",
sampleBaseDir+"PATtuple_152_1_oV5.root",
sampleBaseDir+"PATtuple_153_1_ZbE.root",
sampleBaseDir+"PATtuple_154_1_VoQ.root",
sampleBaseDir+"PATtuple_155_3_RyP.root",
sampleBaseDir+"PATtuple_156_1_UW6.root",
sampleBaseDir+"PATtuple_156_2_F54.root",
sampleBaseDir+"PATtuple_157_1_Fd2.root",
sampleBaseDir+"PATtuple_157_1_nze.root",
sampleBaseDir+"PATtuple_158_1_vOu.root",
sampleBaseDir+"PATtuple_159_1_0ES.root",
sampleBaseDir+"PATtuple_15_1_QlC.root",
sampleBaseDir+"PATtuple_160_1_z5C.root",
sampleBaseDir+"PATtuple_161_1_2J0.root",
sampleBaseDir+"PATtuple_161_1_3vy.root",
sampleBaseDir+"PATtuple_162_1_Am9.root",
sampleBaseDir+"PATtuple_163_1_aJ7.root",
sampleBaseDir+"PATtuple_164_1_rcJ.root",
sampleBaseDir+"PATtuple_165_1_A5j.root",
sampleBaseDir+"PATtuple_166_1_YOx.root",
sampleBaseDir+"PATtuple_166_1_fcz.root",
sampleBaseDir+"PATtuple_167_1_wHv.root",
sampleBaseDir+"PATtuple_168_1_ijJ.root",
sampleBaseDir+"PATtuple_168_1_mc2.root",
sampleBaseDir+"PATtuple_169_1_38h.root",
sampleBaseDir+"PATtuple_16_1_zDn.root",
sampleBaseDir+"PATtuple_170_1_UA8.root",
sampleBaseDir+"PATtuple_171_1_BTe.root",
sampleBaseDir+"PATtuple_172_3_2sk.root",
sampleBaseDir+"PATtuple_172_3_apx.root",
sampleBaseDir+"PATtuple_173_1_e8k.root",
sampleBaseDir+"PATtuple_174_1_Di9.root",
sampleBaseDir+"PATtuple_175_1_Gtj.root",
sampleBaseDir+"PATtuple_176_1_5g3.root",
sampleBaseDir+"PATtuple_176_1_slS.root",
sampleBaseDir+"PATtuple_177_1_M08.root",
sampleBaseDir+"PATtuple_178_1_WXJ.root",
sampleBaseDir+"PATtuple_179_1_FSm.root",
sampleBaseDir+"PATtuple_17_1_wS4.root",
sampleBaseDir+"PATtuple_180_1_bF5.root",
sampleBaseDir+"PATtuple_180_1_xYi.root",
sampleBaseDir+"PATtuple_181_1_3hd.root",
sampleBaseDir+"PATtuple_182_2_UmE.root",
sampleBaseDir+"PATtuple_183_1_bNr.root",
sampleBaseDir+"PATtuple_184_2_qYg.root",
sampleBaseDir+"PATtuple_185_1_eGh.root",
sampleBaseDir+"PATtuple_186_2_ba8.root",
sampleBaseDir+"PATtuple_187_1_FPf.root",
sampleBaseDir+"PATtuple_188_1_TiA.root",
sampleBaseDir+"PATtuple_189_1_sVu.root",
sampleBaseDir+"PATtuple_18_1_9rr.root",
sampleBaseDir+"PATtuple_190_1_aK8.root",
sampleBaseDir+"PATtuple_191_1_EgT.root",
sampleBaseDir+"PATtuple_192_1_JsX.root",
sampleBaseDir+"PATtuple_193_1_Lh9.root",
sampleBaseDir+"PATtuple_194_1_2mx.root",
sampleBaseDir+"PATtuple_195_1_ZbV.root",
sampleBaseDir+"PATtuple_196_1_NwA.root",
sampleBaseDir+"PATtuple_197_1_Gu6.root",
sampleBaseDir+"PATtuple_198_1_yP5.root",
sampleBaseDir+"PATtuple_199_1_WFO.root",
sampleBaseDir+"PATtuple_19_2_ZYl.root",
sampleBaseDir+"PATtuple_1_1_gMb.root",
sampleBaseDir+"PATtuple_200_1_SdU.root",
sampleBaseDir+"PATtuple_201_1_l78.root",
sampleBaseDir+"PATtuple_202_1_2Mp.root",
sampleBaseDir+"PATtuple_203_1_stp.root",
sampleBaseDir+"PATtuple_204_1_oux.root",
sampleBaseDir+"PATtuple_205_1_dSe.root",
sampleBaseDir+"PATtuple_206_1_2sb.root",
sampleBaseDir+"PATtuple_207_1_rKr.root",
sampleBaseDir+"PATtuple_208_1_O9M.root",
sampleBaseDir+"PATtuple_209_1_FLY.root",
sampleBaseDir+"PATtuple_20_1_XFa.root",
sampleBaseDir+"PATtuple_20_3_Hms.root",
sampleBaseDir+"PATtuple_210_1_eoj.root",
sampleBaseDir+"PATtuple_211_1_2es.root",
sampleBaseDir+"PATtuple_212_1_LM4.root",
sampleBaseDir+"PATtuple_213_1_nmG.root",
sampleBaseDir+"PATtuple_214_1_6g9.root",
sampleBaseDir+"PATtuple_215_1_clZ.root",
sampleBaseDir+"PATtuple_216_1_i8v.root",
sampleBaseDir+"PATtuple_217_1_plf.root",
sampleBaseDir+"PATtuple_218_1_qre.root",
sampleBaseDir+"PATtuple_219_1_yi5.root",
sampleBaseDir+"PATtuple_219_2_wMm.root",
sampleBaseDir+"PATtuple_21_1_c2A.root",
sampleBaseDir+"PATtuple_220_1_EaZ.root",
sampleBaseDir+"PATtuple_220_1_rqg.root",
sampleBaseDir+"PATtuple_221_1_fmB.root",
sampleBaseDir+"PATtuple_222_1_euC.root",
sampleBaseDir+"PATtuple_223_1_DK1.root",
sampleBaseDir+"PATtuple_224_1_BLA.root",
sampleBaseDir+"PATtuple_225_1_T89.root",
sampleBaseDir+"PATtuple_225_1_jSW.root",
sampleBaseDir+"PATtuple_226_1_kMV.root",
sampleBaseDir+"PATtuple_227_2_Pu7.root",
sampleBaseDir+"PATtuple_228_1_nBj.root",
sampleBaseDir+"PATtuple_229_1_E8Y.root",
sampleBaseDir+"PATtuple_22_1_asJ.root",
sampleBaseDir+"PATtuple_230_1_SJT.root",
sampleBaseDir+"PATtuple_231_1_Tvp.root",
sampleBaseDir+"PATtuple_232_1_SKV.root",
sampleBaseDir+"PATtuple_232_1_lsm.root",
sampleBaseDir+"PATtuple_233_1_WgQ.root",
sampleBaseDir+"PATtuple_234_2_cMK.root",
sampleBaseDir+"PATtuple_235_2_d7E.root",
sampleBaseDir+"PATtuple_236_1_0ob.root",
sampleBaseDir+"PATtuple_237_1_08K.root",
sampleBaseDir+"PATtuple_237_1_xW5.root",
sampleBaseDir+"PATtuple_238_1_ang.root",
sampleBaseDir+"PATtuple_239_1_zsp.root",
sampleBaseDir+"PATtuple_23_1_eHy.root",
sampleBaseDir+"PATtuple_240_1_ASm.root",
sampleBaseDir+"PATtuple_241_1_xuv.root",
sampleBaseDir+"PATtuple_241_1_z8C.root",
sampleBaseDir+"PATtuple_242_1_5Sm.root",
sampleBaseDir+"PATtuple_242_1_fFx.root",
sampleBaseDir+"PATtuple_243_1_cO7.root",
sampleBaseDir+"PATtuple_244_1_7On.root",
sampleBaseDir+"PATtuple_245_1_FPh.root",
sampleBaseDir+"PATtuple_245_1_HeD.root",
sampleBaseDir+"PATtuple_246_1_frG.root",
sampleBaseDir+"PATtuple_246_1_jWF.root",
sampleBaseDir+"PATtuple_247_1_jqQ.root",
sampleBaseDir+"PATtuple_248_1_N7Q.root",
sampleBaseDir+"PATtuple_248_1_QCQ.root",
sampleBaseDir+"PATtuple_249_1_Ntl.root",
sampleBaseDir+"PATtuple_24_1_tMj.root",
sampleBaseDir+"PATtuple_250_1_D41.root",
sampleBaseDir+"PATtuple_251_1_E38.root",
sampleBaseDir+"PATtuple_251_1_GQE.root",
sampleBaseDir+"PATtuple_252_1_DVw.root",
sampleBaseDir+"PATtuple_252_1_Mbr.root",
sampleBaseDir+"PATtuple_253_1_S1Y.root",
sampleBaseDir+"PATtuple_254_1_s2F.root",
sampleBaseDir+"PATtuple_255_1_QLU.root",
sampleBaseDir+"PATtuple_255_1_saL.root",
sampleBaseDir+"PATtuple_256_1_mtz.root",
sampleBaseDir+"PATtuple_257_1_sZS.root",
sampleBaseDir+"PATtuple_257_2_BqS.root",
sampleBaseDir+"PATtuple_258_1_Ek9.root",
sampleBaseDir+"PATtuple_258_1_OE9.root",
sampleBaseDir+"PATtuple_259_1_5uj.root",
sampleBaseDir+"PATtuple_259_1_Lj8.root",
sampleBaseDir+"PATtuple_25_1_EMD.root",
sampleBaseDir+"PATtuple_260_1_gOG.root",
sampleBaseDir+"PATtuple_261_1_ObR.root",
sampleBaseDir+"PATtuple_261_1_SBk.root",
sampleBaseDir+"PATtuple_262_1_B5N.root",
sampleBaseDir+"PATtuple_262_1_xxF.root",
sampleBaseDir+"PATtuple_263_1_2lv.root",
sampleBaseDir+"PATtuple_264_1_pyl.root",
sampleBaseDir+"PATtuple_265_1_6tq.root",
sampleBaseDir+"PATtuple_266_1_rDJ.root",
sampleBaseDir+"PATtuple_267_1_k6w.root",
sampleBaseDir+"PATtuple_268_1_sst.root",
sampleBaseDir+"PATtuple_269_1_Axg.root",
sampleBaseDir+"PATtuple_26_1_NA0.root",
sampleBaseDir+"PATtuple_270_1_I7y.root",
sampleBaseDir+"PATtuple_271_1_HSF.root",
sampleBaseDir+"PATtuple_272_1_joZ.root",
sampleBaseDir+"PATtuple_273_1_gj3.root",
sampleBaseDir+"PATtuple_274_1_pxu.root",
sampleBaseDir+"PATtuple_275_1_ZY8.root",
sampleBaseDir+"PATtuple_276_1_EhF.root",
sampleBaseDir+"PATtuple_277_1_7Gs.root",
sampleBaseDir+"PATtuple_278_1_SDV.root",
sampleBaseDir+"PATtuple_279_1_gob.root",
sampleBaseDir+"PATtuple_27_1_3rz.root",
sampleBaseDir+"PATtuple_280_1_wtS.root",
sampleBaseDir+"PATtuple_281_1_5CO.root",
sampleBaseDir+"PATtuple_281_1_MGp.root",
sampleBaseDir+"PATtuple_282_1_P5Y.root",
sampleBaseDir+"PATtuple_283_1_gNN.root",
sampleBaseDir+"PATtuple_284_1_f2t.root",
sampleBaseDir+"PATtuple_285_1_UtH.root",
sampleBaseDir+"PATtuple_286_1_9Hl.root",
sampleBaseDir+"PATtuple_287_1_uch.root",
sampleBaseDir+"PATtuple_288_1_w5o.root",
sampleBaseDir+"PATtuple_289_1_znz.root",
sampleBaseDir+"PATtuple_28_1_0ho.root",
sampleBaseDir+"PATtuple_290_1_LLw.root",
sampleBaseDir+"PATtuple_291_1_wjW.root",
sampleBaseDir+"PATtuple_292_1_DfR.root",
sampleBaseDir+"PATtuple_293_1_ND0.root",
sampleBaseDir+"PATtuple_294_1_flq.root",
sampleBaseDir+"PATtuple_295_1_sHB.root",
sampleBaseDir+"PATtuple_296_1_ptC.root",
sampleBaseDir+"PATtuple_297_1_1Rh.root",
sampleBaseDir+"PATtuple_298_1_a6Q.root",
sampleBaseDir+"PATtuple_298_1_ybl.root",
sampleBaseDir+"PATtuple_299_1_sVv.root",
sampleBaseDir+"PATtuple_29_1_OmV.root",
sampleBaseDir+"PATtuple_2_1_RuC.root",
sampleBaseDir+"PATtuple_300_1_nhG.root",
sampleBaseDir+"PATtuple_301_1_g7r.root",
sampleBaseDir+"PATtuple_302_1_UyB.root",
sampleBaseDir+"PATtuple_303_1_GUc.root",
sampleBaseDir+"PATtuple_304_1_gjg.root",
sampleBaseDir+"PATtuple_305_1_V7y.root",
sampleBaseDir+"PATtuple_306_1_uwg.root",
sampleBaseDir+"PATtuple_307_1_XJ9.root",
sampleBaseDir+"PATtuple_308_1_kxb.root",
sampleBaseDir+"PATtuple_309_1_9Rz.root",
sampleBaseDir+"PATtuple_30_1_k5n.root",
sampleBaseDir+"PATtuple_310_1_dxd.root",
sampleBaseDir+"PATtuple_311_1_C1w.root",
sampleBaseDir+"PATtuple_311_2_tHq.root",
sampleBaseDir+"PATtuple_312_1_m7H.root",
sampleBaseDir+"PATtuple_313_1_M0V.root",
sampleBaseDir+"PATtuple_314_2_bmg.root",
sampleBaseDir+"PATtuple_315_1_Qe5.root",
sampleBaseDir+"PATtuple_316_1_GHd.root",
sampleBaseDir+"PATtuple_317_2_c5Q.root",
sampleBaseDir+"PATtuple_318_1_r7Z.root",
sampleBaseDir+"PATtuple_318_1_so7.root",
sampleBaseDir+"PATtuple_319_1_NTV.root",
sampleBaseDir+"PATtuple_31_1_T93.root",
sampleBaseDir+"PATtuple_320_1_EeP.root",
sampleBaseDir+"PATtuple_320_1_zcg.root",
sampleBaseDir+"PATtuple_321_2_wn9.root",
sampleBaseDir+"PATtuple_322_1_1xg.root",
sampleBaseDir+"PATtuple_323_1_W17.root",
sampleBaseDir+"PATtuple_324_1_eaU.root",
sampleBaseDir+"PATtuple_325_1_UzB.root",
sampleBaseDir+"PATtuple_326_1_IzR.root",
sampleBaseDir+"PATtuple_327_1_dVU.root",
sampleBaseDir+"PATtuple_328_1_WOd.root",
sampleBaseDir+"PATtuple_329_1_xLU.root",
sampleBaseDir+"PATtuple_32_1_z6j.root",
sampleBaseDir+"PATtuple_330_1_ASi.root",
sampleBaseDir+"PATtuple_331_1_Sjy.root",
sampleBaseDir+"PATtuple_332_1_Avi.root",
sampleBaseDir+"PATtuple_333_1_rjb.root",
sampleBaseDir+"PATtuple_334_1_WMq.root",
sampleBaseDir+"PATtuple_335_1_mUD.root",
sampleBaseDir+"PATtuple_336_1_PvF.root",
sampleBaseDir+"PATtuple_337_1_HBc.root",
sampleBaseDir+"PATtuple_338_1_S1r.root",
sampleBaseDir+"PATtuple_339_1_bQG.root",
sampleBaseDir+"PATtuple_33_1_OvQ.root",
sampleBaseDir+"PATtuple_33_1_q7J.root",
sampleBaseDir+"PATtuple_340_1_yRF.root",
sampleBaseDir+"PATtuple_341_1_f0X.root",
sampleBaseDir+"PATtuple_342_1_k9K.root",
sampleBaseDir+"PATtuple_343_1_D8l.root",
sampleBaseDir+"PATtuple_344_1_dCT.root",
sampleBaseDir+"PATtuple_345_1_kon.root",
sampleBaseDir+"PATtuple_346_1_Xv2.root",
sampleBaseDir+"PATtuple_347_1_mzl.root",
sampleBaseDir+"PATtuple_348_1_K2s.root",
sampleBaseDir+"PATtuple_349_1_yCB.root",
sampleBaseDir+"PATtuple_34_1_Dku.root",
sampleBaseDir+"PATtuple_350_1_1RQ.root",
sampleBaseDir+"PATtuple_351_1_cOS.root",
sampleBaseDir+"PATtuple_352_1_CYx.root",
sampleBaseDir+"PATtuple_353_1_lxr.root",
sampleBaseDir+"PATtuple_354_1_0xJ.root",
sampleBaseDir+"PATtuple_355_1_pZx.root",
sampleBaseDir+"PATtuple_356_1_YKR.root",
sampleBaseDir+"PATtuple_357_1_q8G.root",
sampleBaseDir+"PATtuple_358_1_2IT.root",
sampleBaseDir+"PATtuple_359_1_yII.root",
sampleBaseDir+"PATtuple_35_1_cSi.root",
sampleBaseDir+"PATtuple_360_1_QkL.root",
sampleBaseDir+"PATtuple_361_1_r4p.root",
sampleBaseDir+"PATtuple_362_1_Uil.root",
sampleBaseDir+"PATtuple_363_1_WZ8.root",
sampleBaseDir+"PATtuple_364_1_3Bp.root",
sampleBaseDir+"PATtuple_365_1_J3P.root",
sampleBaseDir+"PATtuple_366_1_ciK.root",
sampleBaseDir+"PATtuple_367_1_vS3.root",
sampleBaseDir+"PATtuple_368_1_FFq.root",
sampleBaseDir+"PATtuple_369_1_PIY.root",
sampleBaseDir+"PATtuple_36_1_qev.root",
sampleBaseDir+"PATtuple_370_1_qhT.root",
sampleBaseDir+"PATtuple_371_1_JxC.root",
sampleBaseDir+"PATtuple_372_1_rNZ.root",
sampleBaseDir+"PATtuple_373_1_6Dr.root",
sampleBaseDir+"PATtuple_374_1_SLv.root",
sampleBaseDir+"PATtuple_375_1_l6w.root",
sampleBaseDir+"PATtuple_376_2_Nof.root",
sampleBaseDir+"PATtuple_377_1_MSk.root",
sampleBaseDir+"PATtuple_378_1_5mj.root",
sampleBaseDir+"PATtuple_379_2_hFc.root",
sampleBaseDir+"PATtuple_37_1_L4Q.root",
sampleBaseDir+"PATtuple_37_1_fu8.root",
sampleBaseDir+"PATtuple_380_1_mnh.root",
sampleBaseDir+"PATtuple_381_1_brd.root",
sampleBaseDir+"PATtuple_382_1_8Tc.root",
sampleBaseDir+"PATtuple_383_1_me1.root",
sampleBaseDir+"PATtuple_384_1_4Fv.root",
sampleBaseDir+"PATtuple_385_3_MNi.root",
sampleBaseDir+"PATtuple_386_1_YxX.root",
sampleBaseDir+"PATtuple_387_1_iaP.root",
sampleBaseDir+"PATtuple_388_1_wIF.root",
sampleBaseDir+"PATtuple_389_1_hkN.root",
sampleBaseDir+"PATtuple_38_1_sHw.root",
sampleBaseDir+"PATtuple_390_1_8uu.root",
sampleBaseDir+"PATtuple_391_1_xGF.root",
sampleBaseDir+"PATtuple_392_2_5Dp.root",
sampleBaseDir+"PATtuple_393_2_Vkj.root",
sampleBaseDir+"PATtuple_394_1_3Kp.root",
sampleBaseDir+"PATtuple_395_1_h6g.root",
sampleBaseDir+"PATtuple_396_1_yAQ.root",
sampleBaseDir+"PATtuple_397_1_lUu.root",
sampleBaseDir+"PATtuple_398_1_UyM.root",
sampleBaseDir+"PATtuple_399_1_Uwh.root",
sampleBaseDir+"PATtuple_399_1_Vbt.root",
sampleBaseDir+"PATtuple_39_1_vyQ.root",
sampleBaseDir+"PATtuple_3_1_yHI.root",
sampleBaseDir+"PATtuple_400_1_Q26.root",
sampleBaseDir+"PATtuple_401_1_f0H.root",
sampleBaseDir+"PATtuple_401_2_ITr.root",
sampleBaseDir+"PATtuple_402_1_yLJ.root",
sampleBaseDir+"PATtuple_403_1_yCk.root",
sampleBaseDir+"PATtuple_404_1_P6J.root",
sampleBaseDir+"PATtuple_405_1_5I0.root",
sampleBaseDir+"PATtuple_406_1_7nB.root",
sampleBaseDir+"PATtuple_407_1_w6E.root",
sampleBaseDir+"PATtuple_408_1_Fzu.root",
sampleBaseDir+"PATtuple_409_2_rW8.root",
sampleBaseDir+"PATtuple_40_1_SNT.root",
sampleBaseDir+"PATtuple_40_1_eAk.root",
sampleBaseDir+"PATtuple_410_1_VmP.root",
sampleBaseDir+"PATtuple_411_1_wQE.root",
sampleBaseDir+"PATtuple_412_1_3G4.root",
sampleBaseDir+"PATtuple_413_1_djx.root",
sampleBaseDir+"PATtuple_414_1_5pN.root",
sampleBaseDir+"PATtuple_415_1_Vcp.root",
sampleBaseDir+"PATtuple_416_1_H9M.root",
sampleBaseDir+"PATtuple_417_2_HIs.root",
sampleBaseDir+"PATtuple_418_1_C7A.root",
sampleBaseDir+"PATtuple_419_1_xiJ.root",
sampleBaseDir+"PATtuple_41_1_DQa.root",
sampleBaseDir+"PATtuple_420_1_6eX.root",
sampleBaseDir+"PATtuple_421_1_eN3.root",
sampleBaseDir+"PATtuple_422_2_Jfu.root",
sampleBaseDir+"PATtuple_423_1_dNc.root",
sampleBaseDir+"PATtuple_424_1_sKd.root",
sampleBaseDir+"PATtuple_425_1_yK2.root",
sampleBaseDir+"PATtuple_426_2_d6F.root",
sampleBaseDir+"PATtuple_427_1_1q7.root",
sampleBaseDir+"PATtuple_428_1_CYw.root",
sampleBaseDir+"PATtuple_429_1_guP.root",
sampleBaseDir+"PATtuple_42_1_zEE.root",
sampleBaseDir+"PATtuple_430_1_Fsx.root",
sampleBaseDir+"PATtuple_431_1_56d.root",
sampleBaseDir+"PATtuple_432_1_XHr.root",
sampleBaseDir+"PATtuple_433_1_MIH.root",
sampleBaseDir+"PATtuple_434_1_64T.root",
sampleBaseDir+"PATtuple_435_1_QFp.root",
sampleBaseDir+"PATtuple_436_1_6Kj.root",
sampleBaseDir+"PATtuple_437_1_O2I.root",
sampleBaseDir+"PATtuple_438_1_ENP.root",
sampleBaseDir+"PATtuple_439_1_7yq.root",
sampleBaseDir+"PATtuple_43_1_hQz.root",
sampleBaseDir+"PATtuple_440_1_B0m.root",
sampleBaseDir+"PATtuple_441_1_699.root",
sampleBaseDir+"PATtuple_442_1_3cv.root",
sampleBaseDir+"PATtuple_443_1_6q0.root",
sampleBaseDir+"PATtuple_444_1_Wwl.root",
sampleBaseDir+"PATtuple_445_2_u3Y.root",
sampleBaseDir+"PATtuple_446_1_vYx.root",
sampleBaseDir+"PATtuple_447_1_ZB6.root",
sampleBaseDir+"PATtuple_448_1_nJ1.root",
sampleBaseDir+"PATtuple_449_1_xdU.root",
sampleBaseDir+"PATtuple_44_1_BOg.root",
sampleBaseDir+"PATtuple_450_1_Oui.root",
sampleBaseDir+"PATtuple_451_1_Nry.root",
sampleBaseDir+"PATtuple_452_1_f03.root",
sampleBaseDir+"PATtuple_453_2_jOF.root",
sampleBaseDir+"PATtuple_454_1_OMU.root",
sampleBaseDir+"PATtuple_455_2_qhL.root",
sampleBaseDir+"PATtuple_456_2_iND.root",
sampleBaseDir+"PATtuple_457_2_bns.root",
sampleBaseDir+"PATtuple_458_2_twV.root",
sampleBaseDir+"PATtuple_459_2_LU8.root",
sampleBaseDir+"PATtuple_45_1_wdi.root",
sampleBaseDir+"PATtuple_460_1_mgn.root",
sampleBaseDir+"PATtuple_461_1_364.root",
sampleBaseDir+"PATtuple_462_1_eBL.root",
sampleBaseDir+"PATtuple_463_1_ofO.root",
sampleBaseDir+"PATtuple_464_1_pcH.root",
sampleBaseDir+"PATtuple_465_1_23U.root",
sampleBaseDir+"PATtuple_466_1_RdU.root",
sampleBaseDir+"PATtuple_467_1_QAc.root",
sampleBaseDir+"PATtuple_468_1_wXA.root",
sampleBaseDir+"PATtuple_469_2_oVj.root",
sampleBaseDir+"PATtuple_46_1_Gyf.root",
sampleBaseDir+"PATtuple_470_2_nFj.root",
sampleBaseDir+"PATtuple_471_1_KSQ.root",
sampleBaseDir+"PATtuple_472_1_0oS.root",
sampleBaseDir+"PATtuple_473_2_IVK.root",
sampleBaseDir+"PATtuple_474_1_Gwu.root",
sampleBaseDir+"PATtuple_475_1_l77.root",
sampleBaseDir+"PATtuple_476_1_caw.root",
sampleBaseDir+"PATtuple_477_1_JW7.root",
sampleBaseDir+"PATtuple_478_1_zFL.root",
sampleBaseDir+"PATtuple_479_2_HJT.root",
sampleBaseDir+"PATtuple_47_1_AGj.root",
sampleBaseDir+"PATtuple_480_1_dSs.root",
sampleBaseDir+"PATtuple_481_1_Ts7.root",
sampleBaseDir+"PATtuple_482_1_xfy.root",
sampleBaseDir+"PATtuple_483_1_X1w.root",
sampleBaseDir+"PATtuple_484_1_OqA.root",
sampleBaseDir+"PATtuple_485_1_O1z.root",
sampleBaseDir+"PATtuple_486_1_GLA.root",
sampleBaseDir+"PATtuple_487_1_qEc.root",
sampleBaseDir+"PATtuple_488_1_dZP.root",
sampleBaseDir+"PATtuple_489_1_eaG.root",
sampleBaseDir+"PATtuple_48_1_46L.root",
sampleBaseDir+"PATtuple_490_1_4fs.root",
sampleBaseDir+"PATtuple_491_1_WuS.root",
sampleBaseDir+"PATtuple_492_1_xiM.root",
sampleBaseDir+"PATtuple_493_1_PqV.root",
sampleBaseDir+"PATtuple_494_1_XXL.root",
sampleBaseDir+"PATtuple_495_1_Tnb.root",
sampleBaseDir+"PATtuple_496_2_Mpi.root",
sampleBaseDir+"PATtuple_497_1_56Q.root",
sampleBaseDir+"PATtuple_498_1_v2R.root",
sampleBaseDir+"PATtuple_499_1_usr.root",
sampleBaseDir+"PATtuple_49_1_LT6.root",
sampleBaseDir+"PATtuple_4_1_NvL.root",
sampleBaseDir+"PATtuple_500_1_oSD.root",
sampleBaseDir+"PATtuple_501_1_fqo.root",
sampleBaseDir+"PATtuple_502_1_xYb.root",
sampleBaseDir+"PATtuple_503_2_2nK.root",
sampleBaseDir+"PATtuple_504_1_mxq.root",
sampleBaseDir+"PATtuple_505_1_OcX.root",
sampleBaseDir+"PATtuple_506_1_nqG.root",
sampleBaseDir+"PATtuple_507_1_rIx.root",
sampleBaseDir+"PATtuple_508_1_w8a.root",
sampleBaseDir+"PATtuple_509_1_a0i.root",
sampleBaseDir+"PATtuple_509_2_CfC.root",
sampleBaseDir+"PATtuple_50_1_hhz.root",
sampleBaseDir+"PATtuple_510_2_AH9.root",
sampleBaseDir+"PATtuple_511_1_jiI.root",
sampleBaseDir+"PATtuple_512_1_97V.root",
sampleBaseDir+"PATtuple_513_1_9O9.root",
sampleBaseDir+"PATtuple_514_1_yDz.root",
sampleBaseDir+"PATtuple_515_1_1xN.root",
sampleBaseDir+"PATtuple_516_1_EQm.root",
sampleBaseDir+"PATtuple_517_1_Krk.root",
sampleBaseDir+"PATtuple_518_1_Njv.root",
sampleBaseDir+"PATtuple_519_1_h0U.root",
sampleBaseDir+"PATtuple_51_1_6l7.root",
sampleBaseDir+"PATtuple_520_1_GRz.root",
sampleBaseDir+"PATtuple_521_1_Qej.root",
sampleBaseDir+"PATtuple_522_1_ray.root",
sampleBaseDir+"PATtuple_523_1_al3.root",
sampleBaseDir+"PATtuple_524_1_JP4.root",
sampleBaseDir+"PATtuple_525_1_dHR.root",
sampleBaseDir+"PATtuple_526_1_PCf.root",
sampleBaseDir+"PATtuple_527_1_UUm.root",
sampleBaseDir+"PATtuple_528_1_FPL.root",
sampleBaseDir+"PATtuple_529_1_5iu.root",
sampleBaseDir+"PATtuple_52_1_gRG.root",
sampleBaseDir+"PATtuple_530_1_0Uh.root",
sampleBaseDir+"PATtuple_531_1_liS.root",
sampleBaseDir+"PATtuple_532_2_tPn.root",
sampleBaseDir+"PATtuple_533_1_cFh.root",
sampleBaseDir+"PATtuple_534_2_YhK.root",
sampleBaseDir+"PATtuple_535_1_nbk.root",
sampleBaseDir+"PATtuple_536_1_Wrs.root",
sampleBaseDir+"PATtuple_537_1_7Xa.root",
sampleBaseDir+"PATtuple_538_1_SQ2.root",
sampleBaseDir+"PATtuple_539_1_XBN.root",
sampleBaseDir+"PATtuple_53_1_uzh.root",
sampleBaseDir+"PATtuple_540_1_lRj.root",
sampleBaseDir+"PATtuple_541_1_jHC.root",
sampleBaseDir+"PATtuple_542_1_p6Q.root",
sampleBaseDir+"PATtuple_543_1_mhG.root",
sampleBaseDir+"PATtuple_544_1_gEV.root",
sampleBaseDir+"PATtuple_545_1_eMI.root",
sampleBaseDir+"PATtuple_546_1_tu7.root",
sampleBaseDir+"PATtuple_547_2_9nw.root",
sampleBaseDir+"PATtuple_548_1_LEQ.root",
sampleBaseDir+"PATtuple_549_1_rzL.root",
sampleBaseDir+"PATtuple_54_1_a5M.root",
sampleBaseDir+"PATtuple_550_1_d7x.root",
sampleBaseDir+"PATtuple_551_1_Cxj.root",
sampleBaseDir+"PATtuple_552_1_F2Q.root",
sampleBaseDir+"PATtuple_553_1_xN1.root",
sampleBaseDir+"PATtuple_553_2_UGr.root",
sampleBaseDir+"PATtuple_554_2_CCK.root",
sampleBaseDir+"PATtuple_555_2_UyW.root",
sampleBaseDir+"PATtuple_556_2_zoN.root",
sampleBaseDir+"PATtuple_557_1_0k4.root",
sampleBaseDir+"PATtuple_558_2_kEB.root",
sampleBaseDir+"PATtuple_559_3_mxu.root",
sampleBaseDir+"PATtuple_55_1_UWD.root",
sampleBaseDir+"PATtuple_560_2_BMp.root",
sampleBaseDir+"PATtuple_561_1_ytw.root",
sampleBaseDir+"PATtuple_562_1_ofB.root",
sampleBaseDir+"PATtuple_563_1_PL5.root",
sampleBaseDir+"PATtuple_564_1_6FZ.root",
sampleBaseDir+"PATtuple_565_1_XVW.root",
sampleBaseDir+"PATtuple_566_1_PJx.root",
sampleBaseDir+"PATtuple_567_1_9CD.root",
sampleBaseDir+"PATtuple_568_1_tsW.root",
sampleBaseDir+"PATtuple_569_1_sVU.root",
sampleBaseDir+"PATtuple_56_2_tVK.root",
sampleBaseDir+"PATtuple_570_2_EHa.root",
sampleBaseDir+"PATtuple_570_2_fXI.root",
sampleBaseDir+"PATtuple_571_1_WAo.root",
sampleBaseDir+"PATtuple_572_1_G16.root",
sampleBaseDir+"PATtuple_573_1_HZt.root",
sampleBaseDir+"PATtuple_574_1_nsw.root",
sampleBaseDir+"PATtuple_575_1_jyF.root",
sampleBaseDir+"PATtuple_576_2_M0u.root",
sampleBaseDir+"PATtuple_577_1_993.root",
sampleBaseDir+"PATtuple_578_1_7vl.root",
sampleBaseDir+"PATtuple_579_1_LwA.root",
sampleBaseDir+"PATtuple_57_1_LMD.root",
sampleBaseDir+"PATtuple_580_1_5qP.root",
sampleBaseDir+"PATtuple_581_1_inl.root",
sampleBaseDir+"PATtuple_582_1_Z8b.root",
sampleBaseDir+"PATtuple_583_1_4ma.root",
sampleBaseDir+"PATtuple_584_1_rUY.root",
sampleBaseDir+"PATtuple_585_1_P1m.root",
sampleBaseDir+"PATtuple_586_1_DLl.root",
sampleBaseDir+"PATtuple_587_2_44v.root",
sampleBaseDir+"PATtuple_587_2_oZH.root",
sampleBaseDir+"PATtuple_588_1_vnv.root",
sampleBaseDir+"PATtuple_589_1_8G9.root",
sampleBaseDir+"PATtuple_58_1_w1f.root",
sampleBaseDir+"PATtuple_590_1_c01.root",
sampleBaseDir+"PATtuple_591_1_KyC.root",
sampleBaseDir+"PATtuple_592_1_by5.root",
sampleBaseDir+"PATtuple_593_1_tcG.root",
sampleBaseDir+"PATtuple_594_1_sXx.root",
sampleBaseDir+"PATtuple_595_1_b0b.root",
sampleBaseDir+"PATtuple_596_1_sRV.root",
sampleBaseDir+"PATtuple_597_2_gih.root",
sampleBaseDir+"PATtuple_598_2_6AA.root",
sampleBaseDir+"PATtuple_598_2_v5X.root",
sampleBaseDir+"PATtuple_599_1_Xya.root",
sampleBaseDir+"PATtuple_59_1_2oq.root",
sampleBaseDir+"PATtuple_5_1_59x.root",
sampleBaseDir+"PATtuple_600_1_85h.root",
sampleBaseDir+"PATtuple_601_1_Pjk.root",
sampleBaseDir+"PATtuple_602_1_meM.root",
sampleBaseDir+"PATtuple_603_1_Lck.root",
sampleBaseDir+"PATtuple_603_3_87u.root",
sampleBaseDir+"PATtuple_604_1_v3w.root",
sampleBaseDir+"PATtuple_604_2_xBm.root",
sampleBaseDir+"PATtuple_605_1_cRl.root",
sampleBaseDir+"PATtuple_606_1_bzX.root",
sampleBaseDir+"PATtuple_607_1_Yoo.root",
sampleBaseDir+"PATtuple_608_1_qje.root",
sampleBaseDir+"PATtuple_609_1_4uF.root",
sampleBaseDir+"PATtuple_60_1_N4A.root",
sampleBaseDir+"PATtuple_610_1_U1W.root",
sampleBaseDir+"PATtuple_611_2_DuL.root",
sampleBaseDir+"PATtuple_612_1_9xu.root",
sampleBaseDir+"PATtuple_613_2_XAU.root",
sampleBaseDir+"PATtuple_614_1_Yef.root",
sampleBaseDir+"PATtuple_615_1_FUL.root",
sampleBaseDir+"PATtuple_616_2_OpK.root",
sampleBaseDir+"PATtuple_617_2_WCs.root",
sampleBaseDir+"PATtuple_618_1_nvY.root",
sampleBaseDir+"PATtuple_619_1_KNM.root",
sampleBaseDir+"PATtuple_61_1_ZW8.root",
sampleBaseDir+"PATtuple_620_1_eHK.root",
sampleBaseDir+"PATtuple_621_1_P3i.root",
sampleBaseDir+"PATtuple_622_1_Wa6.root",
sampleBaseDir+"PATtuple_623_1_ypb.root",
sampleBaseDir+"PATtuple_624_1_qnw.root",
sampleBaseDir+"PATtuple_625_1_EJA.root",
sampleBaseDir+"PATtuple_626_1_Xw6.root",
sampleBaseDir+"PATtuple_627_1_9oa.root",
sampleBaseDir+"PATtuple_628_1_Q5t.root",
sampleBaseDir+"PATtuple_629_1_kR4.root",
sampleBaseDir+"PATtuple_62_1_OYE.root",
sampleBaseDir+"PATtuple_630_1_dBz.root",
sampleBaseDir+"PATtuple_631_1_ofn.root",
sampleBaseDir+"PATtuple_631_2_xeo.root",
sampleBaseDir+"PATtuple_632_1_Dvt.root",
sampleBaseDir+"PATtuple_633_1_eY0.root",
sampleBaseDir+"PATtuple_634_1_qqB.root",
sampleBaseDir+"PATtuple_635_1_Ynt.root",
sampleBaseDir+"PATtuple_636_1_UCY.root",
sampleBaseDir+"PATtuple_637_2_3ED.root",
sampleBaseDir+"PATtuple_637_2_V2c.root",
sampleBaseDir+"PATtuple_638_1_v3L.root",
sampleBaseDir+"PATtuple_639_1_2Ln.root",
sampleBaseDir+"PATtuple_63_1_kdc.root",
sampleBaseDir+"PATtuple_640_1_OxW.root",
sampleBaseDir+"PATtuple_641_1_YAF.root",
sampleBaseDir+"PATtuple_642_1_920.root",
sampleBaseDir+"PATtuple_642_1_WsT.root",
sampleBaseDir+"PATtuple_643_1_IVR.root",
sampleBaseDir+"PATtuple_643_1_uH8.root",
sampleBaseDir+"PATtuple_644_1_1m3.root",
sampleBaseDir+"PATtuple_645_1_Yco.root",
sampleBaseDir+"PATtuple_646_1_32S.root",
sampleBaseDir+"PATtuple_647_2_Y3t.root",
sampleBaseDir+"PATtuple_648_1_tje.root",
sampleBaseDir+"PATtuple_649_1_bCk.root",
sampleBaseDir+"PATtuple_64_1_MvP.root",
sampleBaseDir+"PATtuple_650_1_Lx8.root",
sampleBaseDir+"PATtuple_651_1_UR8.root",
sampleBaseDir+"PATtuple_652_1_BHq.root",
sampleBaseDir+"PATtuple_652_1_Yik.root",
sampleBaseDir+"PATtuple_653_1_Sr0.root",
sampleBaseDir+"PATtuple_654_1_PEF.root",
sampleBaseDir+"PATtuple_655_2_dyE.root",
sampleBaseDir+"PATtuple_656_1_CPi.root",
sampleBaseDir+"PATtuple_657_1_2Gt.root",
sampleBaseDir+"PATtuple_658_1_8lh.root",
sampleBaseDir+"PATtuple_65_1_moo.root",
sampleBaseDir+"PATtuple_66_1_Ser.root",
sampleBaseDir+"PATtuple_67_1_yrv.root",
sampleBaseDir+"PATtuple_68_1_ZEf.root",
sampleBaseDir+"PATtuple_68_1_eTN.root",
sampleBaseDir+"PATtuple_69_1_mkj.root",
sampleBaseDir+"PATtuple_6_1_J48.root",
sampleBaseDir+"PATtuple_70_2_MlN.root",
sampleBaseDir+"PATtuple_71_2_Q94.root",
sampleBaseDir+"PATtuple_72_1_2sE.root",
sampleBaseDir+"PATtuple_73_1_Fhq.root",
sampleBaseDir+"PATtuple_74_1_AvM.root",
sampleBaseDir+"PATtuple_75_1_l8C.root",
sampleBaseDir+"PATtuple_76_1_GH3.root",
sampleBaseDir+"PATtuple_77_1_K91.root",
sampleBaseDir+"PATtuple_78_1_pwC.root",
sampleBaseDir+"PATtuple_79_1_xKr.root",
sampleBaseDir+"PATtuple_7_1_w2U.root",
sampleBaseDir+"PATtuple_80_1_7k1.root",
sampleBaseDir+"PATtuple_81_1_DCk.root",
sampleBaseDir+"PATtuple_82_1_tXp.root",
sampleBaseDir+"PATtuple_83_1_l8C.root",
sampleBaseDir+"PATtuple_84_1_8tH.root",
sampleBaseDir+"PATtuple_85_1_yPi.root",
sampleBaseDir+"PATtuple_86_1_iHU.root",
sampleBaseDir+"PATtuple_87_1_WRr.root",
sampleBaseDir+"PATtuple_88_1_fXS.root",
sampleBaseDir+"PATtuple_89_1_jL2.root",
sampleBaseDir+"PATtuple_8_1_4aX.root",
sampleBaseDir+"PATtuple_90_1_Cdj.root",
sampleBaseDir+"PATtuple_91_1_d5k.root",
sampleBaseDir+"PATtuple_92_1_Yuc.root",
sampleBaseDir+"PATtuple_93_1_TkW.root",
sampleBaseDir+"PATtuple_94_1_Q3L.root",
sampleBaseDir+"PATtuple_95_1_Rml.root",
sampleBaseDir+"PATtuple_96_1_LS2.root",
sampleBaseDir+"PATtuple_97_1_HKr.root",
sampleBaseDir+"PATtuple_98_3_FVz.root",
sampleBaseDir+"PATtuple_99_1_amY.root",
sampleBaseDir+"PATtuple_9_2_jRO.root",
]
