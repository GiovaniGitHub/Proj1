import wave
import os

import numpy as np
from scipy.io import wavfile
from os import path
from config import config


def load_audio(name_file):
    """
    Load a wave audio

    Args:
        name_file: The string name of a file, without a path, only name file

    Returns:
        A dict with message with status (OK, FAIL) and a value with 'body' name
        .If the message is FAIL, body will be except object or text message.
         And if the message is OK, the body will be the a tuple with frequency
         (Hz) and numpy.array with values.
    """
    file_name = path.join(path.abspath(config.DB_DIR),name_file)
    if path.isfile(file_name):
        try:
            file_wave = wavfile.read(file_name)
        except Exception as e:
            return {'message': 'FAIL', 'body' : e}

        return {'message': 'OK', 'body': file_wave}
    else:
        return {'message': 'FAIL', 'body': "The file {} don't exist.".format(name_file)}

