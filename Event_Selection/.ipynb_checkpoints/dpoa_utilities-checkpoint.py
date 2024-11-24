import numpy as np
import awkward as ak

import json

nanoaod_filenames = {}

nanoaod_filenames['Met_collision'] = ['https://opendata.cern.ch/record/30526/files/CMS_Run2016G_MET_NANOAOD_UL2016_MiniAODv2_NanoAODv9-v1_1110000_file_index.txt', 
                          'https://opendata.cern.ch/record/30526/files/CMS_Run2016G_MET_NANOAOD_UL2016_MiniAODv2_NanoAODv9-v1_270000_file_index.txt', 
                          'https://opendata.cern.ch/record/30559/files/CMS_Run2016H_MET_NANOAOD_UL2016_MiniAODv2_NanoAODv9-v1_120000_file_index.txt', 
                          'https://opendata.cern.ch/record/30559/files/CMS_Run2016H_MET_NANOAOD_UL2016_MiniAODv2_NanoAODv9-v1_280000_file_index.txt', 
                          'https://opendata.cern.ch/record/30559/files/CMS_Run2016H_MET_NANOAOD_UL2016_MiniAODv2_NanoAODv9-v1_70000_file_index.txt'
                                 ]

nanoaod_filenames['SingleMuon_collision'] =['https://opendata.cern.ch/record/30530/files/CMS_Run2016G_SingleMuon_NANOAOD_UL2016_MiniAODv2_NanoAODv9-v1_130000_file_index.txt', 
                          'https://opendata.cern.ch/record/30530/files/CMS_Run2016G_SingleMuon_NANOAOD_UL2016_MiniAODv2_NanoAODv9-v1_70000_file_index.txt', 
                          'https://opendata.cern.ch/record/30563/files/CMS_Run2016H_SingleMuon_NANOAOD_UL2016_MiniAODv2_NanoAODv9-v1_120000_file_index.txt', 
                          'https://opendata.cern.ch/record/30563/files/CMS_Run2016H_SingleMuon_NANOAOD_UL2016_MiniAODv2_NanoAODv9-v1_1210000_file_index.txt', 
                          'https://opendata.cern.ch/record/30563/files/CMS_Run2016H_SingleMuon_NANOAOD_UL2016_MiniAODv2_NanoAODv9-v1_130000_file_index.txt',
                          'https://opendata.cern.ch/record/30563/files/CMS_Run2016H_SingleMuon_NANOAOD_UL2016_MiniAODv2_NanoAODv9-v1_280000_file_index.txt',
                          'https://opendata.cern.ch/record/30563/files/CMS_Run2016H_SingleMuon_NANOAOD_UL2016_MiniAODv2_NanoAODv9-v1_70000_file_index.txt'
                                 ]

nanoaod_filenames['SingleElectron_collision'] = ['https://opendata.cern.ch/record/30529/files/CMS_Run2016G_SingleElectron_NANOAOD_UL2016_MiniAODv2_NanoAODv9-v1_110000_file_index.txt', 
                          'https://opendata.cern.ch/record/30529/files/CMS_Run2016G_SingleElectron_NANOAOD_UL2016_MiniAODv2_NanoAODv9-v1_260000_file_index.txt', 
                          'https://opendata.cern.ch/record/30529/files/CMS_Run2016G_SingleElectron_NANOAOD_UL2016_MiniAODv2_NanoAODv9-v1_270000_file_index.txt', 
                          'https://opendata.cern.ch/record/30562/files/CMS_Run2016H_SingleElectron_NANOAOD_UL2016_MiniAODv2_NanoAODv9-v1_120000_file_index.txt', 
                          'https://opendata.cern.ch/record/30562/files/CMS_Run2016H_SingleElectron_NANOAOD_UL2016_MiniAODv2_NanoAODv9-v1_270000_file_index.txt',
                          'https://opendata.cern.ch/record/30562/files/CMS_Run2016H_SingleElectron_NANOAOD_UL2016_MiniAODv2_NanoAODv9-v1_280000_file_index.txt',
                          'https://opendata.cern.ch/record/30562/files/CMS_Run2016H_SingleElectron_NANOAOD_UL2016_MiniAODv2_NanoAODv9-v1_70000_file_index.txt'
                                 ]

