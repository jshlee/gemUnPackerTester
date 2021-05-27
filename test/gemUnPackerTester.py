import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Era_Phase2C11M9_cff import Phase2C11M9

process = cms.Process('gemTester',Phase2C11M9)

process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('gemAnalyzer.gemAnalyzer.gemUnPackerTester_cfi')

process.gemUnPackerTester.gemDigi = cms.InputTag("muonGEMDigis",'','gemTester')
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

process.source = cms.Source("PoolSource",                           
  fileNames = cms.untracked.vstring('file:/store/relval/CMSSW_11_3_0_pre4/RelValZMM_14/GEN-SIM-RECO/PU_113X_mcRun4_realistic_v4_2026D76PU200-v1/00000/028001e8-5c24-48e7-8162-5da736ad7d38.root'),
)

process.TFileService = cms.Service('TFileService', fileName = cms.string('gemTester.root') )
process.rawDataCollector.RawCollectionList = cms.VInputTag(cms.InputTag("gemPacker",'','gemTester'))

process.p = cms.Path(process.gemPacker+process.rawDataCollector+process.muonGEMDigis+process.gemUnPackerTester)

