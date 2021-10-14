import os
import subprocess
import glob
import pandas as pd

def Stanford_Relation_Extractor():


    print('Relation Extraction Started')

    # if this throws a permission error:
    # cd stanford-openie/
    # chmod +x process_large_corpus.sh
    # cd ..
    for f in glob.glob(os.getcwd() + "/data/output/kg/*.txt"):
        print("Extracting relations for " + f.split("/")[-1])
        current_directory = os.getcwd()
        os.chdir('/home/cbrou/Desktop/knowledge-graph/stanford-openie')

        p = subprocess.Popen(['/home/cbrou/Desktop/knowledge-graph/stanford-openie/process_large_corpus.sh',f,f + '-out.csv'], stdout=subprocess.PIPE)

        output, err = p.communicate()


    print('Relation Extraction Completed')


if __name__ == '__main__':
    Stanford_Relation_Extractor()
