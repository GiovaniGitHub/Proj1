from src.utils import load_audio
from sklearn.decomposition import FastICA, PCA
from config import config

print(config.DB_DIR)
msg = load_audio("CTR-R11-NaoFam_ch1.wav")

# if msg['message'] == 'OK':
#     v = msg['file']

#     ica = FastICA(n_components=3)
#     S_ = ica.fit_transform(v)  # Reconstruct signals

# else:
#     print(msg)
