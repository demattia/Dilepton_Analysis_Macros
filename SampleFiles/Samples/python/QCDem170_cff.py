sampleDataSet = '/QCD_Pt_170_250_EMEnriched_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'  

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_2_patch4" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_5" # release used to create new files with

sampleNumEvents = 31697066

sampleXSec = 30990 * 0.148 # pb

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7F::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "BKGMC"





samplePatDBSName=""

sampleBaseDir="/store/user/lpcdve/DisplacedLeptons/QCDem170_pat_20130203/demattia//QCD_Pt_170_250_EMEnriched_TuneZ2star_8TeV_pythia6/QCDem170_pat_20130203/5fe3dadd93bf8608b396f970098158ed/"
samplePatFiles = [
sampleBaseDir+"PATtuple_11_1_yfa.root",
sampleBaseDir+"PATtuple_253_1_cj5.root",
sampleBaseDir+"PATtuple_263_1_iWk.root",
sampleBaseDir+"PATtuple_616_1_xr8.root",
sampleBaseDir+"PATtuple_118_2_lDz.root",
sampleBaseDir+"PATtuple_434_4_Ye7.root",
sampleBaseDir+"PATtuple_297_1_HqP.root",
sampleBaseDir+"PATtuple_622_1_dkI.root",
sampleBaseDir+"PATtuple_568_1_hQT.root",
sampleBaseDir+"PATtuple_96_2_FXC.root",
sampleBaseDir+"PATtuple_318_2_kH8.root",
sampleBaseDir+"PATtuple_421_4_8Ov.root",
sampleBaseDir+"PATtuple_562_4_3Z3.root",
sampleBaseDir+"PATtuple_635_3_S7y.root",
sampleBaseDir+"PATtuple_638_3_YOy.root",
sampleBaseDir+"PATtuple_12_1_kpT.root",
sampleBaseDir+"PATtuple_218_1_Ctg.root",
sampleBaseDir+"PATtuple_346_1_FNN.root",
sampleBaseDir+"PATtuple_468_1_49F.root",
sampleBaseDir+"PATtuple_581_1_7N7.root",
sampleBaseDir+"PATtuple_101_2_6q2.root",
sampleBaseDir+"PATtuple_154_2_et5.root",
sampleBaseDir+"PATtuple_636_3_zz4.root",
sampleBaseDir+"PATtuple_231_5_okd.root",
sampleBaseDir+"PATtuple_46_1_1c3.root",
sampleBaseDir+"PATtuple_103_1_Anb.root",
sampleBaseDir+"PATtuple_204_1_JsO.root",
sampleBaseDir+"PATtuple_499_1_gOi.root",
sampleBaseDir+"PATtuple_502_1_TQ8.root",
sampleBaseDir+"PATtuple_594_2_RfM.root",
sampleBaseDir+"PATtuple_191_3_Fgy.root",
sampleBaseDir+"PATtuple_18_1_feH.root",
sampleBaseDir+"PATtuple_368_1_oxy.root",
sampleBaseDir+"PATtuple_501_1_T6z.root",
sampleBaseDir+"PATtuple_604_2_tc9.root",
sampleBaseDir+"PATtuple_89_2_OsJ.root",
sampleBaseDir+"PATtuple_639_3_XDd.root",
sampleBaseDir+"PATtuple_43_1_UDK.root",
sampleBaseDir+"PATtuple_273_1_STz.root",
sampleBaseDir+"PATtuple_314_1_iI2.root",
sampleBaseDir+"PATtuple_493_1_lps.root",
sampleBaseDir+"PATtuple_573_1_9Zc.root",
sampleBaseDir+"PATtuple_590_1_lgq.root",
sampleBaseDir+"PATtuple_224_2_DE6.root",
sampleBaseDir+"PATtuple_261_1_BNW.root",
sampleBaseDir+"PATtuple_362_1_3QF.root",
sampleBaseDir+"PATtuple_479_1_4aq.root",
sampleBaseDir+"PATtuple_576_1_yEo.root",
sampleBaseDir+"PATtuple_549_2_tcB.root",
sampleBaseDir+"PATtuple_172_2_i43.root",
sampleBaseDir+"PATtuple_574_4_LBJ.root",
sampleBaseDir+"PATtuple_69_1_kZU.root",
sampleBaseDir+"PATtuple_208_1_ixU.root",
sampleBaseDir+"PATtuple_395_2_Ys3.root",
sampleBaseDir+"PATtuple_416_3_mu1.root",
sampleBaseDir+"PATtuple_71_1_8gO.root",
sampleBaseDir+"PATtuple_270_1_60G.root",
sampleBaseDir+"PATtuple_600_2_OZ3.root",
sampleBaseDir+"PATtuple_79_1_VSx.root",
sampleBaseDir+"PATtuple_164_1_qfF.root",
sampleBaseDir+"PATtuple_252_1_5w3.root",
sampleBaseDir+"PATtuple_337_1_I8A.root",
sampleBaseDir+"PATtuple_369_1_PMr.root",
sampleBaseDir+"PATtuple_463_1_P95.root",
sampleBaseDir+"PATtuple_291_2_rbv.root",
sampleBaseDir+"PATtuple_113_3_KNc.root",
sampleBaseDir+"PATtuple_411_1_ZgQ.root",
sampleBaseDir+"PATtuple_304_1_aED.root",
sampleBaseDir+"PATtuple_531_1_9ga.root",
sampleBaseDir+"PATtuple_104_2_o6B.root",
sampleBaseDir+"PATtuple_427_3_NXC.root",
sampleBaseDir+"PATtuple_16_1_EI2.root",
sampleBaseDir+"PATtuple_483_1_vkM.root",
sampleBaseDir+"PATtuple_329_2_4Bn.root",
sampleBaseDir+"PATtuple_59_2_i2S.root",
sampleBaseDir+"PATtuple_342_2_Ysj.root",
sampleBaseDir+"PATtuple_199_1_Jwr.root",
sampleBaseDir+"PATtuple_332_1_njm.root",
sampleBaseDir+"PATtuple_504_1_0Ak.root",
sampleBaseDir+"PATtuple_349_1_xoQ.root",
sampleBaseDir+"PATtuple_295_1_BkR.root",
sampleBaseDir+"PATtuple_366_2_85g.root",
sampleBaseDir+"PATtuple_558_4_1ig.root",
sampleBaseDir+"PATtuple_24_2_KWC.root",
sampleBaseDir+"PATtuple_617_2_RLA.root",
sampleBaseDir+"PATtuple_236_1_21n.root",
sampleBaseDir+"PATtuple_381_1_c2i.root",
sampleBaseDir+"PATtuple_408_1_z1v.root",
sampleBaseDir+"PATtuple_170_2_Pxr.root",
sampleBaseDir+"PATtuple_14_1_mCX.root",
sampleBaseDir+"PATtuple_15_1_esE.root",
sampleBaseDir+"PATtuple_388_1_crl.root",
sampleBaseDir+"PATtuple_495_1_DQx.root",
sampleBaseDir+"PATtuple_92_2_B6c.root",
sampleBaseDir+"PATtuple_518_3_htp.root",
sampleBaseDir+"PATtuple_129_1_KcJ.root",
sampleBaseDir+"PATtuple_238_1_cQr.root",
sampleBaseDir+"PATtuple_233_1_L4r.root",
sampleBaseDir+"PATtuple_198_1_kpj.root",
sampleBaseDir+"PATtuple_279_1_bPl.root",
sampleBaseDir+"PATtuple_360_1_ub5.root",
sampleBaseDir+"PATtuple_392_1_9SK.root",
sampleBaseDir+"PATtuple_466_1_4w6.root",
sampleBaseDir+"PATtuple_460_1_goI.root",
sampleBaseDir+"PATtuple_174_2_sHK.root",
sampleBaseDir+"PATtuple_76_1_vBB.root",
sampleBaseDir+"PATtuple_126_1_LDi.root",
sampleBaseDir+"PATtuple_121_1_krX.root",
sampleBaseDir+"PATtuple_235_1_sbL.root",
sampleBaseDir+"PATtuple_397_1_frp.root",
sampleBaseDir+"PATtuple_95_2_KOB.root",
sampleBaseDir+"PATtuple_277_1_foC.root",
sampleBaseDir+"PATtuple_340_2_4Qh.root",
sampleBaseDir+"PATtuple_415_2_1QO.root",
sampleBaseDir+"PATtuple_162_1_GK3.root",
sampleBaseDir+"PATtuple_378_1_aMf.root",
sampleBaseDir+"PATtuple_596_2_mxz.root",
sampleBaseDir+"PATtuple_591_2_fS2.root",
sampleBaseDir+"PATtuple_13_1_g3N.root",
sampleBaseDir+"PATtuple_78_1_g53.root",
sampleBaseDir+"PATtuple_149_1_0Gu.root",
sampleBaseDir+"PATtuple_249_1_shz.root",
sampleBaseDir+"PATtuple_276_1_ayl.root",
sampleBaseDir+"PATtuple_399_1_thg.root",
sampleBaseDir+"PATtuple_592_2_wNg.root",
sampleBaseDir+"PATtuple_422_4_pnp.root",
sampleBaseDir+"PATtuple_438_1_poH.root",
sampleBaseDir+"PATtuple_630_1_yh6.root",
sampleBaseDir+"PATtuple_26_2_jz8.root",
sampleBaseDir+"PATtuple_22_1_4R2.root",
sampleBaseDir+"PATtuple_119_1_ww7.root",
sampleBaseDir+"PATtuple_124_1_p4f.root",
sampleBaseDir+"PATtuple_125_1_bmi.root",
sampleBaseDir+"PATtuple_465_1_IYm.root",
sampleBaseDir+"PATtuple_621_1_JFC.root",
sampleBaseDir+"PATtuple_570_4_0PD.root",
sampleBaseDir+"PATtuple_58_1_ZR0.root",
sampleBaseDir+"PATtuple_478_1_HHq.root",
sampleBaseDir+"PATtuple_528_1_FTi.root",
sampleBaseDir+"PATtuple_547_2_D7W.root",
sampleBaseDir+"PATtuple_431_3_sTL.root",
sampleBaseDir+"PATtuple_256_1_55f.root",
sampleBaseDir+"PATtuple_237_1_sit.root",
sampleBaseDir+"PATtuple_442_1_Ww3.root",
sampleBaseDir+"PATtuple_490_1_iFS.root",
sampleBaseDir+"PATtuple_491_1_uJ9.root",
sampleBaseDir+"PATtuple_435_4_fq6.root",
sampleBaseDir+"PATtuple_510_1_dZr.root",
sampleBaseDir+"PATtuple_157_2_fyn.root",
sampleBaseDir+"PATtuple_292_1_pOi.root",
sampleBaseDir+"PATtuple_53_2_t5d.root",
sampleBaseDir+"PATtuple_593_2_c9H.root",
sampleBaseDir+"PATtuple_55_1_L7L.root",
sampleBaseDir+"PATtuple_196_1_mzq.root",
sampleBaseDir+"PATtuple_245_1_IXW.root",
sampleBaseDir+"PATtuple_403_1_ZX2.root",
sampleBaseDir+"PATtuple_370_1_ogR.root",
sampleBaseDir+"PATtuple_569_1_Aog.root",
sampleBaseDir+"PATtuple_6_2_fb9.root",
sampleBaseDir+"PATtuple_210_1_CkZ.root",
sampleBaseDir+"PATtuple_90_2_6UU.root",
sampleBaseDir+"PATtuple_115_2_vCo.root",
sampleBaseDir+"PATtuple_45_1_2Yg.root",
sampleBaseDir+"PATtuple_38_1_q1b.root",
sampleBaseDir+"PATtuple_216_1_cs7.root",
sampleBaseDir+"PATtuple_244_1_ncU.root",
sampleBaseDir+"PATtuple_363_1_czz.root",
sampleBaseDir+"PATtuple_509_1_dTa.root",
sampleBaseDir+"PATtuple_100_2_PrH.root",
sampleBaseDir+"PATtuple_1_2_24d.root",
sampleBaseDir+"PATtuple_606_2_kxt.root",
sampleBaseDir+"PATtuple_512_2_vbo.root",
sampleBaseDir+"PATtuple_404_1_80A.root",
sampleBaseDir+"PATtuple_400_1_sdl.root",
sampleBaseDir+"PATtuple_406_1_2WT.root",
sampleBaseDir+"PATtuple_461_1_pRK.root",
sampleBaseDir+"PATtuple_542_1_pxl.root",
sampleBaseDir+"PATtuple_589_1_UqF.root",
sampleBaseDir+"PATtuple_116_2_Ag2.root",
sampleBaseDir+"PATtuple_169_2_135.root",
sampleBaseDir+"PATtuple_232_2_ASS.root",
sampleBaseDir+"PATtuple_213_1_0XO.root",
sampleBaseDir+"PATtuple_489_1_Ul5.root",
sampleBaseDir+"PATtuple_449_1_rsw.root",
sampleBaseDir+"PATtuple_595_2_HZu.root",
sampleBaseDir+"PATtuple_54_2_bmP.root",
sampleBaseDir+"PATtuple_513_2_jti.root",
sampleBaseDir+"PATtuple_41_1_XFE.root",
sampleBaseDir+"PATtuple_82_1_bpB.root",
sampleBaseDir+"PATtuple_203_1_TbA.root",
sampleBaseDir+"PATtuple_553_1_9gW.root",
sampleBaseDir+"PATtuple_281_2_cxE.root",
sampleBaseDir+"PATtuple_108_3_G2I.root",
sampleBaseDir+"PATtuple_120_1_KVV.root",
sampleBaseDir+"PATtuple_223_1_YzU.root",
sampleBaseDir+"PATtuple_258_1_MKU.root",
sampleBaseDir+"PATtuple_444_1_i4y.root",
sampleBaseDir+"PATtuple_64_2_twm.root",
sampleBaseDir+"PATtuple_63_3_7pQ.root",
sampleBaseDir+"PATtuple_557_4_lan.root",
sampleBaseDir+"PATtuple_418_4_a5z.root",
sampleBaseDir+"PATtuple_335_1_T9J.root",
sampleBaseDir+"PATtuple_451_1_G9F.root",
sampleBaseDir+"PATtuple_605_2_5iP.root",
sampleBaseDir+"PATtuple_133_1_2mK.root",
sampleBaseDir+"PATtuple_143_1_91k.root",
sampleBaseDir+"PATtuple_272_1_W1I.root",
sampleBaseDir+"PATtuple_367_1_6Sb.root",
sampleBaseDir+"PATtuple_278_1_xXw.root",
sampleBaseDir+"PATtuple_488_1_zFB.root",
sampleBaseDir+"PATtuple_511_2_KYe.root",
sampleBaseDir+"PATtuple_183_2_8FT.root",
sampleBaseDir+"PATtuple_175_3_IKN.root",
sampleBaseDir+"PATtuple_561_4_v1O.root",
sampleBaseDir+"PATtuple_176_3_CRc.root",
sampleBaseDir+"PATtuple_75_1_LOo.root",
sampleBaseDir+"PATtuple_620_1_I2r.root",
sampleBaseDir+"PATtuple_52_2_9rg.root",
sampleBaseDir+"PATtuple_559_4_CUl.root",
sampleBaseDir+"PATtuple_166_1_yQi.root",
sampleBaseDir+"PATtuple_202_1_HpF.root",
sampleBaseDir+"PATtuple_10_1_tSR.root",
sampleBaseDir+"PATtuple_533_1_5qe.root",
sampleBaseDir+"PATtuple_98_2_sJ5.root",
sampleBaseDir+"PATtuple_413_2_kJt.root",
sampleBaseDir+"PATtuple_51_3_il7.root",
sampleBaseDir+"PATtuple_85_1_NP0.root",
sampleBaseDir+"PATtuple_214_1_nVe.root",
sampleBaseDir+"PATtuple_146_1_ExZ.root",
sampleBaseDir+"PATtuple_221_1_mhm.root",
sampleBaseDir+"PATtuple_445_1_Ksd.root",
sampleBaseDir+"PATtuple_472_1_Mhf.root",
sampleBaseDir+"PATtuple_469_1_ZfB.root",
sampleBaseDir+"PATtuple_234_1_xU6.root",
sampleBaseDir+"PATtuple_344_2_deQ.root",
sampleBaseDir+"PATtuple_243_1_akI.root",
sampleBaseDir+"PATtuple_457_1_xoW.root",
sampleBaseDir+"PATtuple_538_1_yI9.root",
sampleBaseDir+"PATtuple_611_1_kEf.root",
sampleBaseDir+"PATtuple_105_2_zzc.root",
sampleBaseDir+"PATtuple_339_2_wEf.root",
sampleBaseDir+"PATtuple_184_2_gwE.root",
sampleBaseDir+"PATtuple_410_1_fy6.root",
sampleBaseDir+"PATtuple_382_1_sWq.root",
sampleBaseDir+"PATtuple_572_1_8Ma.root",
sampleBaseDir+"PATtuple_320_2_GFK.root",
sampleBaseDir+"PATtuple_181_2_Kji.root",
sampleBaseDir+"PATtuple_20_1_rHx.root",
sampleBaseDir+"PATtuple_271_1_J86.root",
sampleBaseDir+"PATtuple_141_1_Ido.root",
sampleBaseDir+"PATtuple_389_1_vsw.root",
sampleBaseDir+"PATtuple_588_1_ADI.root",
sampleBaseDir+"PATtuple_459_1_Jft.root",
sampleBaseDir+"PATtuple_8_1_Jot.root",
sampleBaseDir+"PATtuple_73_1_GIA.root",
sampleBaseDir+"PATtuple_80_1_zc2.root",
sampleBaseDir+"PATtuple_247_1_wOn.root",
sampleBaseDir+"PATtuple_303_1_X2S.root",
sampleBaseDir+"PATtuple_506_1_zmn.root",
sampleBaseDir+"PATtuple_283_2_P0E.root",
sampleBaseDir+"PATtuple_158_2_krb.root",
sampleBaseDir+"PATtuple_81_1_ziR.root",
sampleBaseDir+"PATtuple_32_1_RpC.root",
sampleBaseDir+"PATtuple_494_1_uNs.root",
sampleBaseDir+"PATtuple_437_1_YRg.root",
sampleBaseDir+"PATtuple_226_2_GiH.root",
sampleBaseDir+"PATtuple_626_3_oX4.root",
sampleBaseDir+"PATtuple_145_1_3Xh.root",
sampleBaseDir+"PATtuple_132_1_4Iu.root",
sampleBaseDir+"PATtuple_128_1_CAk.root",
sampleBaseDir+"PATtuple_257_1_FIz.root",
sampleBaseDir+"PATtuple_345_1_o5Q.root",
sampleBaseDir+"PATtuple_515_2_caW.root",
sampleBaseDir+"PATtuple_37_1_Pei.root",
sampleBaseDir+"PATtuple_432_1_220.root",
sampleBaseDir+"PATtuple_607_2_QxQ.root",
sampleBaseDir+"PATtuple_565_4_rR1.root",
sampleBaseDir+"PATtuple_375_1_5Y0.root",
sampleBaseDir+"PATtuple_359_1_Ppr.root",
sampleBaseDir+"PATtuple_492_1_0Wl.root",
sampleBaseDir+"PATtuple_642_1_9wj.root",
sampleBaseDir+"PATtuple_66_2_Rdx.root",
sampleBaseDir+"PATtuple_602_2_fN7.root",
sampleBaseDir+"PATtuple_409_2_f0I.root",
sampleBaseDir+"PATtuple_229_2_rSj.root",
sampleBaseDir+"PATtuple_641_1_47D.root",
sampleBaseDir+"PATtuple_114_2_Y7P.root",
sampleBaseDir+"PATtuple_179_2_U2i.root",
sampleBaseDir+"PATtuple_212_1_HFe.root",
sampleBaseDir+"PATtuple_535_1_QrK.root",
sampleBaseDir+"PATtuple_450_1_77q.root",
sampleBaseDir+"PATtuple_171_2_3vL.root",
sampleBaseDir+"PATtuple_136_1_han.root",
sampleBaseDir+"PATtuple_315_1_DHU.root",
sampleBaseDir+"PATtuple_467_1_ZyZ.root",
sampleBaseDir+"PATtuple_414_2_Ykg.root",
sampleBaseDir+"PATtuple_631_3_QQj.root",
sampleBaseDir+"PATtuple_301_1_RC4.root",
sampleBaseDir+"PATtuple_529_1_b1F.root",
sampleBaseDir+"PATtuple_521_2_efo.root",
sampleBaseDir+"PATtuple_586_2_0SI.root",
sampleBaseDir+"PATtuple_325_2_3K6.root",
sampleBaseDir+"PATtuple_629_1_d7F.root",
sampleBaseDir+"PATtuple_424_4_AuV.root",
sampleBaseDir+"PATtuple_264_1_vGc.root",
sampleBaseDir+"PATtuple_262_1_kcU.root",
sampleBaseDir+"PATtuple_65_2_ZPj.root",
sampleBaseDir+"PATtuple_429_3_phg.root",
sampleBaseDir+"PATtuple_633_4_rP7.root",
sampleBaseDir+"PATtuple_160_1_IFV.root",
sampleBaseDir+"PATtuple_298_1_24c.root",
sampleBaseDir+"PATtuple_260_1_7yH.root",
sampleBaseDir+"PATtuple_355_1_3YL.root",
sampleBaseDir+"PATtuple_309_1_ehV.root",
sampleBaseDir+"PATtuple_155_2_9g9.root",
sampleBaseDir+"PATtuple_30_2_Kes.root",
sampleBaseDir+"PATtuple_206_1_MO7.root",
sampleBaseDir+"PATtuple_443_1_XLU.root",
sampleBaseDir+"PATtuple_330_1_oxN.root",
sampleBaseDir+"PATtuple_225_2_Q9X.root",
sampleBaseDir+"PATtuple_546_2_3tL.root",
sampleBaseDir+"PATtuple_35_1_eew.root",
sampleBaseDir+"PATtuple_87_1_Kyn.root",
sampleBaseDir+"PATtuple_374_1_QQp.root",
sampleBaseDir+"PATtuple_222_1_3eR.root",
sampleBaseDir+"PATtuple_194_1_bvP.root",
sampleBaseDir+"PATtuple_117_2_8eh.root",
sampleBaseDir+"PATtuple_563_4_7qf.root",
sampleBaseDir+"PATtuple_56_1_QVt.root",
sampleBaseDir+"PATtuple_448_1_lwr.root",
sampleBaseDir+"PATtuple_452_1_LKk.root",
sampleBaseDir+"PATtuple_532_1_Tf5.root",
sampleBaseDir+"PATtuple_555_1_Y6Z.root",
sampleBaseDir+"PATtuple_40_1_vIh.root",
sampleBaseDir+"PATtuple_282_1_VT6.root",
sampleBaseDir+"PATtuple_49_2_ELt.root",
sampleBaseDir+"PATtuple_296_1_s05.root",
sampleBaseDir+"PATtuple_380_1_xlP.root",
sampleBaseDir+"PATtuple_293_1_taS.root",
sampleBaseDir+"PATtuple_634_3_hIi.root",
sampleBaseDir+"PATtuple_242_1_RoQ.root",
sampleBaseDir+"PATtuple_453_1_taf.root",
sampleBaseDir+"PATtuple_474_1_jgF.root",
sampleBaseDir+"PATtuple_324_2_3LE.root",
sampleBaseDir+"PATtuple_560_4_uuR.root",
sampleBaseDir+"PATtuple_497_1_B3O.root",
sampleBaseDir+"PATtuple_582_3_5tS.root",
sampleBaseDir+"PATtuple_68_1_357.root",
sampleBaseDir+"PATtuple_122_1_mCA.root",
sampleBaseDir+"PATtuple_357_1_MJe.root",
sampleBaseDir+"PATtuple_554_1_lcw.root",
sampleBaseDir+"PATtuple_365_2_I2i.root",
sampleBaseDir+"PATtuple_21_1_YMc.root",
sampleBaseDir+"PATtuple_197_1_ulb.root",
sampleBaseDir+"PATtuple_317_1_gFH.root",
sampleBaseDir+"PATtuple_473_1_Uzk.root",
sampleBaseDir+"PATtuple_111_2_qI4.root",
sampleBaseDir+"PATtuple_486_2_WoJ.root",
sampleBaseDir+"PATtuple_285_1_JRt.root",
sampleBaseDir+"PATtuple_269_1_Vw5.root",
sampleBaseDir+"PATtuple_405_1_cxa.root",
sampleBaseDir+"PATtuple_393_2_JQD.root",
sampleBaseDir+"PATtuple_83_1_IYm.root",
sampleBaseDir+"PATtuple_536_1_Djq.root",
sampleBaseDir+"PATtuple_519_1_vFw.root",
sampleBaseDir+"PATtuple_625_1_Ord.root",
sampleBaseDir+"PATtuple_302_1_G6d.root",
sampleBaseDir+"PATtuple_48_3_u6R.root",
sampleBaseDir+"PATtuple_350_1_mWO.root",
sampleBaseDir+"PATtuple_137_1_pEC.root",
sampleBaseDir+"PATtuple_167_1_9bZ.root",
sampleBaseDir+"PATtuple_254_1_STz.root",
sampleBaseDir+"PATtuple_192_2_vyX.root",
sampleBaseDir+"PATtuple_239_1_53f.root",
sampleBaseDir+"PATtuple_186_2_xvq.root",
sampleBaseDir+"PATtuple_29_2_oLO.root",
sampleBaseDir+"PATtuple_39_1_rVC.root",
sampleBaseDir+"PATtuple_336_1_2ou.root",
sampleBaseDir+"PATtuple_383_1_s7m.root",
sampleBaseDir+"PATtuple_390_2_NrG.root",
sampleBaseDir+"PATtuple_109_3_NBQ.root",
sampleBaseDir+"PATtuple_361_1_V0z.root",
sampleBaseDir+"PATtuple_354_1_5uM.root",
sampleBaseDir+"PATtuple_289_2_wNC.root",
sampleBaseDir+"PATtuple_134_1_hU5.root",
sampleBaseDir+"PATtuple_255_1_y37.root",
sampleBaseDir+"PATtuple_484_1_o6I.root",
sampleBaseDir+"PATtuple_407_1_tMY.root",
sampleBaseDir+"PATtuple_503_1_qTz.root",
sampleBaseDir+"PATtuple_583_2_vNt.root",
sampleBaseDir+"PATtuple_577_4_iVh.root",
sampleBaseDir+"PATtuple_539_1_sgU.root",
sampleBaseDir+"PATtuple_371_1_xPw.root",
sampleBaseDir+"PATtuple_608_1_Hsd.root",
sampleBaseDir+"PATtuple_520_2_Pbc.root",
sampleBaseDir+"PATtuple_550_2_vnx.root",
sampleBaseDir+"PATtuple_627_3_jqb.root",
sampleBaseDir+"PATtuple_123_1_d54.root",
sampleBaseDir+"PATtuple_327_1_C7S.root",
sampleBaseDir+"PATtuple_567_1_mo7.root",
sampleBaseDir+"PATtuple_227_2_Rk2.root",
sampleBaseDir+"PATtuple_27_2_S7u.root",
sampleBaseDir+"PATtuple_25_2_eWU.root",
sampleBaseDir+"PATtuple_127_1_zD8.root",
sampleBaseDir+"PATtuple_165_1_UjY.root",
sampleBaseDir+"PATtuple_307_1_Src.root",
sampleBaseDir+"PATtuple_523_1_VSE.root",
sampleBaseDir+"PATtuple_615_2_Uqc.root",
sampleBaseDir+"PATtuple_5_3_95q.root",
sampleBaseDir+"PATtuple_290_1_wf8.root",
sampleBaseDir+"PATtuple_364_1_SHb.root",
sampleBaseDir+"PATtuple_455_1_T6Q.root",
sampleBaseDir+"PATtuple_545_2_uyL.root",
sampleBaseDir+"PATtuple_207_1_eKw.root",
sampleBaseDir+"PATtuple_274_1_1jm.root",
sampleBaseDir+"PATtuple_220_1_hjS.root",
sampleBaseDir+"PATtuple_358_1_TiB.root",
sampleBaseDir+"PATtuple_527_1_KAR.root",
sampleBaseDir+"PATtuple_211_1_St5.root",
sampleBaseDir+"PATtuple_180_2_P5z.root",
sampleBaseDir+"PATtuple_19_1_mN4.root",
sampleBaseDir+"PATtuple_507_1_2cj.root",
sampleBaseDir+"PATtuple_613_1_Nnc.root",
sampleBaseDir+"PATtuple_50_2_AiK.root",
sampleBaseDir+"PATtuple_173_2_WdD.root",
sampleBaseDir+"PATtuple_28_2_6BH.root",
sampleBaseDir+"PATtuple_74_1_6Wp.root",
sampleBaseDir+"PATtuple_498_1_OAj.root",
sampleBaseDir+"PATtuple_456_1_v82.root",
sampleBaseDir+"PATtuple_480_1_w7S.root",
sampleBaseDir+"PATtuple_544_1_8Qm.root",
sampleBaseDir+"PATtuple_112_2_iyJ.root",
sampleBaseDir+"PATtuple_321_2_v8A.root",
sampleBaseDir+"PATtuple_482_1_UIL.root",
sampleBaseDir+"PATtuple_516_2_WoG.root",
sampleBaseDir+"PATtuple_60_2_P7u.root",
sampleBaseDir+"PATtuple_552_2_N0I.root",
sampleBaseDir+"PATtuple_420_2_qvH.root",
sampleBaseDir+"PATtuple_331_1_O11.root",
sampleBaseDir+"PATtuple_485_1_s2h.root",
sampleBaseDir+"PATtuple_522_2_lBS.root",
sampleBaseDir+"PATtuple_398_2_Gde.root",
sampleBaseDir+"PATtuple_187_2_6n9.root",
sampleBaseDir+"PATtuple_601_2_L9K.root",
sampleBaseDir+"PATtuple_67_1_XJd.root",
sampleBaseDir+"PATtuple_188_2_tl8.root",
sampleBaseDir+"PATtuple_177_2_McK.root",
sampleBaseDir+"PATtuple_585_3_kAg.root",
sampleBaseDir+"PATtuple_436_4_B5w.root",
sampleBaseDir+"PATtuple_4_3_RQz.root",
sampleBaseDir+"PATtuple_612_1_LD2.root",
sampleBaseDir+"PATtuple_425_3_1Cc.root",
sampleBaseDir+"PATtuple_305_1_stF.root",
sampleBaseDir+"PATtuple_464_1_yR9.root",
sampleBaseDir+"PATtuple_322_2_M3X.root",
sampleBaseDir+"PATtuple_91_2_ohw.root",
sampleBaseDir+"PATtuple_579_3_wm0.root",
sampleBaseDir+"PATtuple_131_1_HEH.root",
sampleBaseDir+"PATtuple_240_1_DHc.root",
sampleBaseDir+"PATtuple_439_2_xLa.root",
sampleBaseDir+"PATtuple_423_4_AhS.root",
sampleBaseDir+"PATtuple_328_3_6rr.root",
sampleBaseDir+"PATtuple_86_1_PAx.root",
sampleBaseDir+"PATtuple_201_1_F00.root",
sampleBaseDir+"PATtuple_219_1_i7U.root",
sampleBaseDir+"PATtuple_347_2_ykv.root",
sampleBaseDir+"PATtuple_419_4_aQB.root",
sampleBaseDir+"PATtuple_135_1_pEj.root",
sampleBaseDir+"PATtuple_624_1_fJW.root",
sampleBaseDir+"PATtuple_205_1_OZd.root",
sampleBaseDir+"PATtuple_159_1_o8x.root",
sampleBaseDir+"PATtuple_299_1_X5S.root",
sampleBaseDir+"PATtuple_394_3_399.root",
sampleBaseDir+"PATtuple_47_3_sfL.root",
sampleBaseDir+"PATtuple_94_1_5nm.root",
sampleBaseDir+"PATtuple_541_1_oAO.root",
sampleBaseDir+"PATtuple_3_3_MKl.root",
sampleBaseDir+"PATtuple_34_1_PsT.root",
sampleBaseDir+"PATtuple_537_1_0pU.root",
sampleBaseDir+"PATtuple_185_2_AEa.root",
sampleBaseDir+"PATtuple_287_2_L6z.root",
sampleBaseDir+"PATtuple_430_3_H60.root",
sampleBaseDir+"PATtuple_84_1_g2V.root",
sampleBaseDir+"PATtuple_150_1_NVR.root",
sampleBaseDir+"PATtuple_130_1_tdX.root",
sampleBaseDir+"PATtuple_265_1_LMG.root",
sampleBaseDir+"PATtuple_266_1_Drl.root",
sampleBaseDir+"PATtuple_268_1_lyE.root",
sampleBaseDir+"PATtuple_475_1_SgO.root",
sampleBaseDir+"PATtuple_250_1_5uv.root",
sampleBaseDir+"PATtuple_353_1_kGG.root",
sampleBaseDir+"PATtuple_458_1_uW2.root",
sampleBaseDir+"PATtuple_526_1_bwW.root",
sampleBaseDir+"PATtuple_534_1_Epf.root",
sampleBaseDir+"PATtuple_580_1_JH5.root",
sampleBaseDir+"PATtuple_110_2_Mrj.root",
sampleBaseDir+"PATtuple_598_2_IOq.root",
sampleBaseDir+"PATtuple_182_2_gN3.root",
sampleBaseDir+"PATtuple_33_2_Acl.root",
sampleBaseDir+"PATtuple_628_3_UqZ.root",
sampleBaseDir+"PATtuple_9_1_DQF.root",
sampleBaseDir+"PATtuple_161_1_AGF.root",
sampleBaseDir+"PATtuple_640_1_k9m.root",
sampleBaseDir+"PATtuple_323_2_CWi.root",
sampleBaseDir+"PATtuple_36_1_hAm.root",
sampleBaseDir+"PATtuple_319_1_Vms.root",
sampleBaseDir+"PATtuple_215_1_g6X.root",
sampleBaseDir+"PATtuple_70_1_dfi.root",
sampleBaseDir+"PATtuple_248_1_CoM.root",
sampleBaseDir+"PATtuple_514_2_2z2.root",
sampleBaseDir+"PATtuple_584_3_XkE.root",
sampleBaseDir+"PATtuple_57_1_3YQ.root",
sampleBaseDir+"PATtuple_259_1_Aa9.root",
sampleBaseDir+"PATtuple_333_1_1Gx.root",
sampleBaseDir+"PATtuple_300_1_Iw3.root",
sampleBaseDir+"PATtuple_623_1_r62.root",
sampleBaseDir+"PATtuple_230_2_coh.root",
sampleBaseDir+"PATtuple_88_2_iKT.root",
sampleBaseDir+"PATtuple_163_1_gKP.root",
sampleBaseDir+"PATtuple_193_1_Ehp.root",
sampleBaseDir+"PATtuple_401_1_f9l.root",
sampleBaseDir+"PATtuple_644_1_EVB.root",
sampleBaseDir+"PATtuple_505_1_Vsu.root",
sampleBaseDir+"PATtuple_496_1_OhU.root",
sampleBaseDir+"PATtuple_525_1_ynW.root",
sampleBaseDir+"PATtuple_391_2_D5g.root",
sampleBaseDir+"PATtuple_288_2_WlY.root",
sampleBaseDir+"PATtuple_396_2_Se8.root",
sampleBaseDir+"PATtuple_61_2_rmo.root",
sampleBaseDir+"PATtuple_556_4_j53.root",
sampleBaseDir+"PATtuple_140_1_oyw.root",
sampleBaseDir+"PATtuple_280_1_33p.root",
sampleBaseDir+"PATtuple_384_1_3bh.root",
sampleBaseDir+"PATtuple_153_2_ieS.root",
sampleBaseDir+"PATtuple_614_2_Q90.root",
sampleBaseDir+"PATtuple_564_4_JoG.root",
sampleBaseDir+"PATtuple_386_1_0Nj.root",
sampleBaseDir+"PATtuple_618_2_qXV.root",
sampleBaseDir+"PATtuple_433_4_vwh.root",
sampleBaseDir+"PATtuple_168_1_n8C.root",
sampleBaseDir+"PATtuple_348_1_vlK.root",
sampleBaseDir+"PATtuple_454_1_QMa.root",
sampleBaseDir+"PATtuple_471_1_uQi.root",
sampleBaseDir+"PATtuple_551_2_XEp.root",
sampleBaseDir+"PATtuple_334_1_J52.root",
sampleBaseDir+"PATtuple_106_2_H6Y.root",
sampleBaseDir+"PATtuple_306_1_x4O.root",
sampleBaseDir+"PATtuple_402_1_1yV.root",
sampleBaseDir+"PATtuple_152_2_pHe.root",
sampleBaseDir+"PATtuple_597_2_4cp.root",
sampleBaseDir+"PATtuple_343_2_HrN.root",
sampleBaseDir+"PATtuple_643_3_OVa.root",
sampleBaseDir+"PATtuple_387_1_zaw.root",
sampleBaseDir+"PATtuple_93_2_oeE.root",
sampleBaseDir+"PATtuple_428_3_Ook.root",
sampleBaseDir+"PATtuple_144_1_SNH.root",
sampleBaseDir+"PATtuple_209_1_3Qv.root",
sampleBaseDir+"PATtuple_217_1_Qhf.root",
sampleBaseDir+"PATtuple_178_2_QAM.root",
sampleBaseDir+"PATtuple_487_2_nbm.root",
sampleBaseDir+"PATtuple_2_3_sPP.root",
sampleBaseDir+"PATtuple_189_2_HRS.root",
sampleBaseDir+"PATtuple_619_2_cYW.root",
sampleBaseDir+"PATtuple_377_2_wzo.root",
sampleBaseDir+"PATtuple_44_1_DG0.root",
sampleBaseDir+"PATtuple_308_1_Rly.root",
sampleBaseDir+"PATtuple_603_1_ACL.root",
sampleBaseDir+"PATtuple_540_1_RNY.root",
sampleBaseDir+"PATtuple_610_2_gPs.root",
sampleBaseDir+"PATtuple_575_4_SWC.root",
sampleBaseDir+"PATtuple_72_1_Y3e.root",
sampleBaseDir+"PATtuple_310_1_hfg.root",
sampleBaseDir+"PATtuple_338_1_wxZ.root",
sampleBaseDir+"PATtuple_470_1_cUT.root",
sampleBaseDir+"PATtuple_62_2_lhk.root",
sampleBaseDir+"PATtuple_599_2_QBo.root",
sampleBaseDir+"PATtuple_548_2_JTo.root",
sampleBaseDir+"PATtuple_99_3_TUI.root",
sampleBaseDir+"PATtuple_476_1_ly2.root",
sampleBaseDir+"PATtuple_97_2_yJa.root",
sampleBaseDir+"PATtuple_228_2_24M.root",
sampleBaseDir+"PATtuple_31_2_El7.root",
sampleBaseDir+"PATtuple_246_1_oWS.root",
sampleBaseDir+"PATtuple_447_1_Ux8.root",
sampleBaseDir+"PATtuple_500_1_18a.root",
sampleBaseDir+"PATtuple_138_1_XRZ.root",
sampleBaseDir+"PATtuple_412_1_CHv.root",
sampleBaseDir+"PATtuple_7_2_jIo.root",
sampleBaseDir+"PATtuple_286_2_JsN.root",
sampleBaseDir+"PATtuple_326_2_cG4.root",
sampleBaseDir+"PATtuple_284_2_K24.root",
sampleBaseDir+"PATtuple_251_1_S3x.root",
sampleBaseDir+"PATtuple_312_1_1qU.root",
sampleBaseDir+"PATtuple_440_1_x1B.root",
sampleBaseDir+"PATtuple_441_1_xhE.root",
sampleBaseDir+"PATtuple_481_1_ifX.root",
sampleBaseDir+"PATtuple_102_3_OFI.root",
sampleBaseDir+"PATtuple_42_1_R3f.root",
sampleBaseDir+"PATtuple_376_1_pC5.root",
sampleBaseDir+"PATtuple_637_3_5Qa.root",
sampleBaseDir+"PATtuple_241_1_8Id.root",
sampleBaseDir+"PATtuple_200_1_BJ7.root",
sampleBaseDir+"PATtuple_351_1_FoQ.root",
sampleBaseDir+"PATtuple_508_1_sEw.root",
sampleBaseDir+"PATtuple_524_1_JdQ.root",
sampleBaseDir+"PATtuple_462_1_xYk.root",
sampleBaseDir+"PATtuple_517_2_9Jb.root",
sampleBaseDir+"PATtuple_148_1_KNs.root",
sampleBaseDir+"PATtuple_195_1_aW7.root",
sampleBaseDir+"PATtuple_275_1_kJS.root",
sampleBaseDir+"PATtuple_379_1_V5v.root",
sampleBaseDir+"PATtuple_446_1_QCM.root",
sampleBaseDir+"PATtuple_352_1_sZb.root",
sampleBaseDir+"PATtuple_372_2_XgO.root",
sampleBaseDir+"PATtuple_417_4_Z3v.root",
sampleBaseDir+"PATtuple_373_1_BAs.root",
sampleBaseDir+"PATtuple_356_1_Un1.root",
sampleBaseDir+"PATtuple_294_1_IBF.root",
sampleBaseDir+"PATtuple_587_2_v5M.root",
sampleBaseDir+"PATtuple_566_4_8L2.root",
sampleBaseDir+"PATtuple_426_3_523.root",
sampleBaseDir+"PATtuple_139_1_3kA.root",
sampleBaseDir+"PATtuple_316_1_iFJ.root",
sampleBaseDir+"PATtuple_385_1_hms.root",
sampleBaseDir+"PATtuple_267_1_eoq.root",
sampleBaseDir+"PATtuple_142_1_d0U.root",
sampleBaseDir+"PATtuple_313_1_Boy.root",
sampleBaseDir+"PATtuple_341_1_DaP.root",
sampleBaseDir+"PATtuple_190_2_NsT.root",
sampleBaseDir+"PATtuple_578_2_Xe6.root",
sampleBaseDir+"PATtuple_151_1_oHX.root",
sampleBaseDir+"PATtuple_311_1_Vd1.root",
sampleBaseDir+"PATtuple_23_2_oZi.root",
sampleBaseDir+"PATtuple_156_2_d0Z.root",
sampleBaseDir+"PATtuple_571_4_Fqu.root",
sampleBaseDir+"PATtuple_632_3_v1g.root",
sampleBaseDir+"PATtuple_77_1_TKf.root",
sampleBaseDir+"PATtuple_147_1_ptU.root",
sampleBaseDir+"PATtuple_530_1_Ixg.root",
sampleBaseDir+"PATtuple_609_2_2ZS.root",
sampleBaseDir+"PATtuple_477_1_aAN.root",
sampleBaseDir+"PATtuple_543_1_YNU.root",
sampleBaseDir+"PATtuple_107_2_gwI.root",
sampleBaseDir+"PATtuple_17_1_LKn.root",
]