nanoaod_filenames['Z1JetsToNuNu_PtZ-150To250'] = ['https://opendata.cern.ch/record/73746/files/CMS_mc_RunIISummer20UL16NanoAODv9_Z1JetsToNuNu_M-50_LHEFilterPtZ-150To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8_NANOAODSIM_106X_mcRun2_asymptotic_v17-v1_2430000_file_index.txt', 
                          'https://opendata.cern.ch/record/73746/files/CMS_mc_RunIISummer20UL16NanoAODv9_Z1JetsToNuNu_M-50_LHEFilterPtZ-150To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8_NANOAODSIM_106X_mcRun2_asymptotic_v17-v1_2520000_file_index.txt', 
                          'https://opendata.cern.ch/record/73746/files/CMS_mc_RunIISummer20UL16NanoAODv9_Z1JetsToNuNu_M-50_LHEFilterPtZ-150To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8_NANOAODSIM_106X_mcRun2_asymptotic_v17-v1_2530000_file_index.txt', 
                          'https://opendata.cern.ch/record/73746/files/CMS_mc_RunIISummer20UL16NanoAODv9_Z1JetsToNuNu_M-50_LHEFilterPtZ-150To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8_NANOAODSIM_106X_mcRun2_asymptotic_v17-v1_40000_file_index.txt', 
                          'https://opendata.cern.ch/record/73746/files/CMS_mc_RunIISummer20UL16NanoAODv9_Z1JetsToNuNu_M-50_LHEFilterPtZ-150To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8_NANOAODSIM_106X_mcRun2_asymptotic_v17-v1_50000_file_index.txt'
                                 ]

nanoaod_filenames['Z1JetsToNuNu_PtZ-250To400'] = ['https://opendata.cern.ch/record/73748/files/CMS_mc_RunIISummer20UL16NanoAODv9_Z1JetsToNuNu_M-50_LHEFilterPtZ-250To400_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8_NANOAODSIM_106X_mcRun2_asymptotic_v17-v1_2430000_file_index.txt', 
                          'https://opendata.cern.ch/record/73748/files/CMS_mc_RunIISummer20UL16NanoAODv9_Z1JetsToNuNu_M-50_LHEFilterPtZ-250To400_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8_NANOAODSIM_106X_mcRun2_asymptotic_v17-v1_2520000_file_index.txt', 
                          'https://opendata.cern.ch/record/73748/files/CMS_mc_RunIISummer20UL16NanoAODv9_Z1JetsToNuNu_M-50_LHEFilterPtZ-250To400_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8_NANOAODSIM_106X_mcRun2_asymptotic_v17-v1_40000_file_index.txt', 
                          'https://opendata.cern.ch/record/73748/files/CMS_mc_RunIISummer20UL16NanoAODv9_Z1JetsToNuNu_M-50_LHEFilterPtZ-250To400_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8_NANOAODSIM_106X_mcRun2_asymptotic_v17-v1_50000_file_index.txt'
                                 ]

nanoaod_filenames['Z1JetsToNuNu_PtZ-400ToInf'] = ['https://opendata.cern.ch/record/73750/files/CMS_mc_RunIISummer20UL16NanoAODv9_Z1JetsToNuNu_M-50_LHEFilterPtZ-400ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8_NANOAODSIM_106X_mcRun2_asymptotic_v17-v1_2430000_file_index.txt', 
                          'https://opendata.cern.ch/record/73750/files/CMS_mc_RunIISummer20UL16NanoAODv9_Z1JetsToNuNu_M-50_LHEFilterPtZ-400ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8_NANOAODSIM_106X_mcRun2_asymptotic_v17-v1_2530000_file_index.txt', 
                          'https://opendata.cern.ch/record/73750/files/CMS_mc_RunIISummer20UL16NanoAODv9_Z1JetsToNuNu_M-50_LHEFilterPtZ-400ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8_NANOAODSIM_106X_mcRun2_asymptotic_v17-v1_50000_file_index.txt'
                                 ]

