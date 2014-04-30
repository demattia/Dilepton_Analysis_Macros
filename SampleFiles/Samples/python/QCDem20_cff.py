sampleDataSet = '/QCD_Pt_20_30_EMEnriched_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'  

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_2_patch4" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_5" # release used to create new files with

sampleNumEvents = 35040695

sampleXSec = 2.886E8 * 0.0101 # pb

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7F::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "BKGMC"





samplePatDBSName=""

sampleBaseDir="/store/user/lpcdve/DisplacedLeptons/QCDem20_pat_20130203/demattia//QCD_Pt_20_30_EMEnriched_TuneZ2star_8TeV_pythia6/QCDem20_pat_20130203/5fe3dadd93bf8608b396f970098158ed/"
samplePatFiles = [
sampleBaseDir+"PATtuple_443_1_NpS.root",
sampleBaseDir+"PATtuple_214_1_pfd.root",
sampleBaseDir+"PATtuple_39_1_31a.root",
sampleBaseDir+"PATtuple_416_1_rJm.root",
sampleBaseDir+"PATtuple_570_1_xAU.root",
sampleBaseDir+"PATtuple_679_1_iPX.root",
sampleBaseDir+"PATtuple_36_1_RM6.root",
sampleBaseDir+"PATtuple_189_1_QbY.root",
sampleBaseDir+"PATtuple_511_1_SMI.root",
sampleBaseDir+"PATtuple_534_1_lg0.root",
sampleBaseDir+"PATtuple_635_1_jAE.root",
sampleBaseDir+"PATtuple_685_1_te8.root",
sampleBaseDir+"PATtuple_1_1_cZ3.root",
sampleBaseDir+"PATtuple_13_1_z2C.root",
sampleBaseDir+"PATtuple_282_1_0mG.root",
sampleBaseDir+"PATtuple_66_1_2wb.root",
sampleBaseDir+"PATtuple_444_1_jh8.root",
sampleBaseDir+"PATtuple_182_1_Ukg.root",
sampleBaseDir+"PATtuple_117_1_x53.root",
sampleBaseDir+"PATtuple_271_1_rmb.root",
sampleBaseDir+"PATtuple_595_1_2XV.root",
sampleBaseDir+"PATtuple_599_1_Tk1.root",
sampleBaseDir+"PATtuple_549_1_Fu4.root",
sampleBaseDir+"PATtuple_108_1_6Px.root",
sampleBaseDir+"PATtuple_345_1_BhL.root",
sampleBaseDir+"PATtuple_290_1_Obg.root",
sampleBaseDir+"PATtuple_225_1_CRZ.root",
sampleBaseDir+"PATtuple_691_1_KSP.root",
sampleBaseDir+"PATtuple_538_1_sjV.root",
sampleBaseDir+"PATtuple_579_1_hXk.root",
sampleBaseDir+"PATtuple_143_1_H0Q.root",
sampleBaseDir+"PATtuple_161_1_GWG.root",
sampleBaseDir+"PATtuple_69_1_TRh.root",
sampleBaseDir+"PATtuple_285_1_gRe.root",
sampleBaseDir+"PATtuple_319_1_tdp.root",
sampleBaseDir+"PATtuple_219_1_Xd1.root",
sampleBaseDir+"PATtuple_249_1_TXl.root",
sampleBaseDir+"PATtuple_258_1_hiv.root",
sampleBaseDir+"PATtuple_269_1_FnJ.root",
sampleBaseDir+"PATtuple_30_1_AXb.root",
sampleBaseDir+"PATtuple_20_1_Rw7.root",
sampleBaseDir+"PATtuple_151_1_EPH.root",
sampleBaseDir+"PATtuple_24_1_SYZ.root",
sampleBaseDir+"PATtuple_399_1_jVM.root",
sampleBaseDir+"PATtuple_300_1_lUm.root",
sampleBaseDir+"PATtuple_403_1_1lx.root",
sampleBaseDir+"PATtuple_266_1_d3F.root",
sampleBaseDir+"PATtuple_590_1_Z2i.root",
sampleBaseDir+"PATtuple_680_1_rMT.root",
sampleBaseDir+"PATtuple_11_1_CzZ.root",
sampleBaseDir+"PATtuple_23_1_GUz.root",
sampleBaseDir+"PATtuple_574_1_YVw.root",
sampleBaseDir+"PATtuple_648_2_5kE.root",
sampleBaseDir+"PATtuple_554_1_n7A.root",
sampleBaseDir+"PATtuple_156_1_I9O.root",
sampleBaseDir+"PATtuple_344_1_7Z1.root",
sampleBaseDir+"PATtuple_540_1_FCE.root",
sampleBaseDir+"PATtuple_661_1_YaQ.root",
sampleBaseDir+"PATtuple_649_1_P9Z.root",
sampleBaseDir+"PATtuple_99_1_hnI.root",
sampleBaseDir+"PATtuple_250_1_y6f.root",
sampleBaseDir+"PATtuple_376_1_LKm.root",
sampleBaseDir+"PATtuple_239_1_S2H.root",
sampleBaseDir+"PATtuple_658_1_vhI.root",
sampleBaseDir+"PATtuple_616_1_01F.root",
sampleBaseDir+"PATtuple_100_1_38w.root",
sampleBaseDir+"PATtuple_103_1_SoV.root",
sampleBaseDir+"PATtuple_246_1_EOA.root",
sampleBaseDir+"PATtuple_233_1_RAM.root",
sampleBaseDir+"PATtuple_555_1_AZZ.root",
sampleBaseDir+"PATtuple_446_1_Dbl.root",
sampleBaseDir+"PATtuple_482_1_nbJ.root",
sampleBaseDir+"PATtuple_675_1_0G2.root",
sampleBaseDir+"PATtuple_553_1_Dkq.root",
sampleBaseDir+"PATtuple_308_1_Fue.root",
sampleBaseDir+"PATtuple_366_1_2th.root",
sampleBaseDir+"PATtuple_537_1_ZLI.root",
sampleBaseDir+"PATtuple_550_1_BQp.root",
sampleBaseDir+"PATtuple_147_1_81D.root",
sampleBaseDir+"PATtuple_185_1_HOg.root",
sampleBaseDir+"PATtuple_154_1_DWZ.root",
sampleBaseDir+"PATtuple_248_1_Bno.root",
sampleBaseDir+"PATtuple_420_1_OmR.root",
sampleBaseDir+"PATtuple_337_1_WxK.root",
sampleBaseDir+"PATtuple_413_1_PPi.root",
sampleBaseDir+"PATtuple_212_1_RmF.root",
sampleBaseDir+"PATtuple_580_1_aPn.root",
sampleBaseDir+"PATtuple_619_1_y1S.root",
sampleBaseDir+"PATtuple_699_1_1SY.root",
sampleBaseDir+"PATtuple_439_1_yX5.root",
sampleBaseDir+"PATtuple_184_1_1o8.root",
sampleBaseDir+"PATtuple_264_1_Me7.root",
sampleBaseDir+"PATtuple_610_1_6ZB.root",
sampleBaseDir+"PATtuple_49_1_sIx.root",
sampleBaseDir+"PATtuple_682_1_BZb.root",
sampleBaseDir+"PATtuple_657_1_gwu.root",
sampleBaseDir+"PATtuple_81_1_eyk.root",
sampleBaseDir+"PATtuple_153_1_V4q.root",
sampleBaseDir+"PATtuple_89_1_xlE.root",
sampleBaseDir+"PATtuple_384_1_l5Y.root",
sampleBaseDir+"PATtuple_289_1_hsb.root",
sampleBaseDir+"PATtuple_445_1_tSh.root",
sampleBaseDir+"PATtuple_686_1_q9s.root",
sampleBaseDir+"PATtuple_106_1_vm2.root",
sampleBaseDir+"PATtuple_57_1_Vmb.root",
sampleBaseDir+"PATtuple_280_1_rME.root",
sampleBaseDir+"PATtuple_138_1_8RZ.root",
sampleBaseDir+"PATtuple_93_1_0SR.root",
sampleBaseDir+"PATtuple_666_1_Gbk.root",
sampleBaseDir+"PATtuple_92_1_oLV.root",
sampleBaseDir+"PATtuple_343_1_oY4.root",
sampleBaseDir+"PATtuple_463_1_8Mr.root",
sampleBaseDir+"PATtuple_497_1_bP8.root",
sampleBaseDir+"PATtuple_481_1_vQZ.root",
sampleBaseDir+"PATtuple_577_1_25H.root",
sampleBaseDir+"PATtuple_251_1_Nef.root",
sampleBaseDir+"PATtuple_320_1_Qew.root",
sampleBaseDir+"PATtuple_491_1_lTs.root",
sampleBaseDir+"PATtuple_615_1_cDL.root",
sampleBaseDir+"PATtuple_179_2_PxS.root",
sampleBaseDir+"PATtuple_77_1_Dzz.root",
sampleBaseDir+"PATtuple_194_1_Jyj.root",
sampleBaseDir+"PATtuple_130_1_vXE.root",
sampleBaseDir+"PATtuple_578_1_z8y.root",
sampleBaseDir+"PATtuple_683_1_Srr.root",
sampleBaseDir+"PATtuple_551_1_jYX.root",
sampleBaseDir+"PATtuple_602_1_UqS.root",
sampleBaseDir+"PATtuple_80_1_tDu.root",
sampleBaseDir+"PATtuple_173_1_vdx.root",
sampleBaseDir+"PATtuple_22_1_smy.root",
sampleBaseDir+"PATtuple_475_1_Cym.root",
sampleBaseDir+"PATtuple_34_1_S0r.root",
sampleBaseDir+"PATtuple_82_1_bNT.root",
sampleBaseDir+"PATtuple_115_1_qRP.root",
sampleBaseDir+"PATtuple_326_1_da1.root",
sampleBaseDir+"PATtuple_559_1_5db.root",
sampleBaseDir+"PATtuple_545_1_x22.root",
sampleBaseDir+"PATtuple_60_1_1yg.root",
sampleBaseDir+"PATtuple_167_1_1xD.root",
sampleBaseDir+"PATtuple_386_1_Mv4.root",
sampleBaseDir+"PATtuple_575_1_Bhj.root",
sampleBaseDir+"PATtuple_660_1_X6N.root",
sampleBaseDir+"PATtuple_377_1_dXk.root",
sampleBaseDir+"PATtuple_397_1_avx.root",
sampleBaseDir+"PATtuple_644_1_Wa1.root",
sampleBaseDir+"PATtuple_306_1_Inb.root",
sampleBaseDir+"PATtuple_477_1_h3t.root",
sampleBaseDir+"PATtuple_315_1_M9J.root",
sampleBaseDir+"PATtuple_608_1_F9i.root",
sampleBaseDir+"PATtuple_142_1_Z9O.root",
sampleBaseDir+"PATtuple_448_1_Gea.root",
sampleBaseDir+"PATtuple_150_1_yaW.root",
sampleBaseDir+"PATtuple_253_1_gPW.root",
sampleBaseDir+"PATtuple_496_1_w8c.root",
sampleBaseDir+"PATtuple_529_2_1fp.root",
sampleBaseDir+"PATtuple_452_1_viF.root",
sampleBaseDir+"PATtuple_404_1_1xa.root",
sampleBaseDir+"PATtuple_274_1_9B8.root",
sampleBaseDir+"PATtuple_238_1_3ug.root",
sampleBaseDir+"PATtuple_627_1_ac4.root",
sampleBaseDir+"PATtuple_614_1_FuX.root",
sampleBaseDir+"PATtuple_585_1_M0n.root",
sampleBaseDir+"PATtuple_617_1_92H.root",
sampleBaseDir+"PATtuple_651_1_7Tt.root",
sampleBaseDir+"PATtuple_38_1_uqG.root",
sampleBaseDir+"PATtuple_95_1_oWZ.root",
sampleBaseDir+"PATtuple_107_1_jY3.root",
sampleBaseDir+"PATtuple_406_1_Vf1.root",
sampleBaseDir+"PATtuple_470_1_woT.root",
sampleBaseDir+"PATtuple_277_1_idY.root",
sampleBaseDir+"PATtuple_639_1_wRm.root",
sampleBaseDir+"PATtuple_609_1_Cxh.root",
sampleBaseDir+"PATtuple_41_1_Mkz.root",
sampleBaseDir+"PATtuple_144_1_dEt.root",
sampleBaseDir+"PATtuple_15_1_l70.root",
sampleBaseDir+"PATtuple_433_1_oE5.root",
sampleBaseDir+"PATtuple_292_1_39G.root",
sampleBaseDir+"PATtuple_222_1_VIO.root",
sampleBaseDir+"PATtuple_31_1_UuR.root",
sampleBaseDir+"PATtuple_168_1_Frp.root",
sampleBaseDir+"PATtuple_164_1_B60.root",
sampleBaseDir+"PATtuple_500_1_cMh.root",
sampleBaseDir+"PATtuple_331_1_i0Z.root",
sampleBaseDir+"PATtuple_335_1_iKc.root",
sampleBaseDir+"PATtuple_272_1_bee.root",
sampleBaseDir+"PATtuple_558_1_CQY.root",
sampleBaseDir+"PATtuple_618_1_lLf.root",
sampleBaseDir+"PATtuple_111_1_Eiz.root",
sampleBaseDir+"PATtuple_218_1_3B0.root",
sampleBaseDir+"PATtuple_589_1_QsG.root",
sampleBaseDir+"PATtuple_562_1_YPR.root",
sampleBaseDir+"PATtuple_502_1_0YZ.root",
sampleBaseDir+"PATtuple_542_1_L7D.root",
sampleBaseDir+"PATtuple_704_1_Onv.root",
sampleBaseDir+"PATtuple_503_1_FxC.root",
sampleBaseDir+"PATtuple_505_1_8b7.root",
sampleBaseDir+"PATtuple_79_1_XCU.root",
sampleBaseDir+"PATtuple_305_1_Sgx.root",
sampleBaseDir+"PATtuple_462_1_CB8.root",
sampleBaseDir+"PATtuple_565_1_h9C.root",
sampleBaseDir+"PATtuple_535_1_FJY.root",
sampleBaseDir+"PATtuple_688_1_iIG.root",
sampleBaseDir+"PATtuple_296_1_VC0.root",
sampleBaseDir+"PATtuple_324_1_E5Q.root",
sampleBaseDir+"PATtuple_348_1_hhS.root",
sampleBaseDir+"PATtuple_101_1_Of4.root",
sampleBaseDir+"PATtuple_362_1_9Me.root",
sampleBaseDir+"PATtuple_689_1_yb1.root",
sampleBaseDir+"PATtuple_449_1_FrI.root",
sampleBaseDir+"PATtuple_473_1_H3U.root",
sampleBaseDir+"PATtuple_547_1_smr.root",
sampleBaseDir+"PATtuple_175_1_f0v.root",
sampleBaseDir+"PATtuple_457_1_Jy8.root",
sampleBaseDir+"PATtuple_87_1_vQ2.root",
sampleBaseDir+"PATtuple_203_1_yt2.root",
sampleBaseDir+"PATtuple_628_1_vmr.root",
sampleBaseDir+"PATtuple_646_1_40W.root",
sampleBaseDir+"PATtuple_201_1_s6O.root",
sampleBaseDir+"PATtuple_355_1_S2c.root",
sampleBaseDir+"PATtuple_395_1_mMz.root",
sampleBaseDir+"PATtuple_423_1_hqm.root",
sampleBaseDir+"PATtuple_329_1_Dlk.root",
sampleBaseDir+"PATtuple_418_1_8yZ.root",
sampleBaseDir+"PATtuple_581_1_wvD.root",
sampleBaseDir+"PATtuple_698_1_mQy.root",
sampleBaseDir+"PATtuple_45_1_O4F.root",
sampleBaseDir+"PATtuple_287_1_WVP.root",
sampleBaseDir+"PATtuple_162_1_VEM.root",
sampleBaseDir+"PATtuple_487_1_gLh.root",
sampleBaseDir+"PATtuple_177_1_bgV.root",
sampleBaseDir+"PATtuple_539_1_Rv7.root",
sampleBaseDir+"PATtuple_576_1_Ujl.root",
sampleBaseDir+"PATtuple_148_1_TtS.root",
sampleBaseDir+"PATtuple_441_1_hfT.root",
sampleBaseDir+"PATtuple_230_1_um5.root",
sampleBaseDir+"PATtuple_234_1_BkH.root",
sampleBaseDir+"PATtuple_517_1_rtd.root",
sampleBaseDir+"PATtuple_548_2_E16.root",
sampleBaseDir+"PATtuple_85_1_3NJ.root",
sampleBaseDir+"PATtuple_350_1_gn8.root",
sampleBaseDir+"PATtuple_476_1_sSl.root",
sampleBaseDir+"PATtuple_631_1_afW.root",
sampleBaseDir+"PATtuple_279_1_j8s.root",
sampleBaseDir+"PATtuple_119_1_oVm.root",
sampleBaseDir+"PATtuple_124_1_BZ3.root",
sampleBaseDir+"PATtuple_483_1_XqG.root",
sampleBaseDir+"PATtuple_254_1_WJ2.root",
sampleBaseDir+"PATtuple_244_1_6mE.root",
sampleBaseDir+"PATtuple_25_1_LFG.root",
sampleBaseDir+"PATtuple_294_1_U2U.root",
sampleBaseDir+"PATtuple_390_1_Wbj.root",
sampleBaseDir+"PATtuple_383_1_2ku.root",
sampleBaseDir+"PATtuple_419_1_9Uf.root",
sampleBaseDir+"PATtuple_493_1_8mN.root",
sampleBaseDir+"PATtuple_606_1_bXH.root",
sampleBaseDir+"PATtuple_525_1_O8z.root",
sampleBaseDir+"PATtuple_314_1_6bw.root",
sampleBaseDir+"PATtuple_499_1_PNN.root",
sampleBaseDir+"PATtuple_557_1_fud.root",
sampleBaseDir+"PATtuple_642_1_0ER.root",
sampleBaseDir+"PATtuple_703_1_p3i.root",
sampleBaseDir+"PATtuple_122_1_Kzh.root",
sampleBaseDir+"PATtuple_401_1_2sO.root",
sampleBaseDir+"PATtuple_302_1_D0K.root",
sampleBaseDir+"PATtuple_243_1_WMP.root",
sampleBaseDir+"PATtuple_659_1_nXU.root",
sampleBaseDir+"PATtuple_584_1_8uH.root",
sampleBaseDir+"PATtuple_307_1_0Gs.root",
sampleBaseDir+"PATtuple_388_1_ytm.root",
sampleBaseDir+"PATtuple_400_1_rOv.root",
sampleBaseDir+"PATtuple_484_1_JLe.root",
sampleBaseDir+"PATtuple_220_1_aJn.root",
sampleBaseDir+"PATtuple_479_1_6Zp.root",
sampleBaseDir+"PATtuple_514_1_8qv.root",
sampleBaseDir+"PATtuple_5_1_vIi.root",
sampleBaseDir+"PATtuple_54_1_A50.root",
sampleBaseDir+"PATtuple_346_1_A3C.root",
sampleBaseDir+"PATtuple_375_1_St5.root",
sampleBaseDir+"PATtuple_560_1_tyH.root",
sampleBaseDir+"PATtuple_598_1_9FK.root",
sampleBaseDir+"PATtuple_571_1_rmI.root",
sampleBaseDir+"PATtuple_519_1_iNi.root",
sampleBaseDir+"PATtuple_187_1_HGo.root",
sampleBaseDir+"PATtuple_78_1_dpq.root",
sampleBaseDir+"PATtuple_474_1_EeH.root",
sampleBaseDir+"PATtuple_263_1_cCc.root",
sampleBaseDir+"PATtuple_18_1_JuW.root",
sampleBaseDir+"PATtuple_129_1_c9s.root",
sampleBaseDir+"PATtuple_112_1_v6F.root",
sampleBaseDir+"PATtuple_588_1_NlW.root",
sampleBaseDir+"PATtuple_586_1_YvP.root",
sampleBaseDir+"PATtuple_382_1_4Ug.root",
sampleBaseDir+"PATtuple_465_1_5sQ.root",
sampleBaseDir+"PATtuple_510_1_JKj.root",
sampleBaseDir+"PATtuple_620_1_UzR.root",
sampleBaseDir+"PATtuple_623_1_FBY.root",
sampleBaseDir+"PATtuple_426_1_PaM.root",
sampleBaseDir+"PATtuple_323_1_xwJ.root",
sampleBaseDir+"PATtuple_332_1_fXF.root",
sampleBaseDir+"PATtuple_211_1_a64.root",
sampleBaseDir+"PATtuple_684_1_QQR.root",
sampleBaseDir+"PATtuple_145_1_Rw5.root",
sampleBaseDir+"PATtuple_158_1_Abl.root",
sampleBaseDir+"PATtuple_295_1_JbV.root",
sampleBaseDir+"PATtuple_322_1_rtv.root",
sampleBaseDir+"PATtuple_339_1_0A6.root",
sampleBaseDir+"PATtuple_396_1_aoa.root",
sampleBaseDir+"PATtuple_563_1_jGO.root",
sampleBaseDir+"PATtuple_652_1_4uO.root",
sampleBaseDir+"PATtuple_86_1_pwJ.root",
sampleBaseDir+"PATtuple_321_1_sb8.root",
sampleBaseDir+"PATtuple_245_1_J9w.root",
sampleBaseDir+"PATtuple_32_1_R14.root",
sampleBaseDir+"PATtuple_51_1_fph.root",
sampleBaseDir+"PATtuple_336_1_mrb.root",
sampleBaseDir+"PATtuple_488_1_NjS.root",
sampleBaseDir+"PATtuple_490_1_N3O.root",
sampleBaseDir+"PATtuple_260_1_H0O.root",
sampleBaseDir+"PATtuple_624_1_QNv.root",
sampleBaseDir+"PATtuple_541_1_N4N.root",
sampleBaseDir+"PATtuple_464_1_rpp.root",
sampleBaseDir+"PATtuple_369_1_0nC.root",
sampleBaseDir+"PATtuple_630_1_CiK.root",
sampleBaseDir+"PATtuple_58_1_QgC.root",
sampleBaseDir+"PATtuple_59_1_CtG.root",
sampleBaseDir+"PATtuple_430_1_XeS.root",
sampleBaseDir+"PATtuple_485_1_5Pp.root",
sampleBaseDir+"PATtuple_506_1_gjA.root",
sampleBaseDir+"PATtuple_113_1_Bdr.root",
sampleBaseDir+"PATtuple_309_1_9mI.root",
sampleBaseDir+"PATtuple_109_1_5N2.root",
sampleBaseDir+"PATtuple_7_1_xK4.root",
sampleBaseDir+"PATtuple_9_1_wE3.root",
sampleBaseDir+"PATtuple_186_1_j7u.root",
sampleBaseDir+"PATtuple_286_1_bDg.root",
sampleBaseDir+"PATtuple_98_1_VmP.root",
sampleBaseDir+"PATtuple_435_1_aID.root",
sampleBaseDir+"PATtuple_437_1_v7S.root",
sampleBaseDir+"PATtuple_209_1_DjU.root",
sampleBaseDir+"PATtuple_354_1_WnR.root",
sampleBaseDir+"PATtuple_114_1_n8J.root",
sampleBaseDir+"PATtuple_141_1_RQb.root",
sampleBaseDir+"PATtuple_53_1_Adn.root",
sampleBaseDir+"PATtuple_155_1_VhD.root",
sampleBaseDir+"PATtuple_381_1_f6P.root",
sampleBaseDir+"PATtuple_594_1_fEN.root",
sampleBaseDir+"PATtuple_40_1_XUn.root",
sampleBaseDir+"PATtuple_378_1_nsa.root",
sampleBaseDir+"PATtuple_412_1_CyU.root",
sampleBaseDir+"PATtuple_16_1_Ye1.root",
sampleBaseDir+"PATtuple_160_1_g7t.root",
sampleBaseDir+"PATtuple_88_1_P2t.root",
sampleBaseDir+"PATtuple_140_1_2CM.root",
sampleBaseDir+"PATtuple_120_1_fKG.root",
sampleBaseDir+"PATtuple_259_1_4s9.root",
sampleBaseDir+"PATtuple_587_1_Dfr.root",
sampleBaseDir+"PATtuple_662_1_YCM.root",
sampleBaseDir+"PATtuple_330_1_lbR.root",
sampleBaseDir+"PATtuple_604_1_mXw.root",
sampleBaseDir+"PATtuple_634_1_BC4.root",
sampleBaseDir+"PATtuple_507_1_hzK.root",
sampleBaseDir+"PATtuple_663_1_m6Y.root",
sampleBaseDir+"PATtuple_582_1_SXN.root",
sampleBaseDir+"PATtuple_533_1_Ro7.root",
sampleBaseDir+"PATtuple_63_1_pS0.root",
sampleBaseDir+"PATtuple_21_1_Y3o.root",
sampleBaseDir+"PATtuple_281_1_o7q.root",
sampleBaseDir+"PATtuple_70_2_wlM.root",
sampleBaseDir+"PATtuple_55_1_kNR.root",
sampleBaseDir+"PATtuple_61_1_v5K.root",
sampleBaseDir+"PATtuple_76_1_QuB.root",
sampleBaseDir+"PATtuple_206_1_Ysv.root",
sampleBaseDir+"PATtuple_665_1_OHW.root",
sampleBaseDir+"PATtuple_696_1_asC.root",
sampleBaseDir+"PATtuple_174_1_Wuk.root",
sampleBaseDir+"PATtuple_231_1_hEe.root",
sampleBaseDir+"PATtuple_327_1_TO5.root",
sampleBaseDir+"PATtuple_645_1_IcY.root",
sampleBaseDir+"PATtuple_697_1_c7h.root",
sampleBaseDir+"PATtuple_522_1_Htx.root",
sampleBaseDir+"PATtuple_347_1_iQW.root",
sampleBaseDir+"PATtuple_223_1_pqm.root",
sampleBaseDir+"PATtuple_411_1_FKB.root",
sampleBaseDir+"PATtuple_380_1_NDl.root",
sampleBaseDir+"PATtuple_494_1_FVv.root",
sampleBaseDir+"PATtuple_434_1_zjP.root",
sampleBaseDir+"PATtuple_237_1_XSU.root",
sampleBaseDir+"PATtuple_261_1_dna.root",
sampleBaseDir+"PATtuple_600_1_hVu.root",
sampleBaseDir+"PATtuple_690_1_JU5.root",
sampleBaseDir+"PATtuple_136_1_6iM.root",
sampleBaseDir+"PATtuple_6_1_beT.root",
sampleBaseDir+"PATtuple_451_1_x9l.root",
sampleBaseDir+"PATtuple_478_1_zmF.root",
sampleBaseDir+"PATtuple_257_1_JUh.root",
sampleBaseDir+"PATtuple_425_1_voI.root",
sampleBaseDir+"PATtuple_428_1_Rqu.root",
sampleBaseDir+"PATtuple_504_1_5x2.root",
sampleBaseDir+"PATtuple_152_1_b4e.root",
sampleBaseDir+"PATtuple_284_1_RgP.root",
sampleBaseDir+"PATtuple_310_1_R7D.root",
sampleBaseDir+"PATtuple_358_1_txe.root",
sampleBaseDir+"PATtuple_447_1_mqQ.root",
sampleBaseDir+"PATtuple_515_1_nEv.root",
sampleBaseDir+"PATtuple_312_1_F2f.root",
sampleBaseDir+"PATtuple_372_1_LWY.root",
sampleBaseDir+"PATtuple_544_1_TzY.root",
sampleBaseDir+"PATtuple_706_1_IWw.root",
sampleBaseDir+"PATtuple_647_1_Sur.root",
sampleBaseDir+"PATtuple_64_1_PHz.root",
sampleBaseDir+"PATtuple_213_1_ifm.root",
sampleBaseDir+"PATtuple_256_1_s2a.root",
sampleBaseDir+"PATtuple_638_1_Dos.root",
sampleBaseDir+"PATtuple_669_1_VjO.root",
sampleBaseDir+"PATtuple_48_1_nId.root",
sampleBaseDir+"PATtuple_17_1_Iqi.root",
sampleBaseDir+"PATtuple_118_1_ZNN.root",
sampleBaseDir+"PATtuple_357_1_hvX.root",
sampleBaseDir+"PATtuple_157_1_ELe.root",
sampleBaseDir+"PATtuple_202_1_6ok.root",
sampleBaseDir+"PATtuple_276_1_aOq.root",
sampleBaseDir+"PATtuple_240_1_5e0.root",
sampleBaseDir+"PATtuple_353_1_1jI.root",
sampleBaseDir+"PATtuple_513_1_9RK.root",
sampleBaseDir+"PATtuple_572_2_TRE.root",
sampleBaseDir+"PATtuple_3_1_gLj.root",
sampleBaseDir+"PATtuple_469_1_uNr.root",
sampleBaseDir+"PATtuple_456_1_ymx.root",
sampleBaseDir+"PATtuple_402_1_Vwz.root",
sampleBaseDir+"PATtuple_593_1_gvV.root",
sampleBaseDir+"PATtuple_678_1_tHT.root",
sampleBaseDir+"PATtuple_677_1_ydC.root",
sampleBaseDir+"PATtuple_543_1_k5R.root",
sampleBaseDir+"PATtuple_131_1_0Jb.root",
sampleBaseDir+"PATtuple_242_1_3Hm.root",
sampleBaseDir+"PATtuple_601_1_yhU.root",
sampleBaseDir+"PATtuple_643_1_7vu.root",
sampleBaseDir+"PATtuple_629_1_hjx.root",
sampleBaseDir+"PATtuple_569_2_a7x.root",
sampleBaseDir+"PATtuple_42_1_VRn.root",
sampleBaseDir+"PATtuple_334_1_c66.root",
sampleBaseDir+"PATtuple_410_1_zf2.root",
sampleBaseDir+"PATtuple_227_1_kfD.root",
sampleBaseDir+"PATtuple_466_1_jFK.root",
sampleBaseDir+"PATtuple_701_1_oL3.root",
sampleBaseDir+"PATtuple_546_1_WkL.root",
sampleBaseDir+"PATtuple_43_1_tXt.root",
sampleBaseDir+"PATtuple_461_1_jRJ.root",
sampleBaseDir+"PATtuple_455_1_wxD.root",
sampleBaseDir+"PATtuple_267_1_MFC.root",
sampleBaseDir+"PATtuple_409_1_GXH.root",
sampleBaseDir+"PATtuple_467_1_PsP.root",
sampleBaseDir+"PATtuple_299_1_Pxh.root",
sampleBaseDir+"PATtuple_349_1_nVv.root",
sampleBaseDir+"PATtuple_221_1_rz1.root",
sampleBaseDir+"PATtuple_702_1_rIY.root",
sampleBaseDir+"PATtuple_316_1_ak8.root",
sampleBaseDir+"PATtuple_459_1_fQt.root",
sampleBaseDir+"PATtuple_14_1_dru.root",
sampleBaseDir+"PATtuple_27_1_t7P.root",
sampleBaseDir+"PATtuple_96_1_IvL.root",
sampleBaseDir+"PATtuple_304_1_x7S.root",
sampleBaseDir+"PATtuple_125_1_hgm.root",
sampleBaseDir+"PATtuple_352_1_K6h.root",
sampleBaseDir+"PATtuple_391_1_kYW.root",
sampleBaseDir+"PATtuple_226_1_iNX.root",
sampleBaseDir+"PATtuple_492_1_V79.root",
sampleBaseDir+"PATtuple_670_1_q8k.root",
sampleBaseDir+"PATtuple_26_1_fcf.root",
sampleBaseDir+"PATtuple_291_1_Pmj.root",
sampleBaseDir+"PATtuple_195_1_33P.root",
sampleBaseDir+"PATtuple_204_2_DW8.root",
sampleBaseDir+"PATtuple_568_1_y4d.root",
sampleBaseDir+"PATtuple_52_1_F3T.root",
sampleBaseDir+"PATtuple_424_1_HKV.root",
sampleBaseDir+"PATtuple_208_1_Ibp.root",
sampleBaseDir+"PATtuple_217_1_Omb.root",
sampleBaseDir+"PATtuple_104_1_Z5d.root",
sampleBaseDir+"PATtuple_29_1_BbB.root",
sampleBaseDir+"PATtuple_389_1_A3E.root",
sampleBaseDir+"PATtuple_407_1_TJx.root",
sampleBaseDir+"PATtuple_442_1_Kgp.root",
sampleBaseDir+"PATtuple_472_1_WC3.root",
sampleBaseDir+"PATtuple_33_1_Lfc.root",
sampleBaseDir+"PATtuple_149_1_MaC.root",
sampleBaseDir+"PATtuple_215_1_sq9.root",
sampleBaseDir+"PATtuple_621_1_HlX.root",
sampleBaseDir+"PATtuple_521_1_eau.root",
sampleBaseDir+"PATtuple_298_1_ZTX.root",
sampleBaseDir+"PATtuple_398_1_MsG.root",
sampleBaseDir+"PATtuple_180_1_Cvw.root",
sampleBaseDir+"PATtuple_460_1_5d2.root",
sampleBaseDir+"PATtuple_671_1_Os6.root",
sampleBaseDir+"PATtuple_102_1_Nx9.root",
sampleBaseDir+"PATtuple_359_1_1n7.root",
sampleBaseDir+"PATtuple_97_1_Bdg.root",
sampleBaseDir+"PATtuple_181_1_fKT.root",
sampleBaseDir+"PATtuple_436_1_2c2.root",
sampleBaseDir+"PATtuple_440_1_z4j.root",
sampleBaseDir+"PATtuple_370_1_lDE.root",
sampleBaseDir+"PATtuple_528_1_anm.root",
sampleBaseDir+"PATtuple_303_1_cR6.root",
sampleBaseDir+"PATtuple_262_1_7DE.root",
sampleBaseDir+"PATtuple_127_1_Uqr.root",
sampleBaseDir+"PATtuple_328_1_N2v.root",
sampleBaseDir+"PATtuple_458_1_7k4.root",
sampleBaseDir+"PATtuple_495_1_Eo0.root",
sampleBaseDir+"PATtuple_235_1_2Fj.root",
sampleBaseDir+"PATtuple_28_1_2w2.root",
sampleBaseDir+"PATtuple_133_1_xfj.root",
sampleBaseDir+"PATtuple_613_1_nja.root",
sampleBaseDir+"PATtuple_385_1_LrZ.root",
sampleBaseDir+"PATtuple_530_1_v0a.root",
sampleBaseDir+"PATtuple_700_1_Foa.root",
sampleBaseDir+"PATtuple_387_1_utz.root",
sampleBaseDir+"PATtuple_405_1_eyh.root",
sampleBaseDir+"PATtuple_512_1_oIt.root",
sampleBaseDir+"PATtuple_126_1_p3E.root",
sampleBaseDir+"PATtuple_232_1_Ckx.root",
sampleBaseDir+"PATtuple_313_1_1SE.root",
sampleBaseDir+"PATtuple_667_1_FUz.root",
sampleBaseDir+"PATtuple_56_1_i0E.root",
sampleBaseDir+"PATtuple_71_1_k8l.root",
sampleBaseDir+"PATtuple_247_1_Hvj.root",
sampleBaseDir+"PATtuple_655_1_daX.root",
sampleBaseDir+"PATtuple_37_1_3i4.root",
sampleBaseDir+"PATtuple_35_1_oi6.root",
sampleBaseDir+"PATtuple_94_1_bSl.root",
sampleBaseDir+"PATtuple_62_1_8qa.root",
sampleBaseDir+"PATtuple_351_1_LgR.root",
sampleBaseDir+"PATtuple_668_1_kaw.root",
sampleBaseDir+"PATtuple_317_1_Vhh.root",
sampleBaseDir+"PATtuple_183_1_DAr.root",
sampleBaseDir+"PATtuple_365_1_arv.root",
sampleBaseDir+"PATtuple_268_1_zmk.root",
sampleBaseDir+"PATtuple_673_1_Hjo.root",
sampleBaseDir+"PATtuple_12_1_n2g.root",
sampleBaseDir+"PATtuple_200_1_TLe.root",
sampleBaseDir+"PATtuple_363_1_gjq.root",
sampleBaseDir+"PATtuple_368_1_36g.root",
sampleBaseDir+"PATtuple_531_1_dDG.root",
sampleBaseDir+"PATtuple_567_1_voI.root",
sampleBaseDir+"PATtuple_176_1_hSG.root",
sampleBaseDir+"PATtuple_171_1_V2t.root",
sampleBaseDir+"PATtuple_392_1_tma.root",
sampleBaseDir+"PATtuple_333_1_19N.root",
sampleBaseDir+"PATtuple_270_1_NEZ.root",
sampleBaseDir+"PATtuple_394_1_sil.root",
sampleBaseDir+"PATtuple_612_1_HLs.root",
sampleBaseDir+"PATtuple_197_1_FgJ.root",
sampleBaseDir+"PATtuple_408_1_tcB.root",
sampleBaseDir+"PATtuple_228_1_SVR.root",
sampleBaseDir+"PATtuple_191_1_cgG.root",
sampleBaseDir+"PATtuple_421_1_rZm.root",
sampleBaseDir+"PATtuple_520_1_Fex.root",
sampleBaseDir+"PATtuple_468_1_siw.root",
sampleBaseDir+"PATtuple_498_1_WF5.root",
sampleBaseDir+"PATtuple_622_1_P34.root",
sampleBaseDir+"PATtuple_640_1_eoW.root",
sampleBaseDir+"PATtuple_325_1_UOs.root",
sampleBaseDir+"PATtuple_241_1_pdP.root",
sampleBaseDir+"PATtuple_687_1_zPJ.root",
sampleBaseDir+"PATtuple_74_1_MCE.root",
sampleBaseDir+"PATtuple_192_1_Mxn.root",
sampleBaseDir+"PATtuple_207_1_XHe.root",
sampleBaseDir+"PATtuple_450_1_KTQ.root",
sampleBaseDir+"PATtuple_275_1_5tU.root",
sampleBaseDir+"PATtuple_371_1_isQ.root",
sampleBaseDir+"PATtuple_592_1_eMq.root",
sampleBaseDir+"PATtuple_636_1_GUx.root",
sampleBaseDir+"PATtuple_653_1_uUf.root",
sampleBaseDir+"PATtuple_47_1_M0A.root",
sampleBaseDir+"PATtuple_68_1_Ohv.root",
sampleBaseDir+"PATtuple_637_1_0ed.root",
sampleBaseDir+"PATtuple_607_1_BdH.root",
sampleBaseDir+"PATtuple_297_1_cH7.root",
sampleBaseDir+"PATtuple_422_1_WGQ.root",
sampleBaseDir+"PATtuple_480_1_m3m.root",
sampleBaseDir+"PATtuple_216_1_FNr.root",
sampleBaseDir+"PATtuple_526_1_Hbb.root",
sampleBaseDir+"PATtuple_453_1_XF5.root",
sampleBaseDir+"PATtuple_625_1_4NH.root",
sampleBaseDir+"PATtuple_19_1_u3p.root",
sampleBaseDir+"PATtuple_84_1_ZgE.root",
sampleBaseDir+"PATtuple_198_1_DUp.root",
sampleBaseDir+"PATtuple_252_1_TR2.root",
sampleBaseDir+"PATtuple_527_1_BRT.root",
sampleBaseDir+"PATtuple_566_1_qIj.root",
sampleBaseDir+"PATtuple_591_1_DSd.root",
sampleBaseDir+"PATtuple_674_1_HDv.root",
sampleBaseDir+"PATtuple_165_1_6AR.root",
sampleBaseDir+"PATtuple_170_1_dX8.root",
sampleBaseDir+"PATtuple_471_1_Gdb.root",
sampleBaseDir+"PATtuple_532_1_6dz.root",
sampleBaseDir+"PATtuple_626_1_Qvq.root",
sampleBaseDir+"PATtuple_4_1_qTa.root",
sampleBaseDir+"PATtuple_110_1_KG3.root",
sampleBaseDir+"PATtuple_692_1_lZ4.root",
sampleBaseDir+"PATtuple_656_1_XVx.root",
sampleBaseDir+"PATtuple_523_1_A1v.root",
sampleBaseDir+"PATtuple_178_1_FKM.root",
sampleBaseDir+"PATtuple_166_1_4f7.root",
sampleBaseDir+"PATtuple_278_1_mRx.root",
sampleBaseDir+"PATtuple_169_1_hp3.root",
sampleBaseDir+"PATtuple_163_1_rWf.root",
sampleBaseDir+"PATtuple_414_1_GJj.root",
sampleBaseDir+"PATtuple_489_1_DJH.root",
sampleBaseDir+"PATtuple_255_1_lH9.root",
sampleBaseDir+"PATtuple_501_1_tu4.root",
sampleBaseDir+"PATtuple_632_1_pz3.root",
sampleBaseDir+"PATtuple_650_1_8lW.root",
sampleBaseDir+"PATtuple_10_1_vjC.root",
sampleBaseDir+"PATtuple_137_1_eOc.root",
sampleBaseDir+"PATtuple_135_1_oD8.root",
sampleBaseDir+"PATtuple_90_1_29N.root",
sampleBaseDir+"PATtuple_196_1_zvi.root",
sampleBaseDir+"PATtuple_121_1_Rj0.root",
sampleBaseDir+"PATtuple_379_1_JUt.root",
sampleBaseDir+"PATtuple_229_1_QCy.root",
sampleBaseDir+"PATtuple_265_1_eMG.root",
sampleBaseDir+"PATtuple_508_1_7xo.root",
sampleBaseDir+"PATtuple_564_1_8Hr.root",
sampleBaseDir+"PATtuple_641_1_BP3.root",
sampleBaseDir+"PATtuple_695_1_egT.root",
sampleBaseDir+"PATtuple_596_1_Vpo.root",
sampleBaseDir+"PATtuple_676_1_ogB.root",
sampleBaseDir+"PATtuple_116_1_wf3.root",
sampleBaseDir+"PATtuple_342_1_cDJ.root",
sampleBaseDir+"PATtuple_432_1_41h.root",
sampleBaseDir+"PATtuple_293_1_7nl.root",
sampleBaseDir+"PATtuple_438_1_qfL.root",
sampleBaseDir+"PATtuple_417_1_rQ2.root",
sampleBaseDir+"PATtuple_693_1_gNH.root",
sampleBaseDir+"PATtuple_50_1_uMg.root",
sampleBaseDir+"PATtuple_128_1_4Mw.root",
sampleBaseDir+"PATtuple_427_1_0ZE.root",
sampleBaseDir+"PATtuple_611_1_EhY.root",
sampleBaseDir+"PATtuple_573_1_v1x.root",
sampleBaseDir+"PATtuple_72_1_7J3.root",
sampleBaseDir+"PATtuple_431_1_jKH.root",
sampleBaseDir+"PATtuple_236_1_58V.root",
sampleBaseDir+"PATtuple_199_1_uxc.root",
sampleBaseDir+"PATtuple_681_1_T5S.root",
sampleBaseDir+"PATtuple_146_1_f77.root",
sampleBaseDir+"PATtuple_288_1_C1I.root",
sampleBaseDir+"PATtuple_364_1_UdU.root",
sampleBaseDir+"PATtuple_193_1_ipL.root",
sampleBaseDir+"PATtuple_552_1_LA8.root",
sampleBaseDir+"PATtuple_8_1_LlM.root",
sampleBaseDir+"PATtuple_132_1_kZA.root",
sampleBaseDir+"PATtuple_83_1_0Au.root",
sampleBaseDir+"PATtuple_283_1_dfH.root",
sampleBaseDir+"PATtuple_367_1_c3S.root",
sampleBaseDir+"PATtuple_429_1_EmV.root",
sampleBaseDir+"PATtuple_205_1_j8P.root",
sampleBaseDir+"PATtuple_694_1_Z2u.root",
sampleBaseDir+"PATtuple_67_1_rwP.root",
sampleBaseDir+"PATtuple_139_1_EFJ.root",
sampleBaseDir+"PATtuple_373_1_n0k.root",
sampleBaseDir+"PATtuple_672_1_9bS.root",
sampleBaseDir+"PATtuple_134_1_nCI.root",
sampleBaseDir+"PATtuple_73_1_7pB.root",
sampleBaseDir+"PATtuple_123_1_QdL.root",
sampleBaseDir+"PATtuple_159_1_RtH.root",
sampleBaseDir+"PATtuple_311_1_Q9d.root",
sampleBaseDir+"PATtuple_374_1_G92.root",
sampleBaseDir+"PATtuple_633_1_Qge.root",
sampleBaseDir+"PATtuple_556_1_nNT.root",
sampleBaseDir+"PATtuple_2_1_l9o.root",
sampleBaseDir+"PATtuple_105_1_QZ9.root",
sampleBaseDir+"PATtuple_486_1_soa.root",
sampleBaseDir+"PATtuple_509_1_0uI.root",
sampleBaseDir+"PATtuple_561_1_2LN.root",
sampleBaseDir+"PATtuple_518_1_opH.root",
sampleBaseDir+"PATtuple_664_1_s2r.root",
sampleBaseDir+"PATtuple_597_1_udl.root",
sampleBaseDir+"PATtuple_360_1_Mbd.root",
sampleBaseDir+"PATtuple_583_1_HcP.root",
sampleBaseDir+"PATtuple_705_1_Y9a.root",
sampleBaseDir+"PATtuple_46_1_mW0.root",
sampleBaseDir+"PATtuple_318_1_9OS.root",
sampleBaseDir+"PATtuple_393_1_rZc.root",
sampleBaseDir+"PATtuple_190_1_Q4l.root",
sampleBaseDir+"PATtuple_338_1_Zxu.root",
sampleBaseDir+"PATtuple_210_1_5NY.root",
sampleBaseDir+"PATtuple_172_1_teY.root",
sampleBaseDir+"PATtuple_356_1_JjR.root",
sampleBaseDir+"PATtuple_301_1_XJM.root",
sampleBaseDir+"PATtuple_75_1_1Rd.root",
sampleBaseDir+"PATtuple_415_1_clF.root",
sampleBaseDir+"PATtuple_224_1_kef.root",
sampleBaseDir+"PATtuple_654_1_p9Z.root",
sampleBaseDir+"PATtuple_603_1_Y0y.root",
sampleBaseDir+"PATtuple_65_1_zQ6.root",
sampleBaseDir+"PATtuple_273_1_wyF.root",
sampleBaseDir+"PATtuple_605_1_k6R.root",
sampleBaseDir+"PATtuple_524_1_DTZ.root",
sampleBaseDir+"PATtuple_536_1_fAX.root",
sampleBaseDir+"PATtuple_188_1_xaH.root",
sampleBaseDir+"PATtuple_91_1_4KP.root",
sampleBaseDir+"PATtuple_44_1_Lrk.root",
sampleBaseDir+"PATtuple_340_1_hTC.root",
sampleBaseDir+"PATtuple_341_1_gVB.root",
sampleBaseDir+"PATtuple_454_1_nQT.root",
sampleBaseDir+"PATtuple_361_1_pwT.root",
sampleBaseDir+"PATtuple_516_1_Vsm.root",
]