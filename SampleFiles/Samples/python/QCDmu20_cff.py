sampleDataSet = '/QCD_Pt_20_MuEnrichedPt_15_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v3/AODSIM'  

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_2_patch4" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_5" # release used to create new files with

sampleNumEvents = 21484602

sampleXSec = 3.64E8 * 3.7E-4 # pb

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7F::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "BKGMC"




samplePatDBSName=""

sampleBaseDir="file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/QCDmu20_pat_20140328/demattia//QCD_Pt_20_MuEnrichedPt_15_TuneZ2star_8TeV_pythia6/QCDmu20_pat_20140328/5fe3dadd93bf8608b396f970098158ed/"
samplePatFiles = [
sampleBaseDir+"PATtuple_100_1_TGm.root",
sampleBaseDir+"PATtuple_101_1_XZ3.root",
sampleBaseDir+"PATtuple_102_1_sh5.root",
sampleBaseDir+"PATtuple_103_1_u5T.root",
sampleBaseDir+"PATtuple_104_1_y91.root",
sampleBaseDir+"PATtuple_105_1_9X3.root",
sampleBaseDir+"PATtuple_106_1_9UT.root",
sampleBaseDir+"PATtuple_107_1_FQC.root",
sampleBaseDir+"PATtuple_108_1_cga.root",
sampleBaseDir+"PATtuple_109_1_2na.root",
sampleBaseDir+"PATtuple_10_1_MHt.root",
sampleBaseDir+"PATtuple_110_1_B4Z.root",
sampleBaseDir+"PATtuple_111_1_acZ.root",
sampleBaseDir+"PATtuple_112_1_cDF.root",
sampleBaseDir+"PATtuple_113_1_5eF.root",
sampleBaseDir+"PATtuple_114_1_4cQ.root",
sampleBaseDir+"PATtuple_115_1_uwX.root",
sampleBaseDir+"PATtuple_116_1_Vt3.root",
sampleBaseDir+"PATtuple_117_1_IcA.root",
sampleBaseDir+"PATtuple_118_1_gNe.root",
sampleBaseDir+"PATtuple_119_1_Rym.root",
sampleBaseDir+"PATtuple_11_1_e9F.root",
sampleBaseDir+"PATtuple_120_1_12D.root",
sampleBaseDir+"PATtuple_121_1_u1g.root",
sampleBaseDir+"PATtuple_122_1_93g.root",
sampleBaseDir+"PATtuple_123_1_cU9.root",
sampleBaseDir+"PATtuple_124_1_iCA.root",
sampleBaseDir+"PATtuple_125_1_Zy2.root",
sampleBaseDir+"PATtuple_126_1_YfH.root",
sampleBaseDir+"PATtuple_127_1_9dO.root",
sampleBaseDir+"PATtuple_128_1_b5x.root",
sampleBaseDir+"PATtuple_129_1_gM9.root",
sampleBaseDir+"PATtuple_12_1_iBq.root",
sampleBaseDir+"PATtuple_130_1_KTY.root",
sampleBaseDir+"PATtuple_131_1_vfq.root",
sampleBaseDir+"PATtuple_132_1_Goc.root",
sampleBaseDir+"PATtuple_133_1_Wbz.root",
sampleBaseDir+"PATtuple_134_1_GgM.root",
sampleBaseDir+"PATtuple_135_1_EWp.root",
sampleBaseDir+"PATtuple_136_1_d31.root",
sampleBaseDir+"PATtuple_137_1_nN6.root",
sampleBaseDir+"PATtuple_138_1_hNQ.root",
sampleBaseDir+"PATtuple_139_1_7pO.root",
sampleBaseDir+"PATtuple_13_1_IB2.root",
sampleBaseDir+"PATtuple_140_1_cwu.root",
sampleBaseDir+"PATtuple_141_1_BNX.root",
sampleBaseDir+"PATtuple_142_1_lxS.root",
sampleBaseDir+"PATtuple_143_1_iBl.root",
sampleBaseDir+"PATtuple_144_1_qaU.root",
sampleBaseDir+"PATtuple_145_1_q17.root",
sampleBaseDir+"PATtuple_146_1_Df1.root",
sampleBaseDir+"PATtuple_147_1_fma.root",
sampleBaseDir+"PATtuple_148_1_x6R.root",
sampleBaseDir+"PATtuple_149_1_c3p.root",
sampleBaseDir+"PATtuple_14_1_u57.root",
sampleBaseDir+"PATtuple_150_1_lee.root",
sampleBaseDir+"PATtuple_151_1_Yq4.root",
sampleBaseDir+"PATtuple_152_1_TqZ.root",
sampleBaseDir+"PATtuple_153_1_M6M.root",
sampleBaseDir+"PATtuple_154_1_xNL.root",
sampleBaseDir+"PATtuple_155_1_Yv0.root",
sampleBaseDir+"PATtuple_156_1_vCc.root",
sampleBaseDir+"PATtuple_157_1_0iu.root",
sampleBaseDir+"PATtuple_158_1_6uu.root",
sampleBaseDir+"PATtuple_159_1_ZsT.root",
sampleBaseDir+"PATtuple_15_1_Yc1.root",
sampleBaseDir+"PATtuple_160_1_LTf.root",
sampleBaseDir+"PATtuple_161_1_Djt.root",
sampleBaseDir+"PATtuple_162_1_6lB.root",
sampleBaseDir+"PATtuple_163_1_Ldy.root",
sampleBaseDir+"PATtuple_164_1_ZtE.root",
sampleBaseDir+"PATtuple_165_1_oyc.root",
sampleBaseDir+"PATtuple_166_1_1xM.root",
sampleBaseDir+"PATtuple_167_1_TDp.root",
sampleBaseDir+"PATtuple_168_1_FYI.root",
sampleBaseDir+"PATtuple_169_1_qUB.root",
sampleBaseDir+"PATtuple_16_1_PIa.root",
sampleBaseDir+"PATtuple_170_1_C8k.root",
sampleBaseDir+"PATtuple_171_1_1EY.root",
sampleBaseDir+"PATtuple_172_1_FWa.root",
sampleBaseDir+"PATtuple_173_1_Gtl.root",
sampleBaseDir+"PATtuple_174_1_DJc.root",
sampleBaseDir+"PATtuple_175_1_vW4.root",
sampleBaseDir+"PATtuple_176_1_vLu.root",
sampleBaseDir+"PATtuple_177_1_Ca4.root",
sampleBaseDir+"PATtuple_178_1_trx.root",
sampleBaseDir+"PATtuple_179_1_8Ni.root",
sampleBaseDir+"PATtuple_17_1_U63.root",
sampleBaseDir+"PATtuple_180_1_eDS.root",
sampleBaseDir+"PATtuple_181_1_PJC.root",
sampleBaseDir+"PATtuple_182_1_b09.root",
sampleBaseDir+"PATtuple_183_1_q7E.root",
sampleBaseDir+"PATtuple_184_1_drY.root",
sampleBaseDir+"PATtuple_185_1_kJ7.root",
sampleBaseDir+"PATtuple_186_1_RJF.root",
sampleBaseDir+"PATtuple_187_1_oQW.root",
sampleBaseDir+"PATtuple_188_1_BkL.root",
sampleBaseDir+"PATtuple_189_1_olg.root",
sampleBaseDir+"PATtuple_18_1_qFR.root",
sampleBaseDir+"PATtuple_190_1_Cfm.root",
sampleBaseDir+"PATtuple_191_1_Izs.root",
sampleBaseDir+"PATtuple_192_1_6pe.root",
sampleBaseDir+"PATtuple_193_1_I0y.root",
sampleBaseDir+"PATtuple_194_1_bc4.root",
sampleBaseDir+"PATtuple_195_1_vgd.root",
sampleBaseDir+"PATtuple_196_1_e8h.root",
sampleBaseDir+"PATtuple_197_1_iOC.root",
sampleBaseDir+"PATtuple_198_1_fsE.root",
sampleBaseDir+"PATtuple_199_1_NVE.root",
sampleBaseDir+"PATtuple_19_1_qY1.root",
sampleBaseDir+"PATtuple_1_1_JBO.root",
sampleBaseDir+"PATtuple_200_1_boE.root",
sampleBaseDir+"PATtuple_201_1_iiS.root",
sampleBaseDir+"PATtuple_202_1_1V3.root",
sampleBaseDir+"PATtuple_203_1_7kx.root",
sampleBaseDir+"PATtuple_204_1_wu4.root",
sampleBaseDir+"PATtuple_205_1_Cyq.root",
sampleBaseDir+"PATtuple_206_1_HIR.root",
sampleBaseDir+"PATtuple_207_1_gwg.root",
sampleBaseDir+"PATtuple_208_1_qLT.root",
sampleBaseDir+"PATtuple_209_1_Etd.root",
sampleBaseDir+"PATtuple_20_1_Jc5.root",
sampleBaseDir+"PATtuple_210_1_m3Y.root",
sampleBaseDir+"PATtuple_211_1_APg.root",
sampleBaseDir+"PATtuple_212_1_AJN.root",
sampleBaseDir+"PATtuple_213_1_S96.root",
sampleBaseDir+"PATtuple_214_1_B2V.root",
sampleBaseDir+"PATtuple_215_1_CHy.root",
sampleBaseDir+"PATtuple_216_1_RGU.root",
sampleBaseDir+"PATtuple_217_1_5sA.root",
sampleBaseDir+"PATtuple_218_1_O4b.root",
sampleBaseDir+"PATtuple_219_1_xFf.root",
sampleBaseDir+"PATtuple_21_1_VgX.root",
sampleBaseDir+"PATtuple_220_1_gzF.root",
sampleBaseDir+"PATtuple_221_1_sHJ.root",
sampleBaseDir+"PATtuple_222_1_38T.root",
sampleBaseDir+"PATtuple_223_1_P3j.root",
sampleBaseDir+"PATtuple_224_1_MKZ.root",
sampleBaseDir+"PATtuple_225_1_7SQ.root",
sampleBaseDir+"PATtuple_226_1_nhT.root",
sampleBaseDir+"PATtuple_227_1_PFB.root",
sampleBaseDir+"PATtuple_228_1_lyK.root",
sampleBaseDir+"PATtuple_229_1_VJR.root",
sampleBaseDir+"PATtuple_22_1_fnO.root",
sampleBaseDir+"PATtuple_230_1_7Ka.root",
sampleBaseDir+"PATtuple_231_1_ECT.root",
sampleBaseDir+"PATtuple_232_1_O9T.root",
sampleBaseDir+"PATtuple_233_1_AeF.root",
sampleBaseDir+"PATtuple_234_1_x5S.root",
sampleBaseDir+"PATtuple_235_1_wKT.root",
sampleBaseDir+"PATtuple_236_1_hQ1.root",
sampleBaseDir+"PATtuple_237_1_PVi.root",
sampleBaseDir+"PATtuple_238_1_C5L.root",
sampleBaseDir+"PATtuple_239_1_UlO.root",
sampleBaseDir+"PATtuple_23_1_pkT.root",
sampleBaseDir+"PATtuple_240_1_m74.root",
sampleBaseDir+"PATtuple_241_1_nap.root",
sampleBaseDir+"PATtuple_242_1_s2A.root",
sampleBaseDir+"PATtuple_243_1_70g.root",
sampleBaseDir+"PATtuple_244_1_hxQ.root",
sampleBaseDir+"PATtuple_245_1_Goq.root",
sampleBaseDir+"PATtuple_246_1_RuO.root",
sampleBaseDir+"PATtuple_247_1_tGR.root",
sampleBaseDir+"PATtuple_248_1_EFh.root",
sampleBaseDir+"PATtuple_249_1_qwV.root",
sampleBaseDir+"PATtuple_24_1_Oys.root",
sampleBaseDir+"PATtuple_250_1_47y.root",
sampleBaseDir+"PATtuple_251_1_yMQ.root",
sampleBaseDir+"PATtuple_252_1_83E.root",
sampleBaseDir+"PATtuple_253_1_E5z.root",
sampleBaseDir+"PATtuple_254_1_phU.root",
sampleBaseDir+"PATtuple_255_1_bRX.root",
sampleBaseDir+"PATtuple_256_1_322.root",
sampleBaseDir+"PATtuple_257_1_XL0.root",
sampleBaseDir+"PATtuple_258_1_UHk.root",
sampleBaseDir+"PATtuple_259_1_wqe.root",
sampleBaseDir+"PATtuple_25_1_U59.root",
sampleBaseDir+"PATtuple_260_1_03H.root",
sampleBaseDir+"PATtuple_261_1_vud.root",
sampleBaseDir+"PATtuple_262_1_GvR.root",
sampleBaseDir+"PATtuple_263_1_egI.root",
sampleBaseDir+"PATtuple_264_1_3aj.root",
sampleBaseDir+"PATtuple_265_1_hR4.root",
sampleBaseDir+"PATtuple_266_1_1Mj.root",
sampleBaseDir+"PATtuple_267_1_cwF.root",
sampleBaseDir+"PATtuple_268_1_GDi.root",
sampleBaseDir+"PATtuple_269_1_ztj.root",
sampleBaseDir+"PATtuple_26_1_Pc6.root",
sampleBaseDir+"PATtuple_270_1_nL8.root",
sampleBaseDir+"PATtuple_271_1_MWy.root",
sampleBaseDir+"PATtuple_272_1_3hE.root",
sampleBaseDir+"PATtuple_273_1_n0Z.root",
sampleBaseDir+"PATtuple_274_1_L8S.root",
sampleBaseDir+"PATtuple_275_1_o9G.root",
sampleBaseDir+"PATtuple_276_1_c71.root",
sampleBaseDir+"PATtuple_277_1_t0J.root",
sampleBaseDir+"PATtuple_278_1_b93.root",
sampleBaseDir+"PATtuple_279_1_oWW.root",
sampleBaseDir+"PATtuple_27_1_XAT.root",
sampleBaseDir+"PATtuple_280_1_cQR.root",
sampleBaseDir+"PATtuple_281_1_qU4.root",
sampleBaseDir+"PATtuple_282_1_aQN.root",
sampleBaseDir+"PATtuple_283_1_hUs.root",
sampleBaseDir+"PATtuple_284_1_4GD.root",
sampleBaseDir+"PATtuple_285_1_OYa.root",
sampleBaseDir+"PATtuple_286_1_LU2.root",
sampleBaseDir+"PATtuple_287_1_EMZ.root",
sampleBaseDir+"PATtuple_288_1_sCd.root",
sampleBaseDir+"PATtuple_289_1_bZq.root",
sampleBaseDir+"PATtuple_28_1_d8c.root",
sampleBaseDir+"PATtuple_290_1_e6O.root",
sampleBaseDir+"PATtuple_291_1_KCw.root",
sampleBaseDir+"PATtuple_292_1_ygB.root",
sampleBaseDir+"PATtuple_293_1_pbG.root",
sampleBaseDir+"PATtuple_294_1_0Cm.root",
sampleBaseDir+"PATtuple_295_1_a65.root",
sampleBaseDir+"PATtuple_296_1_Wvn.root",
sampleBaseDir+"PATtuple_297_1_HCA.root",
sampleBaseDir+"PATtuple_298_1_3MB.root",
sampleBaseDir+"PATtuple_299_1_KxU.root",
sampleBaseDir+"PATtuple_29_1_DMD.root",
sampleBaseDir+"PATtuple_2_1_TLz.root",
sampleBaseDir+"PATtuple_300_1_e8q.root",
sampleBaseDir+"PATtuple_301_1_6Ik.root",
sampleBaseDir+"PATtuple_302_1_wB6.root",
sampleBaseDir+"PATtuple_303_1_IgG.root",
sampleBaseDir+"PATtuple_304_1_GPy.root",
sampleBaseDir+"PATtuple_305_1_xZO.root",
sampleBaseDir+"PATtuple_306_1_1u7.root",
sampleBaseDir+"PATtuple_307_1_qU6.root",
sampleBaseDir+"PATtuple_308_1_fcM.root",
sampleBaseDir+"PATtuple_309_1_N5b.root",
sampleBaseDir+"PATtuple_30_1_95f.root",
sampleBaseDir+"PATtuple_310_1_Qxq.root",
sampleBaseDir+"PATtuple_311_1_tKF.root",
sampleBaseDir+"PATtuple_312_1_sZH.root",
sampleBaseDir+"PATtuple_313_1_YJ0.root",
sampleBaseDir+"PATtuple_314_1_A40.root",
sampleBaseDir+"PATtuple_315_1_DvE.root",
sampleBaseDir+"PATtuple_316_1_KBa.root",
sampleBaseDir+"PATtuple_317_1_qUw.root",
sampleBaseDir+"PATtuple_318_1_M2Y.root",
sampleBaseDir+"PATtuple_319_1_SdV.root",
sampleBaseDir+"PATtuple_31_1_pIe.root",
sampleBaseDir+"PATtuple_320_1_ygy.root",
sampleBaseDir+"PATtuple_321_1_q3c.root",
sampleBaseDir+"PATtuple_322_1_VCE.root",
sampleBaseDir+"PATtuple_323_1_OkN.root",
sampleBaseDir+"PATtuple_324_1_zUD.root",
sampleBaseDir+"PATtuple_325_1_0TJ.root",
sampleBaseDir+"PATtuple_326_1_mS4.root",
sampleBaseDir+"PATtuple_327_1_98g.root",
sampleBaseDir+"PATtuple_328_1_EJG.root",
sampleBaseDir+"PATtuple_329_1_3WO.root",
sampleBaseDir+"PATtuple_32_1_wbd.root",
sampleBaseDir+"PATtuple_330_1_frN.root",
sampleBaseDir+"PATtuple_331_1_TNd.root",
sampleBaseDir+"PATtuple_332_1_mar.root",
sampleBaseDir+"PATtuple_333_1_1mb.root",
sampleBaseDir+"PATtuple_334_1_VzI.root",
sampleBaseDir+"PATtuple_335_1_hQA.root",
sampleBaseDir+"PATtuple_336_1_RX7.root",
sampleBaseDir+"PATtuple_337_1_k0t.root",
sampleBaseDir+"PATtuple_338_1_fZT.root",
sampleBaseDir+"PATtuple_339_1_ppN.root",
sampleBaseDir+"PATtuple_33_1_qCb.root",
sampleBaseDir+"PATtuple_340_1_3iJ.root",
sampleBaseDir+"PATtuple_341_1_80g.root",
sampleBaseDir+"PATtuple_342_1_D6o.root",
sampleBaseDir+"PATtuple_343_1_mEp.root",
sampleBaseDir+"PATtuple_344_1_R9I.root",
sampleBaseDir+"PATtuple_345_1_yHY.root",
sampleBaseDir+"PATtuple_346_1_8WO.root",
sampleBaseDir+"PATtuple_347_1_Wp6.root",
sampleBaseDir+"PATtuple_348_1_9Ks.root",
sampleBaseDir+"PATtuple_349_1_pGS.root",
sampleBaseDir+"PATtuple_34_1_CWN.root",
sampleBaseDir+"PATtuple_350_1_Zcm.root",
sampleBaseDir+"PATtuple_351_1_4TB.root",
sampleBaseDir+"PATtuple_352_1_MXi.root",
sampleBaseDir+"PATtuple_353_1_UUw.root",
sampleBaseDir+"PATtuple_354_1_qwe.root",
sampleBaseDir+"PATtuple_355_1_vSV.root",
sampleBaseDir+"PATtuple_356_1_9pU.root",
sampleBaseDir+"PATtuple_357_1_xH1.root",
sampleBaseDir+"PATtuple_358_1_qte.root",
sampleBaseDir+"PATtuple_359_1_kPS.root",
sampleBaseDir+"PATtuple_35_1_UYg.root",
sampleBaseDir+"PATtuple_360_1_3qx.root",
sampleBaseDir+"PATtuple_361_1_uoh.root",
sampleBaseDir+"PATtuple_362_1_QJz.root",
sampleBaseDir+"PATtuple_363_1_RiQ.root",
sampleBaseDir+"PATtuple_364_1_Hkn.root",
sampleBaseDir+"PATtuple_365_1_ugA.root",
sampleBaseDir+"PATtuple_366_1_mlo.root",
sampleBaseDir+"PATtuple_367_1_HZm.root",
sampleBaseDir+"PATtuple_368_1_QXI.root",
sampleBaseDir+"PATtuple_369_1_jdg.root",
sampleBaseDir+"PATtuple_36_1_s8E.root",
sampleBaseDir+"PATtuple_370_1_TXq.root",
sampleBaseDir+"PATtuple_371_1_bpY.root",
sampleBaseDir+"PATtuple_372_1_Aro.root",
sampleBaseDir+"PATtuple_373_1_voR.root",
sampleBaseDir+"PATtuple_374_1_Jn3.root",
sampleBaseDir+"PATtuple_375_1_pFT.root",
sampleBaseDir+"PATtuple_376_1_7BQ.root",
sampleBaseDir+"PATtuple_377_1_Rjq.root",
sampleBaseDir+"PATtuple_378_1_GmO.root",
sampleBaseDir+"PATtuple_379_1_Vn1.root",
sampleBaseDir+"PATtuple_37_1_ZZB.root",
sampleBaseDir+"PATtuple_380_1_Tao.root",
sampleBaseDir+"PATtuple_381_1_35T.root",
sampleBaseDir+"PATtuple_382_1_MkU.root",
sampleBaseDir+"PATtuple_383_1_CXw.root",
sampleBaseDir+"PATtuple_384_1_AWV.root",
sampleBaseDir+"PATtuple_385_1_1fi.root",
sampleBaseDir+"PATtuple_386_1_H68.root",
sampleBaseDir+"PATtuple_387_1_VnC.root",
sampleBaseDir+"PATtuple_388_1_ihp.root",
sampleBaseDir+"PATtuple_389_1_3X4.root",
sampleBaseDir+"PATtuple_38_1_ppN.root",
sampleBaseDir+"PATtuple_390_1_pYx.root",
sampleBaseDir+"PATtuple_391_1_bsB.root",
sampleBaseDir+"PATtuple_392_1_3w6.root",
sampleBaseDir+"PATtuple_393_1_k5y.root",
sampleBaseDir+"PATtuple_394_1_Q60.root",
sampleBaseDir+"PATtuple_395_1_Xzc.root",
sampleBaseDir+"PATtuple_396_1_njk.root",
sampleBaseDir+"PATtuple_397_1_9Q1.root",
sampleBaseDir+"PATtuple_398_1_xnQ.root",
sampleBaseDir+"PATtuple_399_1_XNZ.root",
sampleBaseDir+"PATtuple_39_1_nzv.root",
sampleBaseDir+"PATtuple_3_1_CR0.root",
sampleBaseDir+"PATtuple_400_1_kVN.root",
sampleBaseDir+"PATtuple_401_1_ayr.root",
sampleBaseDir+"PATtuple_402_1_p1p.root",
sampleBaseDir+"PATtuple_403_1_L2E.root",
sampleBaseDir+"PATtuple_404_1_tYj.root",
sampleBaseDir+"PATtuple_405_1_okl.root",
sampleBaseDir+"PATtuple_406_1_TPV.root",
sampleBaseDir+"PATtuple_407_1_VJ8.root",
sampleBaseDir+"PATtuple_408_1_rIg.root",
sampleBaseDir+"PATtuple_409_1_iUz.root",
sampleBaseDir+"PATtuple_40_1_E0a.root",
sampleBaseDir+"PATtuple_410_1_Lyi.root",
sampleBaseDir+"PATtuple_411_1_Myv.root",
sampleBaseDir+"PATtuple_412_1_4Lp.root",
sampleBaseDir+"PATtuple_413_1_nm9.root",
sampleBaseDir+"PATtuple_414_1_XzI.root",
sampleBaseDir+"PATtuple_415_1_ai4.root",
sampleBaseDir+"PATtuple_416_1_Mcj.root",
sampleBaseDir+"PATtuple_417_1_40C.root",
sampleBaseDir+"PATtuple_418_1_GsF.root",
sampleBaseDir+"PATtuple_419_1_wyC.root",
sampleBaseDir+"PATtuple_41_1_a9G.root",
sampleBaseDir+"PATtuple_420_1_lMJ.root",
sampleBaseDir+"PATtuple_421_2_0u3.root",
sampleBaseDir+"PATtuple_422_1_AIB.root",
sampleBaseDir+"PATtuple_423_1_RTs.root",
sampleBaseDir+"PATtuple_424_1_YAC.root",
sampleBaseDir+"PATtuple_425_1_Y72.root",
sampleBaseDir+"PATtuple_426_1_v7Q.root",
sampleBaseDir+"PATtuple_427_1_yfD.root",
sampleBaseDir+"PATtuple_428_1_scx.root",
sampleBaseDir+"PATtuple_429_1_29e.root",
sampleBaseDir+"PATtuple_42_1_Aur.root",
sampleBaseDir+"PATtuple_430_1_PzE.root",
sampleBaseDir+"PATtuple_431_1_BwG.root",
sampleBaseDir+"PATtuple_43_1_XY4.root",
sampleBaseDir+"PATtuple_44_1_wCe.root",
sampleBaseDir+"PATtuple_45_1_H6m.root",
sampleBaseDir+"PATtuple_46_1_daE.root",
sampleBaseDir+"PATtuple_47_1_5t1.root",
sampleBaseDir+"PATtuple_48_1_Izl.root",
sampleBaseDir+"PATtuple_49_1_ocS.root",
sampleBaseDir+"PATtuple_4_1_rF3.root",
sampleBaseDir+"PATtuple_50_1_Oqu.root",
sampleBaseDir+"PATtuple_51_1_7Vc.root",
sampleBaseDir+"PATtuple_52_1_8YY.root",
sampleBaseDir+"PATtuple_53_1_272.root",
sampleBaseDir+"PATtuple_54_1_cc1.root",
sampleBaseDir+"PATtuple_55_1_b6M.root",
sampleBaseDir+"PATtuple_56_1_Wu9.root",
sampleBaseDir+"PATtuple_57_1_7BQ.root",
sampleBaseDir+"PATtuple_58_1_ETO.root",
sampleBaseDir+"PATtuple_59_1_Sr8.root",
sampleBaseDir+"PATtuple_5_1_YPh.root",
sampleBaseDir+"PATtuple_60_1_ilB.root",
sampleBaseDir+"PATtuple_61_1_zQg.root",
sampleBaseDir+"PATtuple_62_1_rwS.root",
sampleBaseDir+"PATtuple_63_1_4gd.root",
sampleBaseDir+"PATtuple_64_1_qfu.root",
sampleBaseDir+"PATtuple_65_1_RxK.root",
sampleBaseDir+"PATtuple_66_1_d5w.root",
sampleBaseDir+"PATtuple_67_1_WYS.root",
sampleBaseDir+"PATtuple_68_1_1I4.root",
sampleBaseDir+"PATtuple_69_1_YCh.root",
sampleBaseDir+"PATtuple_6_1_ppq.root",
sampleBaseDir+"PATtuple_70_1_XyJ.root",
sampleBaseDir+"PATtuple_71_1_t0W.root",
sampleBaseDir+"PATtuple_72_1_LRg.root",
sampleBaseDir+"PATtuple_73_1_rz4.root",
sampleBaseDir+"PATtuple_74_1_pMz.root",
sampleBaseDir+"PATtuple_75_1_dQw.root",
sampleBaseDir+"PATtuple_76_1_PmV.root",
sampleBaseDir+"PATtuple_77_1_OxA.root",
sampleBaseDir+"PATtuple_78_1_Yib.root",
sampleBaseDir+"PATtuple_79_1_FUf.root",
sampleBaseDir+"PATtuple_7_1_Dew.root",
sampleBaseDir+"PATtuple_80_1_etI.root",
sampleBaseDir+"PATtuple_81_1_LE2.root",
sampleBaseDir+"PATtuple_82_1_cQP.root",
sampleBaseDir+"PATtuple_83_1_0ff.root",
sampleBaseDir+"PATtuple_84_1_pW9.root",
sampleBaseDir+"PATtuple_85_1_a9h.root",
sampleBaseDir+"PATtuple_86_1_ec5.root",
sampleBaseDir+"PATtuple_87_1_nga.root",
sampleBaseDir+"PATtuple_88_1_SUH.root",
sampleBaseDir+"PATtuple_89_1_JIc.root",
sampleBaseDir+"PATtuple_8_1_hFA.root",
sampleBaseDir+"PATtuple_90_1_PET.root",
sampleBaseDir+"PATtuple_91_1_06g.root",
sampleBaseDir+"PATtuple_92_1_cAP.root",
sampleBaseDir+"PATtuple_93_1_Ijg.root",
sampleBaseDir+"PATtuple_94_1_4Gl.root",
sampleBaseDir+"PATtuple_95_1_R1t.root",
sampleBaseDir+"PATtuple_96_1_f4d.root",
sampleBaseDir+"PATtuple_97_1_pN1.root",
sampleBaseDir+"PATtuple_98_1_Fwh.root",
sampleBaseDir+"PATtuple_99_1_rsk.root",
sampleBaseDir+"PATtuple_9_1_wcv.root",
]