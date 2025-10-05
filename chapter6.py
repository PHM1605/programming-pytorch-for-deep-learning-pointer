from pathlib import Path
import torchaudio
from torch.utils.data import Dataset 

class ESC50WithPitchChange(Dataset):
  def __init__(self, path, pitch_cents):
    files = Path(path).glob("*.wav")
    # [("1-137-A-32.wav","32"), (), ]
    self.items = [(f, f.name.split("-")[-1].replace(".wav",""))
        for f in files]
    self.length = len(self.items)

    # pitch is in cents: 100 = 1 semitone
    self.effects = [
        ["pitch", str(pitch_cents)],
        ["rate", "44100"]
    ]
      
  def __getitem__(self, index):
    filename, label = self.items[index]
    orig_waveform, orig_sr = torchaudio.load(str(filename))

    pitched_waveform, pitched_sr = torchaudio.sox_effects.apply_effects_file(
        str(filename), effects=self.effects
    )
    return (orig_waveform, orig_sr), (pitched_waveform, pitched_sr), label

  def __len__(self):
    return self.length
  


dataset = ESC50WithPitchChange("../ESC-50/train", pitch_cents=300)
(orig, orig_sr), (pitched, pitched_sr), label = dataset[0]

print("SAVING ORIGINAL...")
torchaudio.save("original.wav", orig, orig_sr)

print("SAVING PITCHED...")
torchaudio.save("pitched.wav", pitched, pitched_sr)
