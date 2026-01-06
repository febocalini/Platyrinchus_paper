#!/home/sergio/miniconda2/envs/momi-py36/bin/ python

import momi	
import logging
import pickle			

logging.basicConfig(level=logging.INFO,
                    filename="log_model17platy.log")

sfs = momi.Sfs.load("platy_sfs.gz")

#Modelo 4b - modelo com expansão somente do PCE e migração em todas as direções, com gargalo no Andes

platy_model17 = momi.DemographicModel(N_e=1e5, gen_time=2.3, muts_per_gen=2.5e-9)

platy_model17.set_data(sfs)

platy_model17.add_time_param("tdiv_AF_CEP", lower=5e3, upper=3e6)
platy_model17.add_time_param("tmig_AF_CEP",  upper_constraints=["tdiv_AF_CEP"], lower=5e3)
platy_model17.add_pulse_param("mfrac_AF_CEP", upper=.2)
platy_model17.add_time_param("tmig_CEP_AF",  upper_constraints=["tdiv_AF_CEP"], lower=5e3)
platy_model17.add_pulse_param("mfrac_CEP_AF", upper=.2)
platy_model17.add_growth_param("g_CEP", lower=1e-6, upper=1e-3)

#platy_model17.add_size_param("n_AF", lower=5e3, upper=1e6)
#platy_model17.add_size_param("n_CEP", lower=5e3, upper=1e6)

platy_model17.add_leaf("AF", N=4.88e5)
platy_model17.add_leaf("CEP", g="g_CEP", N=1.28e5)
platy_model17.set_size("CEP", t="tdiv_AF_CEP", g=0)
#platy_model17.set_size("AF", t="tdiv_AF_CEP", g=0)

platy_model17.move_lineages("AF", "CEP", t="tmig_AF_CEP", p="mfrac_AF_CEP")
platy_model17.move_lineages("CEP","AF", t="tmig_CEP_AF", p="mfrac_CEP_AF")
platy_model17.move_lineages("AF", "CEP", t="tdiv_AF_CEP")

platy_model17.add_time_param("tmig_Andes_CEP",  upper_constraints=["tdiv_AF_CEP"], lower=5e3)
platy_model17.add_pulse_param("mfrac_Andes_CEP", upper=.2)
platy_model17.add_time_param("tmig_CEP_Andes",  upper_constraints=["tdiv_AF_CEP"], lower=5e3)
platy_model17.add_pulse_param("mfrac_CEP_Andes", upper=.2)

platy_model17.add_time_param("tmig_Andes_AF",  upper_constraints=["tdiv_AF_CEP"], lower=5e3)
platy_model17.add_pulse_param("mfrac_Andes_AF", upper=.2)
platy_model17.add_time_param("tmig_AF_Andes",  upper_constraints=["tdiv_AF_CEP"], lower=5e3)
platy_model17.add_pulse_param("mfrac_AF_Andes", upper=.2)

#platy_model17.add_size_param("n_Andes", lower=5e3, upper=1e6)
platy_model17.add_time_param("tdiv_CEP_Andes", lower_constraints=["tdiv_AF_CEP"], upper=5e6)
platy_model17.add_size_param("n_bt", lower=1e3, upper=5e4)
platy_model17.add_growth_param("g_Andes", lower=1e-6, upper=1e-3)

platy_model17.add_leaf("Andes",g="g_Andes", N=3.13e5)
platy_model17.set_size("Andes", N="n_bt", t="tdiv_CEP_Andes", g=0)

platy_model17.move_lineages("Andes", "CEP", t="tmig_CEP_Andes", p="mfrac_Andes_CEP")
platy_model17.move_lineages("CEP","Andes", t="tmig_CEP_Andes", p="mfrac_CEP_Andes")
platy_model17.move_lineages("Andes", "AF", t="tmig_Andes_AF", p="mfrac_Andes_AF")
platy_model17.move_lineages("AF","Andes", t="tmig_AF_Andes", p="mfrac_AF_Andes")

platy_model17.move_lineages("CEP", "Andes", t="tdiv_CEP_Andes")

platy_model17.optimize(method='L-BFGS-B')

lik = platy_model17.log_likelihood()

#### output
file = open("bestrun_platy_revisado.txt","a")
file.write("model17=run1" '\n')
file.write("Log_likelihood=")
file.write(str(lik))
file.write('\n')
file.close()

### repetitions ###

results = []
n_runs = 5
platy_model17copy = platy_model2.copy()
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    platy_model2.set_params(platy_model2.get_params(),randomize=True)
    results.append(platy_model17copy.optimize(method='L-BFGS-B'))
    lik=platy_model17copy.log_likelihood()
    print(lik)

# sort results according to log likelihood, platyk the best one
best_result = sorted(results, key=lambda r: r.log_likelihood, reverse=True)[0]

platy_model17copy.set_params(best_result.parameters)
best_result
nparams= len(best_result.parameters)

#### output
file = open("bestrun_platy_revisado.txt","a")
file.write("Model=model17" '\n')
file.write("Log_likelihood=")
file.write(str(best_result.log_likelihood))
file.write('\n')
file.write("n_parameters=")
file.write(str(nparams))
file.write('\n')
file.write("Parameters_estimates:" '\n')
file.write(str(best_result.parameters))
file.write('\n')
file.write('\n')
file.close()

## exportar o melhor modelo

platy_model17 = best_result
f = open("platy_model17.pkl","wb")
platykle.dump(platy_model17,f)
f.close()

###############
quit()
