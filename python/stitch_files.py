import argparse
from pathlib import Path
import scipy.io.wavfile as wavfile
import numpy as np

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    args = parser.parse_args()
    print("Combining wav files in directory: %s" % args.directory)

    dir_path = Path(args.directory)
    filenames = sorted(dir_path.glob("*.wav"))
    for filename in filenames:
        sr, data = wavfile.read(filename)
        print("%ich - %s" % (np.size(data, 1), filename))
        if 'output' in locals():
            output = np.concatenate((output, data), axis=-1)
        else:
            output = data
    print("final num channels %i" % np.size(output, 1))
    wavfile.write(dir_path.joinpath("out.wav"), sr, output)


if __name__ == "__main__":
    main()

