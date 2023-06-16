# Simple MSAF example
from __future__ import print_function
import msaf

# 1. Select audio file
ds_path = "C:/Users/Nath/OneDrive/Área de Trabalho/tcc/msaf-data/msaf-data-extracted/top50Spotify/audio/05-un-x100to.mp3"

# 2. Segment the file using the default MSAF parameters (this might take a few seconds)
boundaries, labels = msaf.process(ds_path, labels_id="scluster", plot=True)
print('Estimated boundaries:', boundaries)
print('Estimated labels:', labels)

# 3. Save segments using the MIREX format
out_file = 'segments.txt'
print('Saving output to %s' % out_file)
msaf.io.write_mirex(boundaries, labels, out_file)

# 4. Evaluate the results
try:
    evals = msaf.eval.process(ds_path, labels_id="scluster", save=True, out_file="results/laplacian/05-un-x100to.csv")
    print('Process evaluation finished')
    # print(evals)
except msaf.exceptions.NoReferencesError:
    file_struct = msaf.input_output.FileStruct(ds_path)
    print("No references found in {}. No evaluation performed.".format(file_struct.ref_file)) 