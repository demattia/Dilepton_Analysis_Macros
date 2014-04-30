sampleDataSet = '/LongLivedChi0ToNuLL_MSquark-1500_MChi-494_TuneZ2Star_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'  

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_2_patch4" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_5" # release used to create new files with

sampleNumEvents = 10000

sampleXSec = 1 # pb

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7A::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "SIGNALMC"






samplePatDBSName=""

sampleBaseDir="file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Chi0ToNuLL_MSquark1500_MChi494_pat_20140329/demattia//LongLivedChi0ToNuLL_MSquark-1500_MChi-494_TuneZ2Star_8TeV-pythia6/Chi0ToNuLL_MSquark1500_MChi494_pat_20140329/44ed12438b36eeb4f61ccae26cc96d54/"
samplePatFiles = [
sampleBaseDir+"PATtuple_1_1_SQ9.root",
sampleBaseDir+"PATtuple_2_1_ZEW.root",
sampleBaseDir+"PATtuple_3_1_bKH.root",
sampleBaseDir+"PATtuple_4_1_8s8.root",
sampleBaseDir+"PATtuple_5_1_vaX.root",
]