nanoaod_filenames['Z2JetsToNuNu_PtZ-150To250'] = ['https://opendata.cern.ch/record/73760/files/CMS_mc_RunIISummer20UL16NanoAODv9_Z2JetsToNuNu_M-50_LHEFilterPtZ-150To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8_NANOAODSIM_106X_mcRun2_asymptotic_v17-v2_2430000_file_index.txt', 
                          'https://opendata.cern.ch/record/73760/files/CMS_mc_RunIISummer20UL16NanoAODv9_Z2JetsToNuNu_M-50_LHEFilterPtZ-150To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8_NANOAODSIM_106X_mcRun2_asymptotic_v17-v2_2520000_file_index.txt', 
                          'https://opendata.cern.ch/record/73760/files/CMS_mc_RunIISummer20UL16NanoAODv9_Z2JetsToNuNu_M-50_LHEFilterPtZ-150To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8_NANOAODSIM_106X_mcRun2_asymptotic_v17-v2_2530000_file_index.txt', 
                          'https://opendata.cern.ch/record/73760/files/CMS_mc_RunIISummer20UL16NanoAODv9_Z2JetsToNuNu_M-50_LHEFilterPtZ-150To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8_NANOAODSIM_106X_mcRun2_asymptotic_v17-v2_40000_file_index.txt'
                                 ]

nanoaod_filenames['Z2JetsToNuNu_PtZ-250To400'] = ['https://opendata.cern.ch/record/73762/files/CMS_mc_RunIISummer20UL16NanoAODv9_Z2JetsToNuNu_M-50_LHEFilterPtZ-250To400_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8_NANOAODSIM_106X_mcRun2_asymptotic_v17-v2_2430000_file_index.txt', 
                          'https://opendata.cern.ch/record/73762/files/CMS_mc_RunIISummer20UL16NanoAODv9_Z2JetsToNuNu_M-50_LHEFilterPtZ-250To400_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8_NANOAODSIM_106X_mcRun2_asymptotic_v17-v2_2520000_file_index.txt', 
                          'https://opendata.cern.ch/record/73762/files/CMS_mc_RunIISummer20UL16NanoAODv9_Z2JetsToNuNu_M-50_LHEFilterPtZ-250To400_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8_NANOAODSIM_106X_mcRun2_asymptotic_v17-v2_2530000_file_index.txt', 
                          'https://opendata.cern.ch/record/73762/files/CMS_mc_RunIISummer20UL16NanoAODv9_Z2JetsToNuNu_M-50_LHEFilterPtZ-250To400_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8_NANOAODSIM_106X_mcRun2_asymptotic_v17-v2_40000_file_index.txt', 
                          'https://opendata.cern.ch/record/73762/files/CMS_mc_RunIISummer20UL16NanoAODv9_Z2JetsToNuNu_M-50_LHEFilterPtZ-250To400_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8_NANOAODSIM_106X_mcRun2_asymptotic_v17-v2_50000_file_index.txt'
                                 ]

nanoaod_filenames['Z2JetsToNuNu_PtZ-400ToInf'] = ['https://opendata.cern.ch/record/73764/files/CMS_mc_RunIISummer20UL16NanoAODv9_Z2JetsToNuNu_M-50_LHEFilterPtZ-400ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8_NANOAODSIM_106X_mcRun2_asymptotic_v17-v1_2430000_file_index.txt', 
                          'https://opendata.cern.ch/record/73764/files/CMS_mc_RunIISummer20UL16NanoAODv9_Z2JetsToNuNu_M-50_LHEFilterPtZ-400ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8_NANOAODSIM_106X_mcRun2_asymptotic_v17-v1_2520000_file_index.txt', 
                          'https://opendata.cern.ch/record/73764/files/CMS_mc_RunIISummer20UL16NanoAODv9_Z2JetsToNuNu_M-50_LHEFilterPtZ-400ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8_NANOAODSIM_106X_mcRun2_asymptotic_v17-v1_40000_file_index.txt', 
                          'https://opendata.cern.ch/record/73764/files/CMS_mc_RunIISummer20UL16NanoAODv9_Z2JetsToNuNu_M-50_LHEFilterPtZ-400ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8_NANOAODSIM_106X_mcRun2_asymptotic_v17-v1_50000_file_index.txt'
                                 ]

