export DHI_SCHEDULER_HOST="hh:cmshhcombr2@hh-scheduler2.cern.ch"
export DHI_HOOK_FILE="$DHI_BASE/dhi/hooks/run2_combination.py"
export DHI_STORE_JOBS="$DHI_BASE/../jobs/"
export DHI_USER_FIRSTCHAR="${DHI_USER:0:1}"
export DHI_CMSSW_VERSION="CMSSW_14_0_0_pre1"
export DHI_COMBINE_VERSION="v9.1.0"
export DHI_WLCG_CACHE_ROOT=""
export DHI_WLCG_USE_CACHE="false"
export DHI_LOCAL_SCHEDULER="True"
export DHI_SCHEDULER_PORT="80"
export DHI_STORE_EOSUSER="$DHI_BASE/dhi/store"
export DHI_SOFTWARE="$DHI_BASE/data/software"
export DHI_DATA="$DHI_BASE/data"
export CreateWSArgs=""
export DHI_STORE_BUNDLES="/eos/user/a/acappati/HHComb/inference_tasks_output/"
export DHI_STORE="/eos/user/a/acappati/HHComb/inference_tasks_output/"
export DHI_USER="acappati"

# paths to cards (to change every time)
export DATACARDS_RUN3="/eos/user/a/acappati/HHComb/datacards_francisco_22Jul"
export ETAUCards="${DATACARDS_RUN3}/hhbbtautau_etau_transfbinary_2022_quantile"
export MUTAUCards="${DATACARDS_RUN3}/hhbbtautau_mutau_transfbinary_2022_quantile"

# cards names
export ETAUboost2022preEE="${ETAUCards}/ETau_BinaryTransf_Boosted_signal_2022.txt"
export ETAUboost2022posEE="${ETAUCards}/ETau_BinaryTransf_Boosted_signal_2022EE.txt"
export ETAURes1b2022preEE="${ETAUCards}/ETau_BinaryTransf_Res1b_signal_2022.txt"
export ETAURes1b2022posEE="${ETAUCards}/ETau_BinaryTransf_Res1b_signal_2022EE.txt"
export ETAURes2b2022preEE="${ETAUCards}/ETau_BinaryTransf_Res2b_signal_2022.txt"
export ETAURes2b2022posEE="${ETAUCards}/ETau_BinaryTransf_Res2b_signal_2022EE.txt"

export MUTAUboost2022preEE="${MUTAUCards}/MuTau_BinaryTransf_Boosted_signal_2022.txt"
export MUTAUboost2022posEE="${MUTAUCards}/MuTau_BinaryTransf_Boosted_signal_2022EE.txt"
export MUTAURes1b2022preEE="${MUTAUCards}/MuTau_BinaryTransf_Res1b_signal_2022.txt"
export MUTAURes1b2022posEE="${MUTAUCards}/MuTau_BinaryTransf_Res1b_signal_2022EE.txt"
export MUTAURes2b2022preEE="${MUTAUCards}/MuTau_BinaryTransf_Res2b_signal_2022.txt"
export MUTAURes2b2022posEE="${MUTAUCards}/MuTau_BinaryTransf_Res2b_signal_2022EE.txt"

# single channel limits
export ETAULimitsPerCat="${ETAUboost2022preEE}:${ETAUboost2022posEE}:${ETAURes2b2022preEE}:${ETAURes2b2022posEE}:${ETAURes1b2022preEE}:${ETAURes1b2022posEE}"
export MUTAULimitsPerCat="${MUTAUboost2022preEE}:${MUTAUboost2022posEE}:${MUTAURes2b2022preEE}:${MUTAURes2b2022posEE}:${MUTAURes1b2022preEE}:${MUTAURes1b2022posEE}"

# combination names
export ETAUComb2022preEE="${ETAUboost2022preEE},${ETAURes1b2022preEE},${ETAURes2b2022preEE}"
export ETAUComb2022posEE="${ETAUboost2022posEE},${ETAURes1b2022posEE},${ETAURes2b2022posEE}"
export ETAUComb2022full="${ETAUComb2022preEE},${ETAUComb2022posEE}"

export MUTAUComb2022preEE="${MUTAUboost2022preEE},${MUTAURes1b2022preEE},${MUTAURes2b2022preEE}"
export MUTAUComb2022posEE="${MUTAUboost2022posEE},${MUTAURes1b2022posEE},${MUTAURes2b2022posEE}"
export MUTAUComb2022full="${MUTAUComb2022preEE},${MUTAUComb2022posEE}"

export COMB2022full="${ETAUComb2022full},${MUTAUComb2022full}"

# names for limits (those used in the command after --multi-datacards)
export ETAULimits="${ETAULimitsPerCat}:${ETAUComb2022preEE}:${ETAUComb2022posEE}:${ETAUComb2022full}"
export MUTAULimits="${MUTAULimitsPerCat}:${MUTAUComb2022preEE}:${MUTAUComb2022posEE}:${MUTAUComb2022full}"
export COMBLimits="${ETAUComb2022preEE}:${ETAUComb2022posEE}:${ETAUComb2022full}:${MUTAUComb2022preEE}:${MUTAUComb2022posEE}:${MUTAUComb2022full}:${COMB2022full}"

# names for plots (those used in the command after --datacard-names, must correspond to the names for limits)
export ETAULimitsNames="boosted_preEE,boosted_postEE,Res2b_preEE,Res2b_postEE,Res1b_preEE,Res1b_postEE,comb_preEE,comb_postEE,comb_etau"
export MUTAULimitsNames="boosted_preEE,boosted_postEE,Res2b_preEE,Res2b_postEE,Res1b_preEE,Res1b_postEE,comb_preEE,comb_postEE,comb_mutau"
export COMBLimitsNames="etau_preEE,etau_postEE,comb_etau,mutau_preEE,mutau_postEE,comb_mutau,comb_full2022"



