from src.utils import load_audio
from sklearn.decomposition import FastICA, PCA
from config import config
import numpy as np

msg2 = load_audio("CTR-R11-NaoFam_ch2.wav")
msg4 = load_audio("CTR-R11-NaoFam_ch4.wav")

if msg2['message'] == 'OK':
    v2 = msg2['body'][1]
    fs2 = msg2['body'][0]

    v4 = msg4['body'][1]
    fs4 = msg4['body'][0]

    sample_v2 = v2[13*fs2:40*fs2]
    sample_v4 = v4[13*fs4:40*fs4]

    X = np.array( [sample_v2, sample_v4] ).T
    ica = FastICA(n_components=4)
    S_ = ica.fit_transform(X)  # Reconstruct signals

else:
    print(msg)
