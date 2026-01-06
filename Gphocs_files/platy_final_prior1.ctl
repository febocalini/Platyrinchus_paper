GENERAL-INFO-START

		seq-file		Platyrinchus_GPHOCS.txt
		trace-file		platy-mcmc-trace1.out
		num-loci		2008
		burn-in		0
		mcmc-iterations		500000
		mcmc-sample-skip		0
		start-mig		0
		iterations-per-log		50
		logs-per-line		100

		tau-theta-print		10000
		tau-theta-alpha		1
		tau-theta-beta		5000

		mig-rate-print		0.001
		mig-rate-alpha		0.002
		mig-rate-beta		0.001

		locus-mut-rate		CONST

		find-finetunes		TRUE
		find-finetunes-num-steps		100
		find-finetunes-samples-per-step		100
		finetune-coal-time		0.1
		finetune-mig-time		0.3
		finetune-theta		0.04
		finetune-mig-rate		0.02
		finetune-tau		0.0000008
		finetune-mixing		0.003


GENERAL-INFO-END


CURRENT-POPS-START

		POP-START
				name		PCE
				samples		FMNH427100 d MZUSP85745 d MZUSP85760 d MZUSP85805 d MZUSP85833 d MZUSPALG159 d MZUSPALG39 d 
		POP-END

		POP-START
				name		SCAF
				samples		O058MZ88334BRRJ d O088MZ91269BRSC d O098MZ91681BRSP d O202OBR026BRMS d O206KU40PACON d O207KU57PACON d O218KU4023GY d COUFT0515 d DZ5020 d DZ6772 d LZUFPI0174 d MCP3089 d MCP5514 d MCP5527 d MPEG70184 d MPEG79461 d MPEG79466 d MPEGDZ4934 d MPEGT23638 d MZUSP94442 d UFG4483 d LSUMZB22637 d LSUMZB7434 d LSUMZB7616 d L28375 d MZUSP90974 d MZUSP90975 d MZUSP90978 d MZUSP91268 d MZUSP91465 d MZUSP91466 d MZUSP92167 d MZUSP92484 d MZUSP92485 d MZUSP92487 d MZUSP93234 d MZUSP93536 d
		POP-END

		POP-START
				name		ANDES
				samples		O223KU18426PECUS d O224KU18521PECUS d LSUMZB11966 d LSUMZB16047 d LSUMZB26448 d LSUMZB27767 d LSUMZB32985 d LSUMZB39987 d LSUMZB5542 d LSUMZB5970 d 
		POP-END

CURRENT-POPS-END


ANCESTRAL-POPS-START

		POP-START
				name		AF
				children		PCE		SCAF
				tau-initial		0.000004
		POP-END

		POP-START
				name		root
				children		AF		ANDES
				tau-initial		0.000005
		POP-END

ANCESTRAL-POPS-END


MIG-BANDS-START

		BAND-START
				source		PCE
				target		SCAF
		BAND-END

		BAND-START
				source		SCAF
				target		PCE
		BAND-END

		BAND-START
				source		PCE
				target		ANDES
		BAND-END

		BAND-START
				source		ANDES
				target		PCE
		BAND-END

		BAND-START
				source		SCAF
				target		ANDES
		BAND-END

		BAND-START
				source		ANDES
				target		SCAF
		BAND-END

MIG-BANDS-END