#########################################################################################
def build_lumi_mask(lumifile, tree, verbose=False):
    # lumifile should be the name/path of the file
    good_luminosity_sections = ak.from_json(open(lumifile, 'rb'))

    # Pull out the good runs as integers
    good_runs = np.array(good_luminosity_sections.fields).astype(int)
    #good_runs

    # Get the good blocks as an awkward array
    # First loop over to get them as a list
    all_good_blocks = []
    for field in good_luminosity_sections.fields:
        all_good_blocks.append(good_luminosity_sections[field])

    # Turn the list into an awkward array
    all_good_blocks = ak.Array(all_good_blocks)
    all_good_blocks[11]

    # Assume that tree is a NanoAOD Events tree
    nevents = tree.num_entries
    if verbose:
        print(f"nevents: {nevents}")
        print()
        print("All good runs")
        print(good_runs)
        print()
        print("All good blocks")
        print(all_good_blocks)
        print()

    # Get the runs and luminosity blocks from the tree
    run = tree['run'].array()
    lumiBlock = tree['luminosityBlock'].array()

    if verbose:
        print("Runs from the tree")
        print(run)
        print()
        print("Luminosity blocks from the tree")
        print(lumiBlock)
        print()

    # ChatGPT helped me with this part!
    # Find index of values in arr2 if those values appear in arr1

    def find_indices(arr1, arr2):
        index_map = {value: index for index, value in enumerate(arr1)}
        return [index_map.get(value, -1) for value in arr2]

    # Get the indices that say where the good runs are in the lumi file
    # for the runs that appear in the tree
    good_runs_indices = find_indices(good_runs, run)

    # For each event, calculate the difference between the luminosity block for that event
    # and the good luminosity blocks for that run for that event
    diff = lumiBlock - all_good_blocks[good_runs_indices]

    if verbose:
        print("difference between event lumi blocks and the good lumi blocks")
        print(diff)
        print()

    # If the lumi block appears between any of those good block numbers, 
    # then one difference will be positive and the other will be negative
    # 
    # If it it outside of the range, both differences will be positive or 
    # both negative.
    #
    # The product will be negagive if the lumi block is in the range
    # and positive if it is not in the range
    prod_diff = ak.prod(diff, axis=2)

    if verbose:
        print("product of the differences")
        print(prod_diff)
        print()

    mask = ak.any(prod_diff<=0, axis=1)

    return mask

#############################################################################

def get_files_for_dataset(dataset, random=False, n=0):
    
    filelist_filename = f'FILE_LIST_{dataset}.txt'
    
    infile = open(filelist_filename)
    filenames = infile.readlines()
    
    if n<1:
        return filenames
    
    else:
        if random:
            subset = np.random.choice(filenames, n)
    
        else:
            subset = filenames[0:n]
        
        return subset
    
###############################################################################

def pretty_print(fields, fmt='40s', require=None, ignore=None):
    
    output = ""
    
    for f in fields:
        PASSED = True
        if require is not None:
            if type(require) != list:
                require = [require]
            PASSED = True
            for r in require:
                if f.find(r) < 0:
                    PASSED = False
        
        # Did not find a string and so skip
        if PASSED is False:
            continue
        
        if ignore is not None:
            if f.find(ignore) >= 0:
                continue
        
        if len(output) + len(f) <= 80:
            output += f"{f:{fmt}} "
        else:
            print(output)
            output = f"{f:{fmt}} "
    
    print(output)
