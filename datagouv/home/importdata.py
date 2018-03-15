from multiprocessing.dummy import Pool as ThreadPool
import importlib

modules=['home.conv_beneficiaire', 'home.conv_ecole_doctorante', 'home.conv_eff_etudiant', 'home.effectif_regional']


pool = ThreadPool(4)

results = pool.map(importlib.import_module, modules)

pool.close()
pool.joint()
