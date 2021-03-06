sampleDataSet = '/DoubleMuParked/Run2012C-22Jan2013-v1/AOD'

# original (i.e. RECO file) release,
# not the one we plan to process them with
sampleRelease = "CMSSW_5_3_7_patch5" 
# release used to create new files with
sampleProcessRelease = "CMSSW_5_3_8" 

sampleNumEvents = 36820243 # according to DBS, as of 13 October 2013

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

sampleBaseDir="file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Data_Mu_Run2012C22Jan_pat_20140327/demattia//DoubleMuParked/Data_Mu_Run2012C22Jan_pat_20140327/ce2ef5771b8bd3b63b0f9db075cc5761/"
samplePatFiles = [
sampleBaseDir+"PATtuple_100_1_Ef9.root",
sampleBaseDir+"PATtuple_101_1_lwB.root",
sampleBaseDir+"PATtuple_102_2_uEL.root",
sampleBaseDir+"PATtuple_103_1_gcs.root",
sampleBaseDir+"PATtuple_104_1_VID.root",
sampleBaseDir+"PATtuple_105_1_otu.root",
sampleBaseDir+"PATtuple_106_1_22V.root",
sampleBaseDir+"PATtuple_107_1_C7X.root",
sampleBaseDir+"PATtuple_108_1_c1f.root",
sampleBaseDir+"PATtuple_109_1_5gV.root",
sampleBaseDir+"PATtuple_10_1_jaL.root",
sampleBaseDir+"PATtuple_110_1_Mhk.root",
sampleBaseDir+"PATtuple_111_2_H7z.root",
sampleBaseDir+"PATtuple_112_1_A4M.root",
sampleBaseDir+"PATtuple_113_1_zE0.root",
sampleBaseDir+"PATtuple_114_1_4jv.root",
sampleBaseDir+"PATtuple_115_1_y3p.root",
sampleBaseDir+"PATtuple_116_1_Mpu.root",
sampleBaseDir+"PATtuple_117_3_3kP.root",
sampleBaseDir+"PATtuple_118_2_4dS.root",
sampleBaseDir+"PATtuple_119_1_Owp.root",
sampleBaseDir+"PATtuple_11_1_y4G.root",
sampleBaseDir+"PATtuple_120_1_GhS.root",
sampleBaseDir+"PATtuple_121_1_vUP.root",
sampleBaseDir+"PATtuple_122_2_3gH.root",
sampleBaseDir+"PATtuple_123_1_z6V.root",
sampleBaseDir+"PATtuple_124_3_WS3.root",
sampleBaseDir+"PATtuple_125_1_c6G.root",
sampleBaseDir+"PATtuple_126_2_JQa.root",
sampleBaseDir+"PATtuple_127_1_PXE.root",
sampleBaseDir+"PATtuple_128_1_1WY.root",
sampleBaseDir+"PATtuple_129_1_OJl.root",
sampleBaseDir+"PATtuple_12_1_zbm.root",
sampleBaseDir+"PATtuple_130_1_XIh.root",
sampleBaseDir+"PATtuple_131_1_Ud6.root",
sampleBaseDir+"PATtuple_132_1_BMq.root",
sampleBaseDir+"PATtuple_133_1_6iN.root",
sampleBaseDir+"PATtuple_134_1_V2o.root",
sampleBaseDir+"PATtuple_135_1_Xtj.root",
sampleBaseDir+"PATtuple_136_1_r4D.root",
sampleBaseDir+"PATtuple_137_1_I3c.root",
sampleBaseDir+"PATtuple_138_1_Us6.root",
sampleBaseDir+"PATtuple_139_1_bgn.root",
sampleBaseDir+"PATtuple_13_1_sY7.root",
sampleBaseDir+"PATtuple_140_1_ru8.root",
sampleBaseDir+"PATtuple_141_1_1At.root",
sampleBaseDir+"PATtuple_142_1_EfC.root",
sampleBaseDir+"PATtuple_143_1_2VD.root",
sampleBaseDir+"PATtuple_144_1_MtL.root",
sampleBaseDir+"PATtuple_145_1_wJ0.root",
sampleBaseDir+"PATtuple_146_1_sLk.root",
sampleBaseDir+"PATtuple_147_1_T9n.root",
sampleBaseDir+"PATtuple_148_1_G0c.root",
sampleBaseDir+"PATtuple_149_1_dg9.root",
sampleBaseDir+"PATtuple_14_1_nmJ.root",
sampleBaseDir+"PATtuple_150_1_ldu.root",
sampleBaseDir+"PATtuple_151_1_uPY.root",
sampleBaseDir+"PATtuple_152_1_AJI.root",
sampleBaseDir+"PATtuple_153_1_ZRV.root",
sampleBaseDir+"PATtuple_154_1_SMo.root",
sampleBaseDir+"PATtuple_155_1_vbP.root",
sampleBaseDir+"PATtuple_156_1_9hd.root",
sampleBaseDir+"PATtuple_157_1_0Fk.root",
sampleBaseDir+"PATtuple_158_1_ijT.root",
sampleBaseDir+"PATtuple_159_1_ab8.root",
sampleBaseDir+"PATtuple_15_1_uv4.root",
sampleBaseDir+"PATtuple_160_1_2Gn.root",
sampleBaseDir+"PATtuple_161_1_Cfl.root",
sampleBaseDir+"PATtuple_162_1_Qw5.root",
sampleBaseDir+"PATtuple_163_1_daL.root",
sampleBaseDir+"PATtuple_164_2_Zhr.root",
sampleBaseDir+"PATtuple_165_1_i9r.root",
sampleBaseDir+"PATtuple_166_1_Gtc.root",
sampleBaseDir+"PATtuple_167_1_PlP.root",
sampleBaseDir+"PATtuple_168_1_roO.root",
sampleBaseDir+"PATtuple_169_1_y6m.root",
sampleBaseDir+"PATtuple_16_1_E8n.root",
sampleBaseDir+"PATtuple_170_1_g4X.root",
sampleBaseDir+"PATtuple_171_1_4ZE.root",
sampleBaseDir+"PATtuple_172_1_HsM.root",
sampleBaseDir+"PATtuple_173_1_b8w.root",
sampleBaseDir+"PATtuple_174_1_Mrg.root",
sampleBaseDir+"PATtuple_175_1_1Lm.root",
sampleBaseDir+"PATtuple_176_1_q13.root",
sampleBaseDir+"PATtuple_177_1_uAw.root",
sampleBaseDir+"PATtuple_178_1_lcZ.root",
sampleBaseDir+"PATtuple_179_1_ULz.root",
sampleBaseDir+"PATtuple_17_2_rPK.root",
sampleBaseDir+"PATtuple_180_1_mkv.root",
sampleBaseDir+"PATtuple_181_1_SWa.root",
sampleBaseDir+"PATtuple_182_1_N9E.root",
sampleBaseDir+"PATtuple_183_1_sRz.root",
sampleBaseDir+"PATtuple_184_1_VE6.root",
sampleBaseDir+"PATtuple_185_2_SDR.root",
sampleBaseDir+"PATtuple_186_1_lSv.root",
sampleBaseDir+"PATtuple_187_1_8Ue.root",
sampleBaseDir+"PATtuple_188_1_zxm.root",
sampleBaseDir+"PATtuple_189_1_2vD.root",
sampleBaseDir+"PATtuple_18_1_5i9.root",
sampleBaseDir+"PATtuple_190_1_TEz.root",
sampleBaseDir+"PATtuple_191_1_Mgt.root",
sampleBaseDir+"PATtuple_192_2_n1a.root",
sampleBaseDir+"PATtuple_193_1_CZ4.root",
sampleBaseDir+"PATtuple_194_1_Ekr.root",
sampleBaseDir+"PATtuple_195_1_tno.root",
sampleBaseDir+"PATtuple_196_2_yuR.root",
sampleBaseDir+"PATtuple_197_1_dvK.root",
sampleBaseDir+"PATtuple_198_1_E4o.root",
sampleBaseDir+"PATtuple_199_1_drb.root",
sampleBaseDir+"PATtuple_19_1_5Ru.root",
sampleBaseDir+"PATtuple_1_1_dXM.root",
sampleBaseDir+"PATtuple_200_2_qvh.root",
sampleBaseDir+"PATtuple_201_1_Ydk.root",
sampleBaseDir+"PATtuple_202_1_IvB.root",
sampleBaseDir+"PATtuple_203_1_CSN.root",
sampleBaseDir+"PATtuple_204_1_uIG.root",
sampleBaseDir+"PATtuple_205_1_BXR.root",
sampleBaseDir+"PATtuple_206_1_sGy.root",
sampleBaseDir+"PATtuple_207_1_Cv4.root",
sampleBaseDir+"PATtuple_208_1_Bys.root",
sampleBaseDir+"PATtuple_209_1_vWA.root",
sampleBaseDir+"PATtuple_20_1_8tn.root",
sampleBaseDir+"PATtuple_210_1_8Ed.root",
sampleBaseDir+"PATtuple_211_1_f18.root",
sampleBaseDir+"PATtuple_212_1_a9Q.root",
sampleBaseDir+"PATtuple_213_1_2nE.root",
sampleBaseDir+"PATtuple_214_1_aMA.root",
sampleBaseDir+"PATtuple_215_1_i4A.root",
sampleBaseDir+"PATtuple_216_1_LJh.root",
sampleBaseDir+"PATtuple_217_1_9dm.root",
sampleBaseDir+"PATtuple_218_1_uIK.root",
sampleBaseDir+"PATtuple_219_1_d04.root",
sampleBaseDir+"PATtuple_21_1_ukL.root",
sampleBaseDir+"PATtuple_220_1_43l.root",
sampleBaseDir+"PATtuple_221_1_vcS.root",
sampleBaseDir+"PATtuple_222_2_fp0.root",
sampleBaseDir+"PATtuple_223_2_MUI.root",
sampleBaseDir+"PATtuple_224_1_RyC.root",
sampleBaseDir+"PATtuple_225_1_v41.root",
sampleBaseDir+"PATtuple_226_1_Aa2.root",
sampleBaseDir+"PATtuple_227_1_MTB.root",
sampleBaseDir+"PATtuple_228_1_mG7.root",
sampleBaseDir+"PATtuple_229_1_eaR.root",
sampleBaseDir+"PATtuple_22_1_vRz.root",
sampleBaseDir+"PATtuple_230_1_T8E.root",
sampleBaseDir+"PATtuple_231_1_DeI.root",
sampleBaseDir+"PATtuple_232_1_5Rp.root",
sampleBaseDir+"PATtuple_233_1_gcq.root",
sampleBaseDir+"PATtuple_234_1_Ebs.root",
sampleBaseDir+"PATtuple_235_1_IP6.root",
sampleBaseDir+"PATtuple_236_1_i04.root",
sampleBaseDir+"PATtuple_237_1_Hj8.root",
sampleBaseDir+"PATtuple_238_1_qbB.root",
sampleBaseDir+"PATtuple_239_1_FBm.root",
sampleBaseDir+"PATtuple_23_1_5P9.root",
sampleBaseDir+"PATtuple_240_2_0cx.root",
sampleBaseDir+"PATtuple_241_1_V48.root",
sampleBaseDir+"PATtuple_242_1_BzG.root",
sampleBaseDir+"PATtuple_243_1_lVG.root",
sampleBaseDir+"PATtuple_244_1_5JS.root",
sampleBaseDir+"PATtuple_245_1_UHx.root",
sampleBaseDir+"PATtuple_246_1_pIl.root",
sampleBaseDir+"PATtuple_247_1_qTa.root",
sampleBaseDir+"PATtuple_248_1_tFf.root",
sampleBaseDir+"PATtuple_249_1_AB1.root",
sampleBaseDir+"PATtuple_24_1_kjK.root",
sampleBaseDir+"PATtuple_250_1_FL5.root",
sampleBaseDir+"PATtuple_251_1_xhU.root",
sampleBaseDir+"PATtuple_252_1_g5i.root",
sampleBaseDir+"PATtuple_253_1_Rde.root",
sampleBaseDir+"PATtuple_254_1_pKq.root",
sampleBaseDir+"PATtuple_255_1_nE0.root",
sampleBaseDir+"PATtuple_256_1_a7z.root",
sampleBaseDir+"PATtuple_257_1_Pie.root",
sampleBaseDir+"PATtuple_258_1_PuT.root",
sampleBaseDir+"PATtuple_259_1_brz.root",
sampleBaseDir+"PATtuple_25_1_eFm.root",
sampleBaseDir+"PATtuple_260_2_O8K.root",
sampleBaseDir+"PATtuple_261_2_btA.root",
sampleBaseDir+"PATtuple_262_1_RN3.root",
sampleBaseDir+"PATtuple_263_2_Y8V.root",
sampleBaseDir+"PATtuple_264_1_8zX.root",
sampleBaseDir+"PATtuple_265_1_q4t.root",
sampleBaseDir+"PATtuple_266_1_CPl.root",
sampleBaseDir+"PATtuple_267_1_joN.root",
sampleBaseDir+"PATtuple_268_1_QXf.root",
sampleBaseDir+"PATtuple_269_1_kQI.root",
sampleBaseDir+"PATtuple_26_1_4GN.root",
sampleBaseDir+"PATtuple_270_1_QQi.root",
sampleBaseDir+"PATtuple_271_1_O0E.root",
sampleBaseDir+"PATtuple_272_1_57O.root",
sampleBaseDir+"PATtuple_273_1_wU2.root",
sampleBaseDir+"PATtuple_274_1_4Y2.root",
sampleBaseDir+"PATtuple_275_1_CJx.root",
sampleBaseDir+"PATtuple_276_1_jBR.root",
sampleBaseDir+"PATtuple_277_1_Ys2.root",
sampleBaseDir+"PATtuple_278_1_3HI.root",
sampleBaseDir+"PATtuple_279_1_jns.root",
sampleBaseDir+"PATtuple_27_1_FZT.root",
sampleBaseDir+"PATtuple_280_1_yg1.root",
sampleBaseDir+"PATtuple_281_1_U36.root",
sampleBaseDir+"PATtuple_282_1_l3A.root",
sampleBaseDir+"PATtuple_283_1_3we.root",
sampleBaseDir+"PATtuple_284_1_cv4.root",
sampleBaseDir+"PATtuple_285_1_Duq.root",
sampleBaseDir+"PATtuple_286_2_cg4.root",
sampleBaseDir+"PATtuple_287_2_S7i.root",
sampleBaseDir+"PATtuple_288_1_Ptw.root",
sampleBaseDir+"PATtuple_289_1_llo.root",
sampleBaseDir+"PATtuple_28_1_Wfz.root",
sampleBaseDir+"PATtuple_290_1_VD1.root",
sampleBaseDir+"PATtuple_291_1_poW.root",
sampleBaseDir+"PATtuple_292_3_zSN.root",
sampleBaseDir+"PATtuple_293_1_aUj.root",
sampleBaseDir+"PATtuple_294_1_GcG.root",
sampleBaseDir+"PATtuple_295_1_8Eh.root",
sampleBaseDir+"PATtuple_296_1_HP9.root",
sampleBaseDir+"PATtuple_297_1_grR.root",
sampleBaseDir+"PATtuple_298_1_bHM.root",
sampleBaseDir+"PATtuple_299_1_krl.root",
sampleBaseDir+"PATtuple_29_1_zYt.root",
sampleBaseDir+"PATtuple_2_1_0uE.root",
sampleBaseDir+"PATtuple_300_1_40R.root",
sampleBaseDir+"PATtuple_301_1_Oea.root",
sampleBaseDir+"PATtuple_302_1_fou.root",
sampleBaseDir+"PATtuple_303_1_Hj6.root",
sampleBaseDir+"PATtuple_304_1_8b9.root",
sampleBaseDir+"PATtuple_305_1_KV2.root",
sampleBaseDir+"PATtuple_306_1_tgi.root",
sampleBaseDir+"PATtuple_307_1_10x.root",
sampleBaseDir+"PATtuple_308_1_nc9.root",
sampleBaseDir+"PATtuple_309_1_Zgu.root",
sampleBaseDir+"PATtuple_30_1_wi1.root",
sampleBaseDir+"PATtuple_310_1_L3t.root",
sampleBaseDir+"PATtuple_311_1_Aot.root",
sampleBaseDir+"PATtuple_312_1_yz0.root",
sampleBaseDir+"PATtuple_313_1_hHm.root",
sampleBaseDir+"PATtuple_314_1_8eS.root",
sampleBaseDir+"PATtuple_315_1_Tv0.root",
sampleBaseDir+"PATtuple_316_1_InT.root",
sampleBaseDir+"PATtuple_317_1_KR2.root",
sampleBaseDir+"PATtuple_318_1_ElG.root",
sampleBaseDir+"PATtuple_319_1_ClD.root",
sampleBaseDir+"PATtuple_31_1_QaN.root",
sampleBaseDir+"PATtuple_320_1_WIV.root",
sampleBaseDir+"PATtuple_321_1_sPW.root",
sampleBaseDir+"PATtuple_322_1_Nay.root",
sampleBaseDir+"PATtuple_323_1_o7l.root",
sampleBaseDir+"PATtuple_324_1_Uq6.root",
sampleBaseDir+"PATtuple_325_1_XLH.root",
sampleBaseDir+"PATtuple_326_1_Wy8.root",
sampleBaseDir+"PATtuple_327_1_DjE.root",
sampleBaseDir+"PATtuple_328_1_3Ie.root",
sampleBaseDir+"PATtuple_329_2_00k.root",
sampleBaseDir+"PATtuple_32_1_Fxt.root",
sampleBaseDir+"PATtuple_330_1_2Dl.root",
sampleBaseDir+"PATtuple_331_1_YSV.root",
sampleBaseDir+"PATtuple_332_1_zly.root",
sampleBaseDir+"PATtuple_333_2_xik.root",
sampleBaseDir+"PATtuple_334_1_mHz.root",
sampleBaseDir+"PATtuple_335_1_2Uh.root",
sampleBaseDir+"PATtuple_336_1_O9R.root",
sampleBaseDir+"PATtuple_337_1_LOP.root",
sampleBaseDir+"PATtuple_338_1_MgH.root",
sampleBaseDir+"PATtuple_339_1_vyN.root",
sampleBaseDir+"PATtuple_33_1_pkC.root",
sampleBaseDir+"PATtuple_340_2_RhB.root",
sampleBaseDir+"PATtuple_341_1_r5j.root",
sampleBaseDir+"PATtuple_342_1_jbJ.root",
sampleBaseDir+"PATtuple_343_2_EKB.root",
sampleBaseDir+"PATtuple_344_1_YTq.root",
sampleBaseDir+"PATtuple_345_1_ysk.root",
sampleBaseDir+"PATtuple_346_1_WPQ.root",
sampleBaseDir+"PATtuple_347_1_Ljn.root",
sampleBaseDir+"PATtuple_348_1_xcS.root",
sampleBaseDir+"PATtuple_349_1_NB3.root",
sampleBaseDir+"PATtuple_34_1_F8G.root",
sampleBaseDir+"PATtuple_350_2_hsO.root",
sampleBaseDir+"PATtuple_351_2_OAZ.root",
sampleBaseDir+"PATtuple_352_1_0A4.root",
sampleBaseDir+"PATtuple_353_1_WnJ.root",
sampleBaseDir+"PATtuple_354_1_5ni.root",
sampleBaseDir+"PATtuple_355_2_8zY.root",
sampleBaseDir+"PATtuple_356_1_4H1.root",
sampleBaseDir+"PATtuple_357_1_2ov.root",
sampleBaseDir+"PATtuple_358_1_AYA.root",
sampleBaseDir+"PATtuple_359_2_N7e.root",
sampleBaseDir+"PATtuple_35_1_niT.root",
sampleBaseDir+"PATtuple_360_1_vvL.root",
sampleBaseDir+"PATtuple_361_1_vlQ.root",
sampleBaseDir+"PATtuple_362_1_uj1.root",
sampleBaseDir+"PATtuple_363_1_wDE.root",
sampleBaseDir+"PATtuple_364_1_iiV.root",
sampleBaseDir+"PATtuple_365_1_VA0.root",
sampleBaseDir+"PATtuple_366_1_0En.root",
sampleBaseDir+"PATtuple_367_1_KV9.root",
sampleBaseDir+"PATtuple_368_1_j2d.root",
sampleBaseDir+"PATtuple_369_1_QtB.root",
sampleBaseDir+"PATtuple_36_1_nco.root",
sampleBaseDir+"PATtuple_370_1_Qpg.root",
sampleBaseDir+"PATtuple_371_1_v5l.root",
sampleBaseDir+"PATtuple_372_1_DpI.root",
sampleBaseDir+"PATtuple_373_1_aUk.root",
sampleBaseDir+"PATtuple_374_2_qDM.root",
sampleBaseDir+"PATtuple_375_2_WXD.root",
sampleBaseDir+"PATtuple_376_2_39v.root",
sampleBaseDir+"PATtuple_377_1_vmq.root",
sampleBaseDir+"PATtuple_378_1_5GE.root",
sampleBaseDir+"PATtuple_379_1_Blm.root",
sampleBaseDir+"PATtuple_37_1_idA.root",
sampleBaseDir+"PATtuple_380_1_Sbo.root",
sampleBaseDir+"PATtuple_381_1_K2q.root",
sampleBaseDir+"PATtuple_382_1_9j2.root",
sampleBaseDir+"PATtuple_383_1_yXm.root",
sampleBaseDir+"PATtuple_384_1_RNS.root",
sampleBaseDir+"PATtuple_385_1_kis.root",
sampleBaseDir+"PATtuple_386_2_SMM.root",
sampleBaseDir+"PATtuple_387_1_WhB.root",
sampleBaseDir+"PATtuple_388_1_DK8.root",
sampleBaseDir+"PATtuple_389_1_Xxl.root",
sampleBaseDir+"PATtuple_38_1_vIS.root",
sampleBaseDir+"PATtuple_390_1_3DY.root",
sampleBaseDir+"PATtuple_391_1_jYk.root",
sampleBaseDir+"PATtuple_392_1_j35.root",
sampleBaseDir+"PATtuple_393_1_hgs.root",
sampleBaseDir+"PATtuple_394_1_Rl9.root",
sampleBaseDir+"PATtuple_395_2_y0c.root",
sampleBaseDir+"PATtuple_396_1_ElE.root",
sampleBaseDir+"PATtuple_397_1_K93.root",
sampleBaseDir+"PATtuple_398_1_PhO.root",
sampleBaseDir+"PATtuple_399_1_asT.root",
sampleBaseDir+"PATtuple_39_2_wuk.root",
sampleBaseDir+"PATtuple_3_1_DTi.root",
sampleBaseDir+"PATtuple_400_1_ECp.root",
sampleBaseDir+"PATtuple_401_1_mmp.root",
sampleBaseDir+"PATtuple_402_1_brg.root",
sampleBaseDir+"PATtuple_403_1_1ui.root",
sampleBaseDir+"PATtuple_404_1_xuA.root",
sampleBaseDir+"PATtuple_405_1_NaD.root",
sampleBaseDir+"PATtuple_406_2_8oN.root",
sampleBaseDir+"PATtuple_407_1_8Ep.root",
sampleBaseDir+"PATtuple_408_1_zxG.root",
sampleBaseDir+"PATtuple_409_1_PLa.root",
sampleBaseDir+"PATtuple_40_1_SiH.root",
sampleBaseDir+"PATtuple_410_2_8Eo.root",
sampleBaseDir+"PATtuple_411_3_Len.root",
sampleBaseDir+"PATtuple_412_1_FvT.root",
sampleBaseDir+"PATtuple_413_1_laf.root",
sampleBaseDir+"PATtuple_414_1_fs2.root",
sampleBaseDir+"PATtuple_415_1_WlZ.root",
sampleBaseDir+"PATtuple_416_1_aSv.root",
sampleBaseDir+"PATtuple_417_1_zMp.root",
sampleBaseDir+"PATtuple_418_1_IEf.root",
sampleBaseDir+"PATtuple_419_1_AJ4.root",
sampleBaseDir+"PATtuple_41_1_u8E.root",
sampleBaseDir+"PATtuple_420_1_O71.root",
sampleBaseDir+"PATtuple_421_1_uyl.root",
sampleBaseDir+"PATtuple_422_1_8J2.root",
sampleBaseDir+"PATtuple_423_1_raX.root",
sampleBaseDir+"PATtuple_424_1_gYG.root",
sampleBaseDir+"PATtuple_425_1_i82.root",
sampleBaseDir+"PATtuple_426_1_87f.root",
sampleBaseDir+"PATtuple_427_1_49B.root",
sampleBaseDir+"PATtuple_428_1_Rjg.root",
sampleBaseDir+"PATtuple_429_1_9at.root",
sampleBaseDir+"PATtuple_42_1_25A.root",
sampleBaseDir+"PATtuple_430_1_UYr.root",
sampleBaseDir+"PATtuple_431_1_emo.root",
sampleBaseDir+"PATtuple_432_1_pwX.root",
sampleBaseDir+"PATtuple_433_1_bHl.root",
sampleBaseDir+"PATtuple_434_1_jrt.root",
sampleBaseDir+"PATtuple_435_1_mPZ.root",
sampleBaseDir+"PATtuple_436_1_6wP.root",
sampleBaseDir+"PATtuple_437_1_mJc.root",
sampleBaseDir+"PATtuple_438_1_j9t.root",
sampleBaseDir+"PATtuple_439_1_Rrz.root",
sampleBaseDir+"PATtuple_43_1_Iwr.root",
sampleBaseDir+"PATtuple_440_2_Z8d.root",
sampleBaseDir+"PATtuple_441_1_ahx.root",
sampleBaseDir+"PATtuple_442_1_g5T.root",
sampleBaseDir+"PATtuple_443_2_OFT.root",
sampleBaseDir+"PATtuple_444_1_w7O.root",
sampleBaseDir+"PATtuple_445_2_pfx.root",
sampleBaseDir+"PATtuple_446_1_unB.root",
sampleBaseDir+"PATtuple_447_1_Knw.root",
sampleBaseDir+"PATtuple_448_2_wIy.root",
sampleBaseDir+"PATtuple_449_1_aBj.root",
sampleBaseDir+"PATtuple_44_1_o54.root",
sampleBaseDir+"PATtuple_450_1_icO.root",
sampleBaseDir+"PATtuple_451_1_ukN.root",
sampleBaseDir+"PATtuple_452_1_NvB.root",
sampleBaseDir+"PATtuple_453_1_2mx.root",
sampleBaseDir+"PATtuple_454_1_S4U.root",
sampleBaseDir+"PATtuple_455_2_8cS.root",
sampleBaseDir+"PATtuple_456_1_Ruk.root",
sampleBaseDir+"PATtuple_457_2_EHe.root",
sampleBaseDir+"PATtuple_458_1_OCu.root",
sampleBaseDir+"PATtuple_459_1_eOe.root",
sampleBaseDir+"PATtuple_45_1_qTK.root",
sampleBaseDir+"PATtuple_460_1_7ZR.root",
sampleBaseDir+"PATtuple_461_1_tuM.root",
sampleBaseDir+"PATtuple_462_1_RZh.root",
sampleBaseDir+"PATtuple_463_2_CC1.root",
sampleBaseDir+"PATtuple_464_2_Jm8.root",
sampleBaseDir+"PATtuple_465_1_9G8.root",
sampleBaseDir+"PATtuple_466_1_5Nx.root",
sampleBaseDir+"PATtuple_467_1_Eth.root",
sampleBaseDir+"PATtuple_468_1_Z6r.root",
sampleBaseDir+"PATtuple_469_1_RfU.root",
sampleBaseDir+"PATtuple_46_1_hue.root",
sampleBaseDir+"PATtuple_470_1_rS9.root",
sampleBaseDir+"PATtuple_471_1_7De.root",
sampleBaseDir+"PATtuple_472_1_T51.root",
sampleBaseDir+"PATtuple_473_2_e19.root",
sampleBaseDir+"PATtuple_474_2_zTz.root",
sampleBaseDir+"PATtuple_475_2_pHb.root",
sampleBaseDir+"PATtuple_476_1_0sO.root",
sampleBaseDir+"PATtuple_477_2_Y26.root",
sampleBaseDir+"PATtuple_478_2_ql6.root",
sampleBaseDir+"PATtuple_479_2_6gL.root",
sampleBaseDir+"PATtuple_47_1_9C3.root",
sampleBaseDir+"PATtuple_480_1_BAF.root",
sampleBaseDir+"PATtuple_481_2_Rpg.root",
sampleBaseDir+"PATtuple_482_1_Stz.root",
sampleBaseDir+"PATtuple_483_1_on8.root",
sampleBaseDir+"PATtuple_484_3_r09.root",
sampleBaseDir+"PATtuple_485_1_ukt.root",
sampleBaseDir+"PATtuple_486_2_IVd.root",
sampleBaseDir+"PATtuple_487_2_DuN.root",
sampleBaseDir+"PATtuple_488_1_YwH.root",
sampleBaseDir+"PATtuple_489_1_NOh.root",
sampleBaseDir+"PATtuple_48_1_A65.root",
sampleBaseDir+"PATtuple_490_1_6gl.root",
sampleBaseDir+"PATtuple_491_1_I3O.root",
sampleBaseDir+"PATtuple_492_2_KBJ.root",
sampleBaseDir+"PATtuple_493_1_7EF.root",
sampleBaseDir+"PATtuple_494_1_s6J.root",
sampleBaseDir+"PATtuple_495_2_Gu6.root",
sampleBaseDir+"PATtuple_496_1_A9b.root",
sampleBaseDir+"PATtuple_497_1_5Hc.root",
sampleBaseDir+"PATtuple_498_1_rlg.root",
sampleBaseDir+"PATtuple_499_2_3T8.root",
sampleBaseDir+"PATtuple_49_1_GaQ.root",
sampleBaseDir+"PATtuple_4_1_Yk3.root",
sampleBaseDir+"PATtuple_500_1_fWn.root",
sampleBaseDir+"PATtuple_501_1_mds.root",
sampleBaseDir+"PATtuple_502_1_6hZ.root",
sampleBaseDir+"PATtuple_503_2_aOC.root",
sampleBaseDir+"PATtuple_504_1_ZZb.root",
sampleBaseDir+"PATtuple_505_1_sRA.root",
sampleBaseDir+"PATtuple_506_1_lJ9.root",
sampleBaseDir+"PATtuple_507_1_RNX.root",
sampleBaseDir+"PATtuple_508_1_P1d.root",
sampleBaseDir+"PATtuple_509_2_OvT.root",
sampleBaseDir+"PATtuple_50_1_Afl.root",
sampleBaseDir+"PATtuple_510_1_DQT.root",
sampleBaseDir+"PATtuple_511_1_bYv.root",
sampleBaseDir+"PATtuple_512_1_GKN.root",
sampleBaseDir+"PATtuple_513_1_Saq.root",
sampleBaseDir+"PATtuple_514_1_8pE.root",
sampleBaseDir+"PATtuple_515_2_VXt.root",
sampleBaseDir+"PATtuple_516_2_4vu.root",
sampleBaseDir+"PATtuple_517_1_gci.root",
sampleBaseDir+"PATtuple_518_1_MvH.root",
sampleBaseDir+"PATtuple_519_1_YH5.root",
sampleBaseDir+"PATtuple_51_1_8zu.root",
sampleBaseDir+"PATtuple_520_3_LMA.root",
sampleBaseDir+"PATtuple_521_1_mo8.root",
sampleBaseDir+"PATtuple_522_1_keu.root",
sampleBaseDir+"PATtuple_523_2_FSg.root",
sampleBaseDir+"PATtuple_524_1_U9a.root",
sampleBaseDir+"PATtuple_525_1_ItY.root",
sampleBaseDir+"PATtuple_526_2_kPI.root",
sampleBaseDir+"PATtuple_527_2_YfC.root",
sampleBaseDir+"PATtuple_528_2_dYR.root",
sampleBaseDir+"PATtuple_529_1_tRP.root",
sampleBaseDir+"PATtuple_52_1_Iqc.root",
sampleBaseDir+"PATtuple_530_1_727.root",
sampleBaseDir+"PATtuple_531_1_37X.root",
sampleBaseDir+"PATtuple_532_1_COC.root",
sampleBaseDir+"PATtuple_533_1_wDh.root",
sampleBaseDir+"PATtuple_534_1_Ank.root",
sampleBaseDir+"PATtuple_535_1_mxu.root",
sampleBaseDir+"PATtuple_536_2_O1i.root",
sampleBaseDir+"PATtuple_537_2_efr.root",
sampleBaseDir+"PATtuple_538_2_7jY.root",
sampleBaseDir+"PATtuple_539_1_vGs.root",
sampleBaseDir+"PATtuple_53_1_a5N.root",
sampleBaseDir+"PATtuple_540_1_EmU.root",
sampleBaseDir+"PATtuple_541_1_hzA.root",
sampleBaseDir+"PATtuple_542_1_M1Z.root",
sampleBaseDir+"PATtuple_543_1_Kr9.root",
sampleBaseDir+"PATtuple_544_2_EPQ.root",
sampleBaseDir+"PATtuple_545_2_RyR.root",
sampleBaseDir+"PATtuple_546_1_set.root",
sampleBaseDir+"PATtuple_547_2_ovP.root",
sampleBaseDir+"PATtuple_548_1_c0c.root",
sampleBaseDir+"PATtuple_549_2_AB3.root",
sampleBaseDir+"PATtuple_54_1_ig2.root",
sampleBaseDir+"PATtuple_550_1_zqT.root",
sampleBaseDir+"PATtuple_551_1_oMS.root",
sampleBaseDir+"PATtuple_552_4_aP7.root",
sampleBaseDir+"PATtuple_553_1_XlX.root",
sampleBaseDir+"PATtuple_554_1_cZ0.root",
sampleBaseDir+"PATtuple_555_2_Rwh.root",
sampleBaseDir+"PATtuple_556_1_Xxv.root",
sampleBaseDir+"PATtuple_557_1_Kb2.root",
sampleBaseDir+"PATtuple_558_1_D52.root",
sampleBaseDir+"PATtuple_559_2_akU.root",
sampleBaseDir+"PATtuple_55_1_RX9.root",
sampleBaseDir+"PATtuple_560_1_jOK.root",
sampleBaseDir+"PATtuple_561_1_Ojg.root",
sampleBaseDir+"PATtuple_562_1_aVX.root",
sampleBaseDir+"PATtuple_563_1_GPe.root",
sampleBaseDir+"PATtuple_564_2_LuE.root",
sampleBaseDir+"PATtuple_565_1_cOd.root",
sampleBaseDir+"PATtuple_566_1_H3H.root",
sampleBaseDir+"PATtuple_567_1_L0r.root",
sampleBaseDir+"PATtuple_568_2_8Lp.root",
sampleBaseDir+"PATtuple_569_2_XtJ.root",
sampleBaseDir+"PATtuple_56_1_0KA.root",
sampleBaseDir+"PATtuple_570_1_wgH.root",
sampleBaseDir+"PATtuple_571_1_rZu.root",
sampleBaseDir+"PATtuple_572_1_rGB.root",
sampleBaseDir+"PATtuple_573_1_UCa.root",
sampleBaseDir+"PATtuple_574_1_S0I.root",
sampleBaseDir+"PATtuple_575_1_kI9.root",
sampleBaseDir+"PATtuple_576_1_Mot.root",
sampleBaseDir+"PATtuple_577_1_3x1.root",
sampleBaseDir+"PATtuple_578_1_rlE.root",
sampleBaseDir+"PATtuple_579_2_1Sw.root",
sampleBaseDir+"PATtuple_57_1_ufp.root",
sampleBaseDir+"PATtuple_580_1_ymK.root",
sampleBaseDir+"PATtuple_581_1_z9q.root",
sampleBaseDir+"PATtuple_582_2_6ou.root",
sampleBaseDir+"PATtuple_583_1_tdg.root",
sampleBaseDir+"PATtuple_584_2_aPW.root",
sampleBaseDir+"PATtuple_585_2_Zk9.root",
sampleBaseDir+"PATtuple_586_1_Uc6.root",
sampleBaseDir+"PATtuple_587_1_99p.root",
sampleBaseDir+"PATtuple_588_1_5We.root",
sampleBaseDir+"PATtuple_589_2_rg4.root",
sampleBaseDir+"PATtuple_58_1_KZZ.root",
sampleBaseDir+"PATtuple_590_1_lGZ.root",
sampleBaseDir+"PATtuple_591_2_PHL.root",
sampleBaseDir+"PATtuple_592_1_0g0.root",
sampleBaseDir+"PATtuple_593_1_qs9.root",
sampleBaseDir+"PATtuple_594_1_j8z.root",
sampleBaseDir+"PATtuple_595_1_Qm2.root",
sampleBaseDir+"PATtuple_596_1_EJx.root",
sampleBaseDir+"PATtuple_597_1_CXq.root",
sampleBaseDir+"PATtuple_598_1_nV9.root",
sampleBaseDir+"PATtuple_599_1_gkN.root",
sampleBaseDir+"PATtuple_59_1_K64.root",
sampleBaseDir+"PATtuple_5_1_3kQ.root",
sampleBaseDir+"PATtuple_600_1_sMC.root",
sampleBaseDir+"PATtuple_601_2_7gb.root",
sampleBaseDir+"PATtuple_602_1_w6W.root",
sampleBaseDir+"PATtuple_603_2_mNq.root",
sampleBaseDir+"PATtuple_604_1_CAD.root",
sampleBaseDir+"PATtuple_605_1_3OH.root",
sampleBaseDir+"PATtuple_606_2_wsk.root",
sampleBaseDir+"PATtuple_607_1_RYL.root",
sampleBaseDir+"PATtuple_608_1_TaM.root",
sampleBaseDir+"PATtuple_609_1_723.root",
sampleBaseDir+"PATtuple_60_1_QY1.root",
sampleBaseDir+"PATtuple_610_1_PMb.root",
sampleBaseDir+"PATtuple_611_3_4tV.root",
sampleBaseDir+"PATtuple_612_1_70Z.root",
sampleBaseDir+"PATtuple_613_1_4X3.root",
sampleBaseDir+"PATtuple_614_1_JKF.root",
sampleBaseDir+"PATtuple_615_1_1hi.root",
sampleBaseDir+"PATtuple_616_1_5Fn.root",
sampleBaseDir+"PATtuple_617_1_UZB.root",
sampleBaseDir+"PATtuple_618_1_HjL.root",
sampleBaseDir+"PATtuple_619_1_Rx0.root",
sampleBaseDir+"PATtuple_61_1_HML.root",
sampleBaseDir+"PATtuple_620_1_GLP.root",
sampleBaseDir+"PATtuple_621_1_A9B.root",
sampleBaseDir+"PATtuple_622_2_6Li.root",
sampleBaseDir+"PATtuple_623_1_APv.root",
sampleBaseDir+"PATtuple_624_1_z48.root",
sampleBaseDir+"PATtuple_625_1_d5f.root",
sampleBaseDir+"PATtuple_626_2_4KL.root",
sampleBaseDir+"PATtuple_627_1_t72.root",
sampleBaseDir+"PATtuple_628_2_L2f.root",
sampleBaseDir+"PATtuple_629_1_FZT.root",
sampleBaseDir+"PATtuple_62_1_CvF.root",
sampleBaseDir+"PATtuple_630_1_aus.root",
sampleBaseDir+"PATtuple_631_1_RTF.root",
sampleBaseDir+"PATtuple_632_1_Bw0.root",
sampleBaseDir+"PATtuple_633_1_HFX.root",
sampleBaseDir+"PATtuple_634_2_QUt.root",
sampleBaseDir+"PATtuple_635_1_QPb.root",
sampleBaseDir+"PATtuple_636_1_lUf.root",
sampleBaseDir+"PATtuple_637_1_AIz.root",
sampleBaseDir+"PATtuple_638_1_zJn.root",
sampleBaseDir+"PATtuple_639_2_5tr.root",
sampleBaseDir+"PATtuple_63_3_icC.root",
sampleBaseDir+"PATtuple_640_1_VoP.root",
sampleBaseDir+"PATtuple_641_1_KuA.root",
sampleBaseDir+"PATtuple_642_1_UuP.root",
sampleBaseDir+"PATtuple_643_2_NWB.root",
sampleBaseDir+"PATtuple_644_2_A3J.root",
sampleBaseDir+"PATtuple_645_2_AnQ.root",
sampleBaseDir+"PATtuple_646_2_Uj0.root",
sampleBaseDir+"PATtuple_647_1_LbV.root",
sampleBaseDir+"PATtuple_648_1_aQv.root",
sampleBaseDir+"PATtuple_649_1_UxR.root",
sampleBaseDir+"PATtuple_64_1_vJ4.root",
sampleBaseDir+"PATtuple_65_1_aS4.root",
sampleBaseDir+"PATtuple_66_1_8bn.root",
sampleBaseDir+"PATtuple_67_1_6cG.root",
sampleBaseDir+"PATtuple_68_1_8d1.root",
sampleBaseDir+"PATtuple_69_3_Ldw.root",
sampleBaseDir+"PATtuple_6_1_aN4.root",
sampleBaseDir+"PATtuple_70_1_Anu.root",
sampleBaseDir+"PATtuple_71_1_e0e.root",
sampleBaseDir+"PATtuple_72_1_Lsn.root",
sampleBaseDir+"PATtuple_73_1_5sY.root",
sampleBaseDir+"PATtuple_74_1_5L2.root",
sampleBaseDir+"PATtuple_75_1_jLL.root",
sampleBaseDir+"PATtuple_76_1_EQP.root",
sampleBaseDir+"PATtuple_77_1_3v0.root",
sampleBaseDir+"PATtuple_78_1_Yxl.root",
sampleBaseDir+"PATtuple_79_1_1QU.root",
sampleBaseDir+"PATtuple_7_1_8kt.root",
sampleBaseDir+"PATtuple_80_1_oCi.root",
sampleBaseDir+"PATtuple_81_1_RzB.root",
sampleBaseDir+"PATtuple_82_1_Eg0.root",
sampleBaseDir+"PATtuple_83_1_heE.root",
sampleBaseDir+"PATtuple_84_1_eXA.root",
sampleBaseDir+"PATtuple_85_1_Xlu.root",
sampleBaseDir+"PATtuple_86_1_afV.root",
sampleBaseDir+"PATtuple_87_1_ZSF.root",
sampleBaseDir+"PATtuple_88_1_WXG.root",
sampleBaseDir+"PATtuple_89_1_xE9.root",
sampleBaseDir+"PATtuple_8_1_t9A.root",
sampleBaseDir+"PATtuple_90_1_O8J.root",
sampleBaseDir+"PATtuple_91_3_NVK.root",
sampleBaseDir+"PATtuple_92_1_DQL.root",
sampleBaseDir+"PATtuple_93_1_jrB.root",
sampleBaseDir+"PATtuple_94_1_GK1.root",
sampleBaseDir+"PATtuple_95_1_6mE.root",
sampleBaseDir+"PATtuple_96_1_Hm1.root",
sampleBaseDir+"PATtuple_97_1_0sH.root",
sampleBaseDir+"PATtuple_98_1_tTu.root",
sampleBaseDir+"PATtuple_99_1_3aV.root",
sampleBaseDir+"PATtuple_9_1_esw.root",